# Proposal 003: Nu-2 invariant energy-only exploit

- family: body_order_energy_exploit
- phase: 3
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Capture the lowest-risk three-body invariant signal for ISO17 energy/gap with minimal implementation surface.

## one_sentence_hypothesis
A truncated nu=2 invariant residual energy head, without descriptor message passing or readout rewrites, can test whether explicit angular body-order features alone explain the source unit's ISO17 energy weakness.

## mechanism_refs
- GEN016-M01-cace-shadow-body-order-representation

## evidence_refs
- paper_artifact:paper_001
- repo_artifact:repo_001
- mechanism_cards.json::GEN016-M01-cace-shadow-body-order-representation B^(2) body-order derivation
- patch_blueprints.json::GEN016-M01-cace-shadow-body-order-representation bounded_edit truncation guidance
- benchmark_diagnosis.json::generation_015/proposal_004 RMD17 Q=4.075989472741923, ISO17 Q=3.623719881734134

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: exploit
- not_a_duplicate_of: Not a local source-block tweak; it adds a separate minimal representation branch but deliberately omits the riskier body-order message update.
- lesson_used: The parent is already strong enough that a low-risk residual probe is preferable to a broad rewrite when testing the first body-order mechanism.

## why_not_duplicate
This differs from proposal_001 by restricting the branch to nu=2 contracted invariants and a linear/tiny MLP energy residual; it is an exploit-sized probe rather than the fuller M01 implementation.

## benchmark_rationale
- rmd17 energy: Should be protected by very small alpha and minimal branch capacity.
- rmd17 force: Lower risk than a message-passed branch.
- rmd17 gap / Q: Expected neutral.
- iso17 energy: Could improve if missing feature is angular/body-order rather than nonlocal decomposition.
- iso17 force: Small smooth residual may mildly improve gradients or remain neutral.
- iso17 gap / Q: Main target is modest gap_penalty reduction.
- training stability / runtime risk: Small/medium; feature scale normalization is the main risk.
- control comparison expectation: Should be close to source if body-order features are unhelpful; a small ISO17 energy improvement is meaningful.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::new MinimalNu2Branch`: compute l=0,1,2 angular monomials; scatter compact edge features to atoms; form squared/contracted nu=2 features only.
- `model/model.py::EvolutionMLIP.__init__`: add branch, LayerNorm, small residual readout, and `body_order_log_scale` initialized near -5.
- `model/model.py::EvolutionMLIP.forward_energy`: call branch after `edge_basis` and add residual to the source energy return.
- `model/train.py::none`: no training-loop changes.

## minimal_edit_plan
1. Implement a compact branch producing per-atom B features from existing `i_idx`, `j_idx`, `unit`, `edge_basis`, and `cutoff_weight`.
2. Use only l<=2 and at most 4-6 projected radial channels; normalize B features before readout.
3. Add `sigmoid(log_scale) * residual.sum()` to the existing source energy.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops.
- [ ] Keep branch residual initialized smaller than proposal_001 because this is an exploit probe.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Small ISO17 Q gain from lower mixed_energy_mae/gap.
- expected tradeoff: Limited capacity may be too weak to help; still adds some overhead.
- failure signal that would falsify this proposal: No ISO17 energy/gap improvement while residual scale remains nonzero, or RMD17 force worsens.

## ablation_or_control
- required control or comparison: generation_015/proposal_004 control.
- optional zero-gate / source-fallback / readout-only ablation: nu=1-only branch to confirm nu=2 contractions are the active ingredient.

## implementation_notes_for_subagent
Prefer the smallest implementation that cleanly exercises M01: no descriptor message, no external dependencies, no changes to source interaction blocks.
