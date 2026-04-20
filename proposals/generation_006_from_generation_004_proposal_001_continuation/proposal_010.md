# Proposal: Dataset-Balanced Late Summary Wildcard

- family: compact_local_equivariant_with_late_invariant_manybody_summary
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: moderate_high
- evidence_mode: balanced

## Summary
Use one very narrow late invariant many-body summary path, but explicitly shape the proposal around balanced cross-dataset recovery, with the design goal of helping ISO17 without paying the large rMD17 energy cost seen in weaker children.

## Motivation
The benchmark dossier says any valid continuation must beat the parent on benchmark-complete quality, not just improve one dataset. A wildcard many-body branch aimed at balance, not maximal capacity, is worth one slot.

## Proposed change
- keep the two-block parent trunk
- attach one late ACE-like invariant summary with width and placement constrained for calibration safety
- if any training change is used, keep it subordinate to preserving mixed energy and split-gap behavior
- avoid nonlocal, electronic, transformer, or irreps-heavy machinery

## Why this is a fit now
It is the most benchmark-balanced version of the allowed many-body idea and complements the cleaner stream-refinement proposals.

## Risks
- difficult to beat the parent without becoming too timid
- still carries body-order integration risk despite the narrow scope

## Selection notes
Wildcard jump-leaning candidate.
