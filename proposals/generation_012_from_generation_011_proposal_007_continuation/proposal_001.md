# Proposal 001: Train-split atomref initialization only

- family: atomref_calibration
- phase: 2
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Recover ISO17 energy transfer by initializing the existing atomref table from training-only composition/energy statistics while leaving all interaction equations and epoch weights unchanged.

## one_sentence_hypothesis
Training-only per-element atomref initialization should reduce global energy offsets on ISO17 without disturbing the conservative force path that made generation_011/proposal_007 force-competitive.

## mechanism_refs
- MATERIALIZED-ENERGY-BASELINE-STAGE2-001

## evidence_refs
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T083923Z/mechanism_cards.json
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T083923Z/patch_blueprints.json
- paper_artifact:paper_001
- paper_artifact:paper_002
- repo_artifact:repo_001
- /home/lmy/.openclaw/workspace/research_runtime/ledger/frontier.jsonl

## historical_relation
- source_unit: generation_011/proposal_007
- relation_to_source: exploit
- not_a_duplicate_of: generation_011/proposal_004/005/006/007/008 changed representation or schedules; this isolates atomref initialization and does not repeat prior vector-capacity edits.
- lesson_used: generation_011/proposal_007 had good ISO17 force but weak ISO17 energy, so use the MACE-style E0 baseline before adding capacity.

## why_not_duplicate
generation_011/proposal_004/005/006/007/008 changed representation or schedules; this isolates atomref initialization and does not repeat prior vector-capacity edits.

## benchmark_rationale
- rmd17 energy: should remain close to source unless the edit directly changes the energy readout or loss weighting; any gain is secondary to ISO17 recovery.
- rmd17 force: protect the source unit's conservative force path; force-only gains are not sufficient if energy/Q regress.
- rmd17 gap / Q: monitor for gap penalty changes caused by calibration drift; source-like RMD17 Q is acceptable.
- iso17 energy: primary diagnostic for generation_012 because generation_011/proposal_007 improved force but left an energy-transfer bottleneck.
- iso17 force: should stay near source; modest regression is acceptable only if energy/Q improves materially.
- iso17 gap / Q: target lower `mixed_energy_mae` and better `Q_iso17` without worsening split gap semantics.
- training stability / runtime risk: bounded; no benchmark data, split, eval, metric-field, or entrypoint changes are allowed.
- control comparison expectation: compare against proposal_010 source-control and the source unit generation_011/proposal_007.

## files_to_edit
- `model/train.py`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: keep existing trainable `atomref` embedding, no architecture change.
- `model/model.py::EvolutionMLIP.forward_energy`: preserve `atomref(numbers).sum() + readout(...).sum()`.
- `model/train.py::train`: before optimizer construction, scan only the training loader to compute count-normalized per-element energy offsets and copy observed values into `model.atomref.weight` under `torch.no_grad()`.
- `model/train.py::run_epoch`: no loss formula change.

## minimal_edit_plan
1. Add a helper in `train.py` that accumulates per-element counts and a simple count-normalized target from training energies and atomic numbers only.
2. Call the helper after model construction/device placement and before AdamW construction; copy only observed atomic numbers into `model.atomref.weight`.
3. Leave `epoch_energy_weight`, `epoch_force_weight`, metric logging keys, dataloaders, cutoffs, RBFs, vector blocks, and output schema unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: lower ISO17 `mixed_energy_mae` and `Q_iso17` via reduced global composition offset.
- expected tradeoff: negligible runtime change; slight risk that crude per-element offsets are noisy in small training split.
- failure signal that would falsify this proposal: ISO17 energy does not improve while RMD17 or ISO17 force worsens beyond source variance.

## ablation_or_control
- required control or comparison: compare directly to proposal_010 source-control and to proposal_002 late-reweight-only ablation.
- optional zero-gate / source-fallback / readout-only ablation: revert atomref weights to source initialization while keeping identical training schedule.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
