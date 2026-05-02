# Proposal 002: Norm-only PaiNN body-order conditioner

- family: painn_norm_body_gate
- phase: 3
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: Isolate whether vector-state norms alone can stabilize the body-order residual with lower variance than the full norm-plus-dot gate.

## one_sentence_hypothesis
Conditioning the existing body-order descriptor only on `||Vv||` will capture PaiNN-style scalar/vector coupling while avoiding the extra dot-product capacity that could overfit ISO17 energy.

## mechanism_refs
- GEN017-M01-painn-style-scalar-vector-mixing-gate

## evidence_refs
- mechanism_cards.json::GEN017-M01 ablation_or_control says norm-only ablation tests whether the PaiNN scalar product term is necessary
- patch_blueprints.json::GEN017-M01 target insertion point in `EvolutionMLIP.forward_energy`
- evidence_provenance.json::repo_artifact:repo_002::src/schnetpack/representation/painn.py::PaiNNMixing.forward
- benchmark_diagnosis.json::iso17 energy_trend=worsening, mixed_energy_mae=0.3058581381200019, gap_penalty=0.11346597420504244
- generation_memory.json::no completed-generation summaries for this exact source, so source-specific variance still needs controlled ablations

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: exploit
- not_a_duplicate_of: The source has no vector-conditioned body-order readout; proposal_001 uses both norm and dot, while this deliberately removes the dot term.
- lesson_used: The source improves Q_total within neutral margin but has ISO17 energy drift; use the weakest PaiNN-derived coupling that can address the drift.

## why_not_duplicate
This proposal is a narrower ablation of the strong M01 mechanism, not a repeat of generation_016/proposal_003 minimal nu=2 branch and not the full M01 proposal. It adds only one vector projection and a norm-conditioned descriptor gate.

## benchmark_rationale
- rmd17 energy: Expected to be nearly unchanged because the new path is tiny and near-zero initialized.
- rmd17 force: Lower force risk than full norm+dot because only vector magnitudes enter.
- rmd17 gap / Q: Should remain within source/control variance.
- iso17 energy: May improve if under-conditioned body-order residual needs vector-state scale but not orientation-channel dot interactions.
- iso17 force: Expected stable; no new edge messages or tensor contractions.
- iso17 gap / Q: A small gain would support norm-based scalar/vector mixing as sufficient.
- training stability / runtime risk: Tiny overhead and low implementation risk.
- control comparison expectation: Should outperform the control if vector magnitude context matters; should be safer than proposal_001 if dot capacity overfits.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add one `body_vector_v = nn.Linear(hidden_dim, hidden_dim)` and a small `body_norm_gate` MLP from `[body_order_descriptor, norm_v]` to descriptor_dim, with zero/negative-start output scale.
- `model/model.py::EvolutionMLIP.forward_energy`: after interactions, compute `v_proj` from `vector_state`, `norm_v = sqrt(sum(v_proj*v_proj, dim=-1)+1e-8)`, concatenate with `body_order_descriptor`, and add a damped correction before readout.
- `model/train.py::none`: keep training schedule unchanged.

## minimal_edit_plan
1. Add a single vector channel projection and descriptor correction MLP.
2. Compute only `norm_v`, not `dot_uv`, and keep the correction scale initialized to no-op.
3. Pass the corrected descriptor through the existing `body_order_readout`; do not touch source scalar/vector readout.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not introduce the dot product term in this ablation.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: A controlled ISO17 energy/gap improvement with less variance than the full gate.
- expected tradeoff: May underfit if dot/alignment information is necessary.
- failure signal that would falsify this proposal: No ISO17 energy/gap gain over control or weaker result than full norm+dot with similar RMD17 stability.

## ablation_or_control
- required control or comparison: Exact generation_016/proposal_002 control and proposal_001 full gate if selected.
- optional zero-gate / source-fallback / readout-only ablation: Set `body_norm_gate` final scale to zero.

## implementation_notes_for_subagent
Keep this intentionally tiny. Do not add `body_vector_u`, do not compute dot products, and do not change body-order radial/type dimensions.
