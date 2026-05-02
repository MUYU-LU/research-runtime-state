# Proposal 007: Scalar-only trainable-atomref backward simplification

- family: scalar_only_atomref_ablation
- phase: 1
- jump_type: backward-simplify
- budget_class: tiny
- expected_capability_gain: Determine whether proposal_007 failed because scalar-only was too weak or because hard-frozen atomref prevented energy adaptation.

## one_sentence_hypothesis
Maintaining the scalar-only readout while unfreezing fitted atomref provides a minimal backward-simplify/control-like ablation for the M02 energy safeguard without reintroducing vector geometry.

## mechanism_refs
- GEN014-M02-atomref-energy-safeguard

## evidence_refs
- mechanism_cards.json::GEN014-M02-atomref-energy-safeguard
- patch_blueprints.json::GEN014-M02-atomref-energy-safeguard
- benchmark_diagnosis.json::proposal_007 scalar-only/frozen-atomref outcome
- generation_013/proposal_001 neutral frozen-atomref intact-readout comparison

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: simplify
- not_a_duplicate_of: Proposal 003 because this proposal is explicitly framed as the backward-simplify diagnostic arm and must not add any other repair.
- why_not_duplicate: It keeps proposal_007's scalar-only model exactly and changes only the training freeze, serving as the simplest energy calibration ablation.
- lesson_used: Do not conclude vector readout is required until frozen atomref has been isolated as a confounder.

## benchmark_rationale
- rmd17 energy: May improve modestly if baseline adaptation is enough.
- rmd17 force: Expected mostly unchanged.
- rmd17 gap / Q: Useful diagnostic even if Q gain is small.
- iso17 energy: Main target; if this recovers energy, atomref freeze was the dominant issue.
- iso17 force: Expected neutral.
- iso17 gap / Q: Q improves only through energy/gap correction.
- training stability / runtime risk: Tiny; minimal train.py edit.
- control comparison expectation: Separates atomref effect from vector-readout repairs.

## files_to_edit
- `model/train.py`

## code_insertion_points
- `model/train.py::train`: delete or bypass the atomref `requires_grad_(False)` block.
- `model/model.py::EvolutionMLIP.__init__`: none; keep scalar-only readout.
- `model/model.py::EvolutionMLIP.forward_energy`: none.

## minimal_edit_plan
1. Leave `model/model.py` unchanged from source.
2. Keep `initialize_atomref_lstsq` but do not freeze atomref afterward.
3. Keep optimizer over all model parameters.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Do not restore `vector_norm` or add gates in this diagnostic unit.

## expected_benchmark_effect
- primary expected gain: Isolated energy/Q recovery if hard-freeze was the culprit.
- expected tradeoff: If scalar-only is fundamentally underexpressive, force and energy remain weak.
- failure signal that would falsify this proposal: Same energy/Q regression as proposal_007.

## ablation_or_control
- required control or comparison: Exact proposal_007 control and vector-readout repair proposals.
- optional zero-gate / source-fallback / readout-only ablation: This is the source-fallback for all vector repair proposals.

## implementation_notes_for_subagent
Treat this as a minimal diagnostic. Architecture must remain byte-for-byte equivalent unless tooling changes whitespace.
