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

Given the reps' fixed capacity to call and research accounts, we should look to maximize 
the incremental business value generated from limited Sales capacity.

### User workflow

How does a rep today choose who to call, or where to allocate their time?

I assume some SDR manager, or the system itself, assigns them a list of accounts with
account info to call. This particular investigation is scoped to the SDRs' tasks, leaving 
whatever happens upstream as an open question for later. We will explore the SDRs tasks,
decisions and workflows first to guide the discovery and leave the question of wether the
SDR managers and their decisions should be considered for later (or as next steps depending
in time)

**Possible process:**

- A rep takes a list of accounts assigned to them in Salesforce.
- Segments it in some way (or not — maybe this is the first point to tackle) and
  prioritizes it (or not). We asume they do and will try to test this in audit
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

The VP says reps are "guessing" who to call, and that this is a problem. That
raises two questions: Are they really guessing? and Why is that a problem?

Whether they are truly guessing should be validated during discovery if possible. 
If it is a problem, the likely underlying reason is that the account universe is larger 
than what reps can realistically cover, which makes rep time and attention the scarce 
resource.

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
decision framework. Maby a solution that allows reps to understand at what point in the
conversion funnel a lead is, so they can better time their efforts.

**Summary.** The real constraint is rep time — scarce human attention, not a shortage of
accounts. The key questions this framing raises:

- Are reps actually guessing?
- Where does an additional hour of rep time create the most value?
- **Is conversion propensity actually the right signal for allocating rep attention?**

Our working hypothesis is that the highest-value use of rep time is the work where human judgment and interaction can materially influence a buying decision—such as qualification, direct conversations, objection handling, and tailored follow-up—while activities like account research, signal interpretation, list sorting, and CRM administration create less incremental value and are better candidates for automation. This should be validated with reps and sales managers in discovery to understand where time is actually spent today, which activities they believe most affect conversion, and where they feel automation could free up meaningful selling capacity.

---

## Entry 6 — Hypotheses for the three key questions

**Date:** 2026-09-04

