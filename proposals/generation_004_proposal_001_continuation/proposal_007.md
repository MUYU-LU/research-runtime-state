# Proposal: Backward-Simplify Single-Block Readout Stress Test

- family: compact_local_equivariant_simplified
- phase: 3
- jump_type: backward-simplify
- budget_class: low
- expected_capability_gain: low_medium
- evidence_mode: balanced

## Summary
Run a backward-simplify ablation by collapsing the source model to a single interaction block while retaining the improved invariant readout path, testing whether the current frontier owes more to head quality than to stack depth.

## Motivation
The source unit is strong, but same-generation control evidence is missing and complexity can conceal where the real gains came from. A disciplined simplification can clarify whether two interaction blocks are necessary for the current benchmark level or whether a cheaper model with a better head preserves most of the value.

## Proposed change
- reduce the trunk from two interaction blocks to one
- keep atomref, local graph construction, energy-first contract, and the best available invariant readout design
- keep optimizer settings conservative and simple
- avoid new body-order, nonlocal, or higher-order mechanisms
- treat the proposal as an attribution and efficiency probe, not a frontier-only bet

## Why this is a fit now
- satisfies the round requirement for a backward-simplify proposal with real interpretive value
- can reveal whether generation_004 gains are concentrated in readout calibration rather than stacked interaction depth
- may improve stability or runtime even if raw `Q_total` drops modestly

## Risks
- likely ceiling loss on ISO17 or hard OOD rMD17 if depth is truly necessary
- if readout changes are also included, attribution may still not be perfectly clean

## Selection notes
This is valuable for round interpretation and efficiency mapping. It is not the main frontier bet, but it is a good candidate if the selected set needs one informative low-budget contrast.
