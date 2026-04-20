# Proposal 010: Block-depth asymmetry wildcard

- family: balanced_local_equivariant
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: low-medium

## Hypothesis
Keeping two interaction blocks but making only the second block slightly more source-tight than the first may preserve early local mixing while reducing late-stage calibration drift.

## Benchmark rationale
The evidence points to overshoot risk inside `BalancedInteractionBlock`, but does not prove that both blocks should share identical refinement strength. A block-asymmetric wildcard explores whether the second pass is where excess mixing is entering, without introducing a new family.

## Proposed change
- preserve the two-block architecture and current readout
- apply a tiny refinement or attenuation only to the second `BalancedInteractionBlock`
- leave the first block at the parent behavior for a clean staged comparison
- do not add any late summary helper, nonlocal branch, or readout-only retry

## Why this is worth trying
It is still small and local, but probes a different failure mode than uniform edits across both blocks.

## Main risks
- could complicate attribution relative to simpler exploits
- may still be too invasive if the parent's symmetry across blocks is important

## Best-case signal
Improved benchmark balance from preserving early directional extraction while calming late-stage calibration drift.
