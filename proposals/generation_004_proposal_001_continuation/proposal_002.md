# Proposal: Readout Exploit with Stability-Weighted Training Rebalance

- family: compact_local_equivariant_readout_enrichment
- phase: 4
- jump_type: exploit
- budget_class: medium
- expected_capability_gain: medium_high
- evidence_mode: balanced

## Summary
Pair the richer invariant energy head with a conservative stability-weighted training rebalance, testing whether ISO17 gains come more cleanly when representational improvement is coupled to gentler energy/force weighting and volatility control.

## Motivation
The source unit succeeded with zero retries and strong final metrics, but both datasets showed mid-training energy spikes, especially ISO17. The evidence refresh says selection must remain benchmark-complete and stability-aware, not force-only. A bounded exploit should therefore improve the head while explicitly protecting energy and gap behavior.

## Proposed change
- start from the same readout-enrichment idea as Proposal 001
- add only minor optimizer/schedule changes, such as slightly softer early force emphasis, flatter late learning-rate decay, or gentler residual warmup
- preserve the source family's local equivariant trunk and two-block depth
- track changes against cross-dataset energy, force, and split-gap behavior instead of only chasing force MAE
- keep parameter growth and training-surface churn modest

## Why this is a fit now
- still exploits the validated family instead of jumping architecture too early
- directly addresses the source unit's one visible softness, namely benchmark-successful but capacity-sensitive training turbulence
- remains easy to interpret against Proposal 001 as a cleaner stability-vs-capacity comparison

## Risks
- schedule tweaks may obscure whether gains came from representation or optimization
- extra conservatism may sacrifice upside if the real bottleneck is almost entirely representational

## Selection notes
A strong exploit companion to Proposal 001. If both are selected, later review can separate pure readout gains from readout-plus-stability gains.
