# Proposal: Backward-Simplify Single-Stage Proposal_004 Ablation

- family: nequip_style_local_equivariant
- phase: 4
- jump_type: backward_simplify
- budget_class: small
- expected_capability_gain: medium
- evidence_mode: balanced

## Summary
Create a backward-simplify ablation of `generation_003/proposal_004` by collapsing the continuation source into a leaner single-stage local equivariant variant, testing whether much of its gain comes from cleaner inductive bias rather than stacked depth.

## Motivation
A good round should not only test higher-capacity exploits and jumps. It should also check whether the winning source can be simplified without losing too much benchmark value, which helps separate essential structure from implementation overhead.

## Proposed change
- preserve the local equivariant interaction family, scalar energy contract, atomref baseline, and autograd-derived force path from `proposal_004`
- reduce the architecture to a single bounded interaction stage or similarly simplified pathway
- keep training and evaluation benchmark-centric, with no contract changes
- avoid adding any new high-capacity branches, triplets, or long-range components

## Why this is a fit now
- provides the required backward-simplify direction using the actual continuation source rather than an older family
- helps identify whether proposal_004's gains depend on stacked complexity or on a cleaner core interaction design
- stays relatively cheap and interpretable for later round review

## Risks
- simplification may erase too much of the source unit's advantage and become non-competitive
- if too similar to the source, it may not provide a meaningful ablation signal

## Selection notes
This is the default backward-simplify candidate for the `generation_004` set and should be interpreted as an ablation against both the main exploit and the source-matched control.
