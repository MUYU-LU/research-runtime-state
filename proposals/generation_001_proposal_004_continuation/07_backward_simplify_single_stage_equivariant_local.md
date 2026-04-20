# Proposal: Single-Stage Equivariant Local Simplification

- family: backward_simplify_equivariant_local
- phase: 4
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: low_to_medium
- evidence_mode: balanced

## Summary
Simplify the winning `proposal_004` family into an even more regular single-stage equivariant-local baseline with reduced channel count and fewer learned transforms, mainly to measure how much of the gain comes from the core symmetry-aware inductive bias alone.

## Motivation
A backward-simplify branch should now calibrate the winner family itself, not only the original base unit. This branch asks whether the strongest result was driven by the essential local equivariant idea or by fragile extra detail.

## Proposed change
- keep local cutoff geometry, scalar energy prediction, atomref baseline, and autograd forces
- reduce hidden width, auxiliary transforms, or readout complexity relative to `proposal_004`
- keep only the minimal scalar plus directional update needed to preserve the family identity
- avoid adding new branches or deeper interaction depth

## Why this is a fit now
- provides a true simplification anchor around the current winner
- helps selection interpret whether added exploit complexity is justified
- preserves runnable-unit fit and benchmark semantics

## Risks
- likely lower ceiling than the main exploit or jump branches
- if oversimplified, may collapse too much of the useful geometric signal

## Selection notes
Recommended as the one bounded backward-simplify proposal for this continuation family.