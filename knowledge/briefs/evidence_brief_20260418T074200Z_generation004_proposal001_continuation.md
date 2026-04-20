# MLIP Evidence Brief

## question
What bounded, benchmark-centric continuation should guide `generation_005` from source unit `generation_004/proposal_001`, in balanced evidence mode, given completed local metrics, train-history trends, runtime/reliability context, prior local evidence, and implementation-fit constraints?

## mode
balanced

## local_context
- Continuation target selected by `research_runtime/ledger/generation_005_continuation_decision.json`:
  - source: `generation_004/proposal_001`
  - `Q_rmd17 = 3.0291`
  - `Q_iso17 = 3.3267`
  - `Q_total = 3.1333`
- Selection rule: highest terminal-success `Q_total` for `generation_004`.
- Parent lineage:
  - `generation_003/proposal_004` was the chosen continuation source for `generation_004`.
  - `generation_004/proposal_001` was written as a bounded exploit of that winner-family, explicitly targeting cross-dataset rebalance rather than a new architecture jump.
- Proposal intent from `research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md`:
  - keep the NequIP-style local equivariant family
  - preserve energy-first force prediction, atomref, and local cutoff interactions
  - tighten residual and normalization calibration
  - improve rMD17 balance without sacrificing cross-dataset upside
- Write boundary for this evidence run:
  - evidence only
  - no runnable-unit edits
  - no round advancement actions
  - no selection file writes
  - no run launches

## current_unit_profile
- Model family: bounded local equivariant MLIP, NequIP-style in spirit but implemented as a compact custom PyTorch unit.
- Phase: exploit continuation of the existing winning family, not a fresh framework jump.
- Known capabilities present in `generation_004/proposal_001/model/model.py`:
  - atom embedding plus atomref baseline
  - cutoff-local neighbor graph from positions
  - scalar and vector hidden states
  - two repeated `BalancedInteractionBlock`s (`num_interactions=2`)
  - cosine cutoff envelope and Gaussian RBF edge basis
  - invariant-plus-directional mixing inside each interaction block
  - energy-first scalar readout, forces from autograd
- Known capabilities missing:
  - no explicit triplet/body-order contraction
  - no irreps/e3nn tensor-product machinery
  - no sparse neighbor builder, still dense all-pairs masking before cutoff
  - no long-range electrostatics or charge decomposition
  - no periodic cell handling
- Likely bottlenecks:
  - vector information still reaches the energy head mostly through vector norms and internal gated mixing, not richer equivariant products
  - locality is expressive enough to win, but body-order and angular compositional capacity remain bounded
  - dense neighbor construction is an engineering liability, though not the main benchmark bottleneck
- Likely implementation surface for bounded next moves:
  - `model/model.py` for interaction/readout changes
  - `model/train.py` for loss-weight or schedule calibration only
  - config assumptions already support bounded hyperparameter retuning without contract changes

## benchmark_dossier
### Source-unit benchmark summary
| dataset | split metrics | mixed force | mixed energy | gap penalty | Q_dataset |
|---|---|---:|---:|---:|---:|
| rMD17 | mild OOD F/E `0.10458 / 0.59297`, hard OOD F/E `0.10503 / 0.59259` | 0.10485 | 0.59274 | 0.00429 | 3.02911 |
| ISO17 | within F/E `0.18116 / 0.75503`, other F/E `0.19033 / 0.79636` | 0.18666 | 0.77982 | 0.04911 | 3.32669 |

### Cross-dataset frontier context
- `Q_total = 3.13326`, best completed non-control continuation in `generation_004`.
- `Q_iso17 > Q_rmd17`, but the source is still balanced because both datasets are strong and gap penalties are small to moderate.
- Relative to the parent `generation_003/proposal_004`:
  - rMD17 improved from mixed F/E `0.10656 / 2.28476` to `0.10485 / 0.59274`
  - ISO17 improved from mixed F/E `0.16930 / 1.58926` to `0.18666 / 0.77982`
  - parent `Q_total = 2.86876`, source `Q_total = 3.13326`
  - gain is therefore benchmark-complete, not force-only

