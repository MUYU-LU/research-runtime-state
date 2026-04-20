# Proposal: Minimal Equivariant Local Interaction

- family: minimal_equivariant_local
- phase: 4
- jump_type: jump
- budget_class: large
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Prototype a minimal local E(3)-equivariant model with radial edge features, directional edge attributes, and one or two lightweight interaction layers while preserving the external benchmark contract.

## Motivation
Fresh evidence identifies a minimal NequIP or MACE-like local equivariant model as the strongest next-phase jump. This proposal tests the phase transition directly instead of only extending the pair-only family.

## Proposed change
- move from scalar-only hidden states to a minimal equivariant representation
- use local edge directions and radial basis features inside a compact interaction block
- keep final outputs compatible with current energy and force interfaces
- keep dataset splits, eval semantics, and metric field names unchanged

## Why this is a fit now
- directly probes the next phase recommended by verified paper and repo evidence
- provides a clean signal on whether the current frontier needs an actual representation jump

## Risks
- highest implementation complexity among the set
- may be slower or more failure-prone under the round budget

## Selection notes
Core jump proposal. Strongly recommended for selection if the round wants at least one true next-phase test.
