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

---

## Entry 12 — Check 0: load and inspect the data

**Date:** 2026-09-05

`training_data.csv` = 1,200 rows × 12 cols; `accounts_to_score.csv` = 300 rows × 11
cols (missing `converted_within_90d`, as expected). Main findings from a first look:

- `account_type` includes "Former Customer" alongside "Suspect"/"Prospect" —
  re-conversion may be a different phenomenon than new conversion; worth segmenting.
- `snapshot_date` varies per row (not one shared cutoff), spanning at least
  2024-11-27 to 2026-07-07 in just the first 5 rows — feeds directly into the
  staleness/drift check.
- `intent_score` has missing values.
- `sales_contacts_90d` exists in both files — the feature most relevant to the
  leakage/circularity question, since it may record prior rep action rather than a
  pre-contact signal.

---

## Entry 13 — Check 1: target variable balance

**Date:** 2026-09-05

Hypothesis: 1,200 rows sounds adequate, but if `converted_within_90d` is rare, the
number of positive examples the model actually learned from could be small enough to
make its patterns fragile. Confirmed — only **78 positives out of 1,200 (6.5%)**,
fairly even across `account_type` (5.9%–7.2%). Absolute count is thin: any further
segmentation (industry, size buckets) will likely leave single-digit conversion counts
per segment, so later segment-level and correlation checks need to be read alongside
sample size, not as standalone numbers.

Also noted from the same cell: conversion rate is essentially flat across `account_type`
(Former Customer 7.2%, Prospect 6.6%, Suspect 6.0%), and each type's share of
conversions tracks its share of the dataset. The field that most obviously encodes "how
warm is this account" carries almost no signal about conversion.

---

## Entry 14 — Check 2: what the model is, and global performance

**Date:** 2026-09-05

The model is an sklearn `Pipeline`: one-hot (`account_type`, `industry`) + median
imputation on 7 numeric features → `GradientBoostingClassifier` (40 trees, depth 2,
lr 0.05, subsample 0.7). `snapshot_date` is **not** a feature.

**Caveat on every number below:** no held-out test set exists, and `training_data.csv`
is presumably what the model was fit on, so results are in-sample and optimistic — a
ceiling on real performance, not an estimate. Not retraining or cross-validating, per
the exercise constraints.

Findings: ROC AUC **0.759**; PR AUC **0.231** against a 0.065 base rate. In the
capacity framing that matters for rep attention, the top 10% by score converts at
**26.7% vs. 6.5% base = 4.1× lift**, capturing 32 of 78 conversions within 120
accounts (top 5% = 3.85×, top 20% = 2.69×). There is real ranking signal here.

---

## Entry 15 — Check 3: performance across segments

**Date:** 2026-09-05

Hypothesis: a global AUC could hide a model that works on one slice and not another,
which would argue for "trust the score here, ignore it there" rather than blanket
trust.

Findings: performance is **flat**, not concentrated. ROC AUC 0.715–0.781 across
`account_type` (Prospect 0.759, Suspect 0.781, Former Customer 0.715) and 0.705–0.821
across `industry`. But each industry holds only 11–16 conversions, so that spread is
almost certainly sampling noise rather than genuine segment differences — no segment
justifies a differential trust rule either way.

Open caveat carried forward: the 4.1× lift is only meaningful if it isn't being driven
by `sales_contacts_90d`. Lift on "accounts reps already contacted" would be circular
and useless for the cold-account allocation decision. That is the next check.

---

## Entry 16 — Correction: Entries 14–15 measured nothing, and have been withdrawn

**Date:** 2026-09-05

**The correction.** Entries 14 and 15 reported performance numbers (ROC AUC 0.759,
4.1× lift at top 10%, segment AUCs) that should never have been produced. The first
question to ask about any trained model is how it scored on a properly separated test
set. There isn't one. The model was fit on the same 1,200 rows those numbers were
computed against, so all of it was the model grading its own homework. Those checks
have been removed from the notebook rather than left in with a caveat attached — a
number known to be inflated is worse than no number, because it gets quoted later
without its footnote.

