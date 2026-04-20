# Proposal: Clean NequIP-Style Interaction Refactor

- family: lightweight_equivariant_refactor
- phase: 4
- jump_type: jump
- budget_class: large
- expected_capability_gain: medium_high
- evidence_mode: balanced

## Summary
Pursue one disciplined representation jump by refactoring the local interaction block toward a cleaner NequIP-like structure, without combining it with an explicit triplet stack in the same unit.

## Motivation
External evidence supports cleaner equivariant interaction composition as a real next-tier capability. The key is to test that idea in isolation rather than repeating an overcombined hybrid design.

## Proposed change
- use the winning proposal_004 direction as the starting point
- upgrade edge handling and equivariant interaction composition toward a more principled local block
- keep the benchmark interface, scalar energy output, and autograd-force path unchanged
- do not add a separate higher-body branch on top of the refactor

## Why this is a fit now
- provides a genuine jump candidate with a higher ceiling than minor winner-family exploits
- isolates representation quality from body-order complexity
- aligns with the evidence brief recommendation for a disciplined jump rather than an overstacked one

## Risks
- higher implementation burden than exploit variants
- may require careful pruning to remain runnable-unit fit

## Selection notes
Useful if selection wants one clean architecture jump beyond the bounded triplet bridge.