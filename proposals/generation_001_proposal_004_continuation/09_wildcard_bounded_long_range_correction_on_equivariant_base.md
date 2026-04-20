# Proposal: Bounded Long-Range Correction on Equivariant Base

- family: long_range_side_branch
- phase: 4
- jump_type: wildcard
- budget_class: large
- expected_capability_gain: uncertain
- evidence_mode: balanced

## Summary
Keep the proposal_004 local equivariant core and add one bounded long-range correction head as a side branch, explicitly deprioritized behind local exploit and body-order probes.

## Motivation
The evidence brief says long-range augmentation is real MLIP territory but not the dominant validated gap for this benchmark pair. This proposal preserves that option without letting it become the default continuation.

## Proposed change
- retain the current local equivariant backbone and benchmark contract
- add a lightweight long-range or latent-charge correction term on top of local features
- keep scalar total energy prediction and autograd forces intact
- bound the branch so it remains diagnosable as a side experiment

## Why this is a fit now
- keeps one speculative branch in the set without displacing the main winner-centered thesis
- may surface useful signal if the local family is nearing its short-range ceiling

## Risks
- weak immediate fit to the current benchmark evidence
- added complexity may not pay off within the round budget

## Selection notes
Wildcard only. Reasonable to leave unselected unless the final mix wants one off-thesis probe.