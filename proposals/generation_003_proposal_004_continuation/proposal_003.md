# Proposal: Cross-Stage Channel-Mix Jump from Proposal_004

- family: nequip_style_local_equivariant
- phase: 5
- jump_type: jump
- budget_class: large
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Take a bounded jump from `generation_003/proposal_004` by adding a controlled cross-stage channel-mixing path that increases interaction capacity while preserving the winning local equivariant backbone and benchmark contract.

## Motivation
The frontier source already shows that the cleaner proposal_004 family can deliver strong benchmark-centric gains. A jump branch should therefore test whether additional inter-stage mixing can raise capacity further without reverting to the fragility seen in more speculative body-order changes.

## Proposed change
- keep the local equivariant interaction backbone, cosine cutoff envelopes, scalar energy readout, and autograd-derived forces from `proposal_004`
- add a bounded cross-stage scalar/vector channel-mixing or bottleneck path between interaction blocks
- keep the modification local and residualized so the baseline proposal_004 behavior remains recoverable
- tune training for balanced rMD17 and ISO17 behavior rather than an ISO17-only push
- avoid explicit triplets, long-range edges, or benchmark-entrypoint changes

## Why this is a fit now
- provides one serious capacity-increase jump while staying inside a validated family
- builds on an already successful design instead of branching from a weaker source
- tests a meaningful representational extension without taking an uncontrolled phase leap

## Risks
- extra channel mixing could destabilize the cleaner calibration that made proposal_004 work
- if the added path is too weak, it may not separate meaningfully from exploit proposals

## Selection notes
This should be treated as one of the primary jump candidates in the `generation_004` proposal set, paired against exploit and control variants from the same source.
