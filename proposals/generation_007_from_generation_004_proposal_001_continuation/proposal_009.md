# Proposal 009: Benchmark-aware dual-dataset calibration wildcard

- family: balanced_local_equivariant
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: medium


## Hypothesis
The next gain may come from training with more explicit protection against benchmark tradeoff failure, for example by shaping optimization around cross-dataset calibration rather than only per-sample energy and force loss. This is a wildcard because it touches training semantics more than architecture, but still remains within the fixed benchmark contract.

## Benchmark rationale
The active brief emphasizes benchmark completeness: mixed force, mixed energy, gap penalties, and cross-dataset `Q` values all matter. If the source is already architecturally close to right, a bounded calibration-oriented training variant may improve `Q_total` by better balancing rMD17 and ISO17 rather than specializing to one.

## Proposed change
- keep the source architecture intact
- introduce a bounded training calibration mechanism that nudges optimization toward balanced benchmark behavior
- preserve autograd forces, datasets, splits, and evaluation semantics
- avoid any change that would turn this into a benchmark-definition edit

## Why this is worth trying
It is a genuine alternative hypothesis to the architecture-first story, but still benchmark-centric and locally implementable.

## Main risks
- could over-engineer training without addressing the real model bottleneck
- may improve one benchmark component while quietly hurting another

## Best-case signal
Lower combined tradeoff cost, especially via reduced gap or better cross-dataset energy-force balance, with source-like runtime reliability.