**Where the AI assistant went wrong.** It computed and reported the full performance
suite (global metrics, then a segment breakdown) with the in-sample problem noted only
as a caveat underneath, and framed it as "a ceiling, so still informative." It then
offered cross-validation and temporal-slicing workarounds — data-science moves to
recover a metric — instead of stopping at the finding that matters. This was corrected
in two steps: first the observation that no test set exists at all, then the
instruction to treat the reader as a product owner making a business decision rather
than a data scientist making a modeling decision. That role instruction has been added
to `CLAUDE.md`.

**What replaced it (Check 2 in the notebook).** Rather than measure performance, check
whether measuring it is even possible. The pickle carries fingerprints of its training
data: all seven numeric medians stored by the imputer match `training_data.csv`
exactly, and the class prior stored by the classifier is 0.0650 — exactly the CSV's
conversion rate. Confirmed, not assumed: **the model was trained on all 1,200 labeled
rows we hold.** The pickle stores no metrics, no evaluation date, no split, no author,
no version.

**The finding, stated for the decision:** nobody at Cordilla can currently say whether
this model works. That is a fact about how the model was produced, not a gap in this
audit. It is the same shape as the earlier Cordilla scoring effort that tested well and
quietly lost credibility — and it means validation has to come from live outcomes, not
from these files. The product question is not whether an AUC clears a bar; it is
whether to put never-validated scores in front of reps at all.

---

## Entry 17 — Second correction: Check 2 withdrawn too, and the audit re-pointed at the data

**Date:** 2026-09-05

**What was wrong with Entry 16's fix.** Entry 16 replaced the withdrawn performance
checks with a new Check 2 that verified, via the pickle's stored imputer medians and
class prior, that the model had been trained on all 1,200 rows of
`training_data.csv` — and presented that as a significant finding about missing
provenance. It isn't a finding. The exercise brief states plainly that
`training_data.csv` is the labeled data the model was trained on. The check confirmed
something already given, and dressed a starting condition up as a discovery. That
check has now been removed from the notebook as well.

**The sharper realization.** A performance number was never going to settle whether to
trust this model. Even a properly separated test set carved out of this data would
inherit whatever is wrong with the data itself: if the labels are unreliable or the
population isn't the one reps actually work, a strong AUC against that same population
is measuring the wrong thing accurately. Data defects sit upstream of performance. The
brief points the same way — "if there's something worth finding in an audit, this is
where it lives," about the training data.

**Considered and rejected:** dropping the model investigation entirely on the grounds
that untestable means uninvestigable. Rejected because "we couldn't test it" gets you
sent back to run a test, whereas naming what is actually broken is a decision. The data
findings also outlive this model — defects in the training population would break a
replacement model too — and they price what a real rebuild would cost.

**Three concerns now driving the audit,** all visible by reading `training_data.csv`
against the environment the brief describes:

1. **Base rate far too high.** Real outreach-to-conversion is described as well under
   1% for cold accounts and low single digits with recent engagement. This data
   converts at 6.5% — several times that. This is likely not the population reps would
   be scored against.
2. **Unobservable labels.** `converted_within_90d` needs 90 days to resolve; with
   2026-08-01 as "today," accounts snapshotted after roughly 2026-05-03 cannot have had
   that window close. 2026-06 and 2026-07 snapshot dates appear in the first few rows,
   so some `0`s may mean "not yet" rather than "no."
3. **Informative missingness on `intent_score`.** Missing on ~40% of rows, with vendor
   coverage skewing to larger accounts, so the gap carries information. The pipeline
   median-imputes it (25.3), turning a systematic gap into a systematic fabrication for
   roughly 40% of accounts.

The notebook's audit-question list has been rewritten around these, with model
performance explicitly struck from it and the reasoning recorded in the notebook.
Next decision: which of the three to check first.

---

