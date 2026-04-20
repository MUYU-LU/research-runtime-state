# Proposal 003: Neighbor-normalization micro-exploit

- family: balanced_local_equivariant
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: medium

## Hypothesis
A minimal neighbor-count normalization refinement inside message aggregation can reduce dataset-specific calibration drift, especially between rMD17 and ISO17, without altering the overall architecture.

## Benchmark rationale
The source wins because it balances force, energy, and gap metrics across both datasets. A tiny aggregation-normalization exploit is consistent with the evidence brief's call for calibration-preserving edits and gives a direct way to test whether local neighborhood scaling remains slightly mismatched across benchmarks.

## Proposed change
- preserve the current block family and message ingredients
- refine only the aggregation normalization or its interpolation with the raw aggregate
- keep readout, atomref, and force derivation untouched
- avoid adding auxiliary branches or extra summary heads

## Why this is worth trying
It stays inside the safest code surface and addresses a plausible cross-dataset calibration lever rather than inventing new representational machinery.

## Main risks
- could behave like a near-control
- small aggregation changes may still degrade rMD17 energy if the source is already near optimum

## Best-case signal
Improved ISO17 robustness with no regression in rMD17 `mixed_energy_mae`, `gap_penalty`, or final `Q_total`.
