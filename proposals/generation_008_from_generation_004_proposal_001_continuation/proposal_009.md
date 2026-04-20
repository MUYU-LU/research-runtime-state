# Proposal 009: Wildcard dual-ablation attribution branch

- family: balanced_local_equivariant
- phase: 4
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: low

## Hypothesis
A deliberate attribution branch that pairs two tiny disable-able edits, for example muting one mix path while preserving another, can reveal which current mechanism is actually carrying the source's benchmark advantage.

## Benchmark rationale
The evidence brief highlights uncertainty about why the source wins so decisively and why control-like behavior was weak. A wildcard attribution proposal is justified if it improves understanding of what must be preserved to beat the source on full benchmark metrics.

## Proposed change
- keep the source family and training regime mostly intact
- introduce two very small toggles or ablations inside `BalancedInteractionBlock`
- ensure each toggle can revert toward source behavior cleanly
- evaluate success only through balanced benchmark outcomes, not isolated force improvements

## Why this is worth trying
It could expose whether the frontier advantage comes from scalar mixing, vector residual behavior, or their interaction, which would guide later exploit choices.

## Main risks
- attribution-focused design may sacrifice raw performance
- combined tiny edits could still perturb calibration more than expected

## Best-case signal
Comparable performance to source plus clearer evidence about which mechanism deserves future exploit effort.