### Control comparison if available
- Nearest explicit control evidence in lineage is `generation_003/proposal_008` (control replicate for the prior round), not a same-round `generation_004` control for this exact source.
- Compared with `generation_003/proposal_008`:
  - control rMD17 mixed F/E `0.17831 / 21.79929`, `Q_rmd17 = 1.72971`
  - control ISO17 mixed F/E `0.22231 / 53.08575`, `Q_iso17 = 2.14150`
- Interpretation: the current source unit is well beyond earlier control-level variance, so its frontier status is not plausibly explained by control noise alone.
- Limitation: no dedicated `generation_004` control replicate is attached to `proposal_001`, so same-generation variance attribution remains incomplete.

### Training dynamics
#### rMD17 trend
- Validation force improves monotonically from `0.2955` at epoch 1 to `0.1046` at epoch 8.
- Validation energy improves from `86.41` to `0.5930`, with a temporary spike at epoch 4 (`28.00`) before recovering strongly.
- Best validation checkpoint is effectively the final epoch on both force and energy.
- No obvious late-epoch instability, divergence, or overfitting signature.

#### ISO17 trend
- Validation force improves from `0.1975` at epoch 1 to `0.1599` at epoch 8.
- Validation energy is noisier early, including a spike at epoch 4 (`69.97`), then improves sharply to `1.04` by epoch 8.
- Final benchmarked mixed energy (`0.7798`) and force (`0.1867`) are both strong despite mid-training volatility.
- Trend suggests the rebalance exploit improved end-state calibration but did not fully remove early optimization turbulence.

### Runtime / reliability
- `run_state = terminal_success`
- `launch_count = 1`, `retry_count = 0`
- `repair_attempts = 0`, `same_failure_class_repairs = 0`
- `implementation_state = launch_ready`
- `remote_smoke_passed = true`, `remote_synced = true`
- Runtime window: roughly 2h58m from launch to finish
- No recorded failure class at finish
- Reliability therefore supports this source as a true frontier candidate rather than a fragile one-off rescue

## mathematical_evidence
- Current interaction block implements a bounded equivariant local update of the form:
  - edge basis from radial basis expansion and cosine cutoff
  - scalar edge gates, invariant directional gates, vector gates, and directional unit-vector injection
  - aggregated scalar/vector messages normalized by neighbor count
  - residual scalar update with layer norm and residual gating
  - residual vector update from gated self-vector and aggregated-vector mixing
- Important algorithmic ingredients seen directly in code:
  - directional invariant term: `sum(src_vector * unit)`
  - vector message: transformed source vector plus learned directional component along `unit`
  - scalar readout from `[scalar_state, vector_norm]`
- Invariance/equivariance judgment:
  - energy is built from scalar readout over scalar state plus norms of vector channels, preserving rotation-invariant energy prediction
  - forces are exact energy gradients, preserving force-from-energy consistency
  - representation is equivariant in spirit through directional vector updates, though not expressed in full irreps formalism
- Why this matters now:
  - current local evidence shows the mathematical form is already sufficient for frontier gains
  - missing next-tier expressivity is not basic equivariance, but richer body-order or scalar-vector coupling beyond norm-only readout
- Relevant external mathematical background from prior verified brief:
  - NequIP-style methods use spherical-harmonic edge attributes and equivariant tensor interactions to preserve geometric structure
  - MACE-style methods add higher-order equivariant products to increase body-order expressivity without needing many layers

## physical_evidence
- Locality assumption fits both benchmarks, which are short-range molecular force tasks.
- Current unit keeps a strict energy-first path, so physical consistency of forces is preserved.
- Small gap penalties on rMD17 (`0.0043`) and moderate but still controlled penalties on ISO17 (`0.0491`) suggest robust split transfer rather than brittle memorization.
- The large energy improvements versus the parent imply better calibration of the local potential surface, not merely sharper force fitting.
- No evidence here that a long-range branch is the urgent next need for this benchmark pair.
- Physically safer next moves are therefore those that preserve the energy-first local geometry pipeline while improving angular/body-order resolution.

