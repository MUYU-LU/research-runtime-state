# Proposal context for generation_004/proposal_001

## Current unit
- unit: generation_004/proposal_001
- source unit: generation_003/proposal_004

## Active evidence
- path: /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260418T081500Z_generation004_proposal001_continuation_refresh.md
- source unit: generation_004/proposal_001
- mode: balanced

```markdown
# MLIP Evidence Brief

## question
What single bounded, benchmark-centric continuation should guide `generation_005` from source unit `generation_004/proposal_001`, after a fresh evidence refresh that adds new local literature beyond the prior continuation brief and keeps balanced evidence mode?

## mode
balanced

## local_context
- Continuation source under review: `research_runtime/generations/generation_004/proposal_001`
- Frontier status from prior round decision context: highest completed non-control `Q_total` in `generation_004`, with `Q_rmd17 = 3.0291`, `Q_iso17 = 3.3267`, `Q_total = 3.1333`.
- Lineage intent from `research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md`: preserve the local equivariant energy-first family, improve calibration and residual behavior, and rebalance rMD17 without sacrificing cross-dataset upside.
- This refresh is evidence-only. No runnable code edits, no selection file, no materialization, no runs.
- Fresh-refresh requirement for this brief: explicitly separate **newly added evidence** from **reused prior evidence**.

## current_unit_profile
- Model family: compact custom local equivariant MLIP, NequIP-style in spirit, not a full irreps framework transplant.
- Phase: exploit continuation, staying inside the validated local equivariant family.
- Present capabilities in `research_runtime/generations/generation_004/proposal_001/model/model.py`:
  - atom embedding plus atomref baseline
  - local cutoff graph from positions
  - scalar and vector channels
  - two repeated `BalancedInteractionBlock`s
  - Gaussian RBF plus cosine cutoff envelope
  - energy-first prediction with forces from autograd
  - scalar update already uses `agg_norm` and `vector_alignment`
- Missing capabilities:
  - no explicit triplet/body-order contraction
  - no irreps tensor products
  - no explicit nonlocal branch or electronic-state inputs
  - dense all-pairs neighbor build before masking
- Likely bottlenecks:
  - final energy readout still compresses vector content to norms only
  - angular/body-order capacity remains bounded despite improved in-block coupling
  - optimization is clean overall, so the next gap is more likely representational than optimizer-only
- Likely implementation surface:
  - `model/model.py` for readout or bounded body-order augmentation
  - `model/train.py` only for secondary schedule polish

## benchmark_dossier
### Dataset metrics
| dataset | split metrics | mixed force | mixed energy | gap penalty | Q_dataset |
|---|---|---:|---:|---:|---:|
| rMD17 | mild OOD F/E `0.10458 / 0.59297`, hard OOD F/E `0.10503 / 0.59259` | 0.10485 | 0.59274 | 0.00429 | 3.02911 |
| ISO17 | within F/E `0.18116 / 0.75503`, other F/E `0.19033 / 0.79636` | 0.18666 | 0.77982 | 0.04911 | 3.32669 |

### Cross-dataset view
- `Q_total = 3.13326`, best completed non-control result in the round context used for continuation.
- Source is balanced, not force-only: both datasets are strong, energy is dramatically improved over parent lineage, and split gaps remain controlled.
- Relative to parent `generation_003/proposal_004`, the biggest gain is energy calibration, especially rMD17 energy.

### Training dynamics
- rMD17:
  - validation force improves from `0.2955` to `0.1046`
  - validation energy improves from `86.41` to `0.5930`
  - temporary energy spike at epoch 4 (`28.00`) but full recovery by the end
- ISO17:
  - validation force improves from `0.1975` to `0.1599`
  - validation energy improves from `45.92` to `1.04`
  - stronger volatility, including epoch-4 energy spike (`69.97`), then recovery
- Best practical reading: end-state is strong and reliable, but ISO17 still shows capacity-sensitive optimization turbulence.

### Runtime / reliability
- terminal success, one launch, zero retries, zero repairs
- smoke passed and synced in prior frontier context
- runtime evidence supports the unit as a real frontier source, not a rescue artifact

### Control comparison
- No same-generation direct control replicate is attached to `generation_004/proposal_001`.
- Reused lineage control reference remains `generation_003/proposal_008`, which is far worse on benchmark-complete metrics.
- Therefore large gains are real, but small future gains should still be interpreted cautiously without a source-matched replicate.

## mathematical_evidence
### Newly added evidence
1. **ACE completeness / efficiency / stability** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`, locally extracted)
   - ACE frames invariant polynomial bases as systematically extensible many-body expansions with guarantees around completeness and efficient recursive evaluation.
   - Important implication here: body-order enrichment does not have to mean a full framework rewrite if a compact invariant basis summary can be injected into the existing local model.
2. **ELoRA** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP参数高效微调 - ELoRA等变低秩适配.pdf`, locally extracted)
   - ELoRA argues that naive low-rank adaptation can break equivariance, and proposes path-dependent low-rank updates that preserve equivariance.
   - Relevant mathematical lesson: if the next move introduces low-rank channel adaptation or extra coupling blocks, symmetry-preserving structure matters more than generic PEFT-style rank reduction.
3. **SO3KRATES / Euclidean Transformer** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`, locally extracted)
   - Separates invariant and equivariant information while avoiding expensive tensor products.
   - Strongly relevant to the present code because the current block already distinguishes scalar and vector streams; the paper supports further separation-and-recombination without full irreps machinery.

### Reused prior evidence
- NequIP and MACE remain the prior reference points for disciplined equivariance and higher-order message passing.
- Prior brief already established that a full irreps-heavy transplant would be higher friction than a bounded family continuation.

