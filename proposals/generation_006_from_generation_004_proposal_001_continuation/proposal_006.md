# Proposal: Stream-Refinement Plus Late Summary Hybrid Jump

- family: compact_local_equivariant_stream_refinement_with_narrow_manybody_hybrid
- phase: 4
- jump_type: jump
- budget_class: medium_high
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Combine a very small in-block stream-refinement exploit with one ultra-narrow late ACE-like invariant summary, explicitly limiting both components so the hybrid remains bounded rather than becoming a rewrite.

## Motivation
Generation_005 implied that neither head-only enrichment nor a larger jump reliably beat the parent. This proposal tests whether the missing capability is a careful combination of better stream use plus a tiny body-order cue.

## Proposed change
- add one minimal invariant/equivariant recombination helper in `BalancedInteractionBlock`
- add one late low-width invariant many-body summary near the second block or pre-readout scalar path
- keep total parameter increase tightly bounded
- do not alter locality, autograd forces, or the basic two-block trunk

## Why this is a fit now
It is the highest-upside bounded jump still supported by the evidence, while staying far short of a framework transplant.

## Risks
- combined edits may blur attribution and increase instability
- could repeat the pattern of plausible mechanism with worse benchmark balance

## Selection notes
High-upside jump, but only if the selected set wants one hybrid risk.
