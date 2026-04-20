# MLIP Evidence Brief

## question
What single bounded, benchmark-centric continuation brief should guide continuation from `generation_004/proposal_001` into target `generation_008` under balanced mode, after the full completed `generation_007` round again failed to beat the source?

## local_context
- Request scope: one evidence-only brief for continuation from `generation_004/proposal_001` into `generation_008`, balanced mode.
- Current continuation decision: `research_runtime/ledger/generation_008_continuation_decision.json` again selects `generation_004/proposal_001` with `Q_rmd17 = 3.0291`, `Q_iso17 = 3.3267`, `Q_total = 3.1333`.
- Selection rule in the ledger: highest `terminal_success Q_total` among the completed generation and parent source.
- All completed `generation_007` children underperformed the source. Best child was `generation_007/proposal_004` at `Q_total = 2.7457`, still well below the parent.
- This brief is evidence-only. It does not edit runnable units, materialize units, write `selection.json`, or launch runs.

## current_unit_profile
- Model family: compact custom local equivariant MLIP with scalar and vector channels.
- Phase: exploit-family continuation from a validated local source, not a framework jump.
- Proven capabilities in `research_runtime/generations/generation_004/proposal_001/model/model.py`:
  - atom embedding plus atomref baseline
  - local cutoff graph from Cartesian positions
  - Gaussian RBF basis plus cosine cutoff envelope
  - two `BalancedInteractionBlock`s
  - in-block scalar/vector coupling through `directional_invariant`, `agg_norm`, and `vector_alignment`
  - energy-first prediction with autograd forces
- Missing capabilities:
  - no explicit triplet or product-basis body-order path
  - no irreps / tensor-product machinery
  - no sparse neighbor builder
  - no nonlocal or electronic-state branch
- Likely bottlenecks:
  - late directional information is still compressed aggressively at the final energy map
  - the source appears calibration-sensitive, especially for rMD17 energy quality
  - the source already sits near a strong local optimum, so many plausible capacity additions regress rather than help
- Likely implementation surface:
  - `model/model.py` for any bounded representational or calibration-preserving edit
  - `model/train.py` only for tightly justified calibration controls

## benchmark_dossier
### Source unit: `generation_004/proposal_001`
- Runtime state: `terminal_success`
- Reliability: `launch_count = 1`, `retry_count = 0`, `repair_attempts = 0`, `remote_smoke_passed = true`, `remote_synced = true`
- rMD17:
  - `mixed_force_mae = 0.10485`
  - `mixed_energy_mae = 0.59274`
  - `gap_penalty = 0.00429`
  - `Q_dataset = 3.02911`
- ISO17:
  - `mixed_force_mae = 0.18666`
  - `mixed_energy_mae = 0.77982`
  - `gap_penalty = 0.04911`
  - `Q_dataset = 3.32669`
- Cross-dataset:
  - `Q_total = 3.13326`
  - `G_delta = 0.26450`
- Training dynamics:
  - both datasets recovered from mid-training energy spikes and finished with improving trends
  - the source is therefore strong but sensitive to calibration drift

### Generation_007 evidence relevant to target generation_008
- `generation_007/proposal_004` (narrow ACE-like invariant summary jump): `Q_total = 2.74573`
  - strongest child, but still clearly below source
  - rMD17 improved relative to some children but ISO17 energy regressed badly (`mixed_energy_mae = 2.85709`)
- `generation_007/proposal_006` (late invariant summary before readout): `Q_total = 2.67363`
  - mixed underperformance, especially vs source on both datasets
- `generation_007/proposal_001` (in-block invariant recombination exploit): `Q_total = 2.66520`
  - ISO17 stayed relatively stronger than rMD17, but rMD17 regressed heavily
- `generation_007/proposal_008` (source-matched control replicate): `Q_total = 2.31666`
  - weak replicate, so variance exists, but it does not erase the parent’s clear frontier status
- Continuation-level conclusion: the source has now survived repeated child rounds. This is strong negative evidence against medium-sized representational jumps that disturb calibration.

