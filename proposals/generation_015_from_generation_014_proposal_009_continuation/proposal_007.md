# Proposal 007: Fixed quarter-strength vector readout simplification

- family: fixed_damped_vector_readout_simplify
- phase: 1
- jump_type: backward-simplify
- budget_class: tiny
- expected_capability_gain: Separate the benefit of vector-norm damping from learned gate capacity by using a fixed conservative vector amplitude.

## one_sentence_hypothesis
A fixed small multiplier on normalized vector norms can test whether the source's ISO17 energy/gap weakness comes from vector amplitude rather than insufficient gate expressiveness.

## mechanism_refs
- GEN015-M01-gated-invariant-vector-readout-damping

## evidence_refs
- mechanism_cards.json::GEN015-M01-gated-invariant-vector-readout-damping::bounded_generation_015_form::damped vector readout
- context.md::generation_014/proposal_009::raw normalized vector readout frontier win with ISO17 energy trend worsening
- context.md::jump_type_stats::backward-simplify best_Q_total=3.825955941893789
- proposal_constraints.json::allowed_mechanisms=GEN015-M01-gated-invariant-vector-readout-damping

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: simplify
- not_a_duplicate_of: proposal_002 because this uses no learned gate parameter and therefore isolates fixed damping from trainable gate behavior.
- why_not_duplicate: Source full-strength vector_norm and proposed learned gates do not answer whether a constant lower vector amplitude is sufficient.
- lesson_used: Backward-simplify proposals have sometimes produced frontier-quality controls; use one to de-risk over-complex gating.

## benchmark_rationale
- rmd17 energy: Expected to be slightly below source if vector amplitude matters, but may stay above scalar-only ancestors.
- rmd17 force: Force may regress due to reduced vector contribution.
- rmd17 gap / Q: Fixed damping could preserve gap stability.
- iso17 energy: Target improvement from reduced vector over-amplitude.
- iso17 force: Risk of lower force gain; acceptable only if ISO17 energy/gap improves meaningfully.
- iso17 gap / Q: Should lower gap_penalty if amplitude is the issue.
- training stability / runtime risk: Minimal; no extra modules and no new parameters.
- control comparison expectation: This is a diagnostic simplify unit; it should be compared directly to learned gate proposals and source control.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: optionally add `self.vector_readout_scale = 0.25` as a plain attribute for clarity.
- `model/model.py::EvolutionMLIP.forward_energy`: replace readout concatenation with `readout_input = torch.cat([scalar_state, self.vector_readout_scale * vector_norm], dim=-1)`.
- `model/train.py::train`: none.

## minimal_edit_plan
1. Add or inline a fixed scalar multiplier such as `0.25` for the normalized vector norm channel.
2. Multiply vector_norm before concatenation.
3. Leave every other source behavior unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not add trainable gate modules in this backward-simplify unit.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Diagnostic ISO17 energy/gap improvement with nearly zero implementation risk.
- expected tradeoff: Likely lower RMD17/ISO17 force performance than source if vector features need full amplitude.
- failure signal that would falsify this proposal: Q_total drops substantially and ISO17 gap/energy do not improve.

## ablation_or_control
- required control or comparison: Exact source control plus scalar low-start learned gate.
- optional zero-gate / source-fallback / readout-only ablation: Fixed 0.25 is an interpretable midpoint between scalar-only and source full vector readout.

## implementation_notes_for_subagent
Keep this as a simplification/control-like diagnostic. Do not introduce learnable parameters beyond the existing source model.
