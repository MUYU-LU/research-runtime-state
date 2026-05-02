# Proposal 009: Simplified body branch with product-basis diagnostic projection

- family: body_branch_product_basis_simplify
- phase: 3
- jump_type: backward-simplify
- budget_class: small
- expected_capability_gain: remove fragile ad-hoc body descriptor degrees while keeping a tiny G018-MECH-002 diagnostic projection to test whether simpler invariants generalize better.

## one_sentence_hypothesis
Collapsing the current body-order branch to a smaller normalized correlation-2 projection should reduce overfit/tradeoff risk while retaining the MACE-inspired product-basis signal most likely to transfer.

## mechanism_refs
- G018-MECH-002

## evidence_refs
- paper_artifact:paper_002
- repo_artifact:repo_002
- patch_blueprints.json:G018-MECH-002
- generation_017 outcome report: body-order/PaiNN local additions mostly created benchmark tradeoffs; a backward-simplify branch is needed.
- mechanism_cards.json:G018-MECH-002.ablation_or_control: current `_symmetrize` branch unchanged and correlation=2 only comparisons.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: simplify
- not_a_duplicate_of: generation_017/proposal_007 because that behaved as a control replicate/no tracked code diff; this makes an explicit smaller body descriptor change based on G018-MECH-002.
- lesson_used: if richer local branches overfit or trade off, simplify the body path and measure whether source gains came from variance rather than descriptor complexity.

## benchmark_rationale
- rmd17 energy: may lose some source energy gain if the body branch was beneficial; bounded simplification tests whether simpler features are enough.
- rmd17 force: fewer body descriptor degrees may stabilize forces and reduce noisy gradients.
- rmd17 gap / Q: expected neutral if source body branch was partly overparameterized; negative if it was essential.
- iso17 energy: simplification may improve gap/generalization if prior body complexity overfit RMD17-like local patterns.
- iso17 force: could improve if gradients become smoother; monitor any loss of geometric expressivity.
- iso17 gap / Q: the main target is reducing gap_penalty rather than maximizing train fit.
- training stability / runtime risk: lower runtime/parameter cost than source body branch; implementation risk is shape mismatch.
- control comparison expectation: should be judged as a diagnostic/simplification: useful if it beats or matches control with lower complexity.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::BodyOrderMessageBranch.__init__`: reduce descriptor/projection width and add one small normalized correlation-2 diagnostic projection.
- `model/model.py::BodyOrderMessageBranch._symmetrize`: replace multi-part fixed descriptor with a smaller `[norm_l, a0_product, low_rank_product]` descriptor; remove any redundant high-dimensional concatenation.
- `model/model.py::BodyOrderMessageBranch.forward`: keep edge aggregation and body readout shape consistent after descriptor_dim update.
- `model/train.py`: no change.

## minimal_edit_plan
1. Identify the current `_symmetrize` descriptor pieces and reduce them to the smallest smooth invariant set: norms plus a low-rank correlation-2 product projection.
2. Update `descriptor_dim`, LayerNorm/readout input sizes, and any projection dimensions accordingly.
3. Keep body_order_scale damping and the parent interaction/readout stack unchanged.
4. Add comments that this is a backward-simplify diagnostic, not a full MACE product-basis implementation.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Ensure descriptor_dim/readout dimensions are internally consistent after simplification.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: lower ISO17 gap or neutral Q with less complexity, clarifying whether body branch complexity is hurting generalization.
- expected tradeoff: may reduce RMD17 Q if the full source body descriptor was necessary.
- failure signal that would falsify this proposal: both datasets lose Q versus source/control without a runtime/stability benefit.

## ablation_or_control
- required control or comparison: exact source control and proposal_003/004 product-basis variants if selected.
- optional zero-gate / source-fallback / readout-only ablation: disable the low-rank product projection to test pure simplification in a later round.

## implementation_notes_for_subagent
Simplify deliberately. Do not add more gates, more readout damping, or PaiNN-like terms. The only new mechanism is the tiny correlation-2 diagnostic projection grounded in G018-MECH-002.
