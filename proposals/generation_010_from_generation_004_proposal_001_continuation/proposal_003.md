# Proposal 003: Shared-channel scalar gate exploit

- family: balanced_scalar_mix_recovery
- phase: 4
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: reduce overfitting risk by sharing a lighter scalar gate across channels or blocks.

## one_sentence_hypothesis
A lower-capacity shared gate over the existing scalar-mix path can preserve the evidence-backed bounded edit while reducing the variance risk of a fully free per-channel gate.

## mechanism_refs
- M-BAL-PAINN-001

## evidence_refs
- mechanism_cards.json::M-BAL-PAINN-001
- evidence_provenance.json
- generation_memory.json
- benchmark_diagnosis.json

## historical_relation
- source_unit: generation_004/proposal_001
- relation_to_source: exploit
- not_a_duplicate_of: proposal_001 and proposal_002 because this intentionally lowers gate capacity, testing whether a simpler scalar control is more robust than channelwise freedom.
- lesson_used: recent descendants show that even small additional flexibility can regress, so a lower-capacity exploit is worth separating from the main learned-gate variants.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: should improve if low-rank gating is enough to curb overmixing.
- rmd17 force: neutral expectation.
- rmd17 gap / Q: modest upside from better calibration and less gate variance.
- iso17 energy: may lag proposal_001 if per-channel control was needed.
- iso17 force: neutral.
- iso17 gap / Q: likely small movement either way.
- training stability / runtime risk: lowest among exploit edits because parameter count stays minimal.
- control comparison expectation: strongest value is interpretability, not raw upside.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::BalancedInteractionBlock.__init__`: add a very small shared or bottlenecked gate parameterization tied to the existing scalar mix.
- `model/model.py::BalancedInteractionBlock.forward`: apply the shared gate in place of the fixed `0.3` coefficient.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Parameterize a low-capacity scalar gate from existing scalar features.
2. Constrain the gate to a narrow interval centered below the source blend weight.
3. Replace the fixed coefficient without changing tensor routing elsewhere.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: lower-variance exploit that may slightly recover `Q_total`.
- expected tradeoff: less expressive than proposal_001 if true channelwise adaptation matters.
- failure signal that would falsify this proposal: no benchmark gain versus control and no improvement over the backward-simplify baseline.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare with proposal_001 to isolate whether gate capacity matters.

## implementation_notes_for_subagent
Stay inside `BalancedInteractionBlock`; do not touch readout or training losses. If a shared gate is easier, prefer one scalar per hidden group over a full new MLP branch.
