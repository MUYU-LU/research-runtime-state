# Proposal 004: Fixed atomref plus residual energy centering

- family: centered_residual_offset
- phase: 3
- jump_type: jump
- budget_class: small
- expected_capability_gain: Combine a frozen composition offset with a tiny residual-centering bias so the readout learns local deviations rather than re-learning global energy scale.

## one_sentence_hypothesis
Subtracting the train residual mean from the readout target implicitly through a learned scalar residual bias, while freezing atomref, should improve energy calibration without touching force semantics.

## mechanism_refs
- MATERIALIZED-FROZEN-LSTSQ-ATOMREF-OFFSET-001

## evidence_refs
- repo_artifact:repo_001::src/schnetpack/transform/atomistic.py::RemoveOffsets
- repo_artifact:repo_001::src/schnetpack/transform/atomistic.py::AddOffsets.forward
- repo_artifact:repo_001::src/schnetpack/configs/experiment/md17.yaml
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T152307Z/patch_blueprints.json

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: jump
- not_a_duplicate_of: generation_012/proposal_005 and Proposals 001/002 because this adds an explicit residual scalar offset/bias path after freezing atomref.
- lesson_used: Source likely overuses the trainable atomref to correct residual energy drift; SchNetPack separates offsets from atomwise residual prediction.

## benchmark_rationale
- rmd17 energy: A residual bias can absorb constant residual mismatch after frozen atomref, protecting the source's strong RMD17 energy.
- rmd17 force: A constant residual bias is position-independent, so it does not alter force gradients.
- rmd17 gap / Q: Should preserve RMD17 Q if the bias improves energy without force cost.
- iso17 energy: May reduce global residual error that fixed atomref alone cannot capture.
- iso17 force: Expected neutral; readout/interactions remain the force path.
- iso17 gap / Q: Could improve Q_iso17 if residual mean mismatch contributes to within/other energy differences.
- training stability / runtime risk: Small parameter addition; negligible runtime.
- control comparison expectation: Should beat pure freeze only if there is a residual constant offset not captured by composition baseline.

## files_to_edit
- `model/model.py`
- `model/train.py`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `self.residual_energy_bias = nn.Parameter(torch.zeros(()))`.
- `model/model.py::EvolutionMLIP.forward_energy`: return `atomref + per_atom_energy.sum() + self.residual_energy_bias`.
- `model/train.py::train`: freeze/exclude atomref after successful least-squares initialization before optimizer creation.

## minimal_edit_plan
1. Add a scalar residual energy bias parameter initialized to zero.
2. Add the bias to the scalar energy after atomref and per-atom residual sum.
3. Implement the Proposal 001-style fitted atomref freeze before optimizer creation.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Ensure the scalar bias broadcasts as a scalar and does not detach energy from autograd.

## expected_benchmark_effect
- primary expected gain: Lower mixed_energy_mae on ISO17 and possibly RMD17 without force degradation.
- expected tradeoff: Bias may be redundant with atomref/readout and add little beyond freeze.
- failure signal that would falsify this proposal: Energy improves on train but validation gap worsens, indicating a global bias is too coarse.

## ablation_or_control
- required control or comparison: Compare against Proposal 001 pure freeze and source control.
- optional zero-gate / source-fallback / readout-only ablation: Bias initialized to zero is a safe no-op at start; if atomref fitting fails, leave atomref trainable but keep bias.

## implementation_notes_for_subagent
This is a phase-3 jump only in the readout/offset decomposition, not a new dataset or metric. Do not add validation-dependent centering or data leakage.
