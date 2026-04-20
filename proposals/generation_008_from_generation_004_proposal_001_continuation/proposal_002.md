# Proposal 002: Vector residual gate micro-exploit

- family: balanced_local_equivariant
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: medium

## Hypothesis
A tighter residual-scale gate on the vector update can preserve the source trunk while reducing overreaction to directional messages, improving cross-dataset calibration without changing the model family.

## Benchmark rationale
The source already shows improving late-epoch trends on both datasets, so the issue is not missing gross capacity but maintaining calibration while preserving directional signal. Since prior exploit variants likely moved too much at once, a one-parameter-style vector residual recalibration is a better fit for the current evidence.

## Proposed change
- keep the present scalar update path and readout contract
- modify only the vector residual scaling logic inside `BalancedInteractionBlock`
- ensure the new parameterization remains bounded and source-faithful
- leave optimizer, schedule, and force-from-energy semantics unchanged unless needed for exact compatibility

## Why this is worth trying
It is the narrowest meaningful exploit candidate for testing whether directional retention can improve without repeating the broader failed representational moves from generation_007.

## Main risks
- effect size may be negligible
- too much damping could reduce useful angular discrimination on ISO17

## Best-case signal
Slightly better ISO17 force and energy behavior with unchanged rMD17 energy stability and runtime cleanliness.
