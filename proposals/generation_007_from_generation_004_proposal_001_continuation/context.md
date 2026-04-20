# Proposal context for generation_004/proposal_001

## Current unit
- unit: generation_004/proposal_001
- source unit: generation_003/proposal_004

## Active evidence
- path: /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260419T1957_generation007_proposal001_continuation.md
- source unit: generation_004/proposal_001
- mode: balanced

```markdown
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
  "unit_summary": {
    "unit": "generation_004/proposal_001",
    "unit_meta": {
      "source_unit": "generation_003/proposal_004",
      "generation_round": "generation_004",
      "proposal_unit": "proposal_001",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md",
      "control_replicate": false
    },
    "proposal_metadata": {
      "family": null,
      "phase": null,
      "jump_type": null,
      "budget_class": null,
      "expected_capability_gain": [],
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md",
      "control_replicate": false
    },
    "runtime_summary": {
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": "unknown_failure"
    },
    "datasets": {
      "rmd17": {
        "metrics_path": "generations/generation_004/proposal_001/outputs/rmd17/benchmark_metrics.json",
        "history_path": "generations/generation_004/proposal_001/outputs/rmd17/train_history.json",
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
          "best_val_energy_mae": 0.5929732666015625,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 3.0291108938796594
      },
      "iso17": {
        "metrics_path": "generations/generation_004/proposal_001/outputs/iso17/benchmark_metrics.json",
        "history_path": "generations/generation_004/proposal_001/outputs/iso17/train_history.json",
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
          "best_val_energy_mae": 1.0377604166666667,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 3.32668622930551
      }
    },
    "Q_rmd17": 3.0291108938796594,
    "Q_iso17": 3.32668622930551,
    "Q_total": 3.1332622612787073,
    "G_delta": 0.26449992779357956,
    "generation_summary": "ledger/generation_004_summary.json",
    "frontier_record": "ledger/frontier.jsonl"
  }
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
  "unit_summary": {
    "unit": "generation_003/proposal_004",
    "unit_meta": {
      "source_unit": "generation_002/proposal_005",
      "generation_round": "generation_003",
      "proposal_unit": "proposal_004",
      "proposal_file": "04_jump_nequip_style_recalibrated_refactor.md",
      "control_replicate": false
    },
    "proposal_metadata": {
      "family": null,
      "phase": null,
      "jump_type": null,
      "budget_class": null,
      "expected_capability_gain": [],
      "proposal_file": "04_jump_nequip_style_recalibrated_refactor.md",
      "control_replicate": false
    },
    "runtime_summary": {
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null
    },
    "datasets": {
      "rmd17": {
        "metrics_path": "generations/generation_003/proposal_004/outputs/rmd17/benchmark_metrics.json",
        "history_path": "generations/generation_003/proposal_004/outputs/rmd17/train_history.json",
        "metrics": {
          "mild_ood_energy_mae": 2.2845567626953125,
          "mild_ood_force_mae": 0.10615500151272864,
          "hard_ood_energy_mae": 2.28490185546875,
          "hard_ood_force_mae": 0.10682270545721985,
          "mixed_force_mae": 0.10655562387942336,
          "mixed_energy_mae": 2.2847638183593753,
          "gap_penalty": 0.006266247807253327,
          "Q_dataset": 2.6795083100762995,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 3.974056053943932,
              "energy_mae": 1.8268427124023439,
              "force_mae": 0.10736066733044572
            },
            "val": {
              "loss": 4.4076569082736965,
              "energy_mae": 2.2845567626953125,
              "force_mae": 0.10615500762383454
            },
            "device": "cuda",
            "learning_rate": 0.0,
            "energy_weight": 1.0,
            "force_weight": 20.0,
            "grad_clip": 5.0
          },
          "best_val_force_mae": 0.10615500762383454,
          "best_val_energy_mae": 1.4970237426757813,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 2.6795083100762995
      },
      "iso17": {
        "metrics_path": "generations/generation_003/proposal_004/outputs/iso17/benchmark_metrics.json",
        "history_path": "generations/generation_003/proposal_004/outputs/iso17/train_history.json",
        "metrics": {
          "within_energy_mae": 1.6992206837871286,
          "within_force_mae": 0.1626173206374492,
          "other_energy_mae": 1.5159589092548076,
          "other_force_mae": 0.17375626559440907,
          "mixed_force_mae": 0.16930068761162512,
          "mixed_energy_mae": 1.589263619067736,
          "gap_penalty": 0.06579385538260052,
          "Q_dataset": 3.22023409124438,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 5.9520263052075215,
              "energy_mae": 2.6536815681079826,
              "force_mae": 0.16491723685055085
            },
            "val": {
              "loss": 3.3838011423746743,
              "energy_mae": 0.24772135416666666,
              "force_mae": 0.15680398543675741
            },
            "device": "cuda",
            "learning_rate": 0.0,
            "energy_weight": 1.0,
            "force_weight": 20.0,
            "grad_clip": 5.0
          },
          "best_val_force_mae": 0.15680398543675741,
          "best_val_energy_mae": 0.24772135416666666,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 3.22023409124438
      }
    },
    "Q_rmd17": 2.6795083100762995,
    "Q_iso17": 3.22023409124438,
    "Q_total": 2.8687623334851278,
    "G_delta": 1.1558621409606864,
    "generation_summary": "ledger/generation_003_summary.json",
    "frontier_record": "ledger/frontier.jsonl"
  }
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

## Generation summary
```json
{
  "generation": "generation_004",
  "created_at_utc": "2026-04-18T12:30:20.867464+00:00",
  "units": [
    {
      "unit": "generation_004/proposal_001",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_001.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": "unknown_failure",
      "Q_rmd17": 3.0291108938796594,
      "Q_iso17": 3.32668622930551,
      "Q_total": 3.1332622612787073,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 0.5929720458984375,
      "rmd17_mild_ood_force_mae": 0.10458182134397793,
      "rmd17_hard_ood_energy_mae": 0.5925932006835938,
      "rmd17_hard_ood_force_mae": 0.10503137192176655,
      "rmd17_mixed_force_mae": 0.1048515516906511,
      "rmd17_mixed_energy_mae": 0.5927447387695313,
      "rmd17_gap_penalty": 0.004287495707365973,
      "rmd17_Q_dataset": 3.0291108938796594,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.10458181903103832,
      "rmd17_best_val_energy_mae": 0.5929732666015625,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 0.7550254293007426,
      "iso17_within_force_mae": 0.1811587671813841,
      "iso17_other_energy_mae": 0.7963562950721154,
      "iso17_other_force_mae": 0.19032591961324216,
      "iso17_mixed_force_mae": 0.18665905864049892,
      "iso17_mixed_energy_mae": 0.7798239487635663,
      "iso17_gap_penalty": 0.04911174683177137,
      "iso17_Q_dataset": 3.32668622930551,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.15994398792584738,
      "iso17_best_val_energy_mae": 1.0377604166666667
    },
    {
      "unit": "generation_004/proposal_002",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_002.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.9728719438179514,
      "Q_iso17": 3.3666897160680302,
      "Q_total": 3.110708164105479,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 0.5796865844726562,
      "rmd17_mild_ood_force_mae": 0.11346382295736111,
      "rmd17_hard_ood_energy_mae": 0.5807351684570312,
      "rmd17_hard_ood_force_mae": 0.1140345740816556,
      "rmd17_mixed_force_mae": 0.11380627363193781,
      "rmd17_mixed_energy_mae": 0.5803157348632813,
      "rmd17_gap_penalty": 0.005015111259466622,
      "rmd17_Q_dataset": 2.9728719438179514,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.11346382210240699,
      "rmd17_best_val_energy_mae": 0.579689208984375,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 0.650325359684406,
      "iso17_within_force_mae": 0.17873083827740485,
      "iso17_other_energy_mae": 0.6927433894230769,
      "iso17_other_force_mae": 0.18977487115046152,
      "iso17_mixed_force_mae": 0.18535725800123884,
      "iso17_mixed_energy_mae": 0.6757761775276085,
      "iso17_gap_penalty": 0.05958241393991309,
      "iso17_Q_dataset": 3.3666897160680302,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.15553108851114908,
      "iso17_best_val_energy_mae": 0.771484375
    },
    {
      "unit": "generation_004/proposal_003",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_003.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.91278187287435,
      "Q_iso17": 3.3500470650609744,
      "Q_total": 3.065824690139668,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 1.5685512084960938,
      "rmd17_mild_ood_force_mae": 0.08815841447329148,
      "rmd17_hard_ood_energy_mae": 1.5686265258789063,
      "rmd17_hard_ood_force_mae": 0.08872427424951457,
      "rmd17_mixed_force_mae": 0.08849793033902534,
      "rmd17_mixed_energy_mae": 1.5685963989257812,
      "rmd17_gap_penalty": 0.006394045307601548,
      "rmd17_Q_dataset": 2.91278187287435,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.08815835198748391,
      "rmd17_best_val_energy_mae": 1.5685526123046876,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 0.7745948715965346,
      "iso17_within_force_mae": 0.16707400126327382,
      "iso17_other_energy_mae": 0.8995567908653846,
      "iso17_other_force_mae": 0.18059184630043232,
      "iso17_mixed_force_mae": 0.17518470828556892,
      "iso17_mixed_energy_mae": 0.8495720231578445,
      "iso17_gap_penalty": 0.07716338468906699,
      "iso17_Q_dataset": 3.3500470650609744,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.1483928163846334,
      "iso17_best_val_energy_mae": 1.9970703125
    },
    {
      "unit": "generation_004/proposal_004",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_004.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.7935780322122152,
      "Q_iso17": 3.1721084802597064,
      "Q_total": 2.926063689028837,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 1.5460761108398438,
      "rmd17_mild_ood_force_mae": 0.1041935924035497,
      "rmd17_hard_ood_energy_mae": 1.5454930419921875,
      "rmd17_hard_ood_force_mae": 0.10439481916511431,
      "rmd17_mixed_force_mae": 0.10431432846048846,
      "rmd17_mixed_energy_mae": 1.54572626953125,
      "rmd17_gap_penalty": 0.0019290423907479411,
      "rmd17_Q_dataset": 2.7935780322122152,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.10419358538102824,
      "rmd17_best_val_energy_mae": 1.5460751342773438,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 2.1062002049814357,
      "iso17_within_force_mae": 0.15504878737622557,
      "iso17_other_energy_mae": 2.02951171875,
      "iso17_other_force_mae": 0.17135219249587794,
      "iso17_mixed_force_mae": 0.164830830448017,
      "iso17_mixed_energy_mae": 2.060187113242574,
      "iso17_gap_penalty": 0.09890992525633782,
      "iso17_Q_dataset": 3.1721084802597064,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.1616599460442861,
      "iso17_best_val_energy_mae": 1.9599609375
    },
    {
      "unit": "generation_004/proposal_006",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_006.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.7891460794531704,
      "Q_iso17": 3.19258956279737,
      "Q_total": 2.9303512986236404,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 0.7956778564453125,
      "rmd17_mild_ood_force_mae": 0.1304198621364776,
      "rmd17_hard_ood_energy_mae": 0.7945776977539063,
      "rmd17_hard_ood_force_mae": 0.13121199369966052,
      "rmd17_mixed_force_mae": 0.13089514107438735,
      "rmd17_mixed_energy_mae": 0.7950177612304687,
      "rmd17_gap_penalty": 0.006051649867787686,
      "rmd17_Q_dataset": 2.7891460794531704,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.13041987771121785,
      "rmd17_best_val_energy_mae": 0.7956788330078125,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 0.615505588644802,
      "iso17_within_force_mae": 0.23030208365456892,
      "iso17_other_energy_mae": 0.7170564152644231,
      "iso17_other_force_mae": 0.2374924047004718,
      "iso17_mixed_force_mae": 0.23461627628211068,
      "iso17_mixed_energy_mae": 0.6764360846165747,
      "iso17_gap_penalty": 0.030647153555648267,
      "iso17_Q_dataset": 3.19258956279737,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.17855258782704672,
      "iso17_best_val_energy_mae": 0.84765625
    },
    {
      "unit": "generation_004/proposal_007",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_007.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.643650904041294,
      "Q_iso17": 2.992901620987732,
      "Q_total": 2.765888654972547,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 2.9046622314453123,
      "rmd17_mild_ood_force_mae": 0.10228787045367062,
      "rmd17_hard_ood_energy_mae": 2.9042823486328126,
      "rmd17_hard_ood_force_mae": 0.10362321079778485,
      "rmd17_mixed_force_mae": 0.10308907466013915,
      "rmd17_mixed_energy_mae": 2.9044343017578127,
      "rmd17_gap_penalty": 0.012953267341894207,
      "rmd17_Q_dataset": 2.643650904041294,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.10228787088301033,
      "rmd17_best_val_energy_mae": 2.771561950683594,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 4.733235999381188,
      "iso17_within_force_mae": 0.14789471405715046,
      "iso17_other_energy_mae": 4.754584585336539,
      "iso17_other_force_mae": 0.16518870505862512,
      "iso17_mixed_force_mae": 0.15827110865803526,
      "iso17_mixed_energy_mae": 4.746045150954399,
      "iso17_gap_penalty": 0.10926814848268517,
      "iso17_Q_dataset": 2.992901620987732,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.16258423030376434,
      "iso17_best_val_energy_mae": 0.6845703125
    },
    {
      "unit": "generation_004/proposal_009",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_009.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 2.9469981144853343,
      "Q_iso17": 3.1930018040184973,
      "Q_total": 3.0330994058219414,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 0.8238478393554688,
      "rmd17_mild_ood_force_mae": 0.10441879377444274,
      "rmd17_hard_ood_energy_mae": 0.8239492797851562,
      "rmd17_hard_ood_force_mae": 0.10505035342252814,
      "rmd17_mixed_force_mae": 0.10479772956329397,
      "rmd17_mixed_energy_mae": 0.8239087036132813,
      "rmd17_gap_penalty": 0.00602646307998428,
      "rmd17_Q_dataset": 2.9469981144853343,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.10441878858709243,
      "rmd17_best_val_energy_mae": 0.823847412109375,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 1.4352606745049505,
      "iso17_within_force_mae": 0.17065073818632281,
      "iso17_other_energy_mae": 1.5959761868990385,
      "iso17_other_force_mae": 0.18243517211996593,
      "iso17_mixed_force_mae": 0.1777213985465087,
      "iso17_mixed_energy_mae": 1.5316899819414034,
      "iso17_gap_penalty": 0.06630846949188782,
      "iso17_Q_dataset": 3.1930018040184973,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.16228397687276205,
      "iso17_best_val_energy_mae": 2.6100260416666665
    },
    {
      "unit": "generation_004/proposal_010",
      "proposal_file": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_003_proposal_004_continuation/proposal_010.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 1,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 1.3983855053348244,
      "Q_iso17": 2.4214479029721154,
      "Q_total": 1.7564573445078762,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 70.2859429321289,
      "rmd17_mild_ood_force_mae": 0.1873397207027301,
      "rmd17_hard_ood_energy_mae": 70.28322552490235,
      "rmd17_hard_ood_force_mae": 0.18801690035872162,
      "rmd17_mixed_force_mae": 0.18774602849632502,
      "rmd17_mixed_energy_mae": 70.28431248779296,
      "rmd17_gap_penalty": 0.003606892041400276,
      "rmd17_Q_dataset": 1.3983855053348244,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.1788369550886564,
      "rmd17_best_val_energy_mae": 6.002201232910156,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 29.370098333075497,
      "iso17_within_force_mae": 0.1791941095918122,
      "iso17_other_energy_mae": 29.509729191706732,
      "iso17_other_force_mae": 0.1901377670925397,
      "iso17_mixed_force_mae": 0.1857603040922487,
      "iso17_mixed_energy_mae": 29.45387684825424,
      "iso17_gap_penalty": 0.058912788467626376,
      "iso17_Q_dataset": 2.4214479029721154,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "worsening",
      "iso17_best_val_force_mae": 0.17838659385840097,
      "iso17_best_val_energy_mae": 25.415364583333332
    }
  ],
  "best_control_Q_total": null
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
- generation_005/proposal_006 | family=None | phase=None | Q_rmd17=2.189522058478086 | Q_iso17=2.7493034470410787 | Q_total=2.3854455444751337 | G_delta=-0.7478167168035736 | status=terminal_success
- generation_005/proposal_007 | family=None | phase=None | Q_rmd17=1.2203477119216792 | Q_iso17=2.4803267557895508 | Q_total=1.6613403772754343 | G_delta=-1.471921884003273 | status=terminal_success
- generation_005/proposal_008 | family=None | phase=None | Q_rmd17=2.331278488695947 | Q_iso17=2.8662515100948727 | Q_total=2.518519046185571 | G_delta=-0.6147432150931365 | status=terminal_success
- generation_005/proposal_004 | family=None | phase=None | Q_rmd17=1.792177270947261 | Q_iso17=2.5753946019130107 | Q_total=2.0663033367852734 | G_delta=-1.0669589244934339 | status=terminal_success
- generation_006/proposal_001 | family=None | phase=None | Q_rmd17=2.318753532542099 | Q_iso17=3.030797882286558 | Q_total=2.56796905495266 | G_delta=-0.5652932063260474 | status=terminal_success
- generation_006/proposal_002 | family=None | phase=None | Q_rmd17=1.9960032698275807 | Q_iso17=2.834550993916821 | Q_total=2.289494973258815 | G_delta=-0.8437672880198925 | status=terminal_success
- generation_006/proposal_003 | family=None | phase=None | Q_rmd17=2.1687006012186143 | Q_iso17=2.778500734797781 | Q_total=2.382130647971323 | G_delta=-0.7511316133073844 | status=terminal_success
- generation_006/proposal_004 | family=None | phase=None | Q_rmd17=1.7172865808417943 | Q_iso17=2.797510387848854 | Q_total=2.095364913294265 | G_delta=-1.0378973479844422 | status=terminal_success
- generation_006/proposal_005 | family=None | phase=None | Q_rmd17=1.7796526548610756 | Q_iso17=2.904218666582249 | Q_total=2.173250758963486 | G_delta=-0.9600115023152211 | status=terminal_success
- generation_006/proposal_008 | family=None | phase=None | Q_rmd17=2.5163806336477292 | Q_iso17=3.0028870650654294 | Q_total=2.686657884643924 | G_delta=-0.44660437663478314 | status=terminal_success
- generation_006/proposal_009 | family=None | phase=None | Q_rmd17=2.241712151744082 | Q_iso17=2.7666154812709722 | Q_total=2.4254283170784934 | G_delta=-0.707833944200214 | status=terminal_success
- generation_006/proposal_006 | family=None | phase=None | Q_rmd17=1.4053262855259885 | Q_iso17=2.7528597358284563 | Q_total=1.876962993131852 | G_delta=-1.2562992681468552 | status=terminal_success

## Evidence brief path
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260419T1957_generation007_proposal001_continuation.md

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
