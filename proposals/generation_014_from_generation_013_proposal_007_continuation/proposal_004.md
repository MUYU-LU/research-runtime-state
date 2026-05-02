# Proposal 004: Gated vector readout with trainable atomref

- family: combined_geometry_energy_safeguard
- phase: 2
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Combine the two strong evidence mechanisms to recover both invariant geometry energy and adaptive baseline calibration from proposal_007.

## one_sentence_hypothesis
A small-gated vector_norm readout plus trainable fitted atomref should jointly repair proposal_007's energy/Q regression while retaining a conservative route back toward geometric force sensitivity.

## mechanism_refs
- GEN014-M01-invariant-vector-readout-repair
- GEN014-M02-atomref-energy-safeguard

## evidence_refs
- mechanism_cards.json::GEN014-M01-invariant-vector-readout-repair
- mechanism_cards.json::GEN014-M02-atomref-energy-safeguard
- patch_blueprints.json::GEN014-M01-invariant-vector-readout-repair
- patch_blueprints.json::GEN014-M02-atomref-energy-safeguard
- benchmark_diagnosis.json::proposal_007::Q_total and energy regression

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: jump
- not_a_duplicate_of: proposals_001_to_003 because this deliberately combines readout repair with atomref adaptation after single-factor repairs establish the two axes.
- why_not_duplicate: No generation_013 selected unit combined scalar-only source recovery with both gated vector_norm and trainable atomref from proposal_007.
- lesson_used: Single-axis atomref changes were neutral; scalar-only was negative. A bounded two-axis repair may be necessary but must remain small.

## benchmark_rationale
- rmd17 energy: Expected improvement from both geometry readout and adaptive E0.
- rmd17 force: Expected improvement from vector readout; atomref is force-neutral.
- rmd17 gap / Q: May recover Q_total if force and energy improve, with gap risk bounded by gate.
- iso17 energy: Primary combined target; both mechanisms address proposal_007 energy drift.
- iso17 force: Expected neutral-to-positive.
- iso17 gap / Q: Q_iso17 should improve if baseline and geometry readout both help transfer.
- training stability / runtime risk: Medium but bounded; no new data, loops, or entrypoints.
- control comparison expectation: Should outperform both proposal_007 and at least one single-factor repair to justify combining mechanisms.

## files_to_edit
- `model/model.py`
- `model/train.py`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: widen readout to `hidden_dim * 2` and add a low-initialized scalar `vector_readout_logit`.
- `model/model.py::EvolutionMLIP.forward_energy`: concatenate `scalar_state` with gated `vector_norm` before readout.
- `model/train.py::train`: keep LSTSQ atomref initialization but remove the hard freeze.

## minimal_edit_plan
1. Implement the Proposal 002 gated vector_norm readout patch.
2. Remove the proposal_007 atomref freeze while preserving LSTSQ initialization.
3. Leave optimizer, schedule, epochs, cutoff, and benchmark IO unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Do not add loss terms or dataset-specific branches.

## expected_benchmark_effect
- primary expected gain: Best chance among bounded proposals to recover proposal_007's Q_total loss.
- expected tradeoff: Harder attribution and possible overcorrection of gap penalty.
- failure signal that would falsify this proposal: Worse than both single-factor variants on Q_total or validation energy instability.

## ablation_or_control
- required control or comparison: Compare to proposal_007, Proposal 002, and Proposal 003.
- optional zero-gate / source-fallback / readout-only ablation: The gate gives a source fallback if vector_norm is not useful.

## implementation_notes_for_subagent
This is the largest bounded repair. Do not touch interaction blocks, dataloader, evaluator, or benchmark configuration.
