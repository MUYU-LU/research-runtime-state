# Proposal: Late-Block Single-Site Stream Exploit

- family: compact_local_equivariant_stream_refinement
- phase: 4
- jump_type: exploit
- budget_class: low_medium
- expected_capability_gain: moderate
- evidence_mode: balanced

## Summary
Apply the extra invariant/equivariant recombination only in the second `BalancedInteractionBlock`, leaving the first block untouched so the model keeps an early parent-like local encoding and only refines late features.

## Motivation
Generation_005 suggests that broad changes can lose benchmark balance. A late-only exploit tests whether the parent mostly needs a safer late refinement instead of a stack-wide modification.

## Proposed change
- first block unchanged
- second block gets one bounded stream-refinement helper
- no readout-only redesign, no body-order branch, no nonlocal path
- training stays near the source schedule unless stability demands tiny polish

## Why this is a fit now
It is the most conservative exploit in the set and directly respects the evidence warning against overbroad changes.

## Risks
- may be too weak to move ISO17 enough
- benefits could vanish if the source bottleneck is distributed across both blocks

## Selection notes
Low-risk exploit for preserving source reliability.
