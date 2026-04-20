# Proposal: Source-Matched Control Replicate

- family: compact_local_equivariant_source_control
- phase: 4
- jump_type: control
- budget_class: low
- expected_capability_gain: attribution
- evidence_mode: balanced

## Summary
Run a source-matched control that preserves the parent architecture and schedule as faithfully as possible, so small future gains from stream refinement or narrow many-body changes can be interpreted against direct round variance.

## Motivation
The earlier control signal was useful but still left attribution doubts. Since generation_006 proposals are intentionally narrow, a clean control is especially valuable for separating real improvements from variance.

## Proposed change
- copy the source unit behavior as exactly as practical
- no in-block refinement, no late ACE-like summary, no readout redesign
- preserve benchmark contract, locality, and runtime behavior
- record clearly that this unit is for attribution, not capability expansion

## Why this is a fit now
The frontier source survived a full child round, so honest variance measurement matters before overinterpreting small deltas.

## Risks
- no capability upside by design
- if fidelity is imperfect, interpretation value drops

## Selection notes
Required control candidate.