## chemical_evidence
- Benchmark regime is molecular, not materials-focused.
- rMD17 and ISO17 both require sensitivity to local angular environment and chemically distinct local configurations.
- Strong improvements in both energy and force imply the present family is learning chemically meaningful local structure rather than only fitting force magnitudes.
- Atomref sensitivity remains relevant because composition baselines matter in molecular datasets; the current unit already preserves an atomref embedding.
- Chemistry-fit implication:
  - bounded local angular/body-order enrichment is plausible
  - aggressive long-range or periodic-design jumps are less directly justified by the current benchmark evidence

## textual_evidence
- Local proposal text for `generation_004/proposal_001` states the design goal clearly: rebalance the winning family rather than add another speculative branch.
- Prior local evidence brief (`evidence_brief_20260417T032900Z_proposal004_continuation.md`) recommended two main paths after the original winner-family jump:
  1. deeper minimal equivariant local exploit
  2. bounded body-order augmentation inside the same family
- Current completed results validate the exploit half strongly: two-stage rebalanced equivariant locality produced the best `generation_004` frontier score.
- Prior round-review brief (`evidence_brief_20260417T103400Z_generation002_round_review.md`) also warned against force-only ranking and highlighted that bounded higher-capacity jumps can help, but only when benchmark balance survives.
- External paper claims carried forward from the prior verified brief:
  - **NequIP**: equivariant convolutions provide more faithful geometric representations and strong data efficiency for interatomic potentials
  - **MACE**: higher-order equivariant message passing increases expressivity and can improve force-field accuracy with limited depth
- Textual conclusion:
  - the current source validates continued local equivariant exploitation
  - the open question is how to add capacity without losing the benchmark balance that this exploit achieved

## code_evidence
### Local code evidence
- `generation_004/proposal_001/model/model.py`
  - `BalancedInteractionBlock` introduces calibrated scalar and vector residual gating
  - `num_interactions=2` confirms this unit is the bounded depth exploit predicted by prior evidence
  - vector alignment and aggregated vector norms are explicitly mixed into scalar updates, improving coupling over the older parent
  - readout still reduces vector content to norms at the end, so final energy expressivity remains partially constrained
- `generation_004/proposal_001/model/train.py`
  - AdamW with cosine annealing
  - explicit warmup of energy weight and mild force-weight tapering across early epochs
  - grad clip `3.0`
  - no exotic optimizer or loss tricks, which strengthens the interpretation that gains came from architecture-plus-calibration fit
- Parent comparison:
  - `generation_003/proposal_004` already had strong equivariant-local geometry, but final rMD17 energy remained much worse than the current exploit
  - current source improved both depth and calibration without changing benchmark I/O

### Repository evidence carried forward from prior brief
- **NequIP** repo (`mir-group/nequip`)
  - README positions the method as E(3)-equivariant interatomic potentials
  - `nequip/model/nequip_models.py` and `nequip/nn/interaction_block.py` exemplify structured equivariant interaction composition
  - implementation fit: moderate, but a full adoption would be heavier than the current bounded codebase
- **MACE** repo (`ACEsuit/mace`)
  - README and module structure show explicit higher-order equivariant product blocks
  - implementation fit: medium-high friction in this codebase because irreps bookkeeping and specialized products would be a larger rewrite

### Fit judgment
- Drop-in to moderate-change next moves:
  - deepen or refine current interaction/readout coupling
  - add bounded triplet/body-order summaries without full irreps infrastructure
- Rewrite-heavy next moves:
  - full NequIP/MACE-style framework transplant

## relevant_papers
1. **SE(3)-Equivariant Graph Neural Networks for Data-Efficient and Accurate Interatomic Potentials** (NequIP, `arXiv:2101.03164`)
   - Relevance: validates continuing the local equivariant family and clarifies the value of disciplined geometric interactions.
2. **Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields** (MACE, `arXiv:2206.07697`)
   - Relevance: supports bounded higher-body augmentation as the most principled next-capacity jump beyond the current two-stage exploit.

## local_literature
- Local literature guidance read from `mlip-evidence/references/local_mlip_literature.md`.
- No new local PDF extraction was required in this evidence run because:
  - decisive ranking evidence is local benchmark output and train history
  - the most relevant external paper/repo evidence had already been grounded in the prior local evidence brief
