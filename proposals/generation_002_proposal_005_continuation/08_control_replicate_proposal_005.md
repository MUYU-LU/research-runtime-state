# Proposal: Control Replicate of proposal_005

- family: control_replicate
- phase: 4
- jump_type: control
- budget_class: small
- expected_capability_gain: none
- evidence_mode: balanced

## Summary
Run an exact replicate of `generation_002/proposal_005` with no intentional architectural, training, evaluation, or contract changes.

## Motivation
Round policy requires exactly one control replicate. Since `proposal_005` is the selected continuation source, the proper control is a direct replicate of that source, while `proposal_007` from generation_002 remains only a historical variance reminder and not an advancement path.

## Proposed change
- exact copy of `generation_002/proposal_005`
- no changes to model architecture, training objective, evaluation logic, metrics, cutoff semantics, or entrypoint contract

## Why this is a fit now
- measures variance around the actual continuation source
- grounds interpretation of small gains from exploit proposals around `proposal_005`
- preserves benchmark-centric comparison discipline

## Risks
- no expected capability gain by design

## Selection notes
This must be the only control replicate in the generation_003 proposal set.