## Entry 18 — Audit paused: what it concluded and what it asks for

**Date:** 2026-09-05

**Notebook structure decision.** The original seven audit questions have been restored
to the notebook intro unedited, rather than rewritten to match what was actually found.
The point is to show the path the work took — setting out to measure performance,
hitting a wall, and finding something more decision-relevant on the way — instead of
presenting a tidy list that hides the detour.

**The blocking finding, stated plainly:** the available data does not allow us to
independently validate out-of-sample model performance, because no labeled holdout set
is provided. `training_data.csv` is the data the model was trained on and
`accounts_to_score.csv` is unlabeled. Numbers were computed before this was recognised
(~0.76 AUC, ~4× top-decile lift) and were removed rather than published with a caveat,
since the caveat does not survive being quoted in a slide.

**The ask:** a properly separated labeled holdout set is a blocking dependency before
any performance claim about this model can be made.

**Problems with the data and training method, independent of performance:**

1. Training population converts at 6.5%, against real-world rates of well under 1% for
   cold accounts and low single digits for engaged ones — not the population reps work.
2. `converted_within_90d` labels for accounts snapshotted after roughly 2026-05-03
   cannot have been observed by 2026-08-01; those `0`s may mean "not yet," and the model
   was trained as though they meant "no."
3. `intent_score` is missing on ~40% of rows and not at random (vendor coverage skews to
   larger accounts); median imputation to 25.3 turns a systematic gap into a systematic
   fabrication.

**Audit paused here.** These findings are sufficient to decide what to do with the
model. The remaining questions (drift, leakage, baseline comparison, feature parity)
would refine the picture but would not change the conclusion, so they are left
unrun rather than pursued for completeness.

---

## Entry 19 — The training problems in plain terms

**Date:** 2026-09-05

Restating the audit findings without the modeling vocabulary, because the distinction
matters for the decision and was getting lost.

**These are two separate problems.** "No test set" means we cannot *measure* the
model — missing knowledge, not proof of a broken model. The training problems mean it
may have *learned the wrong thing* — that is the substantive issue.

**1. It learned on the wrong crowd.** Trained on accounts that convert 6.5% of the
time; reps face accounts that convert under 1% of the time. When it says "12% likely,"
reality is closer to 1.5%. The probabilities are inflated by roughly an order of
magnitude. Whoever built it took the sample's conversion rate at face value and never
corrected back to the real base rate.

**2. It was taught that some accounts failed when the answer wasn't in yet.** The label
asks "converted within 90 days?" For accounts snapshotted in June/July 2026, 90 days
had not passed by the 2026-08-01 cutoff, yet they are recorded as `0`. The honest value
is "unknown." This is a straight dataset-construction error, and it is the one that
corrupts the learned patterns rather than just the numbers: "recent" correlates with
fresh engagement signals, so the model may have learned "recently-active accounts don't
convert" — an artifact of the cutoff, not a fact about the world.

**3. For ~40% of accounts, one input is invented.** No intent data means the pipeline
fills in the median. The accounts missing intent data are systematically the smaller
ones, so the model treats "we know nothing here" as "perfectly average intent," in a
size-correlated pattern.

**Where that leaves the generalization question.** We cannot claim the model
generalizes. But it is not *proven* worthless either: its probabilities are definitely
wrong, its ranking might partially survive, and problem 2 is the main reason to doubt
even the ranking. For a shipping decision this is already enough — unverified, with
known defects, is not something to put in front of reps as a number to trust.

**Next:** resuming the audit to test whether these three hold up under code, and to
look for further defects of the same kind.

---

## Entry 20 — Checks 3–6: the suspicions tested, one corrected, and what else turned up

**Date:** 2026-09-05

Ran the three suspicions from Entry 19 against the data, plus an integrity sweep.

