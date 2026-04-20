# Proposal: Control Replicate of base_unit

- family: control_replicate
- phase: 1
- jump_type: control
- budget_class: small
- expected_capability_gain: none
- evidence_mode: balanced

## Summary
Run an exact replicate of the current best `base_unit` with no intentional architectural changes.

## Motivation
Round policy requires one control replicate to measure run-to-run variance. This branch is not for improvement, only for calibration.

## Proposed change
- exact copy of the current source unit
- no changes to model architecture, training objective, evaluation logic, metrics, or contract

## Why this is a fit now
- mandatory variance estimate
- helps interpret whether small gains from exploit branches are real

## Risks
- no expected capability gain by design

## Selection notes
Must remain eligible for selection as the round control.
