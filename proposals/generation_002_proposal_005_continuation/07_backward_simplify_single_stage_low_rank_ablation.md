# Proposal: Single-Stage Low-Rank Ablation

- family: backward_simplify_low_rank_local
- phase: 4
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: low_to_medium
- evidence_mode: balanced

## Summary
Create a bounded backward-simplify branch by compressing `proposal_005` into a single-stage low-rank local equivariant baseline, mainly to measure how much of its gain comes from the low-rank idea itself versus stacked-stage complexity.

## Motivation
Balanced rounds need one simplification anchor near the current continuation source. `proposal_006` showed simplification is viable but not frontier-leading, so the next simplify branch should be tighter and more diagnostic.

## Proposed change
- reduce `proposal_005` from two stages to one stage
- keep one bounded low-rank scalar-vector mixing pathway so the family identity remains visible
- preserve local cutoff semantics, scalar energy prediction, atomref baseline, and autograd forces
- avoid extra branches or refactors

## Why this is a fit now
- satisfies the requirement for at least one bounded backward-simplify proposal
- helps interpret whether depth or low-rank mixing is the more important ingredient
- remains benchmark-centric by evaluating total cross-dataset quality, not just compute savings

## Risks
- likely lower ceiling than the exploit and jump branches
- oversimplification may erase the useful representation signal entirely

## Selection notes
This should be the only backward-simplify proposal in the set.
