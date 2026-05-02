# Proposal 001: Restore invariant vector-norm readout

- family: invariant_vector_readout_repair
- phase: 2
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Recover the energy/Q lost by scalar-only proposal_007 while keeping its successful local message-passing body unchanged.

## one_sentence_hypothesis
Re-adding `||vector_state||` to the per-atom readout restores the invariant geometry-to-energy path that proposal_007 removed, improving energy and Q_total without changing neighbor lists, splits, metrics, or force-from-energy semantics.

## mechanism_refs
- GEN014-M01-invariant-vector-readout-repair

## evidence_refs
- evidence_quality.json::grade=A::strong_card_target_met
- mechanism_cards.json::GEN014-M01-invariant-vector-readout-repair
- patch_blueprints.json::GEN014-M01-invariant-vector-readout-repair
- benchmark_diagnosis.json::generation_013/proposal_007::Q_total=3.75578478119853::G_delta=-0.07451670430602064

## historical_relation
- source_unit: generation_013/proposal_007
- relation_to_source: exploit
- not_a_duplicate_of: generation_013/proposal_001 because this starts from proposal_007 and changes only the deleted readout path, leaving proposal_007's scalar body and frozen atomref behavior intact.
- why_not_duplicate: generation_013/proposal_007 is scalar-only; this is the direct evidence-backed reversal of only that scalar-only readout decision.
- lesson_used: proposal_007 improved gap modestly but regressed mixed_energy_mae and Q_total; do not optimize gap/force at the expense of energy/Q.

## benchmark_rationale
- rmd17 energy: Expected to improve toward generation_013/proposal_001 by restoring geometry-derived invariant features.
- rmd17 force: Should recover some force sensitivity because energy again depends on vector geometry.
- rmd17 gap / Q: Gap penalty may rise from proposal_007, but Q should improve if energy/force recovery dominates.
- iso17 energy: Primary target; scalar-only proposal_007 worsened ISO17 mixed_energy_mae.
- iso17 force: Expected small improvement or neutral relative to proposal_007.
- iso17 gap / Q: Q_iso17 should improve if energy regression was caused by deleting vector_norm.
- training stability / runtime risk: Low; no new loops and only readout input width returns to `hidden_dim * 2`.
- control comparison expectation: Must beat exact proposal_007 control on Q_total to justify keeping vector readout.

## files_to_edit
- `model/model.py`
- `model/train.py` if needed, otherwise `none`

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: change first readout layer from `nn.Linear(hidden_dim, hidden_dim)` to `nn.Linear(hidden_dim * 2, hidden_dim)`.
- `model/model.py::EvolutionMLIP.forward_energy`: after the interaction loop compute `vector_norm = torch.linalg.norm(vector_state, dim=-1)` and pass `torch.cat([scalar_state, vector_norm], dim=-1)` to `self.readout`.
- `model/train.py::train`: none; preserve proposal_007 atomref behavior.

## minimal_edit_plan
1. Change the readout input dimension to `hidden_dim * 2`.
2. Compute `vector_norm` immediately before per-atom readout.
3. Replace scalar-only readout with concatenated `[scalar_state, vector_norm]` readout.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.
- [ ] Do not change epochs, cutoff, hidden_dim, data splits, output schema, or `main.py`.

## expected_benchmark_effect
- primary expected gain: Higher mixed_energy/Q on ISO17 and RMD17 than proposal_007.
- expected tradeoff: Slight gap penalty regression versus scalar-only source.
- failure signal that would falsify this proposal: Q_total remains below source or energy does not improve while gap worsens.

## ablation_or_control
- required control or comparison: Exact proposal_007 control replicate and generation_013/proposal_001 frozen-atomref intact-readout outcome.
- optional zero-gate / source-fallback / readout-only ablation: If this overcorrects, compare to Proposal 002 gated vector_norm.

## implementation_notes_for_subagent
This is the narrow M01 patch. Do not add new losses, schedules, normalization, or atomref changes in this unit.