- Therefore, this run uses prior locally grounded literature context plus current benchmark artifacts, rather than claiming fresh local PDF verification.

## relevant_repos
1. **NequIP** (`mir-group/nequip`)
   - Why relevant: reference pattern for disciplined local equivariant interactions and energy-to-force contract.
2. **MACE** (`ACEsuit/mace`)
   - Why relevant: reference pattern for bounded higher-order/body-order expressivity.

## capability_gap
### Current code capabilities
- strong local equivariant geometry
- two-stage interaction depth
- stable benchmark-complete performance on both datasets
- calibrated energy/force schedule that finishes cleanly

### Required capabilities for the next tier
- richer body-order or angular composition than current norm-heavy terminal readout
- stronger scalar-vector coupling in the energy head
- ideally more expressive local context without sacrificing current optimization stability

### Missing pieces
- explicit triplet or product-basis mechanism
- final readout that uses more than vector norms
- same-generation control replicate for this exact source family

### Integration risk
- low: further bounded exploit inside current two-stage family
- medium: add compact triplet/body-order summaries to the existing family
- medium-high: transplant full irreps-heavy NequIP/MACE-style blocks
- low scientific priority right now: long-range or periodic machinery for these benchmarks

## implementable_design_moves
1. **Exploit move: richer scalar-vector energy coupling inside the existing two-stage family**
   - principle: keep the winning family and improve how directional information reaches atomwise energies
   - mathematical form: replace or augment norm-only terminal vector features with bounded invariant couplings such as vector alignment summaries or low-rank scalar-vector contractions
   - physical rationale: preserve rotation-invariant energy while retaining more directional information
   - chemistry relevance: should help distinguish local angular environments that norm-only summaries blur
   - code pattern: edit the readout input and final invariant mixing in `model/model.py`
   - implementation friction: low to medium
   - expected effect: modest but plausible gain in both energy calibration and force sharpness, especially on ISO17
   - one bounded control/ablation: same model with current norm-only readout retained

2. **Balanced jump: bounded body-order augmentation within the current family**
   - principle: add limited triplet-aware or pair-product local summaries without leaving the existing energy-first architecture
   - mathematical form: center-wise summary over neighbor-pair interactions or low-rank product features injected into scalar updates
   - physical rationale: capture angular/body-order correlations that two-body local mixing cannot fully resolve
   - chemistry relevance: molecular conformations often depend on correlated neighbor geometry, not only pairwise distances
   - code pattern: add a local helper around neighbor features in `model/model.py`, keep training contract intact
   - implementation friction: medium
   - expected effect: higher ceiling than pure exploit if the added body-order path stays numerically tame
   - one bounded control/ablation: identical two-stage backbone with body-order path toggled off

3. **Conservative exploit: schedule-only calibration refinement**
   - principle: preserve architecture and test whether remaining gap is mainly optimization calibration
   - mathematical form: unchanged model, modest energy/force warmup retuning and possibly residual-scale initialization refinement
   - physical rationale: current training histories still show early volatility, especially on ISO17
   - chemistry relevance: mainly indirect, via better calibration of the same learned local chemistry
   - code pattern: small `train.py` and config edits only
   - implementation friction: low
   - expected effect: low-risk polishing, lower upside than architectural changes
   - one bounded control/ablation: direct replicate against the current source schedule

## exploit_angles
- Best exploit angle: improve scalar-vector coupling in the energy head while preserving the two-stage balanced interaction stack.
- Second exploit angle: mild schedule refinement to reduce early ISO17 volatility, but only as a polishing branch, not the main science move.
- Recommendation within exploit space: prefer representational coupling improvement over pure optimizer tuning, because the current source already trains cleanly to a strong frontier score.

## jump_angles
- Best bounded jump angle: add a compact body-order augmentation inside the current family, not a fresh full-framework rewrite.
- Secondary jump angle: a more NequIP-like disciplined interaction refinement, but only if kept narrow and not combined with triplet complexity in the same unit.
- Deprioritized jump: full irreps-heavy MACE/NequIP transplant or long-range branch introduction, because implementation friction is too high relative to current benchmark evidence.

