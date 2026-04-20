# Proposal: Residual-Gated Dual-Statistic Stream Exploit

- family: compact_local_equivariant_stream_refinement
- phase: 4
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: moderate
- evidence_mode: balanced

## Summary
Keep the source architecture but split the added in-block invariant summary into two cheap statistics, one alignment-like and one magnitude-contrast-like, then gate their contribution through the existing scalar residual path.

## Motivation
The evidence brief says another head-only retry is weakly justified. A dual-statistic exploit tests whether the parent needs slightly richer internal summaries rather than a bigger architecture jump.

## Proposed change
- preserve neighbor construction, atomref, and two interaction blocks
- add two narrow invariant summaries inside each `BalancedInteractionBlock`
- inject them only through the scalar residual gate, not through a new large subnetwork
- keep parameter growth and train-schedule changes minimal

## Why this is a fit now
This stays inside the validated family, but is more structural than the failed generation_005 readout-heavy variants.

## Risks
- may still be too close to the parent to beat `Q_total = 3.1333`
- added summary terms could help ISO17 while slightly hurting rMD17 energy

## Selection notes
Second exploit, complementary to proposal_001 but slightly more expressive.
