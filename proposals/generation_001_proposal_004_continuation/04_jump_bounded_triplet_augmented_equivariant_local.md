# Proposal: Bounded Triplet-Augmented Equivariant Local

- family: minimal_equivariant_body_order_bridge
- phase: 4
- jump_type: jump
- budget_class: large
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Add a small triplet-aware local summary on top of the winning equivariant-local family, explicitly as a bounded body-order jump rather than a full hybrid stack.

## Motivation
The evidence brief argues that local angular chemistry is the next plausible gain, but also warns against repeating the overstacked `proposal_006` pattern. This proposal adds one bounded body-order component while keeping `proposal_004` as the center of gravity.

## Proposed change
- preserve the current scalar plus vector local interaction backbone
- add a compact triplet or pair-product summary around each center atom
- merge the resulting body-order signal into the scalar state in a controlled way
- keep scalar energy prediction and autograd forces unchanged

## Why this is a fit now
- directly tests the best bounded jump identified in the evidence brief
- increases expressivity without defaulting to the failed fully stacked hybrid recipe
- keeps the unit diagnosable against the winner-centered exploit branches

## Risks
- body-order features can add complexity faster than they add useful signal
- implementation details need to stay narrow to avoid proposal_006-style sprawl

## Selection notes
Recommended as the main bounded jump complement to the default exploit path.