**Confirmed, and it is the clearest defect in the audit: censored labels.** Conversion
rate by snapshot age runs 7.3% / 8.1% / 5.9% / 5.6% across the older buckets and
**exactly 0.0% across the 103 accounts whose 90-day window had not closed** by
2026-08-01. A hard zero over 103 rows is mechanical, not behavioural — those outcomes
were unobservable and were recorded as failures anyway. So 8.6% of training rows carry
a label that is false by construction, and the base rate the model was fit on (6.50%)
understates the rate among resolvable rows (7.11%).

**Corrected — the brief's stated mechanism for missing intent data is wrong.** The
brief says intent coverage skews toward larger accounts, and Entry 19 repeated that.
The data does not support it: missing rates by company-size quartile are 40.8% / 42.8%
/ 38.6% / 38.4% — essentially flat. Nobody should reason about this field using the
brief's explanation. What *is* true is more useful: accounts **with** intent data
convert at 8.2%, accounts **without** it at 3.9% — better than 2×. Whether the vendor
has coverage on an account is one of the stronger signals present, and median
imputation (25.3, applied to all 482 missing rows) destroys it. A missing-indicator
flag would preserve it.

**New finding — a staleness gap the model cannot see.** Training snapshots have a
median age of 280 days and reach back 711; the accounts to be scored have a median age
of 121 days. The model takes nine inputs and `snapshot_date` is not among them, so it
cannot tell a two-year-old account picture from last month's or discount the stale
ones. Every other distribution (feature means, account-type mix) matches closely
between the two files, making this age gap the substantive difference between what it
learned on and what it would score.

**Circularity: present but modest.** Conversion rises with rep contacts — 4.7% at zero,
~10–14% at four or five, both measured over the same 90 days. Some of that is outreach
working and some is reps picking accounts that already looked good; neither we nor the
model can separate them from this data. A real caveat for a tool meant to choose who to
contact next, but not large enough to explain the model's behaviour by itself, and cell
counts above five contacts are too small to read.

**Ruled out explicitly (negative findings worth stating):** no duplicate account_ids or
rows, no overlap between training and scoring sets, no impossible trial values, no
negatives, identical columns and category sets across both files. The failures are in
how the data was built and labeled, not in how it was assembled or delivered.

**Where this lands.** The model cannot be validated; separately, its training material
has a labeling error across 8.6% of rows, throws away one of its strongest signals
through imputation, and is on average about five months staler than the accounts it
would score. None of this is fixable by tuning — it needs the training set rebuilt.
Whatever gets shipped should not be a score presented to reps as a trustworthy number.

---

## Entry 21 — Correction to Entry 20's intent-data finding, and a confounder ruled out

**Date:** 2026-09-05

**The muddle.** Entry 20 (and the notebook write-up) placed two claims side by side —
that vendor coverage is missing on ~40% of rows, and that the pipeline median-imputes
those blanks — in a way that read as though imputation explained why smaller accounts
carry intent values. It doesn't, and they are facts about different stages. In
`training_data.csv` the 482 blanks are simply blank; nothing is filled in, and the file
itself is never modified. The median substitution (25.3) happens inside the model
pipeline, via `SimpleImputer`, at **fit time as well as predict time** —
`Pipeline.fit()` runs `fit_transform` on the preprocessing steps before the classifier
sees anything, and `GradientBoostingClassifier` rejects NaN outright, so the model was
trained on imputed values and never had the opportunity to learn from missingness at
all. Smaller accounts hold *real* vendor values, at roughly the same coverage rate as
everyone else.

**The brief's size-skew claim fails under both readings.** Entry 20 tested only
coverage. Retested including the second reading — that the *scores themselves* run
higher for larger accounts:

- Coverage by size quartile: 40.8% / 42.8% / 38.6% / 38.4% missing — flat.
- Score values by size quartile: means 27.5 / 27.7 / 28.1 / 28.1, and correlation
  between `employee_count` and `intent_score` of 0.039 — also flat.

So "intent data skews toward larger accounts" is not present in this file either way.

