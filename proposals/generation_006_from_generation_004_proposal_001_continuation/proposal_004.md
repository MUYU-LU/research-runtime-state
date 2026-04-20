# Proposal: Narrow Late ACE-Like Summary Jump

- family: compact_local_equivariant_with_late_invariant_manybody_summary
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Add one narrow late invariant many-body summary path, ACE-like in spirit, near the final scalar update or pre-readout stage, so the model gets a compact body-order signal without a full ACE or MACE transplant.

## Motivation
ACE remains the main scientifically grounded higher-upside move, but generation_005 showed that a broader body-order attempt was too costly. This proposal narrows the insertion to one late summary site.

## Proposed change
- keep the parent two-block trunk intact
- derive a low-width invariant summary from local neighbor-pair geometry once, late in the network
- fuse that summary into scalar updates only
- avoid full basis-framework rewrites, irreps libraries, or stack-wide product-basis machinery

## Why this is a fit now
It preserves the evidence-backed body-order idea while explicitly correcting for the overreach risk seen in generation_005/proposal_004.

## Risks
- even a narrow body-order path may destabilize energy calibration
- implementation details may still accidentally mimic the failed broader jump too closely

## Selection notes
Primary bounded jump.
