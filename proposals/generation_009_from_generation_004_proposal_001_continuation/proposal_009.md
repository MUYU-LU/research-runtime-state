# Proposal 009: Training-weight stabilization wildcard

- family: balanced_local_equivariant
- phase: 4
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: low-medium

## Hypothesis
A source-faithful model with only a gentler energy/force weighting schedule may preserve the parent's late training recovery better than architecture edits, especially given the benchmark's sensitivity to balanced energy calibration.

## Benchmark rationale
The parent achieved strong final metrics after recovering from mid-training energy spikes on both datasets. Since most generation_008 architecture edits regressed, one wildcard should test whether the remaining improvement headroom is optimization-side rather than representational.

## Proposed change
- keep `model/model.py` unchanged from the parent
- alter only the training schedule in a bounded way, such as slightly smoother energy warmup or less aggressive force weighting transition
- preserve AdamW, cosine schedule, and gradient clipping scale class
- avoid any broader hyperparameter sweep behavior

## Why this is worth trying
It is orthogonal to the failed micro-architecture edits while still fully consistent with the current family and benchmark contract.

## Main risks
- may just overfit training dynamics without improving benchmark generalization
- could be too close to noise to interpret cleanly

## Best-case signal
Better end-of-training energy recovery, especially on ISO17, while retaining parent-like rMD17 behavior.
