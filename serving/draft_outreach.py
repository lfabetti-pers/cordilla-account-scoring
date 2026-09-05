"""
Serving step — approval-queue outreach drafting.

WHAT THIS DOES
    Scores data/accounts_to_score.csv with model/model.pkl once, takes the highest-scoring
    accounts as candidates, and for each one either drafts a short outreach email for a rep
    to approve, or refuses to draft and says why.

WHAT THE SCORE IS FOR
    One job only: deciding which accounts are worth spending a draft on. The score never
    reaches the rep, and no artifact here presents it as a probability. The audit
    (audit/model_data_audit.ipynb) found the model cannot be validated and was trained on a
    population that converts several times more often than the one reps actually work, so
    its level is wrong even where its ordering may be usable.

WHY REFUSAL IS THE PRODUCT
    Cordilla holds nine numeric columns per account — no company name, no contact person,
    no notes. Generating an email from that for every account produces a mail merge, which
    at under-1% conversion burns the sending domain and the tool's credibility with it. So
    the system's real output is not 300 emails. It is: here are the accounts where we
    genuinely have something true to say, and here are the ones where we don't and won't
    pretend. Two things drive the refusals, both straight out of the audit:

      1. Some signals are real but unsayable. An intent-vendor score and a count of web
         visits predict conversion, but you cannot open an email with them without
         sounding like surveillance. They stay internal.
      2. Most snapshots are stale. Median snapshot age in this file is 121 days and the
         oldest is 675, so a "last 90 days" activity field often describes a window that
         closed months ago. Referencing it as recent would simply be false.

WHERE THE REAL LLM CALL PLUGS IN
    generate_opener() below. It is the single AI action in this script, one call per
    candidate. If ANTHROPIC_API_KEY is set it posts to the Messages API; otherwise it falls
    back to a deterministic template filling the identical JSON schema, so the script runs
    end to end and the output stays inspectable. Fallback output is labelled as such
    everywhere it appears.

USAGE
    python serving/draft_outreach.py [--top-n 60]
"""

import argparse
import json
import os
import pickle
import sys
from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "serving" / "out"

# Project constraint: both CSVs are static snapshots as of this date. Never the system clock.
TODAY = pd.Timestamp("2026-08-01")

FEATURES = [
    "account_type", "employee_count", "industry", "intent_score", "mql_count_90d",
    "trial_started", "trial_active_users", "web_touchpoints_90d", "sales_contacts_90d",
]

# Signals that exist and predict, but that a rep cannot say out loud to a prospect.
FORBIDDEN_CLAIMS = [
    "third-party intent data or intent scores",
    "how many times they visited our website",
    "their employee count or company size",
]

FRESH_DAYS = 90     # within this, recency language ("recently", "just") is honest
STALE_DAYS = 180    # beyond this, the evidence is too old to reference at all


def build_evidence(row):
    """Split an account's signals into what can be said to a human and what cannot.

    Only things *they* did count as evidence. Our own rep contacts deliberately do not:
    "we have called you four times" is not a reason to write to someone, and treating our
    own activity as a buying signal is the circularity the audit flagged. Prior contact
    still shapes the tone of the email, it just cannot justify sending one.
    """
    referenceable = []
    if row.trial_started == 1 and row.trial_active_users > 0:
        n = int(row.trial_active_users)
        referenceable.append(
            f"started a trial and {n} of your people {'are' if n != 1 else 'is'} using it"
        )
    elif row.trial_started == 1:
        referenceable.append("signed up for a trial but nobody has logged in yet")
    if row.mql_count_90d > 0:
        n = int(row.mql_count_90d)
        referenceable.append(
            f"{n} {'people' if n != 1 else 'person'} from your team asked us for something"
        )
    if row.account_type == "Former Customer":
        referenceable.append("worked with Cordilla before")

    internal_only = [
        "intent vendor coverage: " + (
            f"yes, score {row.intent_score:.0f}" if pd.notna(row.intent_score) else "none"
        ),
        f"web touchpoints in window: {int(row.web_touchpoints_90d)}",
        f"employee count: {int(row.employee_count)}",
        f"industry: {row.industry}",
    ]
    return referenceable, internal_only


def gate(referenceable, age_days):
    """Deterministic refusals, decided in code rather than left to the model.

    These are auditable and identical on every run. The LLM gets a second chance to refuse
    afterwards, but it never gets to overturn one of these.
    """
    if not referenceable:
        return "no_send", "nothing-to-reference", False
    if age_days > STALE_DAYS:
        return "no_send", f"evidence-too-stale ({age_days}d old)", False
    return "draft", "", age_days <= FRESH_DAYS


