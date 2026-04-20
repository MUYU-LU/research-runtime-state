# Proposal 007: Scalar-mix removal backward-simplify

- family: balanced_local_equivariant
- phase: 3
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: low

## Hypothesis
Removing the auxiliary `scalar_mix_norm` blend entirely may improve reproducibility by making the block closer to the core source interaction logic and reducing opportunities for calibration overshoot.

## Benchmark rationale
Generation_008 `proposal_007` was the best child overall despite still losing badly on ISO17 energy, which strengthens the case that simplification is safer than richer edits. A cleaner backward-simplify test is therefore mandatory and informative.

## Proposed change
- preserve the local equivariant trunk, atomref, and autograd force path
- remove exactly one bounded auxiliary path, namely the scalar mix normalization branch
- keep the rest of the block and training recipe as close to source as possible
- make no readout or framework-level changes

## Why this is worth trying
It directly follows the strongest local signal from generation_008: do less, more faithfully.

## Main risks
- simplification may drop subtle ISO17 discrimination
- could underperform if the removed path was stabilizing harder cases

## Best-case signal
Equal or slightly better `Q_total` with cleaner attribution and lower sensitivity to training variance.
