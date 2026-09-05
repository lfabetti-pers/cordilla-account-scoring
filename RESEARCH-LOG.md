# Research log

Kept as work happens. There's no single fixed structure every entry follows — the shape
depends on what kind of entry it is, specified at logging time. See `CLAUDE.md` for the
update rules — entries are added only on explicit instruction, with the content given at
that time, and are never edited or removed once written.

---

## Entry 1 — Stack and action plan

**Date:** 2026-09-04

**Stack.** Working in VS Code with Claude Code (Sonnet 5) integrated directly in the
editor, driven interactively throughout. `CLAUDE.md` holds the standing working
principles and required outputs for this project so any session picks up the same
context; this log holds the actual hypotheses, plan, and findings as they happen.

**Research plan.** Consolidated high-level approach for the exercise:

1. **Frame the problem.** Identify the user, workflow, real problem, and decision to
   improve. Separate the stakeholder's requested solution (a dashboard) from the
   underlying problem. State initial assumptions and hypotheses explicitly.
2. **Understand the data.** Assess what signals are available, their quality, coverage,
   freshness, and what important context may be missing. Focus on what the data can and
   cannot support.
3. **Evaluate whether a model is even needed.** Ask whether predictive modeling is
   actually the right tool for the problem, or whether a simpler workflow, rule, or
   process change would solve it better. If the model is relevant, audit what it
   reliably tells us, where it fails, and whether its outputs are fit for the decision.
4. **Define the right intervention.** Decide whether and how the model should be used,
   and design the simplest solution that meaningfully improves the user's workflow.
5. **Define success and trust.** Separate model, operational, and business success.
   Define how value, adoption, and reliability would be measured, and how we'd detect
   when the solution stops working.
6. **Make a clear recommendation.** What to do, why, and what to validate next before
   scaling.

**Core mindset carried through all of the above:** problem first, technology second;
evidence over assumptions; business value over technical novelty.

---

## Entry 2 — Starting with problem framing

**Date:** 2026-09-04

Starting with problem framing before touching the model or data: understanding who the
actual user is, their current workflow, and the whole system around them (Salesforce,
marketing automation, intent vendor, product trial usage), in order to form a first
hypothesis of where the real problem actually sits and what business outcome solving it
would improve. "Build us a dashboard so reps stop guessing" is the VP's proposed
solution, not assumed to be the real problem.

---

## Entry 3 — SDR stack and workflow

**Date:** 2026-09-04

**Prompt used:** "Give me a summary of the SDR's stack with a brief definition of what
each platform actually does (one or two sentences), and map a possible SDR workflow —
don't reference the model or data files at this stage, and flag any workflow step as an
assumption where the brief doesn't confirm it."

**Output:**

Stack (systems named in the scenario, purpose only):

- Salesforce (CRM) — system of record for accounts and activity; where the SDR operates
  day to day.
- Marketing automation platform — runs email/nurture campaigns and produces
  marketing-qualified-lead signals.
- Third-party intent data vendor — supplies external buying-signal data aggregated from
  web research behavior.
- Firmographic/technographic enrichment vendor — supplies static company attributes
  (size, industry, tech stack).
- Web/ad attribution vendor — tracks web visits and ad engagement tied back to an
  account.
- Product usage telemetry — tracks self-serve trial activity, only present for accounts
  that started one.

Possible SDR workflow (assumption, not confirmed by the brief): the SDR works an
assigned slice of the account universe inside Salesforce. Absent a working
prioritization signal, they pick who to call or email next using whatever's visible —
list order, recency, company size — and log the outcome back into Salesforce. That's the
"guessing" the ask is naming: not a lack of accounts to work, but no reliable way to
choose among them.

---

## Entry 4 — Problem, objective, and user workflow (translated from original Spanish notes)

**Date:** 2026-09-04

### What is the problem and the objective?

The VP says he doesn't want reps guessing who to call.

The business objective of this area is straightforward: sell as much as possible
(increase company revenue).

