# Proposal: Dataset-Balance-Regularized Anchor Hybrid

- family: balanced_equivariant_hybrid
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: medium
- evidence_mode: balanced

## Summary
Use a wildcard branch that deliberately blends the `proposal_005` continuation source with the balanced behavior lessons from `proposal_001`, emphasizing explicit dataset-balance regularization rather than raw capacity expansion.

## Motivation
The round evidence says the frontier is split between higher ceiling (`proposal_005`) and healthier cross-benchmark balance (`proposal_001`). A wildcard proposal can test whether that tension is best handled by regularized hybridization instead of deeper architecture change.

## Proposed change
- keep a local equivariant two-stage structure with bounded low-rank mixing
- bias the design toward cross-dataset balance and stable energy calibration
- preserve benchmark outputs, locality, and autograd force consistency
- avoid control-only replication and avoid reviving the NaN-prone triplet branch from `proposal_003`

## Why this is a fit now
- directly expresses the balanced generation_003 framing
- gives selection a nonstandard but still bounded option
- stays benchmark-centric by treating `Q_total` and `G_delta` as the real objective

## Risks
- could become too conceptually broad if not kept tightly bounded
- hybrid design may be harder to interpret than a clean exploit or jump

## Selection notes
Useful as one wildcard slot when the round wants a deliberately balance-seeking proposal rather than another pure capacity branch.
