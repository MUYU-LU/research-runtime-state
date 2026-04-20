# Proposal: Multi-Stage Low-Rank Equivariant Mix

- family: minimal_equivariant_local
- phase: 4
- jump_type: jump
- budget_class: large
- expected_capability_gain: medium_high
- evidence_mode: balanced

## Summary
Test a higher-capacity but still bounded jump by combining two-stage interaction depth with low-rank channel mixing in the equivariant pathway, while avoiding explicit extra triplet machinery.

## Motivation
The current winner may still be underpowered in how scalar and vector information mix across stages. This proposal asks whether more structured equivariant composition alone can close part of the remaining gap.

## Proposed change
- extend the proposal_004 family to two stages with stronger learned scalar-vector channel mixing
- keep locality, energy-first prediction, and autograd forces unchanged
- avoid explicit triplet, long-range, or adaptation branches in the same unit
- treat this as a representation-capacity jump rather than a kitchen-sink hybrid

## Why this is a fit now
- probes a different jump axis from the bounded triplet proposal
- keeps the test centered on the validated minimal equivariant family
- may capture some higher-order benefit through composition instead of explicit body-order features

## Risks
- can drift too close to the default exploit if not made meaningfully distinct
- extra capacity may overfit or destabilize under the current epoch budget

## Selection notes
A reasonable third jump slot if selection wants breadth inside the winner family without revisiting proposal_006-style overstacking.