## physical_evidence
### Newly added evidence
1. **Forces Are Not Enough** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`, locally extracted)
   - Direct warning that low test force error does not guarantee good simulation behavior and that stability is a distinct objective.
   - This reinforces the workflow rule to keep energy, gap, and training stability visible, not just force MAE.
2. **SpookyNet** (`/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - SpookyNet含电子自由度非局域力场.pdf`, locally extracted)
   - Highlights failure modes of strict locality when charge, spin, or nonlocal effects matter.
   - For current benchmarks, this is more caution than immediate action: nothing in the present benchmark dossier shows a nonlocal branch is the most urgent bottleneck.
3. **SO3KRATES** (same local PDF as above)
   - Connects stability and extrapolation robustness to richer equivariant representations, but also emphasizes computational efficiency.
   - This supports a bounded representational upgrade over a heavy rewrite.

### Reused prior evidence
- Existing source preserves force-from-energy consistency, locality, and rotationally safe energy construction.
- Current benchmark behavior shows locality is adequate for rMD17 and ISO17 in this frontier setting.

## chemical_evidence
### Newly added evidence
- **SpookyNet** is molecule-centric and explicitly addresses chemistry regimes where electronic state and nonlocality matter. That broadens the chemistry map, but also sharpens the mismatch call: the present benchmark pair does not yet justify adding charge/spin/nonlocal machinery as the next bounded step.
- **Forces Are Not Enough** reinforces that chemically meaningful simulation behavior can diverge from force-only ranking, matching the need to keep benchmark-complete selection criteria.
- **ACE** supports many-body/angular sensitivity as a chemically meaningful way to improve local descriptors without abandoning local molecular modeling.

### Reused prior evidence
- rMD17 and ISO17 both reward local angular discrimination and stable energy surfaces.
- Atomref and energy-first prediction remain chemistry-safe parts of the current design.

## textual_evidence
### Newly added evidence
- **Forces Are Not Enough**: direct claim that force-only evaluation is misaligned with practical MD objectives and that stability should be treated as a key metric.
- **ELoRA**: direct claim that preserving equivariance during low-rank adaptation materially improves data efficiency and accuracy.
- **SO3KRATES**: direct claim that separating invariant/equivariant information can improve the balance of accuracy, stability, and speed without expensive tensor products.
- **SpookyNet**: direct claim that purely local models can miss nonlocal electronic effects, but those effects are especially relevant when electronic states vary.

### Reused prior evidence
- Proposal intent remains an exploit, not a new architecture family jump.
- Prior NequIP/MACE evidence still supports staying geometric and local, with bounded body-order expansion as the natural next-capacity direction.

## code_evidence
### Local code evidence
- `BalancedInteractionBlock` already performs a meaningful mid-block scalar/vector recombination through `agg_norm` and `vector_alignment`.
- The strongest remaining bottleneck is that the final `readout` sees `torch.cat([scalar_state, vector_norm], dim=-1)`, so terminal directional content is reduced to norms.
- This means the code already validated one level of scalar-vector fusion internally, but the energy head still lacks a richer invariant summary of directional structure.
- Dense pair construction is still present, but benchmark evidence does not say this is the main science bottleneck for the next bounded step.

### External code-pattern evidence
- No fresh repository deep-read was completed in this refresh because web fetch was unavailable.
- Prior reused repo evidence for NequIP and MACE remains valid background only.
- Fresh literature still adds actionable code-pattern implications:
  - ACE suggests compact invariant many-body summaries rather than a full new framework.
  - ELoRA warns against generic low-rank edits that would silently break symmetry assumptions.
  - SO3KRATES supports explicit invariant/equivariant stream separation with cheaper coupling than tensor-product-heavy designs.

## relevant_papers
### Newly added evidence
1. **Forces are not Enough: Benchmark and Critical Evaluation for Machine Learning Force Fields with Molecular Simulations**
2. **SpookyNet: Learning force fields with electronic degrees of freedom and nonlocal effects**
3. **ELoRA: Low-Rank Adaptation for Equivariant GNNs**
4. **A Euclidean transformer for fast and stable machine learned force fields**
5. **Atomic Cluster Expansion: Completeness, Efficiency and Stability**

### Reused prior evidence
6. **SE(3)-Equivariant Graph Neural Networks for Data-Efficient and Accurate Interatomic Potentials**
7. **Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields**

## local_literature
### Newly added evidence, all locally verified by extraction
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP力场基准 - Forces Are Not Enough分子模拟评测.pdf`
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - SpookyNet含电子自由度非局域力场.pdf`
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP参数高效微调 - ELoRA等变低秩适配.pdf`
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP分子力场 - 欧氏Transformer快速稳定力场.pdf`
- `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP理论基础 - ACE完备性效率与稳定性.pdf`

### Reused prior evidence
- prior brief grounded NequIP and MACE as the main family-level references

## relevant_repos
### Reused prior evidence
- `mir-group/nequip`
- `ACEsuit/mace`

### Fresh refresh note
- No new repo is promoted to strong evidence in this brief because repository fetch/deep-read was unavailable during this run.

## capability_gap
### Current capabilities
- strong local equivariant family
- validated two-block exploit
- reliable benchmark-complete gains
- internal scalar/vector coupling already improved over parent

### Required next capabilities
- richer terminal invariant summary than vector norms alone
- optional compact many-body/angular signal beyond pairwise aggregation
- preservation of clean optimization and energy-first contract

### Missing pieces
- bounded invariant readout features derived from vector structure beyond norms
- explicit compact body-order summary path
- source-matched control replicate for small-gain attribution

### Integration risk
- low to medium: richer invariant readout inside current head
- medium: ACE-inspired compact many-body summary added to scalar updates
- medium-high: anything that imitates SpookyNet-style nonlocal/electronic modeling in this benchmark phase
- medium-high: generic low-rank tricks that ignore equivariance constraints

## implementable_design_moves
1. **Primary bounded exploit: enrich the terminal invariant energy head**
   - principle: keep the winning two-block family, but let final atomwise energies see more invariant structure than vector norms alone
   - mathematical form: augment readout features with bounded invariant contractions such as self/aggregate vector alignment summaries, low-rank scalar-vector bilinears, or center-wise invariant products computed from existing vector channels
   - physical rationale: preserve rotationally invariant energy while retaining directional information relevant to stable surfaces
   - chemistry relevance: should improve discrimination of local angular environments in molecular benchmarks
   - code pattern: modify final readout inputs in `model/model.py`, reusing already available vector states rather than adding a new framework
   - implementation friction: low to medium
   - expected effect: best chance of improving ISO17 and preserving current rMD17 energy quality
   - bounded control/ablation: same source model with current norm-only readout retained
2. **Secondary balanced jump: ACE-inspired compact body-order summary**
   - principle: add a small invariant many-body summary path without transplanting MACE or full ACE machinery
   - mathematical form: low-order neighbor-pair or recursive invariant basis summaries injected into scalar updates
   - physical rationale: capture angular/body-order structure the current pairwise aggregation may blur
   - chemistry relevance: plausible for conformational discrimination in both datasets
   - code pattern: add a narrow helper around local neighbor features in `model/model.py`
   - implementation friction: medium
   - expected effect: higher upside than readout-only enrichment, but more stability risk
   - bounded control/ablation: identical backbone with summary path toggled off
3. **Deprioritized move: nonlocal/electronic branch**
   - principle: borrow from SpookyNet-style nonlocal chemistry modeling
   - mathematical form: self-attention or explicit electronic-state conditioning
   - physical rationale: useful when locality breaks
   - chemistry relevance: currently weak for this benchmark pair
   - code pattern: rewrite-heavy in this codebase
   - implementation friction: high
   - expected effect: poorly justified for the next bounded continuation
   - bounded control/ablation: not recommended for this round

## strong_evidence
### Newly added evidence
- Local PDF evidence now independently supports three things the prior brief did not freshly verify in this run:
  1. benchmark selection must remain stability-aware and not force-only (`Forces Are Not Enough`)
  2. bounded invariant/equivariant separation can improve stability without tensor-product-heavy rewrites (`SO3KRATES`)
  3. compact many-body enrichment is principled, but should stay symmetry-aware (`ACE`, `ELoRA`)

### Reused prior evidence
- `generation_004/proposal_001` is still the best benchmark-complete continuation source.
- Current runtime/reliability record is clean.
- Prior NequIP/MACE references still justify staying inside the local equivariant family.

## weak_but_relevant
### Newly added evidence
- SpookyNet shows that locality can fail in broader chemistry regimes, but current benchmark evidence does not point there yet.
- ELoRA is about fine-tuning pre-trained equivariant GNNs, not exactly this from-scratch compact model, so its value is architectural caution, not direct method transfer.

### Reused prior evidence
- Same-generation control evidence is still missing.
- ISO17 volatility suggests added capacity could still destabilize training if stacked too aggressively.

## background_context
- The source unit already validated balanced exploitation over speculative jumps.
- This fresh refresh strengthens that conclusion rather than overturning it.
- The new literature mainly narrows *how* to continue: richer invariant coupling first, compact many-body summary second, nonlocality later only if benchmark evidence changes.

## key_findings
1. The frontier decision remains benchmark-complete, not force-only.
2. Fresh local literature strengthens the case for a **bounded invariant readout upgrade** as the next best move.
3. A compact ACE-like body-order path is still the best higher-upside alternative, but it should remain narrow.
4. SpookyNet-style nonlocal/electronic machinery is scientifically interesting but not the right next bounded continuation for rMD17 plus ISO17.
5. Any low-rank or compressed coupling change should respect symmetry structure; generic cheap adaptation is not automatically safe.

## useful_patterns
- Separate invariant and equivariant streams, then recombine through invariant summaries.
- Prefer cheap invariant contractions over heavy irreps rewrites when the current family is already strong.
- Keep stability and energy quality visible during selection and interpretation.
- Use many-body enrichment as a narrow add-on, not a framework transplant.

## risks_or_mismatches
- Data/task mismatch: nonlocal or electronic-state branches are weakly justified by the present benchmarks.
- Method mismatch: a full ACE/MACE/SpookyNet transplant would exceed the bounded continuation budget.
- Codebase mismatch: irreps-heavy or transformer-nonlocal machinery is much larger than the current custom implementation surface.
- Dependency/runtime mismatch: extra symmetry frameworks or attention stacks would raise complexity and could disturb the currently clean runtime profile.
- Likely failure signs:
  - ISO17 energy spikes suggest capacity increases can destabilize training
  - readout-only changes are safer than simultaneous body-order plus nonlocal jumps
  - generic low-rank compression could break symmetry discipline if copied naively from non-equivariant settings

## implementation_fit
- Best fit: enrich the existing terminal invariant readout while keeping the two-block family intact.
- Next-best fit: add a compact ACE-inspired many-body summary path if a slightly higher-risk jump is desired.
- Poor fit now: SpookyNet-style nonlocality, explicit electronic degrees of freedom, or full irreps/transfomer rewrites.
- Overall fit judgment: continue from `generation_004/proposal_001` with a readout-centered exploit, not a family change.

## exploit_angles
- Primary exploit: replace norm-only terminal vector usage with a richer invariant scalar-vector summary in the energy head.
- Secondary exploit: minor schedule polish only after the representational exploit is isolated.
- Evidence-weighted recommendation: take the readout exploit before trying explicit body-order machinery.

## jump_angles
- Best bounded jump: compact ACE-like invariant many-body augmentation inside the current local family.
- Secondary jump: a light SO3KRATES-inspired separation/recombination refinement, but still without nonlocal attention.
- Deprioritized jump: full nonlocal/electronic architecture branch.

## followup_queries
- Can a richer invariant energy head improve ISO17 force/energy without losing rMD17 stability?
- Is a tiny ACE-like summary path measurably better than readout enrichment alone?
- Would a source-matched control replicate materially change confidence in a small gain from readout enrichment?
- Does the current dense neighbor builder become a real practical bottleneck only after representational gains plateau?

## confidence
**high for the continuation family, medium-high for the exact mechanism**

Reasoning: the benchmark dossier already strongly favored staying inside the current source family. The fresh refresh adds multiple new locally verified papers that all point in the same bounded direction: preserve benchmark-centric evaluation, keep symmetry-aware local geometry, and prefer a richer invariant readout before a heavier body-order or nonlocal jump.

```

