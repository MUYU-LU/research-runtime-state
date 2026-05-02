# Proposal 010: Neighbor-density readout wildcard

- family: density_aware_readout
- phase: 4
- jump_type: wildcard
- budget_class: small
- expected_capability_gain: test whether a simple local-density summary at readout captures missing transfer information without altering the interaction core.

## one_sentence_hypothesis
Appending a bounded local neighbor-density summary to the final readout may improve cross-environment calibration, especially on iso17, while avoiding heavier angular or equivariant machinery.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json
- current_code_profile.json
- proposal_constraints.json
- evidence_quality.json
- mechanism_cards.json::HYP-B001
- mechanism_cards.json::HYP-B002

## historical_relation
- source_unit: generation_010/proposal_007
- relation_to_source: jump
- not_a_duplicate_of: proposal_003 because this adds a new density summary signal rather than only recalibrating existing scalar features.
- lesson_used: the source is stable enough that a bounded extra summary feature is a safer wildcard than a large architectural jump.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: should stay close to source if density summary is properly normalized.
- rmd17 force: near-neutral.
- rmd17 gap / Q: small upside only if local coordination statistics are missing.
- iso17 energy: plausible upside through better local-environment calibration.
- iso17 force: likely neutral.
- iso17 gap / Q: modest upside if coordination-count information helps transfer.
- training stability / runtime risk: low-medium.
- control comparison expectation: if this helps while deeper or helper variants do not, the missing signal is probably a simple local summary rather than more capacity.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::EvolutionMLIP.forward_energy`: compute a normalized per-atom neighbor-density summary from `i_idx` and append it to the readout input.
- `model/model.py::EvolutionMLIP.__init__`: widen or wrap the readout input layer to accept the extra density channel in a bounded way.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Compute a normalized local density feature from the existing neighbor list.
2. Add that feature to the readout input with a minimal parameter increase.
3. Keep all interaction blocks unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: small iso17 Q improvement from better local-environment calibration.
- expected tradeoff: the extra feature may be redundant and produce no measurable gain.
- failure signal that would falsify this proposal: flat metrics with no improvement over proposal_003, implying simple extra summaries are not the missing ingredient.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare against proposal_003 to isolate density summary versus generic late calibration.

## implementation_notes_for_subagent
Use only the already built neighbor list. Do not introduce triplets, long-range kernels, or dataset-specific branches.
