# Proposal 004: Readout residual bias calibration

- family: readout_bias_calibration
- phase: 2
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Add a tiny trainable global energy bias/readout residual initialized from training-only residuals to absorb remaining energy offset without changing forces independently.

## one_sentence_hypothesis
A scalar energy residual added to the same potential can correct systematic energy offsets while maintaining forces as autograd derivatives of the scalar energy.

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
- relation_to_source: ablation
- not_a_duplicate_of: Not a duplicate of proposal_001 because it adds a bounded scalar offset path rather than per-element E0 only.
- lesson_used: Generation_011/proposal_007 suggests energy offset, not missing force geometry, is the next bottleneck.

## why_not_duplicate
Not a duplicate of proposal_001 because it adds a bounded scalar offset path rather than per-element E0 only.

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
- `model/model.py::EvolutionMLIP.__init__`: add `self.energy_bias = nn.Parameter(torch.zeros(()))` or a one-dimensional `energy_shift` initialized to zero.
- `model/model.py::EvolutionMLIP.forward_energy`: add this scalar to final total energy after atomref/readout sum.
- `model/train.py::train`: optionally initialize bias from training energy residual after a no-grad source forward pass, using training samples only; otherwise zero-init.
- `model/train.py::run_epoch`: no metric-name change.

## minimal_edit_plan
1. Add one scalar trainable energy-bias parameter in the model.
2. Add it to total energy only, before force autograd, so forces remain conservative; a constant bias has zero direct force contribution.
3. If residual initialization is shape-risky, keep zero-init and train it normally.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: reduce energy MAE from global offset with almost no force/runtime cost.
- expected tradeoff: cannot fix geometry-dependent energy errors; constant shift may help RMD17 more than ISO17 if compositions vary.
- failure signal that would falsify this proposal: energy gap/MAE unchanged, confirming error is not a global offset.

## ablation_or_control
- required control or comparison: source-control proposal_010 and atomref-only proposal_001.
- optional zero-gate / source-fallback / readout-only ablation: initialize the bias to zero and freeze it for exact source fallback.

## implementation_notes_for_subagent
Implement only inside the materialized target unit, normally limited to `model/model.py` and/or `model/train.py` as listed above. Keep benchmark data, split semantics, evaluation semantics, metric field names, and runnable-unit entrypoint contract fixed. Do not add independent force heads: forces must remain `-autograd(total_energy, positions)`. Use only training-split information for any atomref or bias initialization; never use validation/test energies. If a proposed optional step becomes shape-risky, prefer the smallest source-fallback version rather than broad rewrites.
