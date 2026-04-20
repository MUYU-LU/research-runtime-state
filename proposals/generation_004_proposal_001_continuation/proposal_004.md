# Proposal: ACE-Inspired Compact Body-Order Summary Jump

- family: compact_local_equivariant_body_order
- phase: 5
- jump_type: jump
- budget_class: medium_high
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Make a phase-5 jump by injecting a narrow ACE-inspired invariant many-body summary path into the existing local equivariant model, aiming to improve angular discrimination beyond pairwise aggregation while preserving the successful energy-first contract.

## Motivation
Fresh evidence points to compact body-order enrichment as the best higher-upside move after readout exploitation. The source unit is strong enough that some generation_005 budget should test whether explicit low-order many-body summaries can lift both datasets, especially ISO17, without forcing a full MACE or irreps-framework transplant.

## Proposed change
- preserve the current trunk, local cutoff graph, atomref baseline, and autograd force path
- add a small invariant body-order summary computed from local neighbor geometry and inject it into scalar updates or the terminal head
- keep the summary low-order and low-width, emphasizing boundedness over completeness
- avoid framework-scale rewrites, external symmetry libraries, or nonlocal branches
- allow only conservative training changes if the extra summary path increases volatility

## Why this is a fit now
- directly follows the evidence brief's best bounded jump direction
- tests whether the frontier is now limited by missing many-body/angular signal rather than by optimizer tuning
- remains scientifically interpretable because the jump is narrow and source-anchored

## Risks
- body-order additions may worsen ISO17 instability if capacity rises too fast
- implementation complexity is materially higher than the exploit proposals
- if the summary path is too weak, the jump may not reveal whether body-order information truly matters

## Selection notes
This should be one of the main jump candidates for generation_005, but it should be interpreted against the simpler exploits and the control.
