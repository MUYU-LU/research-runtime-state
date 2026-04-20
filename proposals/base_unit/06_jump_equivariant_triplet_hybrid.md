# Proposal: Equivariant Triplet Hybrid

- family: equivariant_hybrid
- phase: 4
- jump_type: jump
- budget_class: large
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Combine a very small equivariant local interaction core with explicit angular or triplet summaries so the jump branch probes both directional structure and representation symmetry in one bounded model.

## Motivation
The evidence says the strongest missing ingredients are neighbor interaction and directional structure, with equivariance as the main next-phase leap. This hybrid jump checks whether a compact combination beats either ingredient alone.

## Proposed change
- keep cutoff-local neighborhoods
- add directional edge attributes and a minimal equivariant interaction update
- include a small triplet or angular summary path merged into the readout
- preserve scalar total energy output and autograd forces

## Why this is a fit now
- aligned with the evidence-backed geometry gap
- offers a more expressive jump than pure scalar triplets without going fully deep or wide

## Risks
- implementation complexity is very high for one round
- harder to diagnose whether gains come from equivariance or triplets

## Selection notes
A high-upside jump wildcard. Best selected when the round owner wants one aggressive hybrid branch.
