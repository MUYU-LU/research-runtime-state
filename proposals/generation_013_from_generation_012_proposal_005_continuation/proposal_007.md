# Proposal 007: Simplify to scalar-only residual with frozen atomref

- family: scalar_residual_frozen_offset
- phase: 1
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: Test whether the vector channel is unnecessary noise once the composition offset is fixed, trading angular expressiveness for energy/gap stability.

## one_sentence_hypothesis
Removing vector-state contributions from the residual readout while freezing atomref may reduce overfit and preserve energy calibration on ISO17 at the cost of some force expressiveness.

## mechanism_refs
- MATERIALIZED-FROZEN-LSTSQ-ATOMREF-OFFSET-001

## evidence_refs
- repo_artifact:repo_001::src/schnetpack/atomistic/atomwise.py::Atomwise.forward
- repo_artifact:repo_001::src/schnetpack/transform/atomistic.py::AddOffsets.forward
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl::generation_012/proposal_005
- /home/lmy/.openclaw/workspace/research_runtime/ledger/all_attempts.jsonl

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: simplify
- not_a_duplicate_of: generation_012/proposal_005 because this removes `vector_norm` from the readout input, reducing the model to scalar residual energy over the same neighbor messages.
- lesson_used: Source's force is good but energy/gap drift remains; a simpler scalar residual can diagnose whether vector augmentation is helping or overfitting.

## benchmark_rationale
- rmd17 energy: May remain good due to frozen atomref and simpler residual.
- rmd17 force: Likely force tradeoff because vector-derived angular sensitivity is reduced.
- rmd17 gap / Q: Q may fall if force loss dominates; useful as a backward-simplify diagnostic.
- iso17 energy: Could improve generalization if vector_norm overfits conformational details.
- iso17 force: Expected possible regression; bounded by keeping scalar message passing and force-from-energy.
- iso17 gap / Q: Lower energy gap could offset some force loss if overfit was the issue.
- training stability / runtime risk: Slightly cheaper readout; no new loops.
- control comparison expectation: If this beats source, later rounds should prefer simpler energy calibration before angular jumps.

## files_to_edit
- `model/model.py`
- `model/train.py`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: change the first readout layer input from `hidden_dim * 2` to `hidden_dim`.
- `model/model.py::EvolutionMLIP.forward_energy`: compute `per_atom_energy = self.readout(scalar_state).squeeze(-1)` and leave vector state only inside interactions.
- `model/train.py::train`: freeze fitted atomref before optimizer creation.

## minimal_edit_plan
1. Adjust readout input dimension to accept only `scalar_state`.
2. Replace the readout concatenation of `scalar_state` and `vector_norm` with `scalar_state` only.
3. Add Proposal 001-style atomref freeze in training.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Ensure model state initialization is fresh; do not try to load incompatible source readout weights.

## expected_benchmark_effect
- primary expected gain: Better ISO17 energy/gap stability if vector readout overfit caused drift.
- expected tradeoff: Force MAE may worsen due to reduced angular/body-order capacity.
- failure signal that would falsify this proposal: Energy/gap do not improve and force worsens materially relative to source.

## ablation_or_control
- required control or comparison: Compare to source control and pure frozen atomref.
- optional zero-gate / source-fallback / readout-only ablation: If scalar-only is too weak, later rounds can reintroduce vector_norm with a learned gate.

## implementation_notes_for_subagent
This is intentionally a backward simplification. Do not compensate by increasing hidden_dim, interactions, epochs, or cutoff.
