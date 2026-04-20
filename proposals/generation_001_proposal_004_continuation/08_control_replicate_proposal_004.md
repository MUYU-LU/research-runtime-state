# Proposal: Control Replicate of proposal_004

- family: control_replicate
- phase: 4
- jump_type: control
- budget_class: small
- expected_capability_gain: none
- evidence_mode: balanced

## Summary
Run an exact replicate of `generation_001/proposal_004` with no intentional architectural, training, evaluation, or contract changes.

## Motivation
Round policy requires exactly one control replicate, and the correct control for this continuation source is the current winning unit rather than the original base unit.

## Proposed change
- exact copy of `generation_001/proposal_004`
- no changes to model architecture, training objective, evaluation logic, metrics, cutoff semantics, or entrypoint contract

## Why this is a fit now
- measures run-to-run variance for the current best family
- provides the anchor needed to interpret small improvements from winner-centered exploit proposals

## Risks
- no expected capability gain by design

## Selection notes
This should be the only control replicate in the set.