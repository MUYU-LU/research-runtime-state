# MLIP Evidence Brief

## question
What bounded, locally supported continuation guidance should be used for `generation_007` in balanced mode when the continuation source remains `generation_004/proposal_001` after all completed `generation_006` children underperformed it?

## local_context
- Request scope: one evidence-only brief for continuation source `generation_004/proposal_001`, target `generation_007`, evidence mode `balanced`.
- Selection record: `research_runtime/ledger/generation_007_continuation_decision.json` keeps `generation_004/proposal_001` as the continuation source with `Q_rmd17 = 3.0291`, `Q_iso17 = 3.3267`, `Q_total = 3.1333`.
- Completed `generation_006` children all trail the parent source. Best child is `generation_006/proposal_008` at `Q_total = 2.6867`, which is still materially below the source.
- Local prior briefs already argued for narrow in-block stream refinement first and a very narrow ACE-like invariant summary second. This brief rechecks that thesis against the `generation_007` continuation decision and fresh local paper/repo evidence only.
- No experiments, code edits, launches, or workflow advancement were performed.

## current_unit_profile
- Model family: compact custom local equivariant MLIP with scalar and vector channels.
- Current implementation surface:
  - `research_runtime/generations/generation_004/proposal_001/model/model.py`
  - `research_runtime/generations/generation_004/proposal_001/model/train.py`
- Present capabilities:
  - atom embedding plus atomref baseline
  - local cutoff graph built from Cartesian positions
  - Gaussian RBF features with cosine cutoff envelope
  - two `BalancedInteractionBlock`s
  - scalar/vector interaction through `directional_invariant`, `agg_norm`, and `vector_alignment`
  - energy-first prediction with forces from autograd
- Missing capabilities:
  - no explicit triplet/product-basis body-order path
  - no irreps/tensor-product machinery
  - no sparse neighbor builder
  - no nonlocal or electronic-state branch
- Likely bottlenecks:
  - final readout still compresses vector content mainly to `vector_norm`
  - current trunk already uses cross-stream information, so head-only enrichment is probably too weak or too unstable
  - parent source has strong calibration and reliability, so larger rewrites face a high burden of proof

## benchmark_dossier
### Source unit: `generation_004/proposal_001`
- Runtime state: `terminal_success`
- Reliability: one launch, zero retries, zero repairs, remote sync and remote smoke passed
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
  - both datasets show recovery after mid-training energy spikes
  - end-state trends are improving, not degrading
  - source is therefore strong but calibration-sensitive
- Generation_007 continuation context:
  - no completed `generation_006` child exceeded the source
  - best child `generation_006/proposal_008` is a source-matched control replicate, useful for attribution caution rather than new mechanism evidence

## mathematical_evidence
1. Local code evidence
   - `BalancedInteractionBlock` computes scalar messages from `(src_scalar + dst_scalar) * scalar_gate + directional_invariant * invariant_gate`.
   - Scalar updates already consume invariant summaries `agg_norm` and `vector_alignment`.
   - Final atomwise energy still depends on `torch.cat([scalar_state, vector_norm], dim=-1)`, so late directional information is reduced to norms.
2. Local paper: **A Euclidean transformer for fast and stable machine learned force fields**
   - Locally extracted from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`.
   - Concrete mechanism: separate invariant and equivariant information, recombine through invariant projections, avoid expensive tensor products.
   - Transferable implication: a bounded extra invariant recombination inside the existing block family is plausible; a full transformer rewrite is not required.
3. Local paper: **Atomic Cluster Expansion: Completeness, Efficiency and Stability**
   - Locally extracted from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`.
   - Concrete mechanism: complete invariant polynomial bases with recursive evaluation and explicit stability concerns.
   - Transferable implication: a very narrow invariant many-body summary path is principled, but only if kept compact and numerically controlled.
4. Local repo: `research_runtime/knowledge/repo_cache/ACEsuit__mace`
   - `mace/modules/symmetric_contraction.py` shows how higher-order equivariant product bases require explicit symmetric contraction machinery.
   - `mace/modules/models.py` shows MACE’s reliance on spherical harmonics, irreps bookkeeping, product bases, and specialized interaction/readout blocks.
   - Transferable implication: a true MACE-style jump is rewrite-heavy in this codebase, so only a tiny invariant summary idea is a bounded fit.