**Confounder ruled out, and the finding strengthens.** The concern was that the 8.2% vs
3.9% conversion gap between covered and uncovered accounts might just be company size
in disguise. It isn't — the gap holds inside every size quartile: 10.0% vs 4.0%, 6.9%
vs 1.5%, 7.7% vs 6.1%, 8.2% vs 4.4%. Whether the vendor has coverage on an account
predicts conversion independently of how big the account is, which makes the pipeline's
median imputation a real loss of signal rather than a cosmetic one: the model cannot
tell "middling intent" from "no coverage at all."

Notebook Check 4 has been rewritten to test all three parts explicitly, and the
findings section corrected to match.

---

## Entry 22 — Why the data diverges from the brief: selection, not drift

**Date:** 2026-09-05

**Hypothesis (mine, as product owner):** the brief's claims about the real world are
correct, and the dataset's divergence from them is evidence either that the sample was
not properly selected or that there has been a large shift in data distribution —
leaning toward the former.

**Tested, and the data supports selection over shift, fairly decisively.**

1. **59.4% of accounts in the sample have already been contacted by a rep** (only 40.6%
   have `sales_contacts_90d == 0`). The universe is described as tens of thousands of
   noncustomers, *mostly untouched*. A sample where the majority has been worked is not
   a draw from that universe. This is the strongest single tell.
2. **Even genuinely cold accounts convert at 4.2%**, not under 1%. Defining cold as no
   rep contact, no MQL, no trial and at most one web touchpoint leaves 71 accounts
   converting at 4.2% against the rest at 7.3%. So the enrichment is not merely a mix
   effect from over-weighting engaged accounts — it runs through the sample, which
   points to the outcome having influenced selection. Caveat: 71 accounts is a small
   base and that rate is noisy.
3. **Distribution shift is actively contradicted.** Over the two years the data spans,
   conversion runs 7.3% / 8.1% / 5.9% / 5.6% by snapshot age — no trend, just noise.
   Intent coverage is similarly flat (40.5% / 40.1% / 39.8% / 36.0%). A shift large
   enough to explain a 6.5%-vs-under-1% gap would show as movement across that span. It
   doesn't. The data is internally stable; what differs is its level against the brief.

**Why this matters for the decision.** The gap cannot be fixed by rescaling the base
rate. If selection had been purely on the outcome, correcting the intercept would leave
the ranking intact. But selection is also on features — contacted accounts, engaged
accounts — so the relationships the model learned come from a slice of the world, and
there is no way from these files to know which of them hold outside that slice.

---

## Entry 23 — Audit findings, consolidated

**Date:** 2026-09-05

Check 7 (selection vs. drift) added to the notebook, and the findings section rewritten
as bullets with the evidence attached to each. The audit's conclusions in full:

- **Performance cannot be validated.** No holdout exists — `training_data.csv` is what
  the model was fit on, `accounts_to_score.csv` is unlabeled. A properly separated
  labeled test set is a blocking dependency before any performance claim.
- **103 rows are labeled false by construction.** Conversion by snapshot age is 7.3% /
  8.1% / 5.9% / 5.6% across older buckets and exactly **0.0%** for the 103 accounts
  whose 90-day window hadn't closed. 8.6% of training rows; true base rate 7.11%, not
  the 6.50% the model was fit on.
- **The sample isn't the population reps work, and it's selection rather than drift.**
  59.4% of accounts have already been contacted in a "mostly untouched" universe; even
  genuinely cold accounts convert at 4.2% against a stated "<1%" (71 accounts, noisy);
  and over the two years the data spans there is no trend in conversion (7.3/8.1/5.9/
  5.6%) or intent coverage (40.5/40.1/39.8/36.0%). Internally stable, wrong level.
  Not fixable by rescaling the base rate, because selection is on features too.
- **The model was never given the chance to learn its best signal.** Accounts with
  intent data convert at 8.2% vs 3.9% without — over 2×, holding inside every size
  quartile, so not size in disguise. All 482 blanks became the median (25.3) *before
  training began*, not merely at scoring time, so the classifier cannot distinguish
  "middling intent" from "no coverage" and never could. A missing-indicator flag would
  have preserved it. The brief's explanation for the gaps (coverage skewing to larger
  accounts) is not true in this file, on either coverage or values.
