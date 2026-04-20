# Proposal: Control Replicate of Generation_003 Proposal_004

- family: nequip_style_local_equivariant
- phase: 4
- jump_type: control
- budget_class: medium
- expected_capability_gain: baseline_variance
- evidence_mode: balanced

## Summary
Use `generation_003/proposal_004` itself as the control replicate for the `generation_004` round so later review can distinguish continuation gains from simple rerun variance on the current strongest benchmark-balanced unit.

## Motivation
`proposal_004` is the dominant performer of `generation_003` by `Q_total`, so the next round needs a direct source-matched control, not just a historical control inherited from `generation_002/proposal_005`. This replicate anchors interpretation of exploit, jump, simplify, and wildcard continuations built from the same source.

## Proposed change
- no proposal-specific architecture edits beyond faithfully materializing the source unit
- preserve the exact local equivariant interaction refactor, cutoff behavior, scalar energy head, atomref baseline, and autograd-derived force path from `generation_003/proposal_004`
- keep training and launch settings aligned with the source unit unless round-level execution policy requires a standard metadata refresh
- record it explicitly as the source-matched control replicate for later benchmark-centric comparison

## Why this is a fit now
- provides the round's required control proposal tied to the actual continuation source
- allows later review to compare new proposals against rerun variance of the best known source rather than against an older family baseline alone
- keeps the round scientifically interpretable as the search moves outward from the current frontier unit

## Risks
- consumes one selected slot without offering directional novelty
- if infrastructure variance is low, the replicate may add little information beyond confirmation

## Selection notes
This proposal should usually be selected as the round control unless inspection or later evidence indicates that a different replicate is required for workflow consistency.
