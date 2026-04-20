# Proposal 002: Vector residual attenuation exploit

- family: balanced_local_equivariant
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: low-medium

## Hypothesis
A more source-tight residual scale on the vector update can keep the useful directional signal while reducing the calibration damage seen from slightly richer vector perturbations in generation_008.

## Benchmark rationale
Generation_008 `proposal_002` showed that even a narrow vector recalibration regressed badly, but that does not rule out a smaller attenuation-style exploit. The source already has a valid invariant/equivariant balance, so the safer question is whether it benefits from less vector residual freedom rather than more.

## Proposed change
- keep the present `directional_invariant`, `agg_norm`, and `vector_alignment` structure
- edit only the residual-scale path for `delta_vector`
- use a tighter bounded scale or source-anchored gate that cannot amplify beyond the current regime
- avoid adding new late summaries or readout changes

## Why this is worth trying
It probes the evidence-backed idea that the frontier may be slightly over-mixed, using one of the narrowest possible edits.

## Main risks
- may remove helpful angular sensitivity
- could still regress both datasets if the source scale is already near-optimal

## Best-case signal
Improved stability and slightly better ISO17 without losing the parent's rMD17 energy advantage.
