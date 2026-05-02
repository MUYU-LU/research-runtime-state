# Proposal 007: Element-conditioned late energy scale

- family: element_energy_scale
- phase: 3
- jump_type: jump
- budget_class: small
- expected_capability_gain: Add a per-element multiplicative scale on the final per-atom readout contribution, initialized at one, to calibrate element-specific energy residuals.

## one_sentence_hypothesis
Element-conditioned energy scaling can correct systematic per-element readout amplitude errors while keeping the same local invariant features and autograd force path.

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
- not_a_duplicate_of: This differs from atomref proposals by scaling geometry-dependent per-atom readout rather than adding a constant E0 baseline.
- lesson_used: The evidence points to atomwise decomposition; scaling readout per element is a bounded extension of that decomposition.

## why_not_duplicate
This differs from atomref proposals by scaling geometry-dependent per-atom readout rather than adding a constant E0 baseline.

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
- `model/model.py::EvolutionMLIP.__init__`: add an embedding or parameter table `readout_scale` over atomic numbers initialized to 1.0, optionally constrained with `1 + 0.1*tanh(raw)`.
- `model/model.py::EvolutionMLIP.forward_energy`: multiply `per_atom_energy` by scale selected by `numbers` before summing, then add atomref.
- `model/train.py::train`: use source or mild late energy schedule; no split/eval changes.
- `model/train.py::run_epoch`: no metric field changes.

## minimal_edit_plan
1. Add a bounded per-element scale parameter initialized for exact source equivalence.
2. Apply the scale only to the scalar per-atom readout contribution before summation; keep atomref and forces conservative.
3. Optionally combine with mild late energy schedule if it remains a small scalar edit.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy transfer where element-specific residual amplitudes differ across molecules.
- expected tradeoff: force gradients are scaled too, so force MAE may move if scales drift.
- failure signal that would falsify this proposal: scales drift but Q_total worsens, indicating calibration destabilized force/energy balance.

## ablation_or_control
- required control or comparison: proposal_001 atomref-only and proposal_010 source-control.
- optional zero-gate / source-fallback / readout-only ablation: clamp all scales to 1.0.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
