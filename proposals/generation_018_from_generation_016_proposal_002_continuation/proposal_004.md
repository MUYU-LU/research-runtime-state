# Proposal 004: Conservative correlation-2 product-basis residual

- family: scalar_product_basis_residual
- phase: 3
- jump_type: exploit
- budget_class: small
- expected_capability_gain: exploit G018-MECH-002 with only a conservative correlation-2 scalar product residual, avoiding a full body descriptor replacement.

## one_sentence_hypothesis
A tiny correlation-2 learned product-basis residual alongside the current body descriptor should test whether MACE-style symmetric contractions add useful chemistry without destabilizing the source model.

## mechanism_refs
- G018-MECH-002

## evidence_refs
- paper_artifact:paper_002
- repo_artifact:repo_002
- patch_blueprints.json:G018-MECH-002.bounded_edit
- mechanism_cards.json:G018-MECH-002.mathematical_form
- generation_016/proposal_002 runtime summary: parent improved over source but ISO17 energy/gap remains weaker than RMD17.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: exploit
- not_a_duplicate_of: proposal_003 because this is additive and correlation-2 only; proposal_003 replaces `_symmetrize` with a broader learned basis.
- lesson_used: generation_017 showed body-order branch changes can regress; use a minimal residual that can be zeroed instead of replacing the working body path.

## benchmark_rationale
- rmd17 energy: should be nearly neutral at initialization and may refine local angular energy.
- rmd17 force: only uses existing smooth `atom_a` features and a small residual, minimizing force disruption.
- rmd17 gap / Q: expected neutral-to-small positive; if Q drops, it is likely overfitting despite the small residual.
- iso17 energy: a compact product-basis correction may help energy decomposition across conformers without global attention cost.
- iso17 force: expected neutral because main interactions dominate forces.
- iso17 gap / Q: potential gain if learned contraction captures transferable angular correlations rather than local gate noise.
- training stability / runtime risk: very small tensor projection overhead; final residual initialized near zero.
- control comparison expectation: should exceed control only through energy/gap improvements, not merely train loss reductions.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::BodyOrderMessageBranch.__init__`: add a `ProductBasisResidual` with low rank, correlation=2, LayerNorm, and residual scale.
- `model/model.py::BodyOrderMessageBranch.forward`: after the current `_symmetrize(atom_a)` descriptor is computed, compute residual descriptor from `atom_a` and concatenate or add after projection.
- `model/model.py::BodyOrderMessageBranch._symmetrize`: leave current fixed descriptor intact for source fallback.
- `model/train.py`: no change.

## minimal_edit_plan
1. Add `ProductBasisResidual` that computes two low-rank projections of flattened `atom_a`, multiplies them elementwise, normalizes, and projects to a small descriptor.
2. Combine residual with existing descriptor through a near-zero scale or a projection that preserves descriptor dimension.
3. Keep correlation=2 only; no third-order products and no descriptor replacement.
4. Preserve existing readout and body_order_scale behavior.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Keep the existing `_symmetrize` source path available and dominant at initialization.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: small ISO17 energy/gap improvement with limited force risk.
- expected tradeoff: may be too conservative to move Q_total beyond control variance.
- failure signal that would falsify this proposal: no ISO17 energy/gap gain versus control or a body residual magnitude that grows while validation gap worsens.

## ablation_or_control
- required control or comparison: source/control replicate plus proposal_003 if selected.
- optional zero-gate / source-fallback / readout-only ablation: set product residual scale to zero; compare low rank 8 vs 16 only if implementation stays simple.

## implementation_notes_for_subagent
Do not remove or rewrite the existing body branch. This is an exploit proposal: add one compact residual from G018-MECH-002 and make source fallback easy.
