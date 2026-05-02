# Proposal 007: Energy-reweighted body-order training exploit

- family: body_order_energy_reweight
- phase: 3
- jump_type: exploit
- budget_class: small
- expected_capability_gain: Give the compact body-order residual enough energy signal to address ISO17 energy/gap without changing evaluation semantics.

## one_sentence_hypothesis
Pairing a minimal body-order residual with a modest code-level energy/force weight shift will test whether the source's ISO17 energy instability is partly a training-target imbalance after adding better geometry features.

## mechanism_refs
- GEN016-M01-cace-shadow-body-order-representation

## evidence_refs
- paper_artifact:paper_001
- repo_artifact:repo_001
- mechanism_cards.json::GEN016-M01-cace-shadow-body-order-representation
- patch_blueprints.json::GEN016-M01-cace-shadow-body-order-representation
- benchmark_diagnosis.json::source training history shows ISO17 force improving while validation energy worsens
- current_code_profile.json::model/train.py code-level defaults TRAIN_ENERGY_WEIGHT=1.0, TRAIN_FORCE_WEIGHT=20.0

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: exploit
- not_a_duplicate_of: This is not a pure training-weight tweak; the training change is paired with a new evidence-backed body-order residual representation path.
- lesson_used: Source under current force-heavy weighting learns forces while ISO17 validation energy worsens, so a small energy-weight nudge is reasonable only with an architecture path that can use it.

## why_not_duplicate
Recent local variants changed gates/readout or code-level defaults; this proposal adds a minimal M01 representation branch and only then changes `TRAIN_ENERGY_WEIGHT`/`TRAIN_FORCE_WEIGHT` slightly inside code, preserving benchmark/eval semantics.

## benchmark_rationale
- rmd17 energy: May improve slightly from energy reweighting; monitor force tradeoff.
- rmd17 force: Risk from lower relative force weight; keep shift modest.
- rmd17 gap / Q: Expected neutral to slight positive if energy improves without force loss.
- iso17 energy: Primary target; body-order features plus energy emphasis should reduce val energy instability.
- iso17 force: Could regress slightly; reject if force loss overwhelms energy gains.
- iso17 gap / Q: Expected positive if mixed_energy_mae and gap_penalty improve.
- training stability / runtime risk: Small/medium; body-order residual adds overhead, train weight shift is low risk.
- control comparison expectation: Should beat source on ISO17 energy/gap with tolerable force tradeoff.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::new MinimalNu2Branch`: same minimal static B feature branch as proposal_003.
- `model/model.py::EvolutionMLIP.__init__/forward_energy`: add B residual head and tiny scale to source energy.
- `model/train.py::TRAIN_ENERGY_WEIGHT / TRAIN_FORCE_WEIGHT`: change code-level defaults modestly, e.g. energy 1.2-1.4 and force 18-19, while preserving warmup and metric semantics.
- `model/train.py::run_epoch`: no new loss terms or metric names.

## minimal_edit_plan
1. Add the minimal static body-order residual branch with near-zero scale.
2. Adjust code-level training constants only in `model/train.py` to modestly emphasize energy while retaining force-dominant training.
3. Leave dataloaders, splits, eval, output metric names, and runnable entrypoint unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops.
- [ ] Keep training-weight shift modest enough that RMD17/ISO17 force MAE remains competitive.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap improvement under a bounded feature-plus-training exploit.
- expected tradeoff: Force MAE may worsen if energy reweighting is too strong.
- failure signal that would falsify this proposal: Energy improves only by sacrificing enough force to lower Q_total, or the body-order residual remains unused.

## ablation_or_control
- required control or comparison: source control and proposal_003 if available.
- optional zero-gate / source-fallback / readout-only ablation: same training weights with body-order residual scale frozen to zero.

## implementation_notes_for_subagent
Keep the training change small and code-local. This proposal changes training-target weighting but not benchmark formulas, split semantics, eval metrics, or entrypoint.
