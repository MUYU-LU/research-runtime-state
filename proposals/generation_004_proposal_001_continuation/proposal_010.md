# Proposal: Radial Frequency-Split Filter Wildcard

- family: compact_local_equivariant_frequency_split
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: medium
- evidence_mode: balanced

## Summary
Add a lightweight radial frequency-split filter bank inside the local interaction pipeline, testing whether separate short-range sharpness and smoother medium-range context can improve cross-dataset behavior without changing the overall family.

## Motivation
The benchmark pair rewards both sharp local discrimination and stable generalization. A single shared radial shaping pathway may be forcing an awkward compromise. This wildcard asks whether splitting those regimes before recombination helps more than simply widening the existing filters.

## Proposed change
- preserve the current local equivariant backbone, atomref baseline, and scalar total-energy contract
- split radial/filter processing into two bounded streams, one biased toward sharper short-range response and one toward smoother medium-range context
- recombine the streams with a conservative gate before the existing scalar-vector update logic
- avoid body-order expansion, nonlocal mechanisms, or large depth increases
- keep training close to the source recipe so the structural change stays interpretable

## Why this is a fit now
- gives the round a second wildcard that probes representation shape rather than generic capacity
- stays within the same code family and implementation surface
- could help ISO17 transfer without discarding the source unit's rMD17 strengths

## Risks
- the split may add complexity without producing a genuinely different effective behavior
- extra branch interaction may worsen optimization turbulence despite the bounded design

## Selection notes
This is the more architecture-shaped wildcard in the set. It pairs well with the low-rank wildcard because the two test very different bounded hypotheses.
