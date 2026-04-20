# Proposal: Symmetry-Safe Low-Rank Readout Adapter Wildcard

- family: compact_local_equivariant_low_rank_adapter
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: medium
- evidence_mode: balanced

## Summary
Test a wildcard continuation that adds a small symmetry-safe low-rank adapter only around invariant readout mixing, using the ELoRA cautionary lesson to probe parameter-efficient enrichment without disturbing the main equivariant trunk.

## Motivation
Fresh evidence argues that naive low-rank edits can silently break equivariance assumptions, but it also suggests that carefully structured low-rank adaptation can be useful. That makes a bounded readout-only adapter an interesting wildcard: higher variance than the standard exploits, but far safer than low-rank edits inside the vector interaction core.

## Proposed change
- preserve the source trunk and message-passing structure
- introduce a low-rank adapter only in invariant scalar processing near the final readout, not in equivariant tensor transport itself
- keep the adapter residual-gated so the model can recover source behavior if the adapter is unhelpful
- avoid generic PEFT-style edits to vector transport or symmetry-sensitive operations
- keep training changes minimal and benchmark interpretation focused on energy, force, gap, and stability together

## Why this is a fit now
- explores a fresh evidence-backed idea without turning the round into a parameter-efficiency project
- keeps the wildcard bounded and benchmark-relevant
- may reveal a cheaper path to extra head capacity if the source trunk is already near-optimal

## Risks
- the adapter may be too weak to matter or too quirky to beat simpler exploits
- even readout-only low-rank structure may add noise without clear scientific gain

## Selection notes
This is a true wildcard, not a default pick. It is most valuable if the selected set wants one unconventional but still symmetry-disciplined experiment.
