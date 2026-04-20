# Proposal: Late-Fusion Scalar-Vector Exploit with Source-Matched Discipline

- family: compact_local_equivariant_late_fusion
- phase: 4
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: medium
- evidence_mode: balanced

## Summary
Exploit the frontier source by adding one bounded late-fusion invariant refinement stage just before energy prediction, allowing the model to recombine scalar and vector summaries once more without altering the main interaction backbone.

## Motivation
The source unit already proved that internal scalar-vector fusion helps. A natural exploit is to extend that idea once at the terminal head, rather than adding a new interaction family. This keeps the intervention small while testing whether the remaining benchmark gap is concentrated in the last step of invariant compression.

## Proposed change
- keep neighbor construction, cutoff logic, message-passing depth, and energy-force contract unchanged
- add a narrow late-fusion module that mixes scalar state with invariant summaries from vector channels before the final MLP readout
- keep the extra refinement shallow and residual-gated so the model can fall back toward source behavior if needed
- avoid explicit triplet logic, nonlocal attention, or large parameter expansion
- keep training close to the source configuration unless a tiny calibration change is required

## Why this is a fit now
- isolates a plausible source bottleneck while staying in the same implementation family
- gives the round a third exploit that is meaningfully different from plain readout-feature concatenation
- is benchmark-safe because it should preserve the source unit's reliability profile if the residual gate behaves conservatively

## Risks
- the extra late-fusion block may be too weak to move the benchmark materially
- if poorly gated, it could destabilize energy calibration despite being small

## Selection notes
Useful as the most architecture-light exploit in the set. It provides a bounded comparison against Proposals 001 and 002.
