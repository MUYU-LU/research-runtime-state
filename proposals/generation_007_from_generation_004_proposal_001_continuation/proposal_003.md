# Proposal 003: Training-calibration exploit around the winning trunk

- family: balanced_local_equivariant
- phase: 4
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: medium


## Hypothesis
If the trunk is already close to optimal, the next gain may come from a benchmark-balanced training recalibration rather than a structural rewrite, specifically by refining energy warmup, force weighting, and optimizer damping around the current source architecture.

## Benchmark rationale
The source is the best completed unit and its train histories are still improving at epoch 8. That suggests there may be remaining optimization headroom. But this should be treated as benchmark-centric calibration work: any gain must preserve rMD17 energy, ISO17 force generalization, and low gap penalties together.

## Proposed change
- freeze the core model family and interaction structure
- adjust only bounded training hyperparameters already present in `train.py`
- emphasize smoother energy recovery and less dataset-specific imbalance
- avoid aggressive schedule changes that could reduce source reliability

## Why this is worth trying
Generation_006 underperformance weakens the case for another readout-only or architecture-heavy swing. A disciplined calibration exploit is a reasonable hedge in the proposal set.

## Main risks
- prior rounds suggest training-only changes may be insufficient
- may produce a near-control outcome with little mechanism learning

## Best-case signal
Slightly better `Q_rmd17` and `Q_iso17` simultaneously through smoother optimization, with no increase in failure or instability.
