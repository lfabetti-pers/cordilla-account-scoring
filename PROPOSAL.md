# Proposal — Cordilla account scoring

_Draft in progress. Target 800–1,200 words, covering the four required sections._

## 1. Problem framing

To solve the rep allocation problem two questions should be ansewred: which accounts should they focus on at each given time and what is the next best action?

A model that calculates conversion likelyhood can defifnitely help to direct attention, the pending question would be which of these accounts need human attention and which dont.

The first question is what decision would be affected by the use of the model, who makes that decision now and how.
At this point we dont fully understand how the decision of which accounts to pay attention to is made (we dont know how sales uses the data, this is a pending question for user interviews), so we cant determine yet if the model would be used by reps, their managers or both. Right now we can only determine if a model has value as an attention driving mechanism or not. The actual use should be determined later. An assumption will be made to propose a first possible use.

The final proof to understand if the model is helping would be using the appropiate busniess metrics (such as revenue per rep hour spen for example). The questions to guide the audit will be:
- performance: general and across segments (should the model be trusted equally on all accounts or is it more valuable fore some?)
- check variable correlation to target
- is it still usefull as it is? my first guess would me no. How old is training data? it should probably be retrained as signals may have changed as well as data distributions (data drift) which is probably what killed the first model in teh first place. COmpare training data distribution with data of accounts to score.

## 2. Model audit

**I would not ship these scores.** Nothing about this model can be verified, and its
worst defects are in the data rather than the algorithm.

**It cannot be validated.** `training_data.csv` is what the model was fit on and
`accounts_to_score.csv` is unlabeled, so no holdout exists for validation. A separated 
labeled test set is a blocking dependency before any performance claim. *(Entry 18.)*

**The training data does not represent the accounts it would be used on.** It converts
at 6.5%, while real conversion is well under 1% for cold accounts, and 59.4% of its
accounts had already been contacted by a rep, in an account base described as mostly
untouched. This is a sampling problem (or deliberate decision we dont yet undertand), 
not drift: across the two years the data covers, conversion rates and vendor coverage 
stay flat, so the data did not change over time —it was selected badly from the start.

**Two defects from how the data was built:**

- **8.6% of labels are false by construction.** Accounts whose 90-day window hadn't
  closed by 2026-08-01 were recorded as failures — exactly 0.0% conversion against
  5.6–8.1% elsewhere. *(Entry 20.)*
- **The model never had access to its strongest signal.** All 482 blank intent scores
  became the median before training began, though vendor coverage separates 8.2% from
  3.9% conversion inside every size band. *(Entries 20–21.)*

**There is also very little signal to learn from.** Of the nine variables, only two
separate converters by more than sampling noise. One is `sales_contacts_90d`, which
records rep action inside the outcome window and so cannot tell us who to call next. The
other is `intent_score`, where the signal is whether the vendor has coverage (4.4% vs
6.7–10.9%) rather than the value, which has no ordering. The other seven are
indistinguishable from chance. *(Entry 24.)*

**The training dataset has to be re engineered:** retraining on a dataset representing the population being
scored, with closed outcome windows and a missing-indicator flag, measured on a real
holdout.

**One open question.** The population could be deliberately narrowed rather than badly
sampled, so this may be a second-stage model for accounts that already passed another
filter — which would change what it is good for. First question for whoever built it.

## 3. AI-assisted serving design

_How the score actually reaches a rep or SDR manager in a way that changes their day.
Explicitly not a per-account brief document and not a priority-tier / routing rule._

Going back to the problem framing, at this point we dont undertand how rep attention is allocated and how accounts are allocated. For this serving pilot i will aim for a solution that helps reps decide how to spend their time to allow them to focus on the tasks that add maximum value. 

Given the lack of user/manager interviews at this point i will make the following asumption: Rep effort adds the most value where human judgment and interaction can materially influence a buying decision; AI should therefore reduce the surrounding research and administrative work so reps can spend more time on those moments.

In the broader framing of the problem this isnt necesarily a model based solution, maby its workflow automation at a simpler level or simple segmentatios reps may not be using yet. But given the context of the challenge at this point i will explor a model + AI solution.

**What it does** (`serving/draft_outreach.py`). The score picks which accounts are worth
drafting outreach for; an LLM writes the email; the rep approves, edits or rejects it. The
score never reaches the rep — each draft instead carries the three features that moved it
and a plain sentence on why it surfaced.

**The product is the refusal.** With nine numeric fields and no company name, contact or
notes, drafting for everyone is a mail merge. So the system writes only where we hold
something a person would recognise — a trial they started, a request from their team, a
past relationship — and only while that fact is recent enough to still be true. Our own
rep contacts don't qualify: "we called you four times" is no reason to write, and treating
our activity as a buying signal repeats the circularity the audit found. That declines 34
of the top 60 — 17 with nothing sayable, 17 with evidence over 180 days old — and names
which, turning a high score with no usable evidence into a call to make rather than an
email to send.

**Assumptions, all untested.** That reps' scarce resource is judgment rather than typing;
that approving beats writing from scratch; that the activity fields are accurate where
present; and that the score orders candidates well enough to be worth using — the weakest
one, which is why the gates are ordinary code that holds whatever the model does.

**How we would know.** Approval rate reads in week one: if reps reject or rewrite most
drafts, the evidence is too thin and we stop. What they edit says what's missing. Then
reply rate per hundred sends against the current cold baseline, and meetings per rep hour.
Withholding a random share of eligible accounts gives a control group — and that pilot
produces the labeled outcomes the audit named as a blocking dependency.

## 4. Productionization and trust

_Explainability for a rep, what to trust vs. double-check, how it stays current, and
the inside-Salesforce vs. outside-Salesforce tradeoff._


