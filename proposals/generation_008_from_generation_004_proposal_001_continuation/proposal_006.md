# Proposal 006: Training-light calibration jump

- family: balanced_local_equivariant
- phase: 4
- jump_type: jump
- budget_class: small
- expected_capability_gain: low

## Hypothesis
A tightly bounded calibration retune, with architecture effectively fixed, may recover part of the source's strong balance if recent underperformance came from training sensitivity rather than representational shortage.

## Benchmark rationale
The source recovered from mid-training energy spikes and finished strong on both datasets, while later children often lost balanced energy quality. Although training-only moves are weaker evidence fits than block micro-edits, one small jump slot is justified to test whether benchmark-complete regression partly reflects calibration fragility.

## Proposed change
- preserve the source architecture exactly or near-exactly
- retune only a small set of training knobs, such as energy/force weighting warmup or gradient clipping
- keep the runtime contract, dataset semantics, and force-from-energy path unchanged
- forbid broad optimizer or epoch-budget changes

## Why this is worth trying
It is a cheap bounded test of whether some observed regression is avoidable with gentler calibration handling, and it complements architecture-focused proposals.

## Main risks
- may collapse into a weak replicate with little scientific value
- training-only changes may not beat the source if the source is already near its optimum regime

## Best-case signal
Slightly improved balanced metrics with the same runtime reliability, suggesting calibration headroom still exists inside the current family.
