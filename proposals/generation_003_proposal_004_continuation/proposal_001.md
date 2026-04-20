# Proposal: Refined Proposal_004 Exploit with rMD17 Rebalancing

- family: nequip_style_local_equivariant
- phase: 5
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Exploit the strong `generation_003/proposal_004` frontier result by keeping its successful NequIP-style local equivariant refactor, but rebalance training and residual scaling to defend rMD17 while preserving its standout cross-dataset upside.

## Motivation
`generation_003/proposal_004` achieved the best observed non-control `Q_total` in the completed round context available for continuation, which makes it the natural source for `generation_004`. The next safest step is not another large architectural jump, but a bounded exploit that preserves the winning interaction family and targets the remaining calibration risk.

## Proposed change
- keep the local equivariant interaction structure, cosine cutoff envelopes, scalar energy readout, atomref baseline, and autograd-derived forces
- preserve the cleaned interaction refactor introduced in `proposal_004`
- tighten residual and normalization calibration so rMD17 behavior is less exposed to over-aggressive updates
- rebalance training toward more stable cross-dataset energy and force tradeoffs instead of pushing a new phase jump
- avoid triplet branches, long-range components, or benchmark-contract changes

## Why this is a fit now
- exploits the strongest validated source unit directly instead of diffusing effort into another speculative branch
- stays benchmark-centric by targeting balance, not one-dataset specialization
- keeps implementation friction moderate by reusing the already validated family and code surface

## Risks
- the exploit may collapse into a near replicate if the calibration edits are too conservative
- if rebalancing is too strong, it may give back the upside that made `proposal_004` the continuation source

## Selection notes
This should be treated as the default exploit anchor for the `generation_004` round and compared against a control replicate plus more adventurous jump branches from the same source.