- **The model is blind to staleness.** Training snapshots median 280 days old (reaching
  711); scoring accounts median 121. `snapshot_date` is not one of its nine inputs.
  Every other distribution matches closely between the files.
- **Circularity present but modest.** Conversion rises with rep contacts (4.7% at zero,
  10–14% at four or five) over the same 90-day window; cause and selection are not
  separable here. Real caveat, not a full explanation.
- **Plumbing is clean.** No duplicates, no train/score overlap, no impossible values, no
  negatives, full feature and category parity. The failures are in labeling and
  sampling, not assembly.

**Bottom line for the proposal:** the model can't be validated, and its training
material is mislabeled on 8.6% of rows, drawn from the wrong population, stripped of
its strongest signal before training began, and about five months staler than what it
would score. None of that is fixable by tuning — it needs the training set rebuilt. Its
scores should not reach a rep as a number presented as trustworthy.

---

## Entry 24 — Check 8: which variables actually carry signal

**Date:** 2026-09-05

Quick test of conversion rate against each variable, run on the 1,097 rows whose
outcome window had closed (the 103 censored rows carry false zeros and would distort
every rate). Ranked by the gap between each variable's best and worst bin, ignoring
bins under 50 accounts, and checked against two standard errors to separate signal from
noise.

**Only two of the nine variables clear sampling noise, and one of them is circular.**

- `sales_contacts_90d` — the widest gap (12.5% at 4+ contacts vs 5.3% at zero, 7.2pp).
  But it records rep action taken inside the same 90 days the outcome is measured, so
  it partly encodes "accounts someone already worked." It cannot be used to decide who
  to work next without assuming the answer.
- `intent_score` — the only clean signal that clears the bar, and what carries it is
  **whether the vendor has coverage at all**, not the number. No coverage converts at
  4.4%; with coverage, 6.7–10.9% *with no ordering across the range* (quartiles run 7.2
  → 10.9 → 6.7 → 10.9). The value is close to meaningless; the presence is the signal.

**Everything else is indistinguishable from chance.** `trial_started` (10.8% vs 6.3%)
and `trial_active_users` are directionally plausible and worth revisiting with more
data, but at 204 and 109 accounts the gaps don't clear two standard errors.
`industry`, `account_type`, `employee_count`, `mql_count_90d` and `web_touchpoints_90d`
are non-monotonic — company size runs 8.3 / 4.8 / 8.0 / 7.3 across quartiles, web
touchpoints 7.9 / 3.8 / 5.4 / 8.0 — which is what noise looks like rather than a
relationship.

**Why it matters.** The model takes nine inputs: one carries clean non-circular signal,
one carries circular signal, and the rest are close to noise. The single clean signal is
the one the pipeline destroys by median-imputing before training. This is the most
compact statement of the audit's case — the problem is the training material, not the
algorithm. There was very little here for any model to learn, and the most usable piece
was discarded before learning began.

---

## Entry 25 — Serving prototype: how the design was chosen, built and tested

**Date:** 2026-09-05

**The constraint that drove everything.** The brief rules out a per-account brief, a
priority tier or routing rule, and a score in a list. All three are things a rep *reads*.
The move that resolved it was to build something a rep **acts on** instead — an artifact
awaiting approval sits outside the excluded set by construction.

**Candidates considered and dropped.** Several designs were worked through before that
was clear: grouping the batch into "plays" by what drives each score; a disagreement queue
comparing the model's ranking against what reps had already worked; a batch-level summary
of which features move scores. Each was rejected on the same test, raised as a challenge
during the session — *why is the score relevant here, couldn't we just sort by variables?*
It was correct, and the honest answer was that in those designs the model was decoration:
the groups came from rules over the features and a `GROUP BY` would produce them. On this
data that is not only a design flaw. With only two of nine variables clearing sampling
noise (Entry 24), a model cannot be doing much a sort cannot.

