# Proposal 001: In-block invariant recombination exploit

- family: balanced_local_equivariant
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: medium


## Hypothesis
The strongest bounded exploit is to enrich `BalancedInteractionBlock` with one extra invariant recombination path derived from existing `self_vector`, `mixed_agg_vector`, `agg_norm`, and alignment statistics, because the source already wins benchmark-completely but still compresses late directional content too aggressively at the readout.

## Benchmark rationale
The source is strong on both rMD17 and ISO17, with especially clean rMD17 energy (`mixed_energy_mae 0.5927`) and a reliable `Q_total 3.1333`. Since generation_006 variants all regressed, the next attempt should preserve this calibration-first regime rather than introduce a large architectural jump. The target is a small gain in directional expressivity that does not worsen `gap_penalty`, late-epoch recovery, or runtime reliability.

## Proposed change
- keep the present local graph, Gaussian RBF basis, cosine cutoff, atomref baseline, and autograd force path
- keep two `BalancedInteractionBlock`s
- add one compact invariant summary branch inside each block before the scalar residual update
- let the new statistic modulate scalar updates, not replace them
- keep readout and training loop close to source unless a small matching retune is clearly needed

## Why this is worth trying
This directly matches the evidence brief's strongest mechanism and stays closest to the current winning code surface. It is the cleanest exploit candidate for improving both datasets without giving up the source unit's stable training recovery.

## Main risks
- could collapse into a near-replica with negligible gain
- could help force detail while slightly hurting energy, which would reduce `Q_total`

## Best-case signal
Small improvement in ISO17 discrimination with flat or slightly improved rMD17 energy and unchanged runtime stability.
