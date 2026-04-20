# Proposal 002: Residual-scale and normalization exploit

- family: balanced_local_equivariant
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: medium


## Hypothesis
The current source already improved over its parent by softening vector residual updates and mixing normalized scalar states. A further bounded exploit is to retune only the residual-scale and normalization blend so the model keeps the same family but recovers more cleanly from mid-training energy spikes.

## Benchmark rationale
The source dossier shows both datasets recovering late after energy spikes. That makes training stability part of the benchmark story, not just an implementation detail. Because `Forces Are Not Enough` warns against overvaluing force-only gains, this proposal aims to improve the energy-force-gap balance rather than chase raw force MAE.

## Proposed change
- preserve the exact interaction topology and feature inventory
- expose a slightly richer but still bounded scalar-mix blend in `BalancedInteractionBlock`
- retune vector residual scaling toward smoother updates at high neighbor count
- keep train.py close to the source, only matching minor calibration if needed

## Why this is worth trying
It is a true exploit of the best-performing mechanism, but narrower than proposal 001. That makes it useful if the selection later wants one very low-risk branch alongside more adventurous candidates.

## Main risks
- may be too small to beat noise or replicate variance
- may slightly over-dampen useful vector updates and hurt ISO17

## Best-case signal
Better late-epoch energy recovery, unchanged runtime reliability, and modest `Q_total` gain from improved calibration rather than larger capacity.
