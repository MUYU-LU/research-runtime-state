# Proposal 001: Scalar-mix interpolation micro-exploit

- family: balanced_local_equivariant
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: medium

## Hypothesis
A smaller, explicitly source-fallback interpolation inside `BalancedInteractionBlock` can retain the source unit's rMD17 energy calibration while slightly improving ISO17 by letting aggregated scalar context influence the block update more gently than prior exploit variants.

## Benchmark rationale
The source remains the frontier anchor at `Q_total 3.1333`, with unusually strong rMD17 energy (`mixed_energy_mae 0.5927`) and balanced ISO17 quality (`Q_dataset 3.3267`). Generation_007 exploit-style children regressed, so the next exploit should shrink the edit surface and prioritize preserving energy and gap behavior over adding visible capacity.

## Proposed change
- keep the current local graph, RBF basis, cosine cutoff, atomref baseline, and autograd force path
- keep two `BalancedInteractionBlock`s and the present readout shape
- replace any hard scalar blend with a learned but bounded interpolation that can collapse back toward source behavior
- avoid new branches, extra body-order helpers, or training-loop churn unless strictly necessary

## Why this is worth trying
It directly targets the evidence brief's strongest remaining exploit angle, micro-calibration inside the winning block family, while staying smaller than the failed generation_007 exploit edits.

## Main risks
- may be too conservative to move `Q_total`
- even a tiny scalar-mix change could still nick rMD17 energy quality

## Best-case signal
Flat rMD17 energy and gap metrics with a modest ISO17 gain, yielding a real benchmark-complete improvement over the source.
