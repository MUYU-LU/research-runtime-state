# Proposal 006: First-layer-only tensor-product geometry probe

- family: first_layer_tensor_product_probe
- phase: 4
- jump_type: exploit
- budget_class: small
- expected_capability_gain: test G018-MECH-003 with the smallest possible explicit tensor-product insertion, limiting runtime and stability risk.

## one_sentence_hypothesis
Applying a low-rank tensor-product branch only after the first interaction block should reveal whether explicit scalar/vector geometric coupling helps before deeper message mixing amplifies errors.

## mechanism_refs
- G018-MECH-003

## evidence_refs
- paper_artifact:paper_003
- repo_artifact:repo_003
- patch_blueprints.json:G018-MECH-003.bounded_edit
- mechanism_cards.json:G018-MECH-003.current_code_insertion_point
- generation_017 outcome report: neutral/bad local mixing changes motivate a bounded first-layer probe rather than a full-stack rewrite.

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: exploit
- not_a_duplicate_of: proposal_005 because this gates the TP branch to one early call site only; proposal_005 applies per interaction block.
- lesson_used: generation_017's stronger local-mixing attempts regressed; use first-layer-only scope as a stability control while still testing the evidence mechanism.

## benchmark_rationale
- rmd17 energy: early geometric coupling may improve local energy features while later source interactions keep behavior stable.
- rmd17 force: only one extra vector/scalar residual limits accumulated force-gradient risk.
- rmd17 gap / Q: expected neutral-to-positive if the mechanism is useful; little runtime overhead.
- iso17 energy: early tensor-product geometry may help conformer features before readout, but less than full-stack proposal_005.
- iso17 force: likely safer than full-stack TP branch; expected minimal regression.
- iso17 gap / Q: may help if source under-represents angular coupling; may be too weak for large gap improvement.
- training stability / runtime risk: small O(E*H) overhead once; branch scale near zero.
- control comparison expectation: should be compared to both source control and proposal_005 to distinguish mechanism benefit from scope.

## files_to_edit
- `model/model.py`
- `model/train.py` none
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInteractionBranch`: implement the same bounded l=0/l=1 branch as G018-MECH-003 but instantiate one module.
- `model/model.py::EvolutionMLIP.__init__`: add `self.first_tp_branch` and residual scale.
- `model/model.py::EvolutionMLIP.forward_energy`: after the first `BalancedInteractionBlock` call only, add TP deltas; subsequent blocks remain source behavior.
- `model/train.py`: no change.

## minimal_edit_plan
1. Implement minimal `TPInteractionBranch` with scalar->scalar, dot(vector,unit)->scalar, and scalar*unit->vector terms; omit vector-vector if needed to stay small.
2. Call it only for interaction index 0 and residual-add deltas with near-zero scale.
3. Reuse existing edge basis, edge_unit, edge_src/edge_dst, and neighbor normalization.
4. Leave body-order branch and final readout unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Ensure only the first interaction layer receives the new TP branch.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: safer force/energy coupling probe with low overhead.
- expected tradeoff: may be underpowered and land within control variance.
- failure signal that would falsify this proposal: even one TP layer causes force regression or no dataset component improves versus control.

## ablation_or_control
- required control or comparison: proposal_005 full-stack TP and exact source control.
- optional zero-gate / source-fallback / readout-only ablation: zero residual scale recovers source; scalar-only TP term can isolate vector update risk.

## implementation_notes_for_subagent
This is an exploit/scope-control version of G018-MECH-003. Do not add multiple TP modules, do not tune training weights, and do not change `config.json`.