## mathematical_evidence
1. **Local source code**
   - `BalancedInteractionBlock` already mixes scalar and vector information through invariant summaries.
   - The final energy head still consumes `torch.cat([scalar_state, vector_norm], dim=-1)`, so late directional information is compressed.
   - However, `generation_007` outcomes show that simply targeting this bottleneck is not enough if the intervention perturbs the parent’s calibrated balance.
2. **Local paper: A Euclidean transformer for fast and stable machine learned force fields**
   - Verified locally from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`.
   - Concrete mechanism: separate invariant and equivariant information and recombine through invariant projections without expensive tensor products.
   - Relevance here: this supports bounded stream-aware edits, but the `generation_007` results show that medium-strength stream/readout interventions still failed to beat the parent.
3. **Local paper: Atomic Cluster Expansion: Completeness, Efficiency and Stability**
   - Verified locally from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`.
   - Concrete mechanism: complete invariant polynomial bases with recursive evaluation and explicit stability considerations.
   - Relevance here: compact many-body summaries are principled, but basis richness and numerical stability matter. The `generation_007/proposal_004` outcome is direct local evidence that even a narrow ACE-like helper can still degrade balanced benchmark performance.
4. **Local repo: `research_runtime/knowledge/repo_cache/ACEsuit__mace`**
   - `mace/modules/symmetric_contraction.py` implements MACE Eq. 10/11 style symmetric contraction machinery.
   - `mace/modules/models.py` shows tight coupling among irreps, product-basis blocks, spherical harmonics, and specialized readouts.
   - Relevance here: true higher-order product-basis behavior is rewrite-heavy in this codebase, so only tiny invariant-summary ideas are bounded fits, and even those now carry negative round evidence.

## physical_evidence
1. **Forces are not Enough**
   - Verified locally from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`.
   - Concrete claim: force/energy test error alone does not align with simulation usefulness, and stability is a key metric.
   - Implication here: balanced continuation must keep energy quality, gap behavior, and training recovery visible. The failed `generation_007` children reinforce that rule.
2. The source preserves force-from-energy consistency and strict locality, and that regime is already validated on rMD17 plus ISO17.
3. Nothing in the current benchmark dossier says the next missing ingredient is nonlocal physics. The main problem is preserving the source’s calibration while seeking modest incremental gain.

## chemical_evidence
- The active benchmark pair is molecular and local-angular, not an obvious charge-transfer or long-range-electronic stress test.
- ACE-style local many-body enrichment is chemically closer to the likely missing signal than nonlocal/electronic branches.
- But the local round result for the ACE-like jump was still negative overall, so chemistry plausibility does not override benchmark evidence.
- The chemistry verdict is therefore conservative: stay local and symmetry-aware, but only with edits small enough to preserve the already-proven calibration regime.

## textual_evidence
- `generation_008_continuation_decision.json` explicitly keeps `generation_004/proposal_001` over every completed `generation_007` child.
- The best `generation_007` child was still a clear loser to the parent, which means the evidence threshold for further architectural novelty is now much higher.
- Prior briefs suggested readout enrichment, in-block refinement, or narrow ACE-like summaries as bounded candidates. The completed `generation_007` round weakens all three as primary next-step justifications unless they are made even smaller and more fallback-friendly.
- The strongest new information in this run is not a new mechanism from literature, but local falsification: several evidence-plausible bounded jumps did not surpass the parent.

## code_evidence
### Local source code
- `research_runtime/generations/generation_004/proposal_001/model/model.py`
  - strongest proven mechanism remains the existing `BalancedInteractionBlock` family
  - current code is compact and internally coherent
  - likely safe surface is a very small calibration-preserving edit, not a new branch
- `research_runtime/generations/generation_004/proposal_001/model/train.py`
  - plain optimizer stack, so benchmark failures are unlikely to be fixed by training cosmetics alone

### Local external repo evidence
- `research_runtime/knowledge/repo_cache/ACEsuit__mace/README.md`
  - emphasizes higher-order equivariant message passing, hidden irreps, correlation order, and specialized training/config surfaces
- `research_runtime/knowledge/repo_cache/ACEsuit__mace/mace/modules/symmetric_contraction.py`
  - confirms real product-basis behavior depends on dedicated symmetric contraction machinery
- `research_runtime/knowledge/repo_cache/ACEsuit__mace/mace/modules/models.py`
  - confirms such methods are not drop-in for the current compact custom model

## relevant_papers
1. *Forces are not Enough: Benchmark and Critical Evaluation for Machine Learning Force Fields with Molecular Simulations*
2. *A Euclidean transformer for fast and stable machine learned force fields*
3. *Atomic Cluster Expansion: Completeness, Efficiency and Stability*

## local_literature
- Verified locally by text extraction:
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`
- Reused local brief anchors:
  - `research_runtime/knowledge/briefs/evidence_brief_20260418T081500Z_generation004_proposal001_continuation_refresh.md`
  - `research_runtime/knowledge/briefs/evidence_brief_20260419T012900Z_generation006_proposal001_continuation.md`
  - `research_runtime/knowledge/briefs/evidence_brief_20260419T1957_generation007_proposal001_continuation.md`

