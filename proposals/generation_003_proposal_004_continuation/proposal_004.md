# Proposal: Energy-Head Recalibration Jump on Proposal_004

- family: nequip_style_local_equivariant
- phase: 5
- jump_type: jump
- budget_class: large
- expected_capability_gain: medium_high
- evidence_mode: balanced

## Summary
Keep the successful `proposal_004` local equivariant backbone, but introduce a bounded energy-head recalibration branch aimed at improving cross-dataset energy behavior without sacrificing the geometric gains already demonstrated by the source unit.

## Motivation
The frontier source looks strong enough that the next jump should not replace its interaction family. Instead, it should probe whether additional benchmark gain is available through better energy calibration and dataset balance on top of the same representational core.

## Proposed change
- preserve the local equivariant interaction stack, cosine cutoff machinery, atomref baseline, and autograd-derived forces from `proposal_004`
- add a bounded auxiliary calibration path or fused energy-head correction on top of the learned scalar summary state
- keep the added path lightweight, residualized, and removable so the base proposal_004 behavior remains the dominant path
- target balanced rMD17 and ISO17 energy/force outcomes rather than chasing one-dataset upside
- avoid triplet constructions, long-range branches, or benchmark-contract edits

## Why this is a fit now
- gives the proposal set a second serious jump axis distinct from channel mixing
- focuses on the most plausible remaining bottleneck after a strong benchmark-centric source win
- stays implementable within the same validated code surface

## Risks
- extra energy calibration may overfit mixed energy while disturbing force quality
- if calibration is too weak, this may not separate enough from exploit proposals

## Selection notes
This should be treated as a benchmark-balance jump candidate, complementary to the cross-stage mixing jump and directly compared against exploit variants from the same source.
