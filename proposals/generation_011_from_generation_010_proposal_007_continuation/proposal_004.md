# Proposal 004: Conservative late helper jump

- family: late_invariant_helper_redux
- phase: 4
- jump_type: jump
- budget_class: small
- expected_capability_gain: test whether a much weaker late helper than prior attempts can recover cross-dataset energy calibration.

## one_sentence_hypothesis
A tightly gated late helper over scalar state and vector norm, initialized much closer to off than earlier helper proposals, may recover some missed higher-order summary without the large regressions seen in generation_010 jumps.

## mechanism_refs
- []

## evidence_refs
- benchmark_diagnosis.json
- current_code_profile.json
- proposal_constraints.json
- evidence_quality.json
- mechanism_cards.json::HYP-B002

## historical_relation
- source_unit: generation_010/proposal_007
- relation_to_source: jump
- not_a_duplicate_of: generation_010/proposal_004 because this reuses the late-helper idea only in a much smaller, more conservative form and now starts from the simplified source instead of generation_004/proposal_001.
- lesson_used: helper-style expansions can be diagnostically useful, but previous active versions were too strong and must be sharply downscaled.

## benchmark_rationale
Discuss expected effects on all relevant benchmark signals, not force-only:
- rmd17 energy: moderate downside risk if the helper perturbs a well-behaved source.
- rmd17 force: near-neutral to slight downside.
- rmd17 gap / Q: useful diagnostic for whether additional summary is worth any cost.
- iso17 energy: main upside target.
- iso17 force: slight upside possible if late geometry summary helps transfer.
- iso17 gap / Q: could improve if the source underfits difficult local environments.
- training stability / runtime risk: low-medium.
- control comparison expectation: should only be kept if it clearly beats control and the exploit family.

## files_to_edit
- `model/model.py`
- `model/train.py`: none

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add a narrow late helper projection, gate, and norm with very conservative initialization.
- `model/model.py::EvolutionMLIP.forward_energy`: compute helper features from `scalar_state`, `vector_norm`, and a simple interaction term before readout.
- `model/train.py::<none>`: none

## minimal_edit_plan
1. Add the smallest useful late helper branch at readout time.
2. Bias its gate strongly toward off and keep helper width narrow.
3. Preserve the source readout path as the dominant path.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: improved iso17 energy/Q if a tiny late summary was missing.
- expected tradeoff: repeat of helper-style regressions on rmd17.
- failure signal that would falsify this proposal: it underperforms the source and the readout-only exploit, showing helper presence is still too costly.

## ablation_or_control
- required control or comparison: proposal_008 exact source replicate.
- optional zero-gate / source-fallback / readout-only ablation: compare against proposal_009 to isolate helper activation versus helper presence.

## implementation_notes_for_subagent
Use smaller hidden width and a more negative gate bias than generation_010/proposal_004. This is a cautious retry, not a full reprise.
