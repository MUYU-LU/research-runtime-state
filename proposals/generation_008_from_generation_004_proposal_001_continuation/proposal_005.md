# Proposal 005: Single-site pre-readout invariant jump

- family: local_invariant_manybody_hybrid
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: high

## Hypothesis
A single-site pre-readout invariant descriptor, added only at the last stage rather than throughout the block stack, can test whether the source mainly lacks a final local many-body summary rather than deeper representational change.

## Benchmark rationale
The evidence brief says late directional compression remains a plausible bottleneck, but generation_007 showed that stronger interventions regress. A one-point pre-readout summary is therefore the cleanest remaining jump that still probes the missing-capability hypothesis without rewriting the trunk.

## Proposed change
- leave the existing interaction blocks unchanged
- add one very small invariant summary near the energy head
- concatenate it conservatively with existing scalar or vector-norm features
- avoid tensor products, irreps, nonlocal edges, or training-schedule overhauls

## Why this is worth trying
It isolates the late-summary hypothesis more cleanly than prior attempts and offers high diagnostic value even if the effect is small.

## Main risks
- readout-local enrichment may repeat the same failure mode as prior children
- may help ISO17 slightly while hurting rMD17 energy enough to lower `Q_total`

## Best-case signal
Better late-stage local discrimination that improves ISO17 and holds the source's rMD17 energy regime.
