# Proposal — Cordilla account scoring

_Draft in progress. Target 800–1,200 words, covering the four required sections._

## 1. Problem framing

_Who makes a decision on this model's output, what that decision is, and what would
tell us it is helping rather than being trusted by default._

To solve the rep allocation problem two questions should be ansewred: which accounts should they focus on at each given time and what is the next best action?

A model that calculates conversion likelyhood can defifnitely help to direct attention, the pending question would be which of these accounts need human attention and which dont.

The first question is what decision would be affected by the use of the model, who makes that decision now and how.
At this point we dont fully understand how the decision of which accounts to pay attention to is made (we dont know how sales uses the data, this is a pending question for user interviews), so we cant determine yet if the model would be used by reps, their managers or both. Right now we can only determine if a model has value as an attention driving mechanism or not. The actual use should be determined later. An assumption will be made to propose a first possible use.

The final proof to understand if the model is helping would be using the appropiate busniess metrics (such as revenue per rep hour spen for example). The questions to guide the audit will be:
- performance: general and across segments (should the model be trusted equally on all accounts or is it more valuable fore some?)
- check variable correlation to target
- is it still usefull as it is? my first guess would me no. How old is training data? it should probably be retrained as signals may have changed as well as data distributions (data drift) which is probably what killed the first model in teh first place. COmpare training data distribution with data of accounts to score.

## 2. Model audit

_What I would trust this model on, what I would not, and whether I would ship its
scores as they are._

## 3. AI-assisted serving design

_How the score actually reaches a rep or SDR manager in a way that changes their day.
Explicitly not a per-account brief document and not a priority-tier / routing rule._

## 4. Productionization and trust

_Explainability for a rep, what to trust vs. double-check, how it stays current, and
the inside-Salesforce vs. outside-Salesforce tradeoff._