## relevant_repos
- `research_runtime/knowledge/repo_cache/ACEsuit__mace`

## mechanism_ledger
| mechanism | source | concrete equation / code / pattern | current-code insertion point | proposal relevance | risk |
|---|---|---|---|---|---|
| force-from-energy contract | source code | scalar energy with autograd forces | must remain unchanged | hard requirement | low |
| in-block invariant recombination | source code + SO3KRATES local PDF | scalar/vector streams mixed via invariant projections | `BalancedInteractionBlock` | still plausible only as a tinier exploit than prior attempts | medium |
| narrow invariant many-body summary | ACE local PDF | compact invariant polynomial / recursive summary | one small helper near scalar update or pre-readout summary | scientifically plausible but locally down-weighted by generation_007 failure | medium-high |
| benchmark-complete stability-aware interpretation | Forces Are Not Enough local PDF | use force, energy, gap, Q, and training behavior together | evaluation logic only | prevents force-only overclaim | low |
| full higher-order product basis | local MACE repo | irreps, symmetric contraction, product-basis stack | rewrite-heavy across model | not bounded here | high |

## capability_gap
### Current code capabilities
- strong local equivariant trunk
- validated benchmark-complete balance
- reliable runtime behavior
- meaningful internal scalar/vector coupling already present

### Required capabilities from evidence
- if any new capacity is added, it must preserve the parent’s rMD17 energy quality and balanced `Q_total`
- any proposed improvement must be more calibration-preserving than the completed generation_007 children

### Missing pieces
- a demonstrated micro-edit that improves directional retention without disturbing the parent’s good energy regime
- cleaner interpretation of replicate variance, since the control-like branch underperformed strongly

### Integration risk
- low-to-medium: ultra-small in-block calibration-preserving exploit
- medium-high: any renewed late-summary or ACE-like helper based on current negative round evidence
- high: product-basis, irreps, or nonlocal jumps

## implementable_design_moves
1. **Primary bounded exploit: source-faithful micro-edit inside the existing block family**
   - mechanism source: current source code plus SO3KRATES-style invariant/equivariant separation principle
   - concrete mechanism: only one very small extra invariant recombination or residual-scale calibration inside `BalancedInteractionBlock`, explicitly smaller than the generation_007 exploit variants
   - current-code insertion point: `BalancedInteractionBlock` in `model/model.py`
   - minimal bounded edit: tiny modification to scalar/vector blending or residual gating, designed to preserve fallback toward source behavior
   - expected effect: best chance of preserving source calibration while testing whether a micro-capacity tweak can help ISO17
   - one bounded control / ablation: exact source-matched replicate
2. **Secondary bounded move: retry invariant summary only if made strictly narrower than generation_007**
   - mechanism source: ACE local PDF plus negative feedback from `generation_007/proposal_004` and `proposal_006`
   - concrete mechanism: one much weaker late invariant statistic, not a new branch family
   - current-code insertion point: single helper feature near scalar update or pre-readout summary
   - minimal bounded edit: lower-width, easy-to-disable summary path
   - expected effect: mainly diagnostic, not strongly recommended from current evidence
   - one bounded control / ablation: same model with summary path disabled

