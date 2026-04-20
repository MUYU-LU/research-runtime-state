# Proposal: Source-Matched Control Replicate for Proposal_001

- family: compact_local_equivariant_control
- phase: 4
- jump_type: control
- budget_class: low
- expected_capability_gain: low
- evidence_mode: balanced

## Summary
Materialize a source-matched control replicate of `generation_004/proposal_001` with only minimal implementation-status and bookkeeping differences, so generation_005 can measure variance and avoid over-interpreting small gains from the exploit and jump branches.

## Motivation
The evidence brief repeatedly flags the lack of a same-generation direct control as an important uncertainty. Because the source unit is already strong and future gains may be small, a control is benchmark-critical rather than optional.

## Proposed change
- preserve the source architecture, training recipe, and benchmark contract as faithfully as possible
- do not introduce proposal-specific model changes unless tiny mechanical adjustments are required for clean materialization
- keep runtime, smoke, and launch handling identical to other selected units
- use the result as the main reference point for judging whether exploit and jump gains are real or just variance

## Why this is a fit now
- directly addresses the main interpretability gap in the current continuation context
- keeps the round benchmark-centric by improving confidence in `Q_total` comparisons, not by chasing raw performance alone
- is low-cost and high-value for later selection review

## Risks
- if control variance is itself high, interpretation may remain noisy
- a perfectly faithful replicate may still differ slightly because of stochastic training effects

## Selection notes
This should be treated as a required selection candidate for generation_005.
