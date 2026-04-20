# Proposal: Dual-Path Mixed-Benchmark Router for Proposal_004

- family: nequip_style_local_equivariant
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: medium_high
- evidence_mode: balanced

## Summary
Build a wildcard continuation from `generation_003/proposal_004` that adds a lightweight dual-path router, allowing separate but softly coupled scalar update streams for RMD17-like and ISO17-like structures before recombining into one benchmark-contract-preserving energy head.

## Motivation
`proposal_004` delivered the strongest `Q_total` in `generation_003`, suggesting its local equivariant refactor is a strong base. A useful wildcard is to test whether part of the remaining mixed-benchmark tension comes from forcing one shared scalar adaptation pathway across datasets with somewhat different structural statistics.

## Proposed change
- preserve the local equivariant neighborhood construction, cutoff envelope, atomref baseline, scalar total-energy contract, and force-from-autograd path from `proposal_004`
- keep a shared geometric interaction trunk, but add two lightweight scalar refinement branches after the main interaction stack
- use a small learned router or confidence gate from pooled structure features to softly mix the branch outputs into a single final per-atom energy contribution
- keep the router bounded and low-capacity so this remains a benchmark-shaping ablation rather than a full architecture jump
- retain conservative training stabilization, including clipped gradients and no benchmark contract changes

## Why this is a fit now
- explores whether `proposal_004` can improve cross-dataset balance without abandoning its winning local equivariant core
- tests a mixed-benchmark specialization idea while remaining within phase-4 budget and implementation scope
- stays interpretable because the shared trunk remains dominant and the branch-specific logic is intentionally shallow

## Risks
- branch specialization may overfit dataset-specific quirks and hurt overall transfer
- even a small router can destabilize early training if branch balance collapses too quickly
- gains may be marginal if the benchmark tension is mostly optimization-related rather than representational

## Selection notes
Treat this as a wildcard continuation focused on benchmark-balance shaping. It is most valuable if selected alongside a simpler exploit and at least one stronger jump, so later review can separate routing effects from raw capacity changes.
