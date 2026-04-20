# Proposal: Backward Simplify Atomwise Local Baseline

- family: backward_simplify_local
- phase: 1
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: low_to_medium
- evidence_mode: balanced

## Summary
Simplify the current pair-scoring architecture into a more regular atomwise local baseline with fewer moving parts, mainly to test variance, optimization stability, and whether some current pair interactions are unnecessary noise.

## Motivation
A backward-simplify branch is useful for calibration. It can reveal whether the current pair MLP is already overcomplicating a weak local signal and can provide a cleaner baseline for later rounds.

## Proposed change
- keep cutoff-locality, atom embeddings, and RBF distance features
- reduce depth and parameter count in the interaction stack
- aggregate local evidence into atomwise states with a simpler scalar readout
- preserve the same train and eval interfaces

## Why this is a fit now
- gives a lower-complexity comparison against richer exploit branches
- may reduce instability or overfitting under small-sample benchmark conditions

## Risks
- likely lower ceiling than message-passing or angular proposals

## Selection notes
Primarily a calibration branch. Useful if the round wants one simplicity anchor beyond the exact control.
