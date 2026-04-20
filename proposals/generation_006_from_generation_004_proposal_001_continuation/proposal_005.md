# Proposal: One-Block ACE-Like Scalar Sidepath Jump

- family: compact_local_equivariant_with_late_invariant_manybody_summary
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: moderate_high
- evidence_mode: balanced

## Summary
Inject a tiny ACE-like invariant sidepath into only the second interaction block's scalar update, using low-order local geometry summaries while keeping vector transport and the final energy head structurally familiar.

## Motivation
The evidence allows one narrow many-body path, but advises against framework-scale rewrites. A single-block sidepath is the cleanest way to test whether body-order information helps only when inserted late and locally.

## Proposed change
- compute a narrow invariant many-body summary from existing local neighbors
- feed it only into the second block scalar update
- no head-only retry, no nonlocal branch, no explicit electronic degrees of freedom
- keep width small enough that the parent behavior remains recoverable

## Why this is a fit now
This is a softer jump than proposal_004 and gives the round one body-order test that is clearly inside the allowed evidence boundary.

## Risks
- summary path may be too weak to justify the added complexity
- if the invariant summary is noisy, ISO17 recovery could worsen

## Selection notes
Secondary jump with slightly lower risk than proposal_004.
