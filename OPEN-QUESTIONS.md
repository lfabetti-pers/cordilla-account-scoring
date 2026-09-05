# Open questions

Scratchpad for questions that come up during discovery, to be answered (or explicitly
left unanswered) as the work progresses. Unlike `RESEARCH-LOG.md`, this file is a
working draft — freely edited, reordered, checked off, or removed as questions get
resolved. Nothing here is a deliverable on its own. Kept deliberately short: only the
questions the current line of reasoning actually depends on, not every question that
comes to mind.

## Core questions (current focus)

- [ ] Are reps actually guessing today?
- [ ] Where does an additional hour of rep time create the most value?
- [ ] About the model: Is conversion propensity actually the right signal for allocating
      rep attention, or does the decision need something closer to incremental value (uplift) that propensity alone doesn't capture?

## Questions for user/team interviews

- [ ] Who operates the marketing automation platform — reps or managers? What do they
      actually do with it?
- [ ] What is the third-party intent vendor data used for, and by whom?
- [ ] How does data from external sources (intent vendor, firmographic/technographic
      enrichment vendor, web/ad attribution vendor) and internal usage telemetry
      integrate into the workflow?
- [ ] Who monitors trial usage data (assumption: managers)? What decision is made based
      on it?

## Model questions
- [ ] What does converted_within_90d actually capture? It's a count/binary of conversion, not revenue. If deal sizes vary a lot, a model optimized for conversion probability could systematically undervalue high-ARR accounts — worth checking if any value/size field exists to sanity-check this gap, even informally.