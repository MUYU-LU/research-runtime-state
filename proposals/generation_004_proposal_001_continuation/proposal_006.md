# Proposal: Higher-Order Late Refinement Bridge Jump

- family: higher_order_local_equivariant_bridge
- phase: 5
- jump_type: jump
- budget_class: high
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Create a bounded higher-order late refinement bridge on top of the current source trunk, testing whether one shallow higher-order equivariant stage near the end of message passing can unlock additional benchmark gains without rewriting the full model family.

## Motivation
The frontier source already shows clean runtime behavior and strong benchmark-complete quality. That makes generation_005 a sensible time to allocate one stronger forward jump toward phase 5, especially if the simpler exploit proposals suggest the trunk is nearing diminishing returns.

## Proposed change
- retain the source model's early local equivariant trunk and stable training recipe as much as possible
- append one narrow higher-order refinement stage late in the stack, then compress back to invariant energy prediction
- keep higher-order channels shallow and residual-gated so the model can degrade gracefully toward source behavior
- preserve benchmark semantics, atomref baseline, and force-from-autograd
- avoid global attention, explicit nonlocal charge/spin modeling, or framework-scale dependency changes

## Why this is a fit now
- offers a real phase-5 test rather than another small phase-4 exploit
- keeps the jump scientifically interpretable by anchoring it to the validated trunk
- probes whether the main remaining gap is limited higher-order angular expressivity

## Risks
- this is the most fragile proposal in the set from an implementation and optimization standpoint
- if the added stage is too small, the jump may not be informative; if too large, it may destabilize training

## Selection notes
This is the highest-variance jump candidate. It should be selected only alongside enough lower-risk proposals to preserve round balance.
