# Proposal 001: Scalar-mix cap exploit

- family: balanced_local_equivariant
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: low-medium

## Hypothesis
A stricter cap on the existing scalar mix path inside `BalancedInteractionBlock` can preserve the parent's rMD17 energy calibration while slightly reducing overshoot risk on ISO17.

## Benchmark rationale
The parent remains the anchor at `Q_total 3.1333` with rare balanced strength across rMD17 (`mixed_energy_mae 0.5927`, `Q_dataset 3.0291`) and ISO17 (`mixed_energy_mae 0.7798`, `Q_dataset 3.3267`). Generation_008 showed direct negative evidence against broader scalar interpolation retries, so the next exploit should be smaller and explicitly source-fallback.

## Proposed change
- keep the current graph, RBF, cutoff, atomref, readout, and force-from-energy contract
- modify only the scalar blend path inside `BalancedInteractionBlock`
- replace the fixed 0.7/0.3 blend with a narrower learned cap or bounded interpolation that can collapse back toward the source behavior
- keep training close to source for attribution clarity

## Why this is worth trying
It stays on the strongest remaining exploit lane from the evidence brief: tiny in-block refinement rather than added capacity.

## Main risks
- may be too conservative to beat variance
- even a tiny scalar recalibration could still hurt rMD17 energy

## Best-case signal
Parent-like rMD17 energy and gap metrics with a modest ISO17 improvement, yielding a real `Q_total` gain.