Given the reps' fixed capacity to call and research accounts, we should look to maximize the incremental business value generated from limited Sales capacity.

**Observation:** it would be possible to go further and analyze how the whole area
functions, but given the challenge's bounded context, the scope here is improving the
reps' operation specifically, not the area as a whole.

### User workflow

How does a rep today choose who to call, or where to allocate their time?

I assume some SDR manager, or the system itself, assigns them a list of accounts with
account info to call (to check whether this can be validated in discovery). This
particular investigation is scoped to the SDRs' tasks, leaving whatever happens upstream
as an open question for later.

**Possible process:**

- A rep takes a list of accounts assigned to them in Salesforce.
- Segments it in some way (or not — maybe this is the first point to tackle) and
  prioritizes it (or not).
- Then goes account by account, reviewing the available info to plan the contact.
- Makes contact via email or call.
- Records the outcome.
- The manager exports results and analyzes them somehow to track team metrics and
  targets.

**Open questions carried out of this entry:**

- Do reps only call, or do they also send emails?
- Who uses the marketing automation platform — reps, managers, or both?
- How do reps choose today? Are they really "guessing," or is there already some
  segmentation/selection logic?
- Is the account data provided by our external vendors actually good? (to be evaluated
  in discovery — correlation with conversion)

---

## Entry 5 — Reframing: attention allocation, and is propensity the right signal?

**Date:** 2026-09-04

The VP says reps are "guessing" who to call, and that this is a problem. That immediately
raises two questions: Are they really guessing? and Why is that a problem?

Whether they are truly guessing should be validated during discovery. If it is a
problem, the likely underlying reason is that the account universe is larger than what
reps can realistically cover, which makes rep time and attention the scarce resource.

That leads to the broader business question:

How should Cordilla allocate scarce human sales attention across its non-customer
account base to maximize incremental commercial value?

**Where does an additional hour of rep time create the most value?**

From there, the goal is not simply to identify the accounts most likely to convert, but
to determine which accounts deserve human attention, when, which activities should reps
focus on and which should instead be automated or avoided.

This creates a critical analytical question:

**Is conversion propensity actually the right signal for allocating rep attention?**

An account with high conversion propensity may convert anyway, while another account may
benefit much more from human outreach. So the inherited model's 90-day conversion score
may be useful, but it may not be sufficient for the business decision.

Assuming the ultimate commercial goal is to maximize ARR, the investigation should
determine whether conversion propensity provides enough information to support the
attention-allocation decision, or whether Cordilla needs a different signal, workflow, or
decision framework.

**Summary.** The real constraint is rep time — scarce human attention, not a shortage of
accounts. The key questions this framing raises:

- Are reps actually guessing?
- Where does an additional hour of rep time create the most value?
- **Is conversion propensity actually the right signal for allocating rep attention?**

---

## Entry 6 — Hypotheses for the three key questions

**Date:** 2026-09-04

**Prompt used:** "Give me a hypothesis for each of the three key questions from Entry
5's summary — whether reps are really guessing, where an hour of rep time creates the
most value (help me form this one), and whether conversion propensity is the right
signal (I'd guess yes, what do you think?). Then make them briefer and log them with
this prompt."

**Output:**

- **Are reps really guessing?** Probably not fully — more likely an informal heuristic
  (recency, company size, visible marketing activity) rather than a validated one. To be
  checked in discovery.
- **Where does an hour of rep time create the most value?** Not the highest-propensity
  accounts (may convert anyway) or the coldest ones (unmovable) — value likely
  concentrates on accounts showing some engagement that haven't converted yet, weighted
  by deal size, since the goal is ARR, not conversion count.
- **Is conversion propensity the right signal?** Useful but not sufficient alone — it
  conflates "will convert anyway" with "needs a nudge," and ignores deal size entirely.
  Treat it as one input to the allocation decision, not the decision itself; also worth
  checking in the audit whether the score is confounded with who was already contacted.

