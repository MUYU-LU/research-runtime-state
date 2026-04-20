# Proposal: Sparse-Neighbor Cleanup on Low-Rank Base

- family: low_rank_equivariant_local
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: medium
- evidence_mode: balanced

## Summary
Test whether the `proposal_005` family is being limited partly by graph construction and neighbor bookkeeping rather than only by representation depth, using a bounded sparse-neighbor cleanup wildcard.

## Motivation
Prior proposal style allowed infrastructure-cleanup hypotheses as long as they preserved benchmark semantics and runnable-unit fit. This branch asks whether a cleaner local neighborhood pipeline can improve training stability and dataset balance without changing the core scientific contract.

## Proposed change
- keep the low-rank two-stage local equivariant model family intact
- simplify or regularize neighbor construction, masking, or edge-feature handling in a bounded way
- preserve cutoff semantics, benchmark outputs, scalar energy prediction, and autograd forces
- avoid changing datasets, metrics, or entrypoint behavior

## Why this is a fit now
- provides a non-architectural wildcard branch inside the chosen continuation family
- may recover benchmark quality through cleaner execution rather than more capacity
- complements the proposal_001 anchor, which pointed toward disciplined rather than maximal complexity

## Risks
- infrastructure cleanup may produce only marginal gains
- if too implementation-driven, it can drift away from a clear research hypothesis

## Selection notes
Good wildcard coverage when the round wants one branch that tests pipeline cleanliness instead of representational expansion.