## Current runtime summary
```json
{
  "implementation_status": {
    "implementation_state": "launch_ready",
    "source_unit": "generation_003/proposal_004",
    "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md",
    "control_replicate": false,
    "changed_files": [
      {
        "path": "model/model.py",
        "sha256": "aa6c16d26fa72de792c66b24eaf2f583373a66eabc338ebae04872489f581ef4"
      },
      {
        "path": "model/train.py",
        "sha256": "a2e5336c32b379cbd3fe183c41a893225992061849571b639d65185d8846e64d"
      }
    ],
    "repair_attempts": 0,
    "same_failure_class_repairs": 0,
    "last_failure_class": "unknown_failure",
    "remote_synced": true,
    "remote_smoke_passed": true,
    "remote_path": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_004/proposal_001",
    "smoke_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_004/proposal_001/outputs/smoke_rmd17.log",
    "smoke_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_004/proposal_001/outputs/smoke_rmd17.log",
    "last_actor": "remote_collect_unit.py",
    "last_updated_utc": "2026-04-17T23:22:58.791549+00:00"
  },
  "run_status": {
    "run_state": "terminal_success",
    "launch_count": 1,
    "retry_count": 0,
    "pid": "3008347",
    "host": "210.45.70.177",
    "launch_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_004/proposal_001/outputs/launch.log",
    "launch_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_004/proposal_001/outputs/launch.log",
    "failure_class": null,
    "launched_at_utc": "2026-04-17T23:13:18.849079+00:00",
    "finished_at_utc": "2026-04-18T02:11:13.011712+00:00",
    "last_actor": "remote_collect_unit.py",
    "last_state_change_utc": "2026-04-18T02:11:13.011754+00:00"
  },
  "unit_summary": {}
}
```

