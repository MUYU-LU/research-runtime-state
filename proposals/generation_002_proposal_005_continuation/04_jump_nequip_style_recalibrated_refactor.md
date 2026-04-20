# Proposal: Recalibrated NequIP-Style Refactor

- family: nequip_style_local_equivariant
- phase: 5
- jump_type: jump
- budget_class: large
- expected_capability_gain: medium_high
- evidence_mode: balanced

## Summary
Take a bounded jump toward the cleaner interaction style hinted by `generation_002/proposal_004`, but re-center it on cross-dataset benchmark balance so ISO17 upside is not accepted at the cost of rMD17 collapse.

## Motivation
`proposal_004` showed real ISO17 potential yet lost on `Q_total` and had negative `G_delta`. That makes it unsuitable as the main continuation, but still worth a controlled jump branch in a balanced round.

## Proposed change
- adopt a cleaner equivariant interaction refactor inspired by the successful ISO17-oriented branch
- preserve locality, scalar energy prediction, atomref baseline, and autograd forces
- explicitly constrain the design to a benchmark-balanced variant rather than a specialized ISO17 push
- do not revive the unstable triplet bridge from `proposal_003`

## Why this is a fit now
- keeps one serious phase-advancing jump in the set
- uses real local evidence instead of paper-only aspiration
- respects the continuation decision by remaining secondary to the `proposal_005` exploit line

## Risks
- may repeat the dataset skew already seen in `proposal_004`
- larger refactor cost than exploit proposals, with medium implementation friction

## Selection notes
This is a bounded jump for upside, not the default frontier choice.
