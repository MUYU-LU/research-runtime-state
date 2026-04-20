# Proposal: Dual-Path Energy Calibration Head

- family: low_rank_equivariant_local
- phase: 5
- jump_type: jump
- budget_class: large
- expected_capability_gain: medium_high
- evidence_mode: balanced

## Summary
Add a bounded dual-path energy readout to the `proposal_005` family so local equivariant features and calibrated scalar summaries can correct each other before the final energy prediction.

## Motivation
The main weakness of `proposal_005` was not missing force signal, but incomplete energy balance across datasets. A jump that targets readout expressiveness may unlock gains without changing the local message-passing contract.

## Proposed change
- preserve the two-stage low-rank equivariant body
- expand the energy head into a bounded dual-path calibration structure
- keep forces derived from the final scalar energy through autograd
- do not add long-range branches, explicit triplets, or benchmark-contract changes

## Why this is a fit now
- directly addresses the benchmark review's energy-balance problem
- remains runnable-unit compatible while still being meaningfully distinct from plain exploit proposals
- complements the `proposal_001` exploit-anchor context, which favored simpler balanced behavior

## Risks
- readout complexity can improve fit while hiding poor internal representation quality
- may not help if the real issue lies inside the interaction stages rather than the head

## Selection notes
A good jump candidate if selection wants one architecture branch focused specifically on benchmark-balanced energy calibration.
