# Proposal: LES-Augmented Side Branch

- family: long_range_side_branch
- phase: 4
- jump_type: wildcard
- budget_class: large
- expected_capability_gain: uncertain
- evidence_mode: balanced

## Summary
Test a bounded long-range latent-charge augmentation layered on top of a local model, framed explicitly as a side branch rather than the default next step.

## Motivation
Fresh evidence verifies LES as a real capability direction, but also says it is not the first-order fit for the current benchmark gap. This proposal exists to keep that option visible without letting it dominate the round.

## Proposed change
- preserve the existing benchmark contract and local energy-force interface
- add a lightweight latent-charge or long-range correction head on top of local features
- keep the branch bounded and secondary to local-geometry improvements

## Why this is a fit now
- evidence-backed but intentionally deprioritized
- useful if the round owner wants one higher-risk divergence from the main local-geometry thesis

## Risks
- may add complexity without targeting the main source-unit deficiency
- could be hard to stabilize inside one round budget

## Selection notes
Wildcard only. Reasonable to leave unselected unless the final mix needs one speculative side branch.