def build_prompt(payload):
    """The prompt a live model would receive. Rendered here so it can be read and argued with."""
    recency = (
        "You may refer to this evidence as recent."
        if payload["allow_recency"]
        else f"This evidence is {payload['snapshot_age_days']} days old. Do NOT call it "
             "recent, and do not use words like 'just', 'recently', or 'this week'."
    )
    return f"""You are drafting a first-touch outreach email for a Cordilla Systems SDR.
Cordilla sells B2B workflow software. The email will be reviewed by a human rep before
anything is sent.

ACCOUNT
  id: {payload['account_id']}
  relationship: {payload['account_type']}
  segment: {payload['size_band']} company in {payload['industry']}
  prior rep contacts: {payload['prior_contacts']}

EVIDENCE YOU MAY REFERENCE (this is all we actually know):
{chr(10).join('  - ' + e for e in payload['referenceable_evidence'])}

{recency}

YOU MAY NOT MENTION, HINT AT, OR ALLUDE TO:
{chr(10).join('  - ' + c for c in payload['forbidden_claims'])}

TASK
Write a subject line and a body under 90 words, grounded only in the evidence above. Plain
sentences, no exclamation marks, no invented facts about their business, no claims about
their industry we cannot support. If the evidence will not carry a message that a real
person would not resent receiving, return no_send instead of writing a weak email — an
unsent email costs us nothing and a bad one costs us the domain.

Return JSON only:
{{"decision": "draft" | "no_send",
  "reason": "<short reason if no_send, else empty>",
  "subject": "<subject line>",
  "body": "<email body>",
  "evidence_used": ["<which evidence items the body actually rests on>"]}}"""


def generate_opener(payload):
    """THE ONE AI ACTION. One call per candidate.

    Input:  the payload dict above (account context, referenceable evidence, recency
            permission, forbidden claims).
    Output: {"decision", "reason", "subject", "body", "evidence_used", "source"}.

    With ANTHROPIC_API_KEY set this hits the Messages API. Without one it falls back to a
    deterministic template that fills the same schema, so the pipeline runs and the design
    is inspectable. Template output is labelled source="template" and is never mistaken
    for a model's writing.
    """
    if os.environ.get("ANTHROPIC_API_KEY"):
        # --- live call plugs in here -------------------------------------------------
        from anthropic import Anthropic  # not in requirements.txt; only needed live

        resp = Anthropic().messages.create(
            model="claude-sonnet-5",
            max_tokens=600,
            messages=[{"role": "user", "content": build_prompt(payload)}],
        )
        out = json.loads(resp.content[0].text)
        out["source"] = "claude-sonnet-5"
        return out
        # -----------------------------------------------------------------------------

    # Fallback: same schema, no network. Mirrors the prompt's rules mechanically.
    lead = payload["referenceable_evidence"][0]
    opener = "I saw that you" if payload["allow_recency"] else "our records show you"
    greeting = "Picking this back up — " if payload["prior_contacts"] > 0 else ""
    if not greeting:
        opener = opener[0].upper() + opener[1:]
    body = (
        f"Hi there,\n\n{greeting}{opener} {lead}. "
        "I work with teams sizing up whether workflow automation is worth the switching "
        "cost, and I can usually tell in one call whether it is.\n\n"
        "Worth fifteen minutes to find out?"
    )
    return {
        "decision": "draft",
        "reason": "",
        "subject": f"Quick question about your {payload['industry'].lower()} workflows",
        "body": body,
        "evidence_used": [lead],
        "source": "template",
    }


