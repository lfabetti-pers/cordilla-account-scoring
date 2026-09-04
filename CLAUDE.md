# CLAUDE.md

## Context

This repo is a take-home exercise for a Dialpad AI Transformation Analyst interview
(an AI-focused product analyst role, not an ML engineering role). Cordilla Systems' VP of
Sales asked for "a dashboard so reps stop guessing which accounts to call" — an
underspecified ask with no stated decision or success metric. A pre-trained model
(`model/model.pkl`) was found sitting unused, with no one vouching for it, against a
backdrop of an earlier Cordilla scoring effort that tested well and quietly lost
credibility months after launch. The job is not to build a bigger thing. It's to frame the
actual decision, audit whether the model deserves trust, design a real (non-obvious) way
its output reaches a rep, and be honest about what's still unproven.

See "Required outputs" below for exactly what the finished repo needs to contain.

## Required outputs

### What PROPOSAL.md must cover

1. **Problem framing.** Before touching the model: who is actually making a decision
   based on its output, what that decision is, and what would show the model is actually
   helping versus being noise everyone trusts by default.
2. **Model audit.** What to trust this model on, what not to, and whether to ship its
   scores as they are. Needs to reflect actual investigation of `model/model.pkl` and
   `data/training_data.csv` — not a generic description of what an audit could look like.
3. **AI-assisted serving design.** How the model's output on `data/accounts_to_score.csv`
   actually reaches a rep or SDR manager in a way that changes their day — not a
   per-account brief, not a priority-tier/routing rule, not just a score in a list. Should
   do real work with the score, in a shape not already named in this brief.
4. **Productionization and trust.** How a rep would know why an account is scored the way
   it is, what they should trust vs. double-check, how the approach stays current over
   time, and where the reasoning lands on Salesforce-native vs. external delivery
   (weighed as a real tradeoff, not asserted).

Target length: roughly 800–1,200 words total across the four sections.

### What the repo must contain

1. **Model audit (`audit/`)** — real code (notebook or scripts) run against
   `model/model.pkl` and `data/training_data.csv`, showing what was actually checked and
   what was found or ruled out.
2. **AI-assisted serving step (`serving/`)** — a rough but real script that loads the
   model, scores `data/accounts_to_score.csv`, and does one genuine AI-assisted thing
   with the output (never a per-account brief or a priority-tier/routing rule). It needs
   to run; it doesn't need to handle every edge case. If there's no live LLM API key
   available, a clearly designed template with a documented plug-in point (what prompt,
   what inputs, what it would return) counts the same as a live call — the design is
   what's being evaluated, not whether a network request fires.
3. **Written proposal (`PROPOSAL.md`)** — see above.
4. **Research log (`RESEARCH-LOG.md`)** — kept live, not written after the fact (see the
   "Research log" section below for the update rules). The final entry, once the work is
   otherwise done, should pull together the base numbers, hypotheses, and assumptions
   that would actually be stood behind in the room — the raw material for a presentation,
   not the presentation itself.
5. **Real git history** — committed incrementally as work actually happens, never
   squashed into one commit at the end (the initial scaffold commit is the one
   deliberate exception, as the shared starting point).

## Role

Act as an analytical and engineering copilot for this exercise. The job is to help produce
clear, defensible work while preserving strong product judgment and business reasoning —
not to write the most code or the most polished analysis.

## General principles

- Treat AI as a technology with capabilities and limitations, not as the starting point.
- Do not assume the stakeholder's requested solution is the real requirement.
- Look for the underlying user problem, decision, workflow, and business outcome.
- Optimize for measurable business value, not technical novelty.
- Prefer the simplest solution that can materially improve the workflow.
- Challenge weak assumptions and proposed solutions when appropriate. Do not blindly
  agree with my ideas.
- Clearly distinguish facts, assumptions, interpretations, and recommendations.
- Avoid analysis that is technically interesting but does not affect a business or
  product decision.
- Consider how any proposed solution would fit into the user's actual workflow and how
  trust, adoption, and impact would be measured.
- Be explicit about uncertainty and limitations.
- Any code or analysis should remain simple enough to be understood, explained,
  modified, and defend live.
- Treat the model and data as untrusted until earned — they weren't produced by us.
  Default posture is to look for reasons to doubt a number, not to confirm it works.
- Verify AI-generated output (metrics, explanations, serving ideas) against the actual
  data and pipeline before it goes into the proposal — don't accept it on the first pass.

## Challenge constraints

- Do not retrain, tune, or replace the provided model.
- Do not modify or regenerate `data/training_data.csv` or `data/accounts_to_score.csv`.
  Use the provided model and data as given.
- Treat **2026-08-01** as "today" for every recency/age calculation — not the system
  clock. Both CSVs are static snapshots as of that date.
- Do not overengineer. Production-grade code, tests, and packaging are not required —
  this is a research repo. Rough-but-real beats polished-but-overbuilt.
- State assumptions explicitly when context is ambiguous.

See "Required outputs" above for what each deliverable must contain, including the
serving-step exclusions and the git-history expectation.

## Research log

`RESEARCH-LOG.md` is the running record of hypotheses, findings, assumptions, dead ends,
relevant AI interactions, corrections, and how the thinking evolved. At least one entry
must name a place an AI tool gave something wrong or generic and what was corrected.

Only update it when I explicitly tell you to, and only with the content I give you for
that update — do not add entries on your own initiative or backfill from earlier
conversation. Never rewrite or delete existing entries; only append.

Each entry should be concise and follow this structure:

- **Hypothesis** — what's being tested or investigated, and why.
- **Research plan** — what was checked and how.
- **Findings** — what was actually found, including dead ends and surprises.
