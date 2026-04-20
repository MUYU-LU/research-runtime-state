# Proposal: SO3KRATES-Style Stream Separation Jump

- family: separated_invariant_equivariant_local_equivariant
- phase: 5
- jump_type: jump
- budget_class: medium_high
- expected_capability_gain: high
- evidence_mode: balanced

## Summary
Introduce a phase-5 jump that more explicitly separates invariant and equivariant streams through the interaction stack, then recombines them with cheap invariant contractions, following the evidence-backed SO3KRATES pattern without adding global attention or a heavy tensor-product rewrite.

## Motivation
The current source already distinguishes scalar and vector channels, but its separation-and-recombination discipline is still fairly simple. Fresh literature suggests that a more explicit stream design can improve stability and efficiency at the same time, which makes it a strong benchmark-centric jump candidate.

## Proposed change
- preserve locality, cutoff graph construction, atomref, and force-from-energy consistency
- refactor the interaction stack so invariant and equivariant pathways are processed more distinctly, with bounded cross-talk through invariant summaries
- keep the depth modest and parameter growth controlled
- return to the same scalar total-energy readout contract at the end
- avoid nonlocal attention, electronic-state inputs, or external irreps infrastructure

## Why this is a fit now
- it is a genuine family-level jump, but still aligned with the current code's scalar/vector organization
- it tests whether better stream discipline improves both benchmark stability and cross-dataset transfer
- it stays closer to the current implementation surface than a transformer or SpookyNet-style branch

## Risks
- the refactor may be large enough to blur attribution if it changes too many subcomponents at once
- better theoretical stream separation may not outperform simpler exploit-level readout upgrades in practice

## Selection notes
Treat this as a high-upside, medium-to-high-risk jump that complements the ACE-style body-order jump rather than duplicating it.