**Where AI reasoning was overridden.** The assistant's proposals kept the score in a
decorative role while presenting them as model-driven. Two counterfactual designs were
then offered — rescoring each account with one added rep contact, and with recent activity
stripped — which do make the model load-bearing (responsiveness and score are uncorrelated
here, −0.007, with zero overlap in their top tens). Both were rejected as too complex for
the deliverable. The direction that stuck came from the product side: use AI to draft the
outreach itself and let the rep's judgment decide whether it is worth sending, since
judgment is where a rep adds value and drafting is not.

**The objection to that, and the fix.** Cordilla holds nine numeric fields per account and
no company name, contact or notes, so drafting for everyone produces a mail merge — which
at under-1% conversion burns the sending domain. The fix is that the system must know when
it has nothing to say. Two deterministic gates: an account needs evidence a human would
recognise (a trial they started, a request from their team, a past relationship), and that
evidence must be recent enough to still be true. Our own rep contacts were deliberately
excluded as evidence, since treating our activity as a buying signal repeats the
circularity from Entry 20. On the 300 accounts this declines 34 of the top 60 — 17 with
nothing sayable, 17 with evidence over 180 days old. The refusals are the product.

**Built** as `serving/draft_outreach.py`: score once, gate, one LLM call per surviving
candidate (with a documented template fallback, since no API key was available), and a
rep-facing approval queue. Per-account explainability was added afterwards — the three
features that moved each score, found by re-scoring with one feature swapped to typical.

**What testing caught.** Running it, rather than reading it, found four real defects. The
first version counted rep contacts as referenceable evidence, producing drafts justified
by "we called you four times" — the audit's circularity leaking into the product. The
template produced ungrammatical prose. A prose-wrapped or malformed model reply crashed
the live path, which matters because models commonly wrap JSON in text. And a set
`ANTHROPIC_API_KEY` crashed on a missing import, since `anthropic` is deliberately not
pinned. The live path was then exercised offline with stub modules returning a normal
reply, a refusal, wrapped JSON and broken JSON.

**One check that mattered more than the rest:** with a stubbed model refusing every
candidate, the gate counts were unchanged. The refusals are ordinary code, not prompt
instructions, so a model can add refusals but never overturn one.

---

## Entry 26 — Final consolidation: what we'd stand behind in the room

**Date:** 2026-09-05

Pulling together the framing, the numbers, the hypotheses and the assumptions. This is
raw material, not a presentation. Everything here is a **first proposal built on two
static CSVs and no access to the people who use the system** — the open questions in
`OPEN-QUESTIONS.md` are not tidy-up items, they are conditions the proposal depends on.

### The real problem, as we framed it

The ask was "a dashboard so reps stop guessing which accounts to call." We did not accept
that as the problem. Two questions sit underneath it: *are reps actually guessing*, and
*why would that be a problem?* Our answer to the second is what reframed the work: the
account universe (tens of thousands of noncustomers) is far larger than reps can cover, so
the scarce resource is **rep attention, not accounts**. That gives the real question:

> Given limited rep capacity, which accounts should receive human sales attention now, and
> where will that attention create the most value?

Three consequences followed. First, a dashboard is a solution to a different problem —
ranking accounts does not by itself change how an hour of rep time gets spent. Second,
conversion propensity is **useful but not sufficient**: it conflates "will convert anyway"
with "needs a nudge," and ignores deal size entirely, while the commercial goal is ARR
rather than conversion count. `converted_within_90d` is a proxy for value, not value.
Third, the highest-value rep work is where human judgment and interaction can move a
buying decision — qualification, conversations, objection handling — while research, list
sorting and CRM admin are candidates for automation. That last point is a **hypothesis, not
a finding**, and it is the single assumption the serving design rests on.

### What we still don't know, and would ask first

