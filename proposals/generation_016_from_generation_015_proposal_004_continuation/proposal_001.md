# Proposal 001: Compact Cartesian body-order residual branch

- family: cartesian_body_order_residual
- phase: 3
- jump_type: jump
- budget_class: medium
- expected_capability_gain: Add explicit angular/body-order invariants to improve ISO17 energy/gap while residual scaling protects the current RMD17 force strength.

## one_sentence_hypothesis
A small invariant B-basis residual energy branch beside the source local message path will supply missing three-body geometry needed by ISO17 conformer energies without changing benchmark semantics or the force-from-energy contract.

## mechanism_refs
- GEN016-M01-cace-shadow-body-order-representation

## evidence_refs
- paper_artifact:paper_001
- repo_artifact:repo_001
- mechanism_cards.json::GEN016-M01-cace-shadow-body-order-representation
- patch_blueprints.json::GEN016-M01-cace-shadow-body-order-representation
- benchmark_diagnosis.json::generation_015/proposal_004 Q_total=3.9176951158891966, ISO17 energy trend worsening, ISO17 gap_penalty=0.09986681269946639
- current_code_profile.json::EvolutionMLIP.forward_energy source insertion points

## historical_relation
- source_unit: generation_015/proposal_004
- relation_to_source: jump
- not_a_duplicate_of: generation_015 local readout/gate/norm variants because this adds a separate polynomial invariant representation path rather than editing BalancedInteractionBlock, vector norms, or scalar gates.
- lesson_used: Source unit has strong RMD17 and improving ISO17 force trend but poor ISO17 validation-energy stability; prioritize energy/gap architecture changes with no-op residual initialization.

## why_not_duplicate
This is not another vector-norm readout or residual-gate adjustment. The edit introduces Cartesian angular monomials, scatter-summed A features, nu=1/2 invariant B features, and a separate per-atom residual energy head with a near-zero learnable scale.

## benchmark_rationale
- rmd17 energy: Should remain close to source because the residual scale starts near zero and atomref/source readout remain intact.
- rmd17 force: Moderate risk from polynomial features; bounded l_max=2 and LayerNorm should prevent large force regressions.
- rmd17 gap / Q: Expected neutral to slight positive if the residual learns smooth local geometry.
- iso17 energy: Primary target; explicit body-order features may reduce mixed_energy_mae and stabilize val energy.
- iso17 force: Could improve if angular gradients are smooth; reject if force trend regresses.
- iso17 gap / Q: Main expected gain is lower gap_penalty and higher Q_iso17.
- training stability / runtime risk: Medium shape/autograd risk; overhead acceptable with radial channels <=8 and no full representation rewrite.
- control comparison expectation: Must beat exact source control on ISO17 energy/gap without losing RMD17 Q beyond round tolerance.

## files_to_edit
- `model/model.py`
- `model/train.py`: none expected, unless a constant for branch width is needed in code-level defaults
- never `config.json` for MLIP-quality changes

## code_insertion_points
- `model/model.py::new CartesianBodyOrderBranch`: implement AngularMonomial(l_max=2), small element-pair embedding, A scatter, nu=1/2 invariant flattening, LayerNorm/MLP energy head.
- `model/model.py::EvolutionMLIP.__init__`: after RBF buffers and before/near `self.interactions`, add `self.body_order_branch`, `self.body_order_readout`, and `self.body_order_log_scale = nn.Parameter(torch.tensor(-4.0))`.
- `model/model.py::EvolutionMLIP.forward_energy`: after `rbf`, `unit`, and `cutoff_weight` are computed, call the branch; after source `per_atom_energy`, return `atomref + per_atom_energy.sum() + sigmoid(scale) * residual_per_atom.sum()`.
- `model/train.py::MODEL_* / TRAIN_* constants`: no semantic change; keep source defaults unless the implementation needs a local constant comment.

## minimal_edit_plan
1. Add a compact body-order branch that builds angular monomials `[1, x, y, z, xx, xy, xz, yy, yz, zz]`, multiplies by a small projected RBF/type basis, scatter-adds to receiver atoms, and constructs nu=1 plus squared/contracted nu=2 invariant features.
2. Add a LayerNorm + two-layer MLP residual per-atom energy head and a near-zero residual scale.
3. Integrate the residual with the existing scalar energy return only; do not modify neighbor list, dataloader, eval, metrics, or entrypoint.

## implementation_checklist
- [ ] Preserve `E = sum_i E_i` plus atomref and residual atomic sum; preserve force-from-energy contract.
- [ ] Preserve benchmark metric field names and runnable entrypoint contract.
- [ ] Modify only the allowed target unit files.
- [ ] Do not edit `config.json`; change MLIP knobs in `model/model.py` or `model/train.py` if needed.
- [ ] Keep tensor shapes compatible with current dataloader and model forward.
- [ ] Add no unbounded cubic neighbor/triplet loops; use scatter/products over compact feature tensors only.
- [ ] Initialize the new residual scale near no-op and verify `scale=0` is a source fallback.
- [ ] Call `mark_unit_implemented.py --unit <UNIT> --actor implementation_subagent` after edits.

## expected_benchmark_effect
- primary expected gain: ISO17 mixed_energy_mae and gap_penalty improve from explicit angular/body-order invariants.
- expected tradeoff: Moderate runtime and possible force-noise risk if B features are not normalized.
- failure signal that would falsify this proposal: ISO17 energy trend still worsens or RMD17 mixed_force_mae regresses beyond tolerance while residual scale grows.

## ablation_or_control
- required control or comparison: generation_015/proposal_004 exact source control.
- optional zero-gate / source-fallback / readout-only ablation: freeze `body_order_log_scale` to a very negative value to verify source-equivalent behavior.

## implementation_notes_for_subagent
Use only PyTorch operations already available in `model/model.py`. Keep radial channels and type channel counts small; this proposal should be a bounded parallel representation residual, not a full external package port.
