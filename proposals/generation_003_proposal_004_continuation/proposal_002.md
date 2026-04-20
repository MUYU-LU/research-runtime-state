# Proposal: Conservative Residual-Stability Exploit on Proposal_004

- family: nequip_style_local_equivariant
- phase: 5
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: medium_high
- evidence_mode: balanced

## Summary
Keep `generation_003/proposal_004` as the architectural base, but push a more conservative residual-routing and normalization variant intended to reduce variance and improve benchmark stability without abandoning the winning family.

## Motivation
The current continuation source already proved that this cleaner local equivariant refactor can win benchmark-centrically. A second exploit should therefore test whether part of the remaining risk comes from update aggressiveness rather than representational limits.

## Proposed change
- preserve the same local equivariant interaction family, scalar energy contract, atomref baseline, and autograd force path
- make residual and gating updates more conservative across interaction layers
- emphasize normalization and stable channel scaling over new representational machinery
- keep training bounded and cross-dataset oriented, not specialized for one benchmark
- avoid adding extra body-order structure, triplets, or global branches

## Why this is a fit now
- gives the round a lower-risk exploit complement to the default exploit anchor
- probes whether proposal_004's gains can be retained with tighter stability controls
- stays well inside the validated implementation surface

## Risks
- being too conservative may lose the performance edge and act like a weak ablation
- stabilization alone may not address the most important remaining calibration bottleneck

## Selection notes
This should be interpreted as the safety-oriented exploit companion to the main proposal_004 continuation line.
