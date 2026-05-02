# Proposal 006: Late readout energy adapter

- family: late_energy_adapter
- phase: 3
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Add a narrow residual MLP on existing scalar/vector-norm readout features that is activated only for energy readout, paired with late energy reweighting.

## one_sentence_hypothesis
A tiny additional energy readout adapter can improve geometry-dependent energy residuals beyond atomref offsets while still deriving forces from the same scalar potential.

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
- relation_to_source: jump
- not_a_duplicate_of: Not a duplicate of generation_011 representation changes because it does not add message-passing capacity; it only augments terminal energy readout with a bounded residual.
- lesson_used: If energy error is not purely composition/global offset, a tiny readout adapter is the next bounded jump before adding expensive equivariance.

## why_not_duplicate
Not a duplicate of generation_011 representation changes because it does not add message-passing capacity; it only augments terminal energy readout with a bounded residual.

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
- `model/model.py`
- `model/train.py`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `energy_adapter = Linear(2H,H//2)->SiLU->Linear(H//2,1)` initialized with near-zero final layer.
- `model/model.py::EvolutionMLIP.forward_energy`: compute adapter on the same `torch.cat([scalar_state, vector_norm], dim=-1)` features and add its summed contribution to per-atom energy.
- `model/train.py::train`: use mild late energy schedule from mechanism card; no dataloader changes.
- `model/train.py::run_epoch`: preserve loss/metric names.

## minimal_edit_plan
1. Add the narrow adapter with zero or very small final-layer initialization so source behavior is the starting point.
2. Add adapter output to `per_atom_energy` before summation; do not create independent force predictions.
3. Pair with conservative final-quarter energy reweighting and leave interaction blocks untouched.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 and RMD17 energy MAE if residual energy shape, not only offset, is limiting.
- expected tradeoff: extra parameters may slightly perturb force gradients; runtime increases minimally.
- failure signal that would falsify this proposal: training instability or force regression without energy improvement.

## ablation_or_control
- required control or comparison: proposal_003 calibration-only and proposal_010 control.
- optional zero-gate / source-fallback / readout-only ablation: zero-initialize and optionally freeze adapter final layer to recover source readout.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
