# Proposal: Minimal In-Block Stream Refinement Exploit

- family: compact_local_equivariant_stream_refinement
- phase: 4
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: moderate_high
- evidence_mode: balanced

## Summary
Refine `BalancedInteractionBlock` with one extra invariant recombination path built from existing scalar, `agg_scalar`, `self_vector`, and `mixed_agg_vector`, keeping the source trunk intact while strengthening directional information retention before the residual update.

## Motivation
`generation_004/proposal_001` stayed frontier after generation_005, and the best child signal came from stream separation rather than readout-only enrichment. This is the lowest-friction exploit that follows that evidence while protecting the source unit's strong rMD17 energy calibration.

## Proposed change
- keep the two-block local equivariant architecture and force-from-energy contract
- add a small invariant summary inside `BalancedInteractionBlock`, not only at the head
- let the scalar update see one more bounded cross-stream statistic before `layer_norm`
- avoid nonlocal attention, electronic-state inputs, and framework rewrites

## Why this is a fit now
It directly targets the strongest surviving mechanism clue from generation_005 while staying close enough to fall back toward parent behavior if the added path contributes little.

## Risks
- small uplift only, possibly hard to separate from variance
- too much extra coupling could reintroduce ISO17 instability

## Selection notes
Primary exploit anchor.
