# Proposal 008: Source-matched control replicate

- family: balanced_local_equivariant
- phase: 4
- jump_type: control
- budget_class: small
- expected_capability_gain: none


## Hypothesis
A faithful control replicate of `generation_004/proposal_001` is still worth carrying because the best completed generation_006 child was effectively a control-like result, and that outcome is important for interpreting whether future changes beat source variance or only noise.

## Benchmark rationale
The continuation source remains the best completed benchmark unit. Since later children underperformed it, selection needs at least one clean control option to anchor round-level interpretation of `Q_rmd17`, `Q_iso17`, `Q_total`, energy trends, and runtime reliability.

## Proposed change
- replicate the current source family with no intended proposal-specific architectural change
- preserve the same local force-from-energy contract and training regime
- allow only the minimal paperwork needed for control materialization later

## Why this is worth trying
It satisfies the required control slot and improves later attribution discipline. A new candidate should not be called a win unless it beats both the source anchor and a source-matched control.

## Main risks
- no new capability by design
- could consume a selection slot if overvalued relative to mechanism-testing branches

## Best-case signal
A stable benchmark reference that lets the round separate real gains from replication variance.
