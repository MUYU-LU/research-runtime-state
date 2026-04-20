# Proposal 005: In-block invariant compression jump

- family: balanced_local_equivariant
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: low-medium

## Hypothesis
A tiny in-block invariant compression term, inserted before the scalar update rather than at readout, can recover useful local body-order structure more safely than readout-adjacent summary retries.

## Benchmark rationale
The evidence brief argues against readout-only retries, but still leaves room for one bounded jump if it is narrower and better integrated with the existing block mechanics. The source already computes `directional_invariant`, `agg_norm`, and `vector_alignment`, so a tiny compression of those same statistics is a more natural jump than a new branch.

## Proposed change
- keep the current trunk and force-from-energy path
- add one small invariant bottleneck inside `BalancedInteractionBlock` that recombines existing invariant statistics only
- forbid extra message-passing depth, nonlocal paths, or external irreps machinery
- keep training changes minimal

## Why this is worth trying
It tests a jump hypothesis while staying closer to the winning block internals than the late-summary attempts that already failed.

## Main risks
- may still amount to excess capacity in disguise
- could worsen energy calibration even if forces look acceptable

## Best-case signal
A small balanced gain that beats the prior jump variants without sacrificing the parent's core calibration.
