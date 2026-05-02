# Proposal 006: Body-order conditioned nonlocal energy

- family: body_order_conditioned_nonlocal
- phase: 4
- jump_type: wildcard
- budget_class: medium
- expected_capability_gain: Combine explicit local body-order representation with a bounded nonlocal energy decomposition to attack ISO17 energy/gap from two evidence-backed paths.

## one_sentence_hypothesis
Using compact body-order descriptors to condition latent charges will produce a more geometry-aware nonlocal residual than scalar-state charges alone, improving ISO17 conformer energy while retaining source fallback scales.

## mechanism_refs
- GEN016-M01-cace-shadow-body-order-representation
- GEN016-M02-bounded-electrostatic-energy-decomposition

## evidence_refs
- paper_artifact:paper_001
- paper_artifact:paper_002
- repo_artifact:repo_001
- mechanism_cards.json::GEN016-M01-cace-shadow-body-order-representation
- mechanism_cards.json::GEN016-M02-bounded-electrostatic-energy-decomposition
- patch_blueprints.json::GEN016-M01-cace-shadow-body-order-representation
- patch_blueprints.json::GEN016-M02-bounded-electrostatic-energy-decomposition
- benchmark_diagnosis.json::generation_015/proposal_004 ISO17 energy/gap bottleneck

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: jump/wildcard hybrid
- not_a_duplicate_of: This combines representation-path and energy-decomposition/nonlocal-path departures; it is not a single local block or readout variant.
- lesson_used: If ISO17 weakness comes from both missing angular descriptors and missing nonlocal decomposition, a coupled but still bounded residual may be needed.

## why_not_duplicate
The proposal uses body-order B features as inputs to the q-head and residual energy head, so it differs from pure body-order residuals and pure scalar-state electrostatic residuals.

## benchmark_rationale
- rmd17 energy: Protected by separate near-zero body-order and electrostatic scales.
- rmd17 force: Higher risk because two residual paths contribute gradients; scales must be tiny.
- rmd17 gap / Q: Expected neutral if source fallback is preserved.
- iso17 energy: Primary expected gain from geometry-conditioned nonlocal energy.
- iso17 force: Could improve if nonlocal residual has smooth angular conditioning; could regress if both branches overfit.
- iso17 gap / Q: Higher upside than single-mechanism proposals, with higher risk.
- training stability / runtime risk: Medium/large; keep branch widths minimal and no descriptor message pass.
- control comparison expectation: Should outperform single-path proposals only if mechanisms are complementary.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::new MinimalBodyOrderBranch`: compute compact B features as in M01 but no message pass.
- `model/model.py::EvolutionMLIP.__init__`: add body-order branch, B projection into hidden_dim, q head over `torch.cat([scalar_state, b_proj], -1)`, electrostatic residual scales, and optional B residual head.
- `model/model.py::EvolutionMLIP.forward_energy`: compute B features from edge tensors; after scalar_state finalization, compute geometry-conditioned q and nonlocal residual; add tiny scaled B-local and electrostatic residuals to source energy.
- `model/train.py::none`: retain source weights.

## minimal_edit_plan
1. Implement minimal B features with l<=2 and few radial/type channels.
2. Project B features and concatenate with final scalar_state for `charge_head`; neutralize q and compute damped all-pair residual.
3. Add source local energy plus two tiny residuals: optional B per-atom energy and geometry-conditioned electrostatic energy.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` local/residual atomic terms plus scalar pair residual and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops; only O(E*Bdim) body-order tensors and O(N^2) pair residual.
- [ ] Initialize both residual scales near no-op to protect source behavior.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Larger ISO17 Q improvement than single-mechanism proposals through energy/gap gains.
- expected tradeoff: More implementation complexity, runtime, and overfitting risk.
- failure signal that would falsify this proposal: Both residual scales grow while ISO17 energy/gap and RMD17 force regress.

## ablation_or_control
- required control or comparison: source control plus single-mechanism proposal comparisons if available.
- optional zero-gate / source-fallback / readout-only ablation: zero B-to-q projection or zero electrostatic scale to isolate the contribution.

## implementation_notes_for_subagent
This is the broadest architecture-departure proposal in the set. Keep it bounded by using static body-order descriptors only; do not add descriptor message passing or full charge-equilibration here.