def size_band(n):
    return "small (<50)" if n < 50 else "mid (50-250)" if n < 250 else "large (250+)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top-n", type=int, default=60,
                    help="how many of the highest-scoring accounts to consider drafting for")
    args = ap.parse_args()

    model_path, data_path = REPO / "model" / "model.pkl", REPO / "data" / "accounts_to_score.csv"
    for p in (model_path, data_path):
        if not p.exists():
            sys.exit(f"missing {p}")

    with open(model_path, "rb") as f:
        model = pickle.load(f)
    df = pd.read_csv(data_path)

    # Score once. This is the only place the model is used.
    df["score"] = model.predict_proba(df[FEATURES])[:, 1]
    df["snapshot_age_days"] = (TODAY - pd.to_datetime(df.snapshot_date)).dt.days

    candidates = df.nlargest(args.top_n, "score")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "prompts").mkdir(exist_ok=True)
    for stale in (OUT / "prompts").glob("*.txt"):  # don't leave last run's prompts behind
        stale.unlink()

    rows = []
    for row in candidates.itertuples():
        referenceable, internal_only = build_evidence(row)
        decision, reason, allow_recency = gate(referenceable, row.snapshot_age_days)

        result = {"decision": decision, "reason": reason, "subject": "", "body": "",
                  "evidence_used": [], "source": "gate"}
        if decision == "draft":
            payload = {
                "account_id": row.account_id,
                "account_type": row.account_type,
                "industry": row.industry,
                "size_band": size_band(row.employee_count),
                "prior_contacts": int(row.sales_contacts_90d),
                "referenceable_evidence": referenceable,
                "forbidden_claims": FORBIDDEN_CLAIMS,
                "allow_recency": allow_recency,
                "snapshot_age_days": int(row.snapshot_age_days),
            }
            (OUT / "prompts" / f"{row.account_id}.txt").write_text(build_prompt(payload))
            result = generate_opener(payload)
            result.setdefault("reason", "")

        rows.append({
            "account_id": row.account_id,
            "decision": result["decision"],
            "reason": result["reason"],
            "subject": result["subject"],
            "body": result["body"],
            "evidence_used": " | ".join(result.get("evidence_used", [])),
            "referenceable_evidence": " | ".join(referenceable),
            "internal_only": " | ".join(internal_only),
            "snapshot_age_days": int(row.snapshot_age_days),
            "score": round(row.score, 4),          # for our analysis, not for the rep
            "source": result.get("source", "gate"),
        })

    out = pd.DataFrame(rows)
    out.to_csv(OUT / "outreach_queue.csv", index=False)

    drafts = out[out.decision == "draft"]
    declined = out[out.decision == "no_send"]
    live = "a live model" if os.environ.get("ANTHROPIC_API_KEY") else "the offline template"

    md = [
        "# Outreach queue — for rep approval",
        "",
        f"_{len(drafts)} drafts, {len(declined)} declined, from the top {args.top_n} of "
        f"{len(df)} accounts. Drafted with {live}._",
        "",
        "**Nothing here sends on its own.** Approve, edit, or reject each one.",
        "",
        "The model's score chose which accounts got a draft and appears nowhere below. Per "
        "the audit it is not a number to trust: it was trained on a population converting "
        "several times more often than the accounts you actually work, so its level is "
        "wrong even where its ordering may hold. Judging whether a draft is worth sending "
        "is the part that needs you.",
        "",
        "---",
        "",
        f"## Drafts ({len(drafts)})",
        "",
    ]
    for r in drafts.itertuples():
        md += [
            f"### {r.account_id} · {r.snapshot_age_days}d-old snapshot",
            f"**Rests on:** {r.evidence_used or r.referenceable_evidence}  ",
            f"**Known but not said:** {r.internal_only}",
            "",
            f"**Subject:** {r.subject}",
            "",
        ]
        md += ["> " + line if line else ">" for line in r.body.split("\n")]
        md += ["", "`[ ] approve   [ ] edit   [ ] reject`", "", "---", ""]

    md += [f"## Declined ({len(declined)})", ""]
    if len(declined):
        md += ["We had nothing true to say to these, so no email was written.", ""]
        for reason, grp in declined.groupby(declined.reason.str.split(" (", regex=False).str[0]):
            md += [f"**{reason}** — {len(grp)} accounts", "",
                   "> " + ", ".join(grp.account_id.tolist()), ""]
    md += [
        "A high score with no referenceable evidence is the system working, not failing. "
        "It means the model likes an account for reasons we cannot put in an email — "
        "usually intent-vendor coverage or web activity. Those are worth a call where you "
        "can ask a question; they are not worth an email that opens by telling someone we "
        "have been watching them.",
        "",
    ]
    (OUT / "outreach_queue.md").write_text("\n".join(md))

    print(f"scored {len(df)} accounts | {args.top_n} candidates -> "
          f"{len(drafts)} drafts, {len(declined)} declined")
    print(f"wrote {OUT/'outreach_queue.md'} and {OUT/'outreach_queue.csv'}")


if __name__ == "__main__":
    main()
