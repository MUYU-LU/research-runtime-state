# Proposal: Frequency-Split Edge Filter Wildcard for Proposal_004

- family: nequip_style_local_equivariant
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: medium
- evidence_mode: balanced

## Summary
Create a second wildcard continuation from `generation_003/proposal_004` by replacing its single edge-filter stream with a lightweight frequency-split filter bank, testing whether short-range sharp corrections and smoother medium-range context should be separated before recombining inside the same local equivariant stack.

## Motivation
The strongest `generation_003` unit likely benefits from a cleaner local interaction bias, but one shared radial/filter shaping pathway may still force an awkward compromise between sharp near-neighbor sensitivity and broader smoothing behavior. A bounded frequency-split variant can probe that tension without jumping to a much larger or more expensive family.

## Proposed change
- preserve the local graph, scalar energy contract, atomref baseline, and autograd force path from `proposal_004`
- split the learned edge/filter processing into two bounded channels: one biased toward sharper short-range response and one toward smoother context aggregation
- fuse the two channels with a conservative learned gate or weighted sum before the scalar/vector update blocks
- keep parameter growth moderate and avoid introducing global attention, long-range message passing, or benchmark-contract changes
- retain conservative optimizer and clipping settings close to the source unit

## Why this is a fit now
- gives the round its second wildcard while staying tightly anchored to the current best-performing source architecture
- probes a concrete representational hypothesis about mixed-benchmark behavior rather than adding generic capacity
- remains phase-4 compatible and implementation-feasible as a bounded continuation

## Risks
- filter splitting may add complexity without enough signal to justify it
- if the gate collapses to one branch, the experiment may reduce to a noisier version of the source model
- extra branch interaction could modestly destabilize optimization despite the bounded design

## Selection notes
This should be treated as the higher-variance wildcard in the set. It pairs well with the simpler backward-simplify ablation and the router wildcard so later review can compare structural specialization hypotheses from three different angles.