## Source runtime summary
```json
{
  "implementation_status": {
    "implementation_state": "launch_ready",
    "source_unit": "generation_002/proposal_005",
    "proposal_file": "04_jump_nequip_style_recalibrated_refactor.md",
    "control_replicate": false,
    "changed_files": [
      {
        "path": "model/model.py",
        "sha256": "89361d68c606e0bbdf030493ed7d46cbeb2c583ee5c8648f59ffbf5e7f3d16c5"
      },
      {
        "path": "model/train.py",
        "sha256": "abe39d2214fb9139bd9d079866464e5c7c0b3b183c6b9b0f19513ccfbfcc588a"
      }
    ],
    "repair_attempts": 0,
    "same_failure_class_repairs": 0,
    "last_failure_class": null,
    "remote_synced": true,
    "remote_smoke_passed": true,
    "remote_path": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_003/proposal_004",
    "smoke_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_003/proposal_004/outputs/smoke_rmd17.log",
    "smoke_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_003/proposal_004/outputs/smoke_rmd17.log",
    "last_actor": "remote_smoke_unit.py",
    "last_updated_utc": "2026-04-17T14:10:22.098297+00:00",
    "notes": [
      "Implemented a bounded NequIP-style recalibrated refactor while preserving the benchmark contract, local neighbor interactions, scalar energy readout, atomref baseline, and autograd-derived forces.",
      "Replaced the prior low-rank stage stack with a cleaner interaction refactor using cosine cutoff envelopes, gated scalar residual updates, tempered vector residual updates, and normalized scalar state updates.",
      "Recalibrated training with AdamW, cosine LR scheduling, gradient clipping, stronger energy emphasis, and short energy-weight warmup for a more benchmark-balanced regime."
    ]
  },
  "run_status": {
    "run_state": "terminal_success",
    "launch_count": 1,
    "retry_count": 0,
    "pid": "2904438",
    "host": "210.45.70.177",
    "launch_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_003/proposal_004/outputs/launch.log",
    "launch_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_003/proposal_004/outputs/launch.log",
    "failure_class": null,
    "launched_at_utc": "2026-04-17T16:20:38.837492+00:00",
    "finished_at_utc": "2026-04-17T17:50:58.624304+00:00",
    "last_actor": "remote_collect_unit.py",
    "last_state_change_utc": "2026-04-17T17:50:58.624351+00:00"
  },
  "unit_summary": {}
}
```

