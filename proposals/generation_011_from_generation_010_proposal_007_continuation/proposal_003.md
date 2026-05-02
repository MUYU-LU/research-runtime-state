# Proposal 003: Tiny readout residual calibrator

- family: balanced_readout_calibrator
- phase: 3
- jump_type: exploit
- budget_class: tiny
- expected_capability_gain: let the source keep its interaction behavior while adding a very small late scalar calibration path into readout.

## one_sentence_hypothesis
A tiny off-biased residual calibrator applied only at readout can improve energy calibration, especially on iso17, without perturbing the successful source interaction dynamics.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json
- current_code_profile.json
- proposal_constraints.json
- evidence_quality.json
- mechanism_cards.json::HYP-B001

## historical_relation
- source_unit: generation_010/proposal_007
- relation_to_source: exploit
- not_a_duplicate_of: generation_010/proposal_004 because that late helper was larger and materially regressed; this proposal only adds a minimal readout-side residual calibrator and keeps interaction blocks unchanged.
- lesson_used: late interventions should be much smaller than prior helper-style jumps because active helper branches were too disruptive.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: should remain near source, maybe slight upside.
- rmd17 force: near-neutral because forces still come from energy and the added head is tiny.
- rmd17 gap / Q: low-risk diagnostic.
- iso17 energy: main possible gain if calibration error is mostly late-stage.
- iso17 force: neutral to slight upside.
- iso17 gap / Q: modest upside if a tiny late correction improves transfer.
- training stability / runtime risk: low.
- control comparison expectation: if this helps while interaction edits do not, the bottleneck is likely in readout calibration.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add a narrow residual calibrator module and off-biased gate for the readout input.
- `model/model.py::EvolutionMLIP.forward_energy`: form a tiny corrected scalar readout state before `self.readout`.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Add one narrow readout calibrator MLP and a gate initialized near zero.
2. Apply it only to the scalar readout state after the interaction stack.
3. Feed the calibrated scalar state into the existing readout without changing the energy sum contract.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: cleaner energy calibration with minimal architectural disturbance.
- expected tradeoff: may do nothing if the limitation is earlier in message passing.
- failure signal that would falsify this proposal: iso17 and rmd17 both stay flat relative to control despite stable training.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: this proposal is itself the readout-only calibration ablation.

## implementation_notes_for_subagent
Keep the calibrator narrow and late. Do not add extra interaction blocks or large helper branches.
