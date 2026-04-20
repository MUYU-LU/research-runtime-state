# Proposal: Cross-Stage Channel Bottleneck Mix

- family: low_rank_equivariant_local
- phase: 5
- jump_type: jump
- budget_class: large
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Push the `proposal_005` family one step further with a more expressive cross-stage bottlenecked channel-mixing scheme that increases composition capacity without introducing explicit higher-body machinery.

## Motivation
The evidence says low-rank scalar-vector mixing is viable and may have the highest non-control ceiling so far. A true jump should test whether better cross-stage composition can improve `Q_total` beyond simple exploit refinements.

## Proposed change
- keep a two-stage local equivariant backbone
- strengthen learned channel mixing across stages through a bounded bottleneck pathway
- retain scalar energy outputs, autograd forces, and the benchmark contract
- avoid triplet augmentation, since `proposal_003` produced NaN outputs and should not be advanced directly

## Why this is a fit now
- explores a higher-capacity continuation that is still code-fit with the current family
- benchmark-centric, because better dataset balance is the success criterion, not raw force alone
- distinct from both the main exploit and the NequIP-style jump

## Risks
- added composition may overfit or destabilize training
- more capacity can worsen ISO17 energy if not calibrated

## Selection notes
Strong jump candidate when the round wants to bet on `proposal_005` as a ceiling-raising family rather than only a stable exploit source.