## rmd17 benchmark dossier
```json
{
  "metrics": {
    "mild_ood_energy_mae": 0.5929720458984375,
    "mild_ood_force_mae": 0.10458182134397793,
    "hard_ood_energy_mae": 0.5925932006835938,
    "hard_ood_force_mae": 0.10503137192176655,
    "mixed_force_mae": 0.1048515516906511,
    "mixed_energy_mae": 0.5927447387695313,
    "gap_penalty": 0.004287495707365973,
    "Q_dataset": 3.0291108938796594,
    "device": "cuda"
  },
  "history": [
    {
      "epoch": 6,
      "train": {
        "loss": 15.348967134423553,
        "energy_mae": 12.71894921875,
        "force_mae": 0.131500896028243
      },
      "val": {
        "loss": 6.038513257011771,
        "energy_mae": 3.4658735961914062,
        "force_mae": 0.1286319831525907
      },
      "device": "cuda",
      "learning_rate": 0.0001464466094067263,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    {
      "epoch": 7,
      "train": {
        "loss": 8.394697527773678,
        "energy_mae": 6.084681396484375,
        "force_mae": 0.11550080670998432
      },
      "val": {
        "loss": 4.677032755553722,
        "energy_mae": 2.4347793579101564,
        "force_mae": 0.1121126701454632
      },
      "device": "cuda",
      "learning_rate": 3.8060233744356646e-05,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    {
      "epoch": 8,
      "train": {
        "loss": 3.979856164485216,
        "energy_mae": 1.8791643676757812,
        "force_mae": 0.10503459000156727
      },
      "val": {
        "loss": 2.684609644584358,
        "energy_mae": 0.5929732666015625,
        "force_mae": 0.10458181903103832
      },
      "device": "cuda",
      "learning_rate": 0.0,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    }
  ],
  "history_summary": {
    "epochs": 8,
    "last_epoch": {
      "epoch": 8,
      "train": {
        "loss": 3.979856164485216,
        "energy_mae": 1.8791643676757812,
        "force_mae": 0.10503459000156727
      },
      "val": {
        "loss": 2.684609644584358,
        "energy_mae": 0.5929732666015625,
        "force_mae": 0.10458181903103832
      },
      "device": "cuda",
      "learning_rate": 0.0,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    "best_val_force_mae": 0.10458181903103832,
    "best_val_energy_mae": 0.5929732666015625
  }
}
```

## iso17 benchmark dossier
```json
{
  "metrics": {
    "within_energy_mae": 0.7550254293007426,
    "within_force_mae": 0.1811587671813841,
    "other_energy_mae": 0.7963562950721154,
    "other_force_mae": 0.19032591961324216,
    "mixed_force_mae": 0.18665905864049892,
    "mixed_energy_mae": 0.7798239487635663,
    "gap_penalty": 0.04911174683177137,
    "Q_dataset": 3.32668622930551,
    "device": "cuda"
  },
  "history": [
    {
      "epoch": 6,
      "train": {
        "loss": 16.691313417978805,
        "energy_mae": 12.704586097037438,
        "force_mae": 0.1993363660833992
      },
      "val": {
        "loss": 6.187129020690918,
        "energy_mae": 2.5341796875,
        "force_mae": 0.18264745672543845
      },
      "device": "cuda",
      "learning_rate": 0.0001464466094067263,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    {
      "epoch": 7,
      "train": {
        "loss": 11.12258027201832,
        "energy_mae": 7.344810803101795,
        "force_mae": 0.18888847393232702
      },
      "val": {
        "loss": 6.189233144124349,
        "energy_mae": 2.9222005208333335,
        "force_mae": 0.1633516401052475
      },
      "device": "cuda",
      "learning_rate": 3.8060233744356646e-05,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    {
      "epoch": 8,
      "train": {
        "loss": 6.050462749246323,
        "energy_mae": 2.3952547281095296,
        "force_mae": 0.18276040118077014
      },
      "val": {
        "loss": 4.2366401354471845,
        "energy_mae": 1.0377604166666667,
        "force_mae": 0.15994398792584738
      },
      "device": "cuda",
      "learning_rate": 0.0,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    }
  ],
  "history_summary": {
    "epochs": 8,
    "last_epoch": {
      "epoch": 8,
      "train": {
        "loss": 6.050462749246323,
        "energy_mae": 2.3952547281095296,
        "force_mae": 0.18276040118077014
      },
      "val": {
        "loss": 4.2366401354471845,
        "energy_mae": 1.0377604166666667,
        "force_mae": 0.15994398792584738
      },
      "device": "cuda",
      "learning_rate": 0.0,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 3.0
    },
    "best_val_force_mae": 0.15994398792584738,
    "best_val_energy_mae": 1.0377604166666667
  }
}
```

## Diff vs source: model.py
- +        self.scalar_mix_norm = nn.LayerNorm(hidden_dim)
- +        self.vector_residual_scale = nn.Parameter(torch.tensor(0.35))
- +        num_nodes = scalar_state.shape[0]
- +        neighbor_count = torch.zeros(num_nodes, device=scalar_state.device, dtype=scalar_state.dtype)
- +        neighbor_count.index_add_(0, i_idx, torch.ones_like(i_idx, dtype=scalar_state.dtype))
- +        neighbor_scale = neighbor_count.clamp_min(1.0).rsqrt().unsqueeze(-1)
- +        agg_scalar = agg_scalar * neighbor_scale
- +        agg_vector = agg_vector * neighbor_scale.unsqueeze(-1)
- +
- -        new_scalar = self.layer_norm(scalar_state + scalar_gate * delta_scalar)
- +        mixed_scalar = scalar_state + scalar_gate * delta_scalar
- +        new_scalar = self.layer_norm(0.7 * mixed_scalar + 0.3 * self.scalar_mix_norm(scalar_state + agg_scalar))
- -        new_vector = vector_state + 0.5 * delta_vector
- +        residual_scale = 0.15 + 0.35 * torch.sigmoid(self.vector_residual_scale)
- +        new_vector = vector_state + residual_scale * delta_vector

## Diff vs source: train.py
- +        betas=(0.9, float(CONFIG.get("adam_beta2", 0.97))),
- -    energy_weight = float(CONFIG.get("energy_weight", 2.0))
- -    force_weight = float(CONFIG.get("force_weight", 12.0))
- -    grad_clip = float(CONFIG.get("grad_clip", 5.0))
- -    energy_warmup_epochs = max(1, int(CONFIG.get("energy_warmup_epochs", 2)))
- +    energy_weight = float(CONFIG.get("energy_weight", 2.4))
- +    force_weight = float(CONFIG.get("force_weight", 10.0))
- +    grad_clip = float(CONFIG.get("grad_clip", 3.0))
- +    energy_warmup_epochs = max(1, int(CONFIG.get("energy_warmup_epochs", 3)))
- -        epoch_energy_weight = energy_weight * min(1.0, epoch / energy_warmup_epochs)
- -        epoch_force_weight = force_weight
- +        warmup_ratio = min(1.0, epoch / energy_warmup_epochs)
- +        epoch_energy_weight = energy_weight * (0.6 + 0.4 * warmup_ratio)
- +        epoch_force_weight = force_weight * (1.1 - 0.1 * warmup_ratio)

