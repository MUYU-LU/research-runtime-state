# Proposal 003: Neighbor-normalization taper exploit

- family: balanced_local_equivariant
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: low-medium

## Hypothesis
A lighter-touch taper on the existing neighbor normalization can preserve the parent's strong rMD17 energy behavior while reducing under- or over-suppression of aggregated local signals on ISO17.

## Benchmark rationale
The parent won with balanced energy and force quality, while generation_008 children suggest that gross capacity is not the missing piece. A very small exploit that only retunes how `agg_scalar` and `agg_vector` are scaled is more defensible than any new branch.

## Proposed change
- keep the current block topology and training recipe near-source
- change only the `neighbor_scale` application to a bounded softened form
- preserve the same aggregation statistics and readout contract
- do not add any new invariant summary helper

## Why this is worth trying
It targets one existing calibration lever inside `BalancedInteractionBlock` without disturbing the broader trunk.

## Main risks
- effect may be too small to register
- changing normalization could quietly hurt both energy and force balance

## Best-case signal
Slightly better ISO17 `Q_dataset` while holding rMD17 energy and low gap penalty near the parent.
