# Proposal: Rich Invariant Readout Exploit from Proposal_001

- family: compact_local_equivariant_readout_enrichment
- phase: 4
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Exploit the current frontier source by keeping its two-block local equivariant trunk intact and replacing the norm-only terminal readout with a richer invariant summary of vector structure, targeting ISO17 uplift while preserving the source unit's strong rMD17 energy calibration.

## Motivation
`generation_004/proposal_001` already delivers balanced frontier quality with `Q_total = 3.1333`, very strong rMD17 energy (`0.5927` mixed) and strong ISO17 quality (`Q_iso17 = 3.3267`). The clearest remaining bottleneck is representational, not reliability: the final energy head only sees `vector_norm`, even though the trunk already learned more meaningful scalar-vector coupling.

## Proposed change
- preserve local graph construction, atomref baseline, energy-first total-energy contract, and autograd-derived forces
- keep the existing two `BalancedInteractionBlock`s unchanged or nearly unchanged
- augment the final per-atom readout with extra invariant summaries derived from vector channels, such as self-channel correlations, channelwise alignment statistics, and bounded scalar-vector bilinears
- keep the change concentrated in `model/model.py`, with at most minor `train.py` polish if needed for stability
- avoid nonlocal branches, irreps-heavy rewrites, or benchmark-contract changes

## Why this is a fit now
- directly matches the freshest evidence brief's strongest recommendation
- attacks the most visible source bottleneck with low-to-medium implementation friction
- stays benchmark-centric by aiming for ISO17 improvement without giving back rMD17 energy or widening split gaps

## Risks
- if the new invariant head is too expressive, ISO17 volatility could worsen
- if the added features collapse to the existing norm-only signal, the run may behave like a near replicate

## Selection notes
This should be treated as the primary exploit anchor for generation_005 and a likely first-tier selection candidate.
