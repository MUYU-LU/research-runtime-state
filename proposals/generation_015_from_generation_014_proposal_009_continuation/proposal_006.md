# Proposal 006: Energy-weighted fine balance for ISO17 calibration

- family: energy_force_balance_calibration
- phase: 1
- jump_type: jump
- budget_class: tiny
- expected_capability_gain: Diagnosis-driven test of whether the source's ISO17 energy/gap weakness is partly a training-objective balance issue rather than architecture alone.

## one_sentence_hypothesis
A modest code-level increase in the energy loss weight with a matching small force-weight reduction may improve ISO17 mixed_energy_mae/gap without changing the successful conservative model architecture.

## mechanism_refs
- []

## evidence_refs
- context.md::generation_014/proposal_009::ISO17_energy_trend=worsening::best_val_energy_mae=0.1471354167::last_val_energy_mae=0.9270833333
- context.md::generation_014/proposal_009::force_weight=20.0::energy_weight=1.0 in observed training rows
- mechanism_cards.json::GEN015-W01-conservative-smoothness-guardrail::weak_hypothesis_constraint_only
- proposal_constraints.json::weak_or_hypothesis_mechanisms=GEN015-W01-conservative-smoothness-guardrail

## historical_relation
- source_unit: generation_014/proposal_009
- relation_to_source: jump
- not_a_duplicate_of: generation_012/proposal_002 because this starts from the current best normalized vector-readout architecture and makes a small explicit code-level weight balance change only, not a broad training-objective redesign.
- why_not_duplicate: The source's current train history shows force-dominated weighting and worsening ISO17 validation energy; this exact source-plus-small-weight-rebalance has not been tested.
- lesson_used: Evidence package does not provide strong external mechanism support for training weights, so this is explicitly diagnosis-driven and should be selected only as a mechanism-diversity probe.

## benchmark_rationale
- rmd17 energy: May improve slightly from higher energy emphasis.
- rmd17 force: Risk of small force regression from lower force emphasis.
- rmd17 gap / Q: Could improve if energy calibration matters more than slight force loss; could regress if force dominates Q.
- iso17 energy: Primary target; late validation energy spike suggests energy calibration pressure may be insufficient.
- iso17 force: Likely slight regression; keep change modest to preserve force gains.
- iso17 gap / Q: Target lower mixed_energy_mae and gap_penalty; Q gain only if energy improvement outweighs force tradeoff.
- training stability / runtime risk: Very low implementation risk; scientific risk is repeating weak training-objective history.
- control comparison expectation: Should be judged against source control and not over-interpreted as evidence-backed architecture mechanism.

## files_to_edit
- `model/model.py` if needed, otherwise `none`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP`: none; preserve architecture exactly.
- `model/train.py::train`: change code-level fallback/default effective training weights to a modestly more energy-balanced setting, for example `energy_weight = 1.2` and `force_weight = 18.0` when not otherwise fixed by handoff conventions; keep warmup structure and scheduler unchanged.
- `model/train.py::run_epoch`: none; keep loss formula `energy_weight * loss_energy + force_weight * loss_force`.

## minimal_edit_plan
1. Do not edit model architecture.
2. In `train.py`, set small code-level defaults or constants so the run records a modest energy-weight increase and force-weight decrease.
3. Preserve atomref fitting, warmup, optimizer, scheduler, epochs, and output JSON schema.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Clearly note in implementation report that this is diagnosis-driven with no strong mechanism card.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: Better ISO17 mixed_energy_mae/gap through slightly stronger energy supervision.
- expected tradeoff: Force metrics can regress, especially RMD17 force.
- failure signal that would falsify this proposal: Force loss outweighs any energy improvement or ISO17 validation energy remains unstable.

## ablation_or_control
- required control or comparison: Exact source control and at least one M01 gated architecture proposal.
- optional zero-gate / source-fallback / readout-only ablation: If energy-weight rebalance helps, later combine only with the best readout gate; do not select as sole mechanism proof.

## implementation_notes_for_subagent
This proposal is intentionally diagnosis-driven because only the readout gate has strong external evidence. Keep the change tiny and code-local; do not alter benchmark config, splits, metrics, data, or entrypoint.
