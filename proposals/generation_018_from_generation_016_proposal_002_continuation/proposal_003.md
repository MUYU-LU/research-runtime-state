# Proposal 003: Low-rank learned symmetric contraction body basis

- family: mace_style_learned_symmetric_contraction
- phase: 4
- jump_type: jump
- budget_class: medium
- expected_capability_gain: replace the ad-hoc Cartesian body descriptor summary with a bounded learned product-basis contraction that can capture reusable many-body angular chemistry.

## one_sentence_hypothesis
A low-rank learned symmetric contraction over the existing `atom_a` tensor should give the body-order branch a richer MACE-like many-body basis than fixed norm/A0 products, improving energy/gap without explicit triplet enumeration.

## mechanism_refs
- G018-MECH-002

## evidence_refs
- paper_artifact:paper_002
- repo_artifact:repo_002
- mechanism_cards.json:G018-MECH-002.repo_code_trace
- patch_blueprints.json:G018-MECH-002
- generation_017 outcome report: local body-order/PaiNN repairs were tradeoffs, so this proposal changes the product-basis mechanism rather than another gate.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: jump
- not_a_duplicate_of: generation_017/proposal_001/proposal_002 because those changed gates around body-order features; this replaces `_symmetrize` with learned contraction weights and explicit correlation order.
- lesson_used: the current best has a body-order residual, but generation_017 local repairs did not beat it; keep the branch but diversify the descriptor family using G018-MECH-002.

## benchmark_rationale
- rmd17 energy: richer low-order angular invariants may improve conformer energy while using the current smooth RBF/cutoff features.
- rmd17 force: contraction is differentiable through existing edge directions and distances; no explicit triplets keeps force gradients stable.
- rmd17 gap / Q: may improve or remain neutral if descriptor dimension is capped and residual scale is damped.
- iso17 energy: many-body product-basis features should help energy transfer across conformers, where current ISO17 energy and gap are the bottlenecks.
- iso17 force: force fit may remain close because local interaction stack is unchanged and body readout remains residual.
- iso17 gap / Q: expected gain from structured descriptor sharing rather than free local MLP gates.
- training stability / runtime risk: tensor contractions over `[N,C,L,T]` are moderate; cap rank/correlation and initialize output near zero.
- control comparison expectation: should beat control if energy/gap improve; if only train loss improves while gap worsens, it repeats generation_017 tradeoffs.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::LearnedSymmetricContraction`: add a small module used by `BodyOrderMessageBranch` to contract `atom_a`.
- `model/model.py::BodyOrderMessageBranch.__init__`: add correlation/order/rank settings, learned contraction weights, update `descriptor_dim`, and keep body residual scale damped.
- `model/model.py::BodyOrderMessageBranch._symmetrize`: replace fixed norm/A0 products with low-rank learned correlation-2/3 scalar contractions.
- `model/model.py::BodyOrderMessageBranch.forward`: keep `atom_a` construction and message aggregation but route descriptors through the new contraction.
- `model/train.py`: no change.

## minimal_edit_plan
1. Implement `LearnedSymmetricContraction` that flattens low-l/current Cartesian channels from `atom_a`, computes correlation-2 products via low-rank projections, and optionally a bounded correlation-3 term.
2. Replace `_symmetrize` return features with normalized learned contraction features while keeping input/output tensor shapes `[N, descriptor_dim]`.
3. Limit descriptor size to no more than the current body descriptor scale; initialize final projection or branch scale near zero.
4. Leave `BalancedInteractionBlock`, readout, train losses, atomref, and benchmark semantics unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not import MACE/e3nn; implement bounded PyTorch contractions only.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 and RMD17 energy/gap via richer many-body angular invariants.
- expected tradeoff: more parameters in body branch may overfit and hurt gap if not damped.
- failure signal that would falsify this proposal: train energy improves but ISO17 other_energy/gap worsens, or runtime grows materially without Q gain.

## ablation_or_control
- required control or comparison: source control and current `_symmetrize` branch behavior.
- optional zero-gate / source-fallback / readout-only ablation: correlation=2 only versus correlation=2+3; final contraction scale zero should recover source body branch contribution.

## implementation_notes_for_subagent
This proposal must be a real descriptor-family replacement, not another local gate. If correlation=3 becomes too complex, implement correlation=2 low-rank contraction cleanly and document the omitted third-order term.
