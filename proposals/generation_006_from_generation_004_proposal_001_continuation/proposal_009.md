# Proposal: Scalar-Normed Block Wildcard

- family: compact_local_equivariant_stream_refinement
- phase: 4
- jump_type: wildcard
- budget_class: low_medium
- expected_capability_gain: moderate
- evidence_mode: balanced

## Summary
Test a wildcard variant where the new in-block stream refinement is paired with tighter scalar normalization and residual balancing, motivated by the source's ability to recover from mid-training spikes and the need to keep added capacity numerically disciplined.

## Motivation
The evidence suggests calibration sensitivity more than missing nonlocal physics. A wildcard that focuses on normalization discipline may preserve the parent's good end-state recovery while still improving use of vector information.

## Proposed change
- keep the parent architecture family
- add one small in-block invariant summary
- retune only local normalization or residual scaling around that summary
- avoid readout-only retries and avoid broad optimizer overhauls

## Why this is a fit now
It is structurally different from the main exploits without violating the bounded evidence constraints.

## Risks
- may mostly affect optimization feel rather than true representational limits
- could underperform if normalization was not the real bottleneck

## Selection notes
Wildcard exploit-leaning candidate.