## Frontier tail
- generation_001/proposal_005 | family=None | phase=None | Q_rmd17=0.9441950186098212 | Q_iso17=1.816600428348992 | Q_total=1.249536912018531 | G_delta=1.26127117890054 | status=terminal_success
- generation_001/proposal_006 | family=None | phase=None | Q_rmd17=0.5641251237740994 | Q_iso17=1.8459469948983962 | Q_total=1.0127627786676032 | G_delta=1.0244970455496123 | status=terminal_success
- generation_001/proposal_007 | family=None | phase=None | Q_rmd17=0.6699802032157187 | Q_iso17=2.0316753558640994 | Q_total=1.146573506642652 | G_delta=1.158307773524661 | status=terminal_success
- generation_001/proposal_008 | family=None | phase=None | Q_rmd17=-0.011980764669461678 | Q_iso17=-0.17750563109147202 | Q_total=-0.0699144679171653 | G_delta=-0.05818020103515619 | status=terminal_success
- generation_002/proposal_003 | family=None | phase=None | Q_rmd17=nan | Q_iso17=nan | Q_total=nan | G_delta=nan | status=terminal_success
- generation_002/proposal_001 | family=None | phase=None | Q_rmd17=1.4495909204284498 | Q_iso17=2.0373939661592195 | Q_total=1.6553219864342192 | G_delta=0.1433946098885266 | status=terminal_success
- generation_002/proposal_002 | family=None | phase=None | Q_rmd17=1.2996950971893326 | Q_iso17=1.9635113068749632 | Q_total=1.5320307705793033 | G_delta=0.02010339403361061 | status=terminal_success
- generation_002/proposal_004 | family=None | phase=None | Q_rmd17=0.8602290393149097 | Q_iso17=2.4555837038519712 | Q_total=1.4186031719028813 | G_delta=-0.09332420464281133 | status=terminal_success
- generation_002/proposal_005 | family=None | phase=None | Q_rmd17=1.5755421719438902 | Q_iso17=1.9679936593168936 | Q_total=1.7129001925244414 | G_delta=0.20097281597874872 | status=terminal_success
- generation_002/proposal_006 | family=None | phase=None | Q_rmd17=1.422692779535817 | Q_iso17=1.87357451745786 | Q_total=1.580501387808532 | G_delta=0.06857401126283946 | status=terminal_success
- generation_002/proposal_007 | family=None | phase=None | Q_rmd17=1.8518629685065369 | Q_iso17=1.6614501263507095 | Q_total=1.7852184737519972 | G_delta=0.2732910972063045 | status=terminal_success
- generation_002/proposal_008 | family=None | phase=None | Q_rmd17=1.5178819115020574 | Q_iso17=1.8057862446298012 | Q_total=1.6186484280967677 | G_delta=0.10672105155107503 | status=terminal_success

## Evidence brief path
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260418T081500Z_generation004_proposal001_continuation_refresh.md

## Proposal writing rule
- proposal decisions must be benchmark-centric, not force-only
- discuss energy, force, gap_penalty, Q fields, train trends, runtime/failure, and control comparison when relevant

