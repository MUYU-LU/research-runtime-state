# Proposal: TAIP-Inspired Adaptation Side Branch

- family: adaptation_side_branch
- phase: 4
- jump_type: wildcard
- budget_class: large
- expected_capability_gain: uncertain
- evidence_mode: balanced

## Summary
Sketch a TAIP-inspired branch that adds a minimal adaptation-oriented auxiliary structure while keeping it clearly labeled as high-risk and poor-fit for immediate execution.

## Motivation
The fresh evidence shows TAIP is benchmark-relevant on MD17 and ISO17 style OOD settings, but it is also a poor implementation fit for the current minimalist base. This branch is included only as a justified high-risk wildcard.

## Proposed change
- keep energy-force outputs and benchmark semantics unchanged
- add only the smallest possible auxiliary adaptation scaffold if selected
- avoid any redesign that would change metric fields or evaluation protocol

## Why this is a fit now
- preserves optional exploration of a benchmark-relevant direction
- keeps the side branch explicit rather than letting it slip into core exploit planning

## Risks
- weakest immediate fit in the whole set
- likely too complex for one bounded round from the current source unit

## Selection notes
Wildcard only. Usually leave unselected unless the round explicitly wants one adaptation research branch.
