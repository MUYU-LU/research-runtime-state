# Proposal 002: Small-gate invariant vector readout

- family: gated_invariant_vector_readout
- phase: 2
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Recover useful vector-readout energy information while limiting the variance that may have motivated proposal_007's scalar-only simplification.

## one_sentence_hypothesis
A learned low-initialized scalar gate on `||vector_state||` lets the model reintroduce invariant geometric energy evidence only when training supports it, improving Q_total with less gap/energy volatility than a full readout restoration.

## mechanism_refs
- GEN014-M01-invariant-vector-readout-repair

## evidence_refs
- mechanism_cards.json::GEN014-M01-invariant-vector-readout-repair::bounded learned gate option
- patch_blueprints.json::GEN014-M01-invariant-vector-readout-repair::optional learned scalar gate
- benchmark_diagnosis.json::proposal_007 improved gap but lost Q_total

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: exploit
- not_a_duplicate_of: proposal_001 because this adds an explicit low-initialized gate rather than restoring vector_norm at full readout strength.
- why_not_duplicate: generation_013/proposal_007 has no vector readout; generation_013/proposal_001 did not test a bounded gate from proposal_007.
- lesson_used: Full vector path may help energy but scalar-only improved gap; gate the mechanism rather than choosing an all-or-nothing readout.

## benchmark_rationale
- rmd17 energy: Expected improvement from partial geometry readout.
- rmd17 force: Expected modest improvement because force can flow through gated vector_norm.
- rmd17 gap / Q: Should protect more of proposal_007's small gap gain than full restoration.
- iso17 energy: Targeted recovery of scalar-only energy regression.
- iso17 force: Neutral to modestly positive.
- iso17 gap / Q: Q improves if the gate avoids overfitting other-conformation energy.
- training stability / runtime risk: Low; one parameter or tiny gate module, no new loops.
- control comparison expectation: Should sit between proposal_007 scalar-only and full vector readout in gap/energy tradeoff.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add `self.vector_readout_logit = nn.Parameter(torch.tensor(-2.0))` or an equivalent scalar gate and widen readout to `hidden_dim * 2`.
- `model/model.py::EvolutionMLIP.forward_energy`: compute `vector_norm`, multiply by `torch.sigmoid(self.vector_readout_logit)`, concatenate with `scalar_state`, then read out energy.
- `model/train.py::train`: none.

## minimal_edit_plan
1. Add a single learned scalar gate initialized so sigmoid is small but nonzero.
2. Restore readout input width to `hidden_dim * 2`.
3. Concatenate `scalar_state` with gated `vector_norm` for per-atom energy.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Keep the gate global and scalar; do not add attention or per-edge heads.

## expected_benchmark_effect
- primary expected gain: Q_total recovery versus proposal_007 with less gap penalty regression than Proposal 001.
- expected tradeoff: May underuse vector geometry if the gate remains too small.
- failure signal that would falsify this proposal: No energy/Q recovery versus proposal_007, or gate causes instability.

## ablation_or_control
- required control or comparison: Compare to exact proposal_007 and Proposal 001 full vector restoration.
- optional zero-gate / source-fallback / readout-only ablation: Gate initialized near zero acts as a source-fallback ablation.

## implementation_notes_for_subagent
Keep this a readout-only exploit. Do not alter `BalancedInteractionBlock` internals or training schedule.