## Current model.py
```python
from __future__ import annotations

import math

import torch
from torch import nn


class BalancedInteractionBlock(nn.Module):
    def __init__(self, hidden_dim: int, num_rbf: int):
        super().__init__()
        self.hidden_dim = hidden_dim

        self.edge_mlp = nn.Sequential(
            nn.Linear(num_rbf, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim * 4),
        )

        self.src_scalar = nn.Linear(hidden_dim, hidden_dim)
        self.dst_scalar = nn.Linear(hidden_dim, hidden_dim)
        self.src_vector = nn.Linear(hidden_dim, hidden_dim)
        self.self_vector = nn.Linear(hidden_dim, hidden_dim)
        self.agg_vector = nn.Linear(hidden_dim, hidden_dim)

        self.scalar_update = nn.Sequential(
            nn.Linear(hidden_dim * 4, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        self.scalar_residual_gate = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        self.vector_gate = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim * 2),
            nn.SiLU(),
            nn.Linear(hidden_dim * 2, hidden_dim * 2),
        )
        self.layer_norm = nn.LayerNorm(hidden_dim)
        self.scalar_mix_norm = nn.LayerNorm(hidden_dim)
        self.vector_residual_scale = nn.Parameter(torch.tensor(0.35))

    def _apply_linear_to_vector(self, linear: nn.Linear, vector: torch.Tensor) -> torch.Tensor:
        return linear(vector.transpose(1, 2)).transpose(1, 2)

    def forward(
        self,
        scalar_state: torch.Tensor,
        vector_state: torch.Tensor,
        i_idx: torch.Tensor,
        j_idx: torch.Tensor,
        unit: torch.Tensor,
        edge_basis: torch.Tensor,
        cutoff_weight: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        edge_params = self.edge_mlp(edge_basis)
        scalar_gate, invariant_gate, vector_gate, direction_gate = edge_params.chunk(4, dim=-1)

        scalar_gate = scalar_gate * cutoff_weight.unsqueeze(-1)
        invariant_gate = invariant_gate * cutoff_weight.unsqueeze(-1)
        vector_gate = vector_gate * cutoff_weight.unsqueeze(-1)
        direction_gate = direction_gate * cutoff_weight.unsqueeze(-1)

        src_scalar = self.src_scalar(scalar_state[j_idx])
        dst_scalar = self.dst_scalar(scalar_state[i_idx])
        src_vector = self._apply_linear_to_vector(self.src_vector, vector_state[j_idx])

        directional_invariant = torch.sum(src_vector * unit.unsqueeze(1), dim=-1)
        scalar_message = (src_scalar + dst_scalar) * scalar_gate + directional_invariant * invariant_gate
        vector_message = src_vector * vector_gate.unsqueeze(-1) + direction_gate.unsqueeze(-1) * unit.unsqueeze(1)

        agg_scalar = torch.zeros_like(scalar_state)
        agg_vector = torch.zeros_like(vector_state)
        agg_scalar.index_add_(0, i_idx, scalar_message)
        agg_vector.index_add_(0, i_idx, vector_message)

        num_nodes = scalar_state.shape[0]
        neighbor_count = torch.zeros(num_nodes, device=scalar_state.device, dtype=scalar_state.dtype)
        neighbor_count.index_add_(0, i_idx, torch.ones_like(i_idx, dtype=scalar_state.dtype))
        neighbor_scale = neighbor_count.clamp_min(1.0).rsqrt().unsqueeze(-1)
        agg_scalar = agg_scalar * neighbor_scale
        agg_vector = agg_vector * neighbor_scale.unsqueeze(-1)

        self_vector = self._apply_linear_to_vector(self.self_vector, vector_state)
        mixed_agg_vector = self._apply_linear_to_vector(self.agg_vector, agg_vector)

        agg_norm = torch.linalg.norm(agg_vector, dim=-1)
        vector_alignment = torch.sum(self_vector * mixed_agg_vector, dim=-1)
        scalar_input = torch.cat([scalar_state, agg_scalar, agg_norm, vector_alignment], dim=-1)
        delta_scalar = self.scalar_update(scalar_input)
        scalar_gate = torch.sigmoid(self.scalar_residual_gate(torch.cat([scalar_state, agg_scalar], dim=-1)))
        mixed_scalar = scalar_state + scalar_gate * delta_scalar
        new_scalar = self.layer_norm(0.7 * mixed_scalar + 0.3 * self.scalar_mix_norm(scalar_state + agg_scalar))

        vector_mix = torch.tanh(self.vector_gate(torch.cat([new_scalar, agg_scalar], dim=-1)))
        self_mix, agg_mix = vector_mix.chunk(2, dim=-1)
        delta_vector = self_mix.unsqueeze(-1) * self_vector + agg_mix.unsqueeze(-1) * mixed_agg_vector
        residual_scale = 0.15 + 0.35 * torch.sigmoid(self.vector_residual_scale)
        new_vector = vector_state + residual_scale * delta_vector
        return new_scalar, new_vector


class EvolutionMLIP(nn.Module):
    def __init__(
        self,
        max_atomic_number: int = 100,
        hidden_dim: int = 96,
        num_rbf: int = 32,
        cutoff: float = 5.0,
        num_interactions: int = 2,
    ):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_rbf = num_rbf
        self.cutoff = cutoff

        self.embedding = nn.Embedding(max_atomic_number + 1, hidden_dim)
        self.atomref = nn.Embedding(max_atomic_number + 1, 1)

        centers = torch.linspace(0.0, cutoff, num_rbf)
        widths = torch.full((num_rbf,), (cutoff / max(num_rbf - 1, 1)) + 1e-6)
        self.register_buffer("rbf_centers", centers)
        self.register_buffer("rbf_widths", widths)

        self.interactions = nn.ModuleList(
            [BalancedInteractionBlock(hidden_dim=hidden_dim, num_rbf=num_rbf) for _ in range(num_interactions)]
        )
        self.readout = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, 1),
        )

    def _rbf(self, distances: torch.Tensor) -> torch.Tensor:
        diff = distances.unsqueeze(-1) - self.rbf_centers
        return torch.exp(-0.5 * (diff / self.rbf_widths) ** 2)

    def _cutoff_weight(self, distances: torch.Tensor) -> torch.Tensor:
        scaled = distances / max(self.cutoff, 1e-6)
        envelope = 0.5 * (torch.cos(math.pi * scaled.clamp(max=1.0)) + 1.0)
        return envelope * (distances < self.cutoff).to(distances.dtype)

    def _build_neighbor_list(self, positions: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        rij = positions[:, None, :] - positions[None, :, :]
        dij = torch.linalg.norm(rij, dim=-1)

        n_atoms = positions.shape[0]
        eye = torch.eye(n_atoms, device=positions.device, dtype=torch.bool)
        mask = (~eye) & (dij < self.cutoff)
        i_idx, j_idx = torch.where(mask)
        return i_idx, j_idx, rij[i_idx, j_idx]

    def forward_energy(self, numbers: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
        scalar_state = self.embedding(numbers)
        vector_state = torch.zeros(numbers.shape[0], self.hidden_dim, 3, device=positions.device, dtype=positions.dtype)
        atomref = self.atomref(numbers).sum()

        i_idx, j_idx, rij = self._build_neighbor_list(positions)
        if i_idx.numel() == 0:
            return atomref

        dij = torch.linalg.norm(rij, dim=-1)
        unit = rij / dij.unsqueeze(-1).clamp_min(1e-9)
        rbf = self._rbf(dij)
        cutoff_weight = self._cutoff_weight(dij)
        edge_basis = rbf * cutoff_weight.unsqueeze(-1)

        for interaction in self.interactions:
            scalar_state, vector_state = interaction(
                scalar_state=scalar_state,
                vector_state=vector_state,
                i_idx=i_idx,
                j_idx=j_idx,
                unit=unit,
                edge_basis=edge_basis,
                cutoff_weight=cutoff_weight,
            )

        vector_norm = torch.linalg.norm(vector_state, dim=-1)
        per_atom_energy = self.readout(torch.cat([scalar_state, vector_norm], dim=-1)).squeeze(-1)
        return atomref + per_atom_energy.sum()

    def forward(self, batch: dict) -> tuple[torch.Tensor, torch.Tensor]:
        positions = batch["positions"].clone().detach().requires_grad_(True)
        energy = self.forward_energy(batch["numbers"], positions)
        forces = -torch.autograd.grad(energy, positions, create_graph=True)[0]
        return energy, forces

```