## strong_evidence
- `generation_004/proposal_001` remains the best completed benchmark unit even after another full continuation round.
- The source is benchmark-strong, runtime-clean, and balanced across rMD17 and ISO17.
- Multiple evidence-plausible `generation_007` children failed to beat the source, which is strong local evidence against medium-sized architectural jumps.
- Local literature continues to support symmetry-aware local geometry, but current round evidence says preservation of calibration matters more than adding plausible mechanism.

## weak_but_relevant
- SO3KRATES still supports bounded invariant/equivariant recombination, but local round results weaken confidence in anything larger than a micro-edit.
- ACE still supports local many-body enrichment, but `generation_007/proposal_004` is direct local caution against even narrow versions that are not tightly controlled.
- The poor source-matched control outcome suggests nontrivial variance or fidelity issues, but not enough to erase the parent’s large performance margin.

## background_context
- Earlier briefs increasingly narrowed the frontier toward bounded local exploits.
- The completed `generation_007` round did not validate those bounded jumps at usable strength.
- The frontier has therefore become more conservative: the evidence now favors source-faithful micro-edits and strong controls over fresh medium-sized representational changes.

## key_findings
1. `generation_004/proposal_001` remains the correct continuation anchor for `generation_008`.
2. The main new evidence is local falsification: several bounded, literature-supported child moves again failed to beat the source.
3. Any next step should be smaller and more fallback-friendly than the completed `generation_007` proposals.
4. The evidence now favors micro-calibration or micro-recombination edits inside the existing block family over renewed readout or many-body jumps.
5. Full MACE-like or nonlocal jumps remain poor implementation fits and are even less justified now.

## useful_patterns
- preserve the winning trunk and force-from-energy contract
- prefer edits that can collapse back toward source behavior
- require full benchmark improvement, not isolated force or ISO17 gains
- treat control comparison as necessary for interpreting any small claimed gain

## risks_or_mismatches
- Data/task mismatch: nonlocal or electronic-state branches remain weakly justified.
- Method mismatch: repeating medium-sized readout or ACE-like summary jumps is poorly supported after generation_007.
- Codebase mismatch: full product-basis or irreps migration remains rewrite-heavy.
- Runtime mismatch: larger edits threaten the parent’s clean reliability.
- Likely failure signs:
  - rMD17 energy regresses while ISO17 improves only slightly
  - training spikes stop recovering by late epochs
  - apparent force gains come with worse mixed energy, gap, or `Q_total`

## implementation_fit
- Best fit: ultra-small source-faithful exploit inside `BalancedInteractionBlock`.
- Acceptable but weaker fit: very narrow diagnostic invariant summary with explicit source control.
- Poor fit: another medium-strength readout jump, ACE-like helper branch at prior strength, full MACE-like transplant, or nonlocal/electronic branch.

## exploit_angles
- Micro-edit the existing scalar/vector blend or residual scale while preserving parent behavior.
- Pair any micro-edit with an exact source-matched control for attribution.
- Do not treat head-only enrichment as the default next exploit from current evidence.

## jump_angles
- Only a very narrow diagnostic invariant-summary jump remains defensible.
- Anything broader than that is not supported by the current local evidence.

## followup_queries
- Is there a truly source-faithful micro-edit inside `BalancedInteractionBlock` that improves ISO17 without moving rMD17 energy off its current optimum?
- Was the weak source-matched control caused mainly by replicate variance or by imperfect fidelity to the source?
- Can any renewed invariant-summary idea be reduced enough to behave like a diagnostic toggle rather than a real branch?

## confidence
**high** on the continuation anchor and on the need for more conservative bounded moves, **medium** on the exact micro-edit mechanism.

Reason: the benchmark-complete continuation decision is decisive, the source profile is clear, and the strongest new evidence is the repeated local failure of several previously plausible bounded jumps. That sharply increases confidence in staying with the source family while narrowing the acceptable next-step envelope.