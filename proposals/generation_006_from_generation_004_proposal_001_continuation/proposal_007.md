# Proposal: Parent-Safe Late-Only Simplification

- family: compact_local_equivariant_stream_refinement
- phase: 4
- jump_type: backward-simplify
- budget_class: low
- expected_capability_gain: variance_reduction
- evidence_mode: balanced

## Summary
Simplify the continuation target by allowing only one late in-block refinement path, with no first-block changes and no auxiliary many-body branch, to maximize preservation of the parent's calibration and runtime reliability.

## Motivation
Because the parent remained better than every generation_005 child, a valid continuation is to simplify the change budget further and ask whether most regressions came from touching too much of the model.

## Proposed change
- keep almost all of `model.py` identical to the source
- permit only a tiny second-block stream tweak
- keep `train.py` as close to source as possible
- use this as a parent-safe calibration-focused continuation, not a readout retry

## Why this is a fit now
It gives the round a true backward-simplify option that still respects the evidence preference for in-block refinement over head-only changes.

## Risks
- may produce little or no gain
- could functionally collapse to a near-control if the allowed tweak is too weak

## Selection notes
Required backward-simplify candidate, useful if the round wants one very conservative branch.