## Current train.py
```python
from __future__ import annotations

import json
from pathlib import Path

import torch

from .dataloader import make_dataloader
from .model import EvolutionMLIP

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


def mae(values):
    vals = [abs(float(v)) for v in values]
    return sum(vals) / max(1, len(vals))


def energy_mae(pred, target):
    return abs(float(pred) - float(target))


def force_mae(pred, target):
    return float(torch.mean(torch.abs(pred - target)).detach().cpu().item())


def get_cuda_device() -> torch.device:
    if not torch.cuda.is_available():
        raise SystemExit("CUDA is required for benchmark runs, but no CUDA device is available.")
    return torch.device("cuda")


def sample_to_device(sample: dict, device: torch.device) -> dict:
    return {
        "numbers": sample["numbers"].to(device),
        "positions": sample["positions"].to(device),
        "energy": sample["energy"].to(device),
        "forces": sample["forces"].to(device),
    }


def run_epoch(
    model,
    loader,
    optimizer=None,
    energy_weight: float = 1.0,
    force_weight: float = 20.0,
    device: torch.device | None = None,
    grad_clip: float | None = None,
):
    if device is None:
        device = get_cuda_device()
    training = optimizer is not None
    energy_errors = []
    force_errors = []
    losses = []

    for batch in loader:
        batch_loss = 0.0
        batch_size = len(batch)
        if training:
            optimizer.zero_grad(set_to_none=True)

        for sample in batch:
            sample = sample_to_device(sample, device)
            pred_energy, pred_forces = model(sample)
            loss_energy = torch.abs(pred_energy - sample["energy"])
            loss_force = torch.mean(torch.abs(pred_forces - sample["forces"]))
            loss = energy_weight * loss_energy + force_weight * loss_force
            batch_loss = batch_loss + loss

            energy_errors.append(energy_mae(pred_energy.detach(), sample["energy"]))
            force_errors.append(force_mae(pred_forces.detach(), sample["forces"]))

        batch_loss = batch_loss / max(batch_size, 1)

        if training:
            batch_loss.backward()
            if grad_clip is not None and grad_clip > 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
            optimizer.step()

        losses.append(float(batch_loss.detach().cpu().item()))

    return {
        "loss": mae(losses),
        "energy_mae": mae(energy_errors),
        "force_mae": mae(force_errors),
    }


def train(
    *,
    dataset: str,
    train_dir: str | Path,
    val_dir: str | Path,
    output_dir: str | Path,
    epochs: int = 8,
    lr: float | None = None,
    batch_size: int = 8,
    max_samples: int | None = None,
):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    train_loader = make_dataloader(dataset, train_dir, batch_size=batch_size, shuffle=True, max_samples=max_samples)
    val_loader = make_dataloader(dataset, val_dir, batch_size=batch_size, shuffle=False, max_samples=max_samples)

    device = get_cuda_device()
    model = EvolutionMLIP(
        hidden_dim=int(CONFIG.get("hidden_dim", 96)),
        num_rbf=int(CONFIG.get("num_rbf", 32)),
        cutoff=float(CONFIG.get("cutoff", 5.0)),
    ).to(device)

    learning_rate = float(lr if lr is not None else CONFIG.get("learning_rate", 1e-3))
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=learning_rate,
        weight_decay=float(CONFIG.get("weight_decay", 1e-5)),
        betas=(0.9, float(CONFIG.get("adam_beta2", 0.97))),
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(epochs, 1))

    energy_weight = float(CONFIG.get("energy_weight", 2.4))
    force_weight = float(CONFIG.get("force_weight", 10.0))
    grad_clip = float(CONFIG.get("grad_clip", 3.0))
    energy_warmup_epochs = max(1, int(CONFIG.get("energy_warmup_epochs", 3)))

    history = []
    for epoch in range(1, epochs + 1):
        warmup_ratio = min(1.0, epoch / energy_warmup_epochs)
        epoch_energy_weight = energy_weight * (0.6 + 0.4 * warmup_ratio)
        epoch_force_weight = force_weight * (1.1 - 0.1 * warmup_ratio)

        model.train()
        train_metrics = run_epoch(
            model,
            train_loader,
            optimizer=optimizer,
            energy_weight=epoch_energy_weight,
            force_weight=epoch_force_weight,
            device=device,
            grad_clip=grad_clip,
        )

        model.eval()
        with torch.enable_grad():
            val_metrics = run_epoch(
                model,
                val_loader,
                optimizer=None,
                energy_weight=epoch_energy_weight,
                force_weight=epoch_force_weight,
                device=device,
                grad_clip=None,
            )

        scheduler.step()

        row = {
            "epoch": epoch,
            "train": train_metrics,
            "val": val_metrics,
            "device": str(device),
            "learning_rate": float(optimizer.param_groups[0]["lr"]),
            "energy_weight": epoch_energy_weight,
            "force_weight": epoch_force_weight,
            "grad_clip": grad_clip,
        }
        history.append(row)

    torch.save(model.state_dict(), output_dir / "model.pt")
    (output_dir / "train_history.json").write_text(json.dumps(history, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "model_path": str(output_dir / "model.pt"),
        "history_path": str(output_dir / "train_history.json"),
        "last_epoch": history[-1],
    }

```