## risks_or_mismatches
- Data/task mismatch risk: low for bounded local angular/body-order moves, higher for long-range or materials-oriented changes.
- Method mismatch risk: a heavier equivariant rewrite may destroy the calibration improvements that made `proposal_001` win.
- Codebase mismatch risk: full irreps machinery is substantially heavier than the current compact custom implementation.
- Dependency/runtime mismatch risk: adding e3nn-like infrastructure would raise runtime and integration complexity without direct benchmark necessity here.
- Likely-failure signs already visible in history:
  - ISO17 training had early energy spikes, so added capacity could easily reintroduce instability if not tightly bounded
  - prior lineage already showed that over-aggressive jumps can help one dimension while damaging balance
- Evidence limitation: lack of a same-generation control replicate for this exact source means small future gains should still be interpreted cautiously.

## implementation_fit
- Highest-fit continuation class: bounded modifications inside `generation_004/proposal_001`'s current two-stage family.
- Best fit among candidate move types:
  1. exploit with richer invariant scalar-vector coupling
  2. balanced bounded body-order augmentation
  3. schedule-only calibration polish
- Poor fit for next bounded step:
  - full framework transplant
  - multi-branch hybrid jump with triplets plus long-range plus new dependencies
- Overall fit judgment: continue from `generation_004/proposal_001` with a benchmark-preserving bounded enhancement, not a rewrite.

## strong_evidence
- `generation_004/proposal_001` is the selected frontier source because it has the highest completed `Q_total` in the round.
- It improved materially over parent `generation_003/proposal_004` on both datasets, especially energy.
- Runtime/reliability context is clean: one launch, zero retries, zero repairs, smoke passed, terminal success.
- Earlier control evidence from the lineage is far below this source, so the source is not plausibly explained by ordinary replicate variance alone.

## weak_but_relevant
- The parent `generation_003/proposal_004` still had slightly better ISO17 force than the current source, suggesting some tradeoff between force sharpness and energy calibration remains possible.
- Prior literature/repo evidence suggests higher-order/body-order enrichment is promising, but this specific codebase has not yet validated a clean version on the current source family.
- Schedule-only improvements may still matter, because both datasets showed early energy turbulence before converging.

## background_context
- Earlier evidence established the local equivariant family as the main winning direction.
- `generation_004/proposal_001` then validated that balanced exploitation of that family can outperform more adventurous alternatives in benchmark-complete terms.
- The `generation_005` decision should therefore preserve the same benchmark-centric discipline: no force-only ranking, no overreaction to one split, and no unnecessary framework jump.

## key_findings
- The current source is a genuine balanced frontier, not just a force improvement.
- The biggest validated gain from parent to source came from energy calibration improvement while retaining strong forces.
- The next step should stay in-family.
- Best balanced recommendation: a bounded body-order or richer scalar-vector coupling enhancement, with preference for the lighter coupling-first exploit if implementation budget is tight.

## useful_patterns
- Two-stage local equivariant depth works.
- Residual-gated calibration and warmup scheduling improved end-state benchmark balance.
- Energy improvement was as important as force improvement for frontier advancement.
- Same-family bounded changes have been more productive here than large speculative jumps.

## followup_queries
- Can a richer invariant scalar-vector readout improve ISO17 force without giving back the current energy gains?
- Can a compact triplet/body-order summary be added without reviving the instability seen in earlier more aggressive jumps?
- Would a same-family control replicate of `generation_004/proposal_001` materially change confidence in small future gains?
- Is dense all-pairs neighbor construction beginning to limit practical scaling or stability enough to justify a pipeline cleanup branch later?

## confidence
**medium-high**

Reasoning: confidence is high that `generation_005` should continue inside the `generation_004/proposal_001` family and remain benchmark-centric. Confidence is slightly lower on the exact next mechanism, because both richer scalar-vector coupling and bounded body-order augmentation are plausible, and there is no same-generation control replicate for this exact source. Balanced recommendation therefore favors a narrow coupling-first exploit, with one bounded body-order jump as the main higher-upside alternative.
