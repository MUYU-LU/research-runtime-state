# Proposal 010: Wildcard narrow phase-5 probe with hard fallback

- family: local_equivariant_probe
- phase: 5
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: medium

## Hypothesis
One explicitly risky but still bounded probe, built around a tiny phase-5 style higher-order hint with a hard fallback to source behavior, is worth carrying so the round does not become purely conservative after repeated negative evidence.

## Benchmark rationale
The evidence heavily disfavors broad novelty, but round policy still benefits from some exploratory coverage. A single wildcard probe keeps search diversity while respecting the benchmark-first lesson that any gain must beat the source on energy, force, gap, and cross-dataset `Q_total` together.

## Proposed change
- preserve the existing local cutoff graph and force-from-energy contract
- add one tiny higher-order-inspired helper or probe feature with explicit low-width and fallback behavior
- confine the change to `model/model.py`
- avoid irreps stacks, tensor products, nonlocal branches, or rewrite-heavy machinery

## Why this is worth trying
It gives the round one disciplined exploration slot without committing to an implementation-heavy framework jump.

## Main risks
- may simply repeat the negative evidence against added representational novelty
- medium budget still carries more calibration risk than the exploit set

## Best-case signal
A surprise balanced gain that shows a very small phase-5 hint can help when wrapped in a strong fallback envelope.
