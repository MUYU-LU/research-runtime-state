# Proposal 010: Compound wildcard combining narrow many-body summary with conservative source fallback

- family: compact_local_equivariant_manybody_hybrid
- phase: 5
- jump_type: wildcard
- budget_class: large
- expected_capability_gain: medium_high


## Hypothesis
A compound design may outperform single-mechanism proposals if the source needs both slightly richer many-body information and a stronger path to fall back toward its already validated behavior. This proposal pairs a very narrow invariant many-body helper with deliberately conservative residual integration.

## Benchmark rationale
This is the highest-risk proposal in the set, but still bounded by the evidence brief. It is benchmark-justified only because the source remains the best completed unit, meaning any worthwhile jump must preserve energy calibration, low gap penalties, and runtime reliability while testing a real capability expansion.

## Proposed change
- keep the local graph, cutoff, atomref, and force-from-energy contract
- add one narrow ACE-like invariant summary helper
- integrate it with conservative gating so the source path remains dominant unless the new summary is useful
- avoid full irreps, tensor-product, or nonlocal rewrites

## Why this is worth trying
It is the set's broadest but still evidence-grounded hypothesis. If selected later, it would test whether bounded capability expansion plus fallback-aware integration can break the stagnation seen after generation_004.

## Main risks
- more moving parts can hurt attribution and calibration
- could regress badly if the many-body helper is not well matched to the source trunk

## Best-case signal
A clear `Q_total` improvement with preserved reliability, showing that the frontier needed a compact phase-5 extension rather than another pure exploit.
