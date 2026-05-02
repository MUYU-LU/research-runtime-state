# Proposal 010: Wildcard learned gate on vector readout with frozen offset

- family: gated_vector_readout_frozen_offset
- phase: 3
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Freeze the composition offset and let the model learn a bounded gate for vector-norm readout contribution, balancing scalar energy stability against angular force expressiveness.

## one_sentence_hypothesis
A sigmoid-bounded vector readout gate can reduce vector-channel overuse for energy calibration while retaining angular information when it helps forces.

## mechanism_refs
- MATERIALIZED-FROZEN-LSTSQ-ATOMREF-OFFSET-001

## evidence_refs
- repo_artifact:repo_001::src/schnetpack/atomistic/atomwise.py::Atomwise.forward
- repo_artifact:repo_001::src/schnetpack/atomistic/response.py::Forces.forward
- repo_artifact:repo_001::src/schnetpack/transform/atomistic.py::AddOffsets.forward
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T152307Z/current_code_profile.json

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: ablation
- not_a_duplicate_of: Backward-simplify Proposal 007 because this keeps vector_norm available but gates its contribution instead of removing it.
- lesson_used: Prior outcome memory suggests large architecture jumps often underperform; a bounded gate is a small wildcard to test vector-channel calibration.

## benchmark_rationale
- rmd17 energy: Frozen atomref plus gated vector contribution may preserve energy while avoiding over-correction.
- rmd17 force: Retaining vector_norm should protect force better than scalar-only simplification.
- rmd17 gap / Q: Expected to sit between source and scalar-only; could improve Q if gate learns useful balance.
- iso17 energy: Target reduced energy/gap drift from unconstrained vector-norm readout.
- iso17 force: Should be less risky than removing vector readout entirely.
- iso17 gap / Q: May improve if vector channel drives other-split energy mismatch.
- training stability / runtime risk: One scalar parameter/gate; negligible runtime.
- control comparison expectation: Should beat scalar-only if vector information is useful, and beat source if gating reduces energy drift.

## files_to_edit
- `model/model.py`
- `model/train.py`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `self.vector_readout_logit = nn.Parameter(torch.tensor(0.0))` or a small initialized negative value.
- `model/model.py::EvolutionMLIP.forward_energy`: compute `vector_norm`, multiply it by `torch.sigmoid(self.vector_readout_logit)` before concatenating with `scalar_state`.
- `model/train.py::train`: freeze fitted atomref before optimizer creation.

## minimal_edit_plan
1. Add one scalar gate parameter to `EvolutionMLIP`.
2. Replace `torch.cat([scalar_state, vector_norm], dim=-1)` with `torch.cat([scalar_state, gate * vector_norm], dim=-1)`.
3. Freeze the fitted atomref as in Proposal 001 before optimizer construction.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Keep the gate scalar/bounded; do not add per-edge or per-atom expensive gating.

## expected_benchmark_effect
- primary expected gain: Improve ISO17 energy/gap while retaining more force accuracy than scalar-only readout.
- expected tradeoff: Gate may learn source-like value and provide little change, or suppress vector information too much.
- failure signal that would falsify this proposal: No energy/gap improvement versus source and force worsens versus source/control.

## ablation_or_control
- required control or comparison: Compare to source control, pure freeze, and scalar-only simplification.
- optional zero-gate / source-fallback / readout-only ablation: A very negative logit approximates scalar-only; a large positive logit approximates source vector readout.

## implementation_notes_for_subagent
Keep the gate bounded and simple. Do not change hidden dimensions or readout layer shapes; the concatenated input remains `hidden_dim * 2`.
