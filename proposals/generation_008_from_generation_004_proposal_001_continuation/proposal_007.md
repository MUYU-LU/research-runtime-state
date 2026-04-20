# Proposal 007: Backward-simplify source-tightening ablation

- family: balanced_local_equivariant
- phase: 3
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: low

## Hypothesis
Removing one nonessential mix or normalization detail from the current block may improve reproducibility and calibration by making the source behavior simpler and easier to preserve across datasets.

## Benchmark rationale
The source is already strong, and repeated failed children suggest the search may be overshooting. A backward-simplify slot is useful because it tests whether some current complexity is helping less than assumed, while still being judged on full benchmark metrics, gap behavior, and training recovery.

## Proposed change
- keep the local equivariant trunk and force-from-energy contract
- simplify exactly one bounded mechanism, such as an auxiliary normalization or blend path
- do not remove the core scalar/vector coupling or the atomref baseline
- keep the training regime close to source for attribution clarity

## Why this is worth trying
It satisfies the required simplify slot and provides a disciplined way to test whether the parent is slightly over-tuned rather than underpowered.

## Main risks
- simplification may just lose useful capacity
- could underperform badly on ISO17 if the removed path was carrying subtle local discrimination

## Best-case signal
Equal or slightly better `Q_total` with lower sensitivity, implying the frontier can advance by trimming instead of adding.
