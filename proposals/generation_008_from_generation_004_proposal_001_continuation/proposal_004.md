# Proposal 004: Ultra-narrow invariant summary jump

- family: local_invariant_manybody_hybrid
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: medium

## Hypothesis
A much weaker invariant summary helper than the generation_007 ACE-like attempt may recover a useful sliver of higher-order local information without repeating the calibration damage seen in broader summary jumps.

## Benchmark rationale
Generation_007 gave negative evidence against medium-strength many-body additions, not necessarily against every diagnostic summary. The only defensible jump now is one that is explicitly narrower, easy to ablate, and judged by benchmark-complete outcomes rather than isolated force gains.

## Proposed change
- keep the current equivariant trunk and readout contract
- add one low-width invariant statistic derived from local neighbor geometry
- inject it only once, either near scalar update or immediately before readout
- design the helper so it can be cleanly disabled or collapse toward source behavior

## Why this is worth trying
It preserves one jump slot for a genuinely missing capability hypothesis while respecting the new evidence that larger jumps are poorly supported.

## Main risks
- still may worsen rMD17 or ISO17 energy despite being narrow
- diagnostic helper may be too weak to matter

## Best-case signal
A small but real balanced gain, especially on ISO17, without the energy blow-up seen in prior broader summary attempts.
