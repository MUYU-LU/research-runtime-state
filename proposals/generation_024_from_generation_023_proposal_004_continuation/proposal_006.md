# Proposal 006: Dual-scale SOG branch with energy-stabilized loss weights

- family: sog_tail_energy_stabilized_objective
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Couple a tiny SOG tail with a bounded energy-weight increase to target ISO17 energy/gap while monitoring force tradeoff.

## one_sentence_hypothesis
A source-near SOG long-range branch may need slightly stronger energy supervision to improve ISO17 transfer energy/gap, so a bounded energy-weight adjustment can test whether objective balance is limiting the new mechanism.

## mechanism_refs
- GEN024-M01-adaptive-sog-realspace-latent-tail

## evidence_refs
- evidence_brief_20260501T222449Z.md
- mechanism_cards.json: SOG branch should be a tiny additive scalar energy preserving force autograd
- patch_blueprints.json: model/train.py has no required semantic change for SOG, so any objective edit must be bounded and explicitly diagnostic
- benchmark_diagnosis.json: ISO17 validation energy at last epoch is unstable/high while best_val_energy_mae is much lower; source force trend still improves
- current code profile: `model/train.py` code-level defaults `TRAIN_ENERGY_WEIGHT=1.0`, `TRAIN_FORCE_WEIGHT=20.0`
- proposal_format.md: training-objective evolution is valid when preserving metric/split semantics and changing code-level defaults only.

## historical_relation
- source_unit: generation_023/proposal_004
- relation_to_source: jump
- not_a_duplicate_of: Not a duplicate of pure SOG proposals because it tests interaction between a small SOG branch and loss balance; not a duplicate of pure training proposals because it includes the evidence-backed SOG mechanism.
- lesson_used: source already optimizes forces well, but ISO17 energy/gap remains weaker; a modest energy weighting may help the scalar long-range tail learn useful amplitudes.

## why_not_duplicate
This proposal is the only one that couples the SOG mechanism to an objective change. It should not also change capacity or trainable widths, so selection can attribute differences to energy-supervised SOG learning rather than a broader architecture search.

## benchmark_rationale
- capacity/scaling hypothesis, if any: none; objective balance plus small mechanism branch.
- rmd17 energy: expected slight improvement from energy_weight 1.25-1.5, though force may trade off.
- rmd17 force: risk of small degradation if force_weight is reduced; prefer keep force_weight=20 and raise energy_weight to 1.25, or at most force_weight=18.
- rmd17 gap / Q: should remain stable; source RMD17 gap is already low at 0.009423666275278415.
- iso17 energy: primary target because source mixed_energy_mae=0.2679998259591584 and last-epoch val energy instability suggests energy supervision may matter.
- iso17 force: expected neutral or mild degradation; reject if force worsens more than energy gains.
- iso17 gap / Q: target lower gap_penalty and improved Q_iso17 through a better learned scalar tail.
- training stability / runtime risk: medium; objective change can alter convergence but no launch protocol or epoch semantics change.
- control comparison expectation: compare to proposal_002 additive SOG without objective change to isolate the loss-balance effect.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::EvolutionMLIP.__init__`: add a conservative additive fixed-width SOG residual as in proposal_002, with total cap <=0.001.
- `model/model.py::EvolutionMLIP.forward_energy`: compute SOG residual from existing neutral charge and all-pair distances; add scalar energy beside `les_tail_energy`.
- `model/train.py::MLIP code-level defaults`: change `TRAIN_ENERGY_WEIGHT` from `1.0` to a bounded value such as `1.25` or `1.5`; keep `TRAIN_FORCE_WEIGHT` at `20.0` unless implementation notes justify `18.0`.
- `model/train.py::run_epoch`: no semantic change to metric collection or evaluation.

## minimal_edit_plan
1. Add the smallest additive fixed-width SOG residual branch to `model/model.py` without removing current LES code.
2. Adjust only code-level training defaults for energy/force balance; do not touch dataset, metrics, or config.
3. Add comments marking the objective change as diagnostic for ISO17 energy/gap and keep all benchmark outputs unchanged.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops unless explicitly justified by budget.
- [ ] Do not change split semantics, dataloader sampling, evaluation formulas, or launch protocol.
- [ ] Keep the objective change bounded and documented in code comments.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: better ISO17 mixed_energy_mae/gap by letting the scalar SOG branch learn under stronger energy signal.
- expected tradeoff: possible force MAE degradation, especially RMD17 force.
- failure signal that would falsify this proposal: force regressions outweigh energy/gap gains, or pure additive SOG matches it without objective adjustment.

## ablation_or_control
- required control or comparison: compare with proposal_002 additive SOG and proposal_010 pure objective change.
- optional zero-gate / source-fallback / readout-only ablation: set SOG gate to zero while keeping objective change to isolate training effect.

## implementation_notes_for_subagent
Do not treat this as permission to redesign training. Only code-level constants may change, and benchmark evaluation semantics must remain untouched. The SOG branch should be the conservative additive residual, not a signed/trainable-width jump.