## physical_evidence
- Local paper: **Forces are not Enough: Benchmark and Critical Evaluation for Machine Learning Force Fields with Molecular Simulations**
  - Locally extracted from `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`.
  - Concrete claim: force/energy test errors alone do not align with downstream MD usefulness, and stability is a key metric.
  - Implication here: balanced continuation must stay benchmark-complete, not force-only.
- The current source keeps force-from-energy consistency and strict locality, and that regime is already validated on rMD17 plus ISO17.
- Nothing in the local benchmark dossier indicates the next bottleneck is missing nonlocal physics.

## chemical_evidence
- The active benchmark pair is molecular and local-angular, not an obvious charge-transfer or long-range-electronic stress test.
- Local ACE evidence is chemically closer to the likely missing signal than a nonlocal/electronic branch because it enriches local many-body/angular discrimination.
- Since the parent source already wins on both datasets, chemistry evidence supports staying local and symmetry-aware before attempting broader chemistry machinery.

## textual_evidence
- `generation_007_continuation_decision.json` explicitly confirms that `generation_004/proposal_001` still dominates all completed `generation_006` candidates.
- The best child being a source-matched control replicate is important caution: some narrow proposal deltas were not even competitive with faithful source behavior.
- Prior local brief evidence and the new decision together weaken the case for speculative jumps and strengthen the case for minimal edits that can fall back toward parent behavior.

## code_evidence
- Source code:
  - `model/model.py` already contains the best-proven mechanism surface, the interaction block rather than the head alone.
  - `model/train.py` is plain enough that another training-only tweak is unlikely to explain the missing gain.
- Local MACE repo evidence:
  - `README.md` states higher-order equivariant message passing depends on hidden irreps, correlation order, and specialized product-basis machinery.
  - `mace/modules/symmetric_contraction.py` implements Eq. 10/11-style symmetric contractions, confirming that genuine higher-order product-basis behavior is not a drop-in patch.
  - `mace/modules/models.py` shows interaction/product/readout stacks coupled tightly to irreps infrastructure.
- Fit judgment from code evidence:
  - drop-in: small invariant recombination inside `BalancedInteractionBlock`
  - moderate-change: one narrow late invariant summary helper
  - rewrite-heavy: true MACE/irreps/product-basis transplant

## relevant_papers
1. *Forces are not Enough: Benchmark and Critical Evaluation for Machine Learning Force Fields with Molecular Simulations*
2. *A Euclidean transformer for fast and stable machine learned force fields*
3. *Atomic Cluster Expansion: Completeness, Efficiency and Stability*

