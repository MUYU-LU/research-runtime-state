# Proposal 004: Ultra-narrow late invariant summary jump

- family: local_invariant_manybody_hybrid
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: medium

## Hypothesis
One even narrower late ACE-like invariant summary than the best generation_008 jump can test whether a tiny missing local many-body statistic exists without repeating the broader regressions.

## Benchmark rationale
Generation_008 `proposal_004` was the best jump at `Q_total 2.5390`, still clearly below the parent but better than other jump attempts. That leaves exactly one defensible jump lane: a single, low-width, easy-to-disable late invariant helper judged by full benchmark balance, not force-only movement.

## Proposed change
- keep the current two-block equivariant trunk unchanged
- add one low-width invariant summary derived from local neighbor geometry only once late in the model
- inject it near the final scalar update or immediately before readout
- make the helper trivially removable or collapsible to zero

## Why this is worth trying
It preserves a bounded diagnostic jump slot while staying inside the evidence brief's very narrow allowance.

## Main risks
- still may degrade rMD17 energy or force balance
- helper may be too weak to matter

## Best-case signal
A measurable ISO17 gain with near-parent rMD17 behavior, indicating a real but small missing invariant summary.