**Prompt used:** "Give me a hypothesis for each of the three key questions from Entry
5's summary — whether reps are really guessing, where an hour of rep time creates the
most value (help me form this one), and whether conversion propensity is the right
signal (I'd guess yes, what do you think?). Then make them briefer and log them with
this prompt."

**Output:**

- **Are reps really guessing?** Hypothesis: Probably not fully — more likely an informal heuristic
  (recency, company size, visible marketing activity) rather than a validated one. To be
  checked in discovery. Probably cant answer this from the provided data, maby by chcking
  correlation of sales_contacts_90d with other variables.
- **Where does an hour of rep time create the most value?** Hypothesis:Not the highest-propensity
  accounts (may convert anyway) or the coldest ones (unmovable) — value likely
  concentrates on accounts showing some engagement that haven't converted yet, weighted
  by deal size, since the goal is ARR, not conversion count. 
- **Is conversion propensity the right signal?** Hypothesis: Useful but not sufficient alone — it
  conflates "will convert anyway" with "needs a nudge," and ignores deal size entirely.
  Treat it as one input to the allocation decision, not the decision itself; also worth
  checking in the audit whether the score is confounded with who was already contacted.

---

## Entry 7 — Parking the three hypothesis questions, moving to the model/data audit

**Date:** 2026-09-05

Leaving the three open questions from Entry 6 (are reps really guessing, where does an
hour of rep time create the most value, is conversion propensity the right signal) as
open for now rather than resolving them further at this stage. Moving next into
auditing the model and data directly, to see what insight that turns up before coming
back to these.

---

## Entry 8 — Key questions for user/team interviews

**Date:** 2026-09-05

Logging a set of questions that can't be resolved from the provided files alone and
should be put directly to the user and team in discovery:

- Who operates the marketing automation platform — reps or managers? What do they
  actually do with it?
- What is the third-party intent vendor data used for, and by whom?
- How does data from external sources (intent vendor, firmographic/technographic
  enrichment vendor, web/ad attribution vendor) and internal usage telemetry integrate
  into the workflow?
- Who monitors trial usage data (assumption: managers)? What decision is made based on
  it?

---

## Entry 9 — Summary: base question, model's role, and the audit question

**Date:** 2026-09-05

The base question here is how to best allocate rep time to maximize business value. This
can be framed as: "Given limited rep capacity, which accounts should receive human sales
attention now, and where will that attention create the most value?"

For this exercise, `converted_within_90d` gives us a measurable proxy for commercial
value, but it is only a proxy. The model predicts likelihood of conversion, not the
incremental effect of a rep contacting an account. So the model should be evaluated as a
tool for better allocation of rep attention, not as proof that contacting a high-scoring
account causes conversion.

**Working hypothesis:** if the model can reliably identify parts of the account base
where conversions are concentrated, and AI can reduce the low-value work required to act
on those opportunities, Cordilla can generate more commercial output from the same rep
capacity.

That leads directly to the audit question:

**Is this model trustworthy enough, and in which situations, to influence how reps
allocate their limited attention?**

**Observation:** we don't currently know how all the available data is used by the
teams (if it's used at all) — this should be addressed with user interviews and deeper
workflow analysis as part of next steps.

Given what we know at this point, and considering that a propensity model was very
promising in the past, it's worth investigating what this model can tell us and whether
further effort is justified. The model alone, though, is probably not enough to solve
the rep-time-allocation problem, since it isn't enough on its own to determine the
next-best-action for reps.

## Entry 10: model framin analysis 

I will now work on the data and model audit to try to determine if the model has any value for our rep time allocation problem, if it is trustworthy and if its performance justifies further efforts on it.

To solve the rep allocation problem two questions should be ansewred: which accounts should they focus on at each given time and what is the next best action?

A model that calculates conversion likelyhood can defifnitely help to direct attention, the pending question would be which of these accounts eed human attention and which dont. Maby the data has a hit to offer on this.

The first question is what decision would be affected by the use of the model and who makes that decision now and how.
At this point we dont really know how accounts are assigned to reps (this is a pending question for user interviews), so we cant determine yet if the model would be used by reps, their managers or both. We dont fully understand how the decision of which accounts to pay attention to is made (we dont know how sales uses the data) so at this point we can only determine if a model has value as an attention driving mechanism or not. The actual use should be determined later, though an assumption will be made to propose a first pilot if the case comes.

Now we will audit the model to frame it generally and see if further efforts are justified. Some research questions are:
- performance: general and across segments (should the model be trusted equally on all accounts or is it more valuable fore some?)
- check for data leakage: if the objective is to score cold accounts, already contacted accounts should be left out of the dataset
- Check for selection bias in the dataset
- check variable correlation to target
- is it still usefull as it is? my first guess would me no. How old is training data? it should probably be retrained as signals may have changed as well as data distributions (data drift) which is probably what killed the first model in teh first place. COmpare training data distribution with data of accounts to score.
- does he model beat basic heuristics?
- 


A conceptual question to be answer further down is how much effort does it take to consolidate this dataset? data sources are varied and probably not integrated. Also maby simpler solutions are not being explored, maby data is not being used at all to prioritize accounts.

How would we know if the model works? at this point we should separate technical metrics from operational metrics and busniness metrics. For the model itself the best metric would probably be conversion lift in the K ranked accounts (where K reflects reps capacity). So if reps can only work 10% of accounts, the metric would be conversion rate in the top 10% by score / overall conversion rate.

Once deployed the best buiness KPI could be revenue per rep hour as it directly reflects model usage impact on economic results. This should be tested in an A/B scenario establishing a baseline with users using the As-Is process and another group using the new model driven process.

Important observation: What does converted_within_90d actually capture? It's a count/binary of conversion, not revenue. If deal sizes vary a lot, a model optimized for conversion probability could systematically undervalue high-ARR accounts — worth checking if any value/size field exists to sanity-check this gap, even informally.

---

## Entry 11 — Adding audit questions and compiling the audit intro

**Date:** 2026-09-05

**Prompt used:** "Before we go into audit, can you think of any other really important
question to be answered at this point to correctly frame the model and make a product
decision?" — asked alongside the performance/segment, correlation, and
staleness/drift questions already drafted for the audit (Entry 10).

**Additional questions proposed:** label leakage/circularity (whether features like
`sales_contacts_90d` are consequences of prior contact rather than independent
predictors, which would make the model learn "who did we already talk to" instead of
"who is likely to convert"); selection bias in the training population (whether
`training_data.csv` is a representative sample of the account universe or already
filtered by past rep/manager selection); calibration of predicted probabilities, not
just ranking quality; baseline comparison against a trivial heuristic; what
`converted_within_90d` actually captures (conversion count vs. revenue/deal size); and
feature parity between `training_data.csv` and `accounts_to_score.csv`.

**Follow-up decision:** dropped the calibration question — not a priority for this
audit. Kept the `converted_within_90d`-captures-revenue question, but as a **noted
limitation rather than a check to run**, since there's no deal-size field available to
resolve it either way.

**Action:** compiled the final objective and 7-question checklist (performance by
segment, variable correlation to target, staleness/drift, label leakage, selection
bias, baseline comparison, feature parity) plus the noted revenue-proxy limitation into
the introduction cell of `audit/model_data_audit.ipynb`, to guide the step-by-step
build of the notebook.
