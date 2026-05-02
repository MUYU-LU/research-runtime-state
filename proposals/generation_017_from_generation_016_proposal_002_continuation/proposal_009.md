# Proposal 009: Weak normalized l2 contraction stabilizer

- family: weak_body_order_normalization
- phase: 3
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: Test a very small weak-evidence descriptor-normalization change to reduce body-order energy drift without expanding to a full CAMP/TACE hierarchy.

## one_sentence_hypothesis
Normalizing the source l1/l2 Cartesian contractions before descriptor messaging may reduce ISO17 energy instability by controlling body-order feature scale, but this is weak/background evidence rather than a strong mechanism claim.

## mechanism_refs
- GEN017-M02-cartesian-tensor-contraction-background (weak_hypothesis only)

## evidence_refs
- mechanism_cards.json::GEN017-M02 claim_strength=weak_hypothesis, strong_ready=false, downgrade_reasons missing repo_code_path and missing_repo_code_trace
- patch_blueprints.json::GEN017-M02 implementation_ready=false and bounded_edit says at most test one additional normalized contraction/background
- benchmark_diagnosis.json::generation_016/proposal_002 ISO17 energy_trend=worsening while force_trend=improving
- proposal_constraints.json::blocked_mechanisms forbids implementation rewrite without patch blueprint; this proposal is intentionally a small diagnosis-driven wildcard, not a strong mechanism

## historical_relation
- source_unit: generation_016/proposal_002
- relation_to_source: ablation
- not_a_duplicate_of: No generation_016 selected proposal tested source-specific l1/l2 descriptor normalization inside the one-step body-order message branch; prior attempts changed branch size, message path, electrostatics, or training weights.
- lesson_used: Fuller body-order capacity harmed energy; if touching Cartesian contractions, keep the edit tiny and scale-controlled.

## why_not_duplicate
This does not add new tensor ranks, full TACE/CAMP contractions, or new evidence-backed mechanisms. It only normalizes existing `_symmetrize` outputs in the current source branch as a weak wildcard diagnostic.

## benchmark_rationale
- rmd17 energy: Could improve or remain stable if descriptor scale is better controlled.
- rmd17 force: Should not add new geometric derivatives beyond existing contractions.
- rmd17 gap / Q: Expected small effect; reject large regression.
- iso17 energy: May improve if late energy drift is caused by unstable body-order descriptor scale.
- iso17 force: Expected mostly stable because no new message edges are added.
- iso17 gap / Q: A positive signal would motivate future stronger evidence gathering for descriptor normalization.
- training stability / runtime risk: Low overhead but weak scientific confidence.
- control comparison expectation: Should only be interpreted as diagnostic unless it clearly beats source control.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::BodyOrderMessageBranch._symmetrize`: after computing `b0`, `b1`, `b2`, and `b0_sq`, apply bounded per-block normalization such as `b1 = b1 / sqrt(mean(b1^2, dim=(1,2), keepdim=True)+eps)` and same for `b2`, or add LayerNorm after concatenation.
- `model/model.py::BodyOrderMessageBranch.__init__`: optionally add `self.symmetrize_norm = nn.LayerNorm(self.descriptor_dim)` if not reusing `initial_norm`.
- `model/train.py::none`: no training change.

## minimal_edit_plan
1. Keep `_angular_monomials`, descriptor dimension, message aggregation, and readout unchanged.
2. Add one normalization step to existing l1/l2 contraction outputs or the concatenated descriptor before `initial_norm`/message.
3. Use a small epsilon and no data-dependent control flow that changes benchmark semantics.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Mark GEN017-M02 as weak/background, not strong evidence.
- [ ] Do not increase descriptor dimension or add full tensor hierarchy.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Reduced ISO17 energy drift via better descriptor scale control.
- expected tradeoff: Weak-evidence proposal; normalization could remove useful magnitude information and lower Q.
- failure signal that would falsify this proposal: No energy/gap improvement or any strong RMD17 regression compared with exact control.

## ablation_or_control
- required control or comparison: Exact source control.
- optional zero-gate / source-fallback / readout-only ablation: Revert normalization to recover source `_symmetrize` behavior.

## implementation_notes_for_subagent
Treat this as a wildcard diagnostic. Do not cite GEN017-M02 as implementation-ready, and do not add new monomials or tensor-contraction paths.