## local_literature
- Verified locally by text extraction:
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`
  - `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`
- Reused local prior-brief anchors:
  - `research_runtime/knowledge/briefs/evidence_brief_20260419T012900Z_generation006_proposal001_continuation.md`
  - `research_runtime/knowledge/briefs/evidence_brief_20260418T081500Z_generation004_proposal001_continuation_refresh.md`

## relevant_repos
- Locally available repo cache only:
  - `research_runtime/knowledge/repo_cache/ACEsuit__mace`

## mechanism_ledger
| mechanism | source | concrete equation / code / pattern | current-code insertion point | proposal relevance | risk |
|---|---|---|---|---|---|
| invariant/equivariant stream recombination | SO3KRATES local PDF + current `BalancedInteractionBlock` | separate streams, recombine via invariant projections without full tensor products | inside `BalancedInteractionBlock` scalar update path | strongest bounded exploit | medium |
| narrow invariant many-body summary | ACE local PDF | compact invariant polynomial / recursive summary rather than full framework transplant | one helper path before scalar update or pre-readout summary | bounded jump option | medium |
| force-from-energy contract | source code | scalar energy with autograd forces | must remain unchanged | hard constraint | low |
| stability-aware evaluation | Forces Are Not Enough local PDF | benchmark decisions must include stability and task-level behavior, not force alone | evaluation interpretation only | prevents wrong proposal choice | low |
| full higher-order product basis | local MACE repo | symmetric contraction + irreps/product basis stack | would require new machinery across model | not bounded here | high |

## capability_gap
- Current code capabilities:
  - good local equivariant trunk
  - strong benchmark-complete balance
  - reliable runtime behavior
- Required capabilities from evidence:
  - retain more directional information late without breaking calibration
  - if adding many-body signal, keep it compact and fallback-friendly
- Missing pieces:
  - stronger late invariant summary than vector norms alone
  - source-matched attribution remains useful, but already available via generation_006 control outcome
- Integration risk:
  - low-to-medium for in-block invariant recombination
  - medium for narrow ACE-like summary
  - high for product-basis or irreps-heavy jumps

## implementable_design_moves
1. Primary exploit
   - mechanism source: SO3KRATES local PDF plus current source code
   - concrete mechanism: one extra invariant recombination path using existing `self_vector`, `mixed_agg_vector`, `agg_norm`, or related contractions before the scalar residual update
   - current-code insertion point: `BalancedInteractionBlock` in `model/model.py`
   - minimal bounded edit: add one compact invariant statistic path inside the block, not a readout rewrite
   - expected effect: preserve parent behavior while improving directional retention
   - bounded control/ablation: same model with the added recombination path disabled
2. Secondary jump
   - mechanism source: ACE local PDF, filtered through local MACE repo fit evidence
   - concrete mechanism: a very narrow late invariant many-body summary, not full symmetric contraction machinery
   - current-code insertion point: one helper feeding scalar update or pre-readout summary in `model/model.py`
   - minimal bounded edit: low-width invariant summary from local neighbor geometry only
   - expected effect: extra angular/body-order signal if the trunk is capacity-limited
   - bounded control/ablation: same model with the summary path zeroed

## strong_evidence
- The parent source remains the best completed benchmark unit even after `generation_006`.
- Source code already shows the winning surface is the interaction block, not just the head.
- SO3KRATES supports bounded invariant/equivariant stream recombination without full tensor-product machinery.
- ACE supports compact invariant many-body summaries, but the local MACE repo shows full higher-order machinery is not a bounded drop-in change.
- Forces Are Not Enough supports using stability-aware, benchmark-complete reasoning rather than force-only metrics.

## weak_but_relevant
- The best `generation_006` child is a control replicate, which is useful for attribution caution but weak as a new mechanism signal.
- ACE-style enrichment is scientifically plausible, but only the narrowest version fits this codebase without rewrite risk.

## background_context
- Earlier continuation evidence had already narrowed the frontier to small in-block refinement first, narrow invariant many-body summary second.
- The `generation_007` continuation decision reinforces that map instead of overturning it.
- Local repo evidence makes the cost of a true MACE-style jump even clearer.

## key_findings
1. `generation_004/proposal_001` is still the correct continuation anchor for `generation_007` in balanced mode.
2. The best bounded next move remains a small internal stream-refinement exploit inside `BalancedInteractionBlock`.
3. A narrow ACE-like invariant summary is the main bounded jump option, but only as a tiny helper path, not a framework transplant.
4. Readout-only retries and full product-basis rewrites are both poorly supported by the local evidence.

## useful_patterns
- keep the parent trunk and force-from-energy contract
- prefer in-block invariant recombination over head-only enrichment
- if adding many-body signal, keep it late, narrow, and optional
- judge gains by full benchmark dossier, not force alone

## risks_or_mismatches
- Data/task mismatch: nonlocal/electronic or long-range branches remain weakly justified.
- Method mismatch: readout-only retries are likely to repeat prior underperformance.
- Codebase mismatch: real MACE-like higher-order product-basis integration is rewrite-heavy here.
- Runtime mismatch: larger architectural jumps risk giving up the source’s clean reliability.
- Likely failure signs:
  - rMD17 energy regresses while ISO17 improves only modestly
  - energy spikes stop recovering by late epochs
  - apparent force gains come with worse gap or `Q_total`

## implementation_fit
- Best fit: small invariant stream-refinement exploit inside `BalancedInteractionBlock`.
- Next-best fit: one very narrow ACE-like invariant summary helper.
- Poor fit: readout-only retry, full MACE/irreps transplant, nonlocal/electronic branch.

## exploit_angles
- Refine internal scalar/vector recombination in the existing block.
- Preserve the current training stack unless a specific instability symptom reappears.

## jump_angles
- Very narrow late ACE-like invariant summary path.
- Nothing broader is justified by the local evidence for this continuation.

## followup_queries
- Which exact invariant statistic inside `BalancedInteractionBlock` best preserves the parent’s fallback behavior?
- Is the narrow ACE-like summary more effective before the scalar update or only at the final readout?
- Can future small gains be interpreted cleanly against the existing source-matched control result from `generation_006/proposal_008`?

## confidence
**high** on continuation family and ranking, **medium-high** on the exact primary mechanism.

Reason: the benchmark-complete continuation decision is decisive, the local code surface is clear, and the local paper/repo evidence all points in the same bounded direction. The only remaining uncertainty is which minimal internal invariant recombination will outperform the already strong parent without harming calibration.
