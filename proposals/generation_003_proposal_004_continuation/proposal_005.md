# Proposal: Control Replicate of Proposal_004

- family: nequip_style_local_equivariant
- phase: 5
- jump_type: control
- budget_class: medium
- expected_capability_gain: none
- evidence_mode: balanced

## Summary
Run an explicit control replicate of `generation_003/proposal_004` to estimate variance around the currently selected continuation source before over-interpreting exploit or jump gains in `generation_004`.

## Motivation
The workflow requires a control in every round, and the strongest way to interpret new proposal_004-based branches is against a same-source replicate rather than only against older family controls.

## Proposed change
- keep `generation_003/proposal_004` unchanged as the direct replicated baseline
- preserve the exact local equivariant interaction family, energy readout, atomref baseline, and autograd-derived force path
- use the same benchmark contract, budget class, and training surface as the source unit
- avoid any architecture or training modifications beyond what the control mechanism requires

## Why this is a fit now
- gives the round a variance anchor centered on the actual continuation source
- prevents over-claiming gains from proposal_004-derived exploit and jump branches
- stays maximally interpretable for selection and post-run evidence review

## Risks
- consumes one execution slot without adding architecture novelty
- if variance is low, the control may contribute little beyond confirmation

## Selection notes
This is the mandatory control candidate for the `generation_004` set and should be included unless a stronger source-matched control becomes necessary for policy reasons.
