# Proposal 008: Exact source-matched control replicate

- family: balanced_local_equivariant
- phase: 4
- jump_type: control
- budget_class: small
- expected_capability_gain: none

## Hypothesis
An exact control replicate of the parent is needed to quantify variance after generation_008 already showed one replicate underperforming by a large margin.

## Benchmark rationale
The parent's lead is too large to dismiss, but generation_008 `proposal_008` at `Q_total 2.5305` shows meaningful run-to-run or implementation-fidelity noise. Another exact control is therefore essential for attribution, especially if a small exploit appears promising.

## Proposed change
- copy the source architecture and training recipe exactly
- make no proposal-specific modeling changes
- preserve all current hyperparameters, data handling, and force-from-energy behavior
- use the result only as a variance anchor for the rest of the round

## Why this is worth trying
Without a clean control, tiny exploit gains or losses will be hard to interpret.

## Main risks
- consumes one slot without opening new capability
- may again underperform due to noise, leaving attribution still messy

## Best-case signal
A control near the parent narrows uncertainty and makes the rest of the round much more interpretable.
