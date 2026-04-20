# Proposal: CACE-Style Higher-Body Bridge

- family: cace_bridge
- phase: 3
- jump_type: jump
- budget_class: large
- expected_capability_gain: medium_high
- evidence_mode: balanced

## Summary
Introduce a CACE-inspired higher-body local representation as a bridge between pair-only invariants and a full irreps-heavy equivariant graph network.

## Motivation
Fresh evidence suggests CACE-style higher-body structure is a plausible bridge jump. It may capture important geometry gains without committing fully to a heavier equivariant stack.

## Proposed change
- add Cartesian or angular higher-body local features around each center atom
- combine these with a compact local interaction module
- preserve scalar energy prediction, autograd forces, and the benchmark interface

## Why this is a fit now
- directly targets the missing body-order structure highlighted by evidence
- offers a distinct jump hypothesis from the minimal equivariant proposal

## Risks
- still a substantial rewrite relative to the source unit
- design details may be more ambiguous than a direct NequIP-style imitation

## Selection notes
Good jump complement to the minimal equivariant branch, especially if the round wants phase-3 to phase-4 bridge coverage.
