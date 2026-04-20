# Proposal 007: Backward simplification of scalar-mix complexity

- family: simplified_balanced_local_equivariant
- phase: 4
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: low_to_medium


## Hypothesis
Some of the current source gain may come from only part of its modifications, while the rest adds variance or hidden calibration cost. A backward-simplify proposal can test whether a slightly simpler scalar-mix path preserves most of the source performance while improving robustness.

## Benchmark rationale
This is not a retreat from benchmark ambition. It is an attribution-focused hypothesis grounded in the fact that later descendants underperformed the source. If the present source is mildly over-tuned, simplification could improve generalization and reduce sensitivity in both datasets.

## Proposed change
- keep the family, graph, basis, and force-from-energy contract
- simplify one part of the scalar mixing or residual gating path
- preserve the successful training regime unless simplification clearly requires a small retune
- treat any improvement as evidence that the frontier has extra complexity without benchmark benefit

## Why this is worth trying
The round needs at least one backward-simplify candidate, and this source is exactly the kind of strong-but-calibration-sensitive unit where simplification may pay off.

## Main risks
- simplification may simply give up useful expressivity and fall below the source on both datasets

## Best-case signal
Equal or better `Q_total` with flatter train dynamics and lower calibration sensitivity.