We never learned how accounts are assigned, how reps choose today, or whether the existing
vendor data is used at all — so we cannot yet say whether this belongs to reps, to their
managers, or both. The interview list is in `OPEN-QUESTIONS.md`: who operates the marketing
automation platform, what the intent vendor data is actually used for and by whom, how the
external sources integrate into the workflow, and who watches trial usage and what they do
about it. Alongside those sit the three framing questions we deliberately left open
(Entry 7): are reps really guessing, where does an additional hour create the most value,
and is propensity the right signal or does the decision need something closer to uplift.

### Model audit: what we found

**We would not ship these scores.** The defects are in the data, not the algorithm.

- **It cannot be validated.** No holdout exists — `training_data.csv` is what the model was
  fit on, `accounts_to_score.csv` is unlabeled. A separated labeled test set is a blocking
  dependency before any performance claim.
- **Wrong population.** Trained on data converting at 6.5% against a real-world rate well
  under 1% for cold accounts; 59.4% of its accounts had already been contacted by a rep in
  an account base described as mostly untouched. Selection, not drift — conversion and
  vendor coverage are flat across the two years the data spans.
- **8.6% of labels are false by construction.** 103 accounts whose 90-day window had not
  closed by 2026-08-01 are recorded at exactly 0.0% conversion, against 5.6–8.1% elsewhere.
  True base rate among resolvable rows is 7.11%, not the 6.50% the model was fit on.
- **Its best signal was destroyed before training.** Intent-vendor coverage separates 8.2%
  from 3.9% conversion and holds inside every size quartile, but all 482 blanks became the
  median (25.3) at fit time, so the classifier never could distinguish "middling intent"
  from "no coverage."
- **There was little to learn from.** Only two of nine variables clear sampling noise, and
  one of them (`sales_contacts_90d`) records rep action inside the outcome window, so it
  cannot tell us who to call next without assuming the answer.

**Next step is not retraining, it is rebuilding the dataset:** a sample drawn from the
population reps actually work, outcome windows that have closed, missing-indicator flags
instead of imputation, snapshot age as a feature, and a real holdout. One open question
first, for whoever built it: the population may have been *deliberately* narrowed rather
than badly sampled, which would make this a second-stage model and change what it is for.

### What we built, and why that shape

`serving/draft_outreach.py`. The score selects which accounts are worth drafting outreach
for; an LLM writes the email; the rep approves, edits or rejects. The score never reaches
the rep, and each draft carries the three features that moved it plus a plain sentence on
why it surfaced.

We chose it because it follows directly from the framing: if rep value lives in judgment
and interaction, the right intervention removes the drafting work and leaves the judgment
call — approving or rejecting — with the person. **The product is the refusal.** With nine
numeric fields and no company name, contact or notes, drafting for everyone is a mail
merge, so the system writes only where we hold something a person would recognise and only
while it is recent enough to still be true. On the 300 accounts that declines 34 of the top
60 (17 with nothing sayable, 17 with evidence over 180 days old) and names which — turning
a high score with no usable evidence into a call to make rather than an email to send. The
gates are ordinary code, so they hold whatever the model does and survive it being retired.

### How we would test it

The metric is the one from the framing: **revenue per rep hour**. The chain has two halves
and both must be measured — hours returned per rep per week, and whether the queue's
accounts close better than what reps pick unaided. Approval rate reads in week one and is
the kill criterion: if reps reject or heavily rewrite most drafts, the evidence is too thin
and we stop. What they edit tells us what is missing. Reply rate per hundred sends against
the current cold baseline follows. Withholding a random share of eligible accounts gives
the control group that separates the tool from the rep — and that same pilot produces the
labeled outcomes the audit named as a blocking dependency.

### The honest summary

We inherited an unvalidated model trained on the wrong population with broken labels, and
a request for a dashboard nobody had justified. What we are proposing is a small, reversible
pilot that buys two things at once: some rep capacity back, and the labeled data that would
let anyone answer the question the model cannot currently answer for itself.
