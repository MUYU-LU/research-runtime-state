# Proposal 005: PaiNN mixer with radial-resolution code defaults

- family: painn_radial_resolution_probe
- phase: 5
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Test whether vector-norm feedback needs slightly finer radial basis resolution to improve ISO17 energy/gap.

## one_sentence_hypothesis
Combining a bounded GEN020-M01 mixer with a small code-level increase in radial basis resolution should reveal whether the current TP vector features lack enough distance detail for ISO17 transfer.

## mechanism_refs
- GEN020-M01-painn-intra-layer-vector-norm-mixing

## evidence_refs
- patch_blueprints.json GEN020-M01 implementation-ready insertion points
- proposal_format.md capacity scaling guidance for bounded radial-resolution probes
- current_code_profile.json source `MODEL_NUM_RBF=32`, cutoff=5.0, H=96
- benchmark_diagnosis.json ISO17 mixed_energy_mae=0.252341, gap_penalty=0.144950

## historical_relation
- source_unit: generation_019/proposal_003
- relation_to_source: jump
- not_a_duplicate_of: Unlike proposals 001-004, this includes a bounded code-level radial basis capacity change and tests a capacity/mechanism interaction; unlike generation_019 proposal_006, it does not revisit rank-2 TP or broad branch changes.
- lesson_used: Generation_019's scale-only child was neutral, so a controlled capacity axis may be needed, but should be paired with source-recoverable M01 rather than a new unproven family.

## why_not_duplicate
This is not pure hyperparameter search: the radial change is a bounded companion to the evidence-backed mixer and targets whether the vector invariants fed into scalar channels carry enough distance resolution.

## benchmark_rationale
- capacity/scaling hypothesis, if any: Increase `MODEL_NUM_RBF` from 32 to 48 in code defaults only; keep hidden_dim=96, cutoff=5.0, and num_interactions unchanged.
- rmd17 energy: Finer radial features could improve or preserve mixed_energy_mae=0.031769 but may overfit; zero-start mixer provides fallback.
- rmd17 force: Watch mixed_force_mae=0.060948 carefully because radial detail affects force gradients.
- rmd17 gap / Q: Q_rmd17=4.166948 should not drop enough to erase any ISO17 gain.
- iso17 energy: Main target is mixed_energy_mae=0.252341 and other_energy_mae=0.279956; radial resolution may improve conformer transfer before norm/dot mixing.
- iso17 force: Expect neutral or small improvement; excessive radial sharpness may harm other_force_mae=0.158451.
- iso17 gap / Q: Success requires lower gap_penalty=0.144950 or higher Q_iso17=3.764325.
- training stability / runtime risk: Medium runtime risk due to larger RBF-dependent layers; still no new neighbor topology or cubic loops.
- control comparison expectation: Interpret against pure M01 proposals; if only this wins, bottleneck was radial detail plus mixing.

## files_to_edit
- `model/model.py`
- `model/train.py`
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::TPInvariantPaiNNMixing`: add bounded per-layer mixer as in GEN020-M01.
- `model/model.py::EvolutionMLIP.__init__`: ensure TP/mixer layers accept the code-level `num_rbf` default.
- `model/train.py::MODEL_NUM_RBF`: change from 32 to 48; do not edit `config.json`.
- `model/train.py`: leave objective weights unchanged.

## minimal_edit_plan
1. Implement source-recoverable per-layer M01 mixer with alpha caps <=0.05.
2. Change only the code default `MODEL_NUM_RBF` to 48 and propagate through existing constructor use.
3. Keep cutoff, hidden_dim, interactions, loss weights, data, and evaluator unchanged.
4. Verify shapes for RBF filters and TPInteractionBranch after the default change.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` and force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py`.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no new triplets, long-range heads, or direct force heads.
- [ ] Keep radial scaling bounded to a single default change.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 energy/gap improvement beyond pure M01 if distance-resolution bottleneck limits vector-norm feedback.
- expected tradeoff: More compute and possible RMD17 force overfitting; should be selected only if mechanism diversity/capacity probing is desired.
- failure signal that would falsify this proposal: Runtime/smoke issues, RMD17 force regression, or no gain over pure M01 variants.

## ablation_or_control
- required control or comparison: Compare to proposal_001 with num_rbf=32 and to source/control.
- optional zero-gate / source-fallback / readout-only ablation: With mixer zeroed, behavior should be a radial-resolution-only probe.

## implementation_notes_for_subagent
Change MLIP knobs in code only. Do not edit benchmark/runtime config. Keep the radial increase modest and avoid simultaneous hidden_dim/depth changes.
