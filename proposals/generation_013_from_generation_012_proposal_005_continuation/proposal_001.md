# Proposal 001: Freeze fitted atomref as fixed offset

- family: frozen_lstsq_atomref_offset
- phase: 2
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Preserve generation_012/proposal_005 force gains while reducing ISO17 energy/gap drift by making the fitted atomref a fixed SchNetPack-style offset.

## one_sentence_hypothesis
Freezing the train-split least-squares atomref immediately after initialization keeps the position-independent composition baseline from drifting under energy-only gradients, protecting ISO17 energy/gap without changing the force-producing residual path.

## mechanism_refs
- MATERIALIZED-FROZEN-LSTSQ-ATOMREF-OFFSET-001

## evidence_refs
- repo_artifact:repo_001::src/schnetpack/transform/atomistic.py::AddOffsets.forward
- repo_artifact:repo_001::src/schnetpack/atomistic/response.py::Forces.forward
- paper_artifact:paper_001::SchNet energy/force equations
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl::generation_012/proposal_005

## historical_relation
- source_unit: generation_012/proposal_005
- relation_to_source: exploit
- not_a_duplicate_of: generation_012/proposal_005 because the source initializes atomref by least squares but still leaves `atomref.weight` trainable in AdamW.
- lesson_used: proposal_005 achieved Q_total=3.8303 and excellent RMD17 energy, but ISO17 validation energy rose late while force improved; preserve the winning local message-passing core and target the offset drift only.

## benchmark_rationale
- rmd17 energy: The source mixed_energy_mae=0.0418 is already very strong; freezing the fitted baseline should preserve this scalar calibration.
- rmd17 force: The atomref is position-independent, so freezing it should leave force gradients governed by residual interactions and readout.
- rmd17 gap / Q: Low RMD17 gap_penalty should remain low; Q_rmd17 should be protected rather than chased with a larger architecture.
- iso17 energy: The main target is source ISO17 mixed_energy_mae=0.3340 and late validation energy drift.
- iso17 force: Force should remain near source mixed_force_mae=0.1853 because the residual force path is unchanged.
- iso17 gap / Q: If atomref drift caused within/other mismatch, gap_penalty=0.0691 should improve and Q_iso17 should rise.
- training stability / runtime risk: Tiny runtime change; optimizer has one fewer trainable embedding tensor.
- control comparison expectation: Should beat a direct source control primarily on ISO17 energy/gap while matching force.

## files_to_edit
- `model/train.py`
- `model/model.py` none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: keep `atomref + per_atom_energy.sum()` unchanged.
- `model/train.py::train`: capture the boolean returned by `initialize_atomref_lstsq(...)`; if true, call `model.atomref.weight.requires_grad_(False)` before constructing AdamW.

## minimal_edit_plan
1. Replace the bare `initialize_atomref_lstsq(...)` call with `atomref_fitted = initialize_atomref_lstsq(...)`.
2. Add `if atomref_fitted: model.atomref.weight.requires_grad_(False)` before optimizer creation.
3. Leave optimizer construction over `model.parameters()` so PyTorch naturally excludes the frozen parameter from gradients.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Do not change dataset splits, eval semantics, loss metric names, or `main.py` entrypoint.

## expected_benchmark_effect
- primary expected gain: Lower ISO17 mixed_energy_mae and gap_penalty with near-source RMD17 Q.
- expected tradeoff: If trainable atomref was compensating residual underfit, energy may not improve and could slightly underfit.
- failure signal that would falsify this proposal: Atomref freezing leaves ISO17 energy/gap unchanged or worsens force despite unchanged residual force path.

## ablation_or_control
- required control or comparison: Compare against generation_012/proposal_005 and the generation_013 source control.
- optional zero-gate / source-fallback / readout-only ablation: Fallback to source behavior when least-squares fitting returns false.

## implementation_notes_for_subagent
This is the smallest evidence-backed edit. Do not refactor the model. The only intended behavior change is making the already-fitted atomref a fixed additive offset before training begins.
