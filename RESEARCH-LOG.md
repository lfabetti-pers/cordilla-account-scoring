# Research log

Kept as work happens. Each entry follows the same structure: Hypothesis, Research plan,
Findings. See `CLAUDE.md` for the update rules — entries are added only on explicit
instruction, with the content given at that time, and are never edited or removed once
written.

---

## Entry 1 — Stack and action plan

**Date:** 2026-09-04

**Stack.** Working in VS Code with Claude Code (Sonnet 5) integrated directly in the
editor, driven interactively throughout. `CLAUDE.md` holds the standing working
principles and required outputs for this project so any session picks up the same
context; this log holds the actual hypotheses, plan, and findings as they happen.

**Hypothesis.** The challenge is deliberately structured to punish jumping straight to
the model (`model.pkl`) or straight to a dashboard. Working problem-first — framing the
decision, understanding the data, and only then asking whether a model is even the right
tool — will produce a more defensible recommendation than starting from what the model
outputs and working backward to a justification.

**Research plan.** Consolidated high-level approach for the exercise:

1. **Frame the problem.** Identify the user, workflow, pain point, and decision to
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

**Findings.** N/A — this entry is the working plan, not a result. Findings land in
later entries as each step is actually carried out.
