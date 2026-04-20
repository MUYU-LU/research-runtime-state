# Proposal context for generation_004/proposal_001

## Current unit
- unit: generation_004/proposal_001
- source unit: generation_003/proposal_004

## Active evidence
- path: /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260419T2020Z_generation008_proposal001_continuation.md
- source unit: generation_004/proposal_001
- mode: balanced

```markdown
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
- generation_006/proposal_005 | family=None | phase=None | Q_rmd17=1.7796526548610756 | Q_iso17=2.904218666582249 | Q_total=2.173250758963486 | G_delta=-0.9600115023152211 | status=terminal_success
- generation_006/proposal_008 | family=None | phase=None | Q_rmd17=2.5163806336477292 | Q_iso17=3.0028870650654294 | Q_total=2.686657884643924 | G_delta=-0.44660437663478314 | status=terminal_success
- generation_006/proposal_009 | family=None | phase=None | Q_rmd17=2.241712151744082 | Q_iso17=2.7666154812709722 | Q_total=2.4254283170784934 | G_delta=-0.707833944200214 | status=terminal_success
- generation_006/proposal_006 | family=None | phase=None | Q_rmd17=1.4053262855259885 | Q_iso17=2.7528597358284563 | Q_total=1.876962993131852 | G_delta=-1.2562992681468552 | status=terminal_success
- generation_007/proposal_007 | family=None | phase=None | Q_rmd17=1.697669884139405 | Q_iso17=2.736641760425823 | Q_total=2.061310040839651 | G_delta=-1.0719522204390564 | status=terminal_success
- generation_007/proposal_002 | family=None | phase=None | Q_rmd17=2.3392492016676045 | Q_iso17=2.6737364342719703 | Q_total=2.456319733079132 | G_delta=-0.6769425281995751 | status=terminal_success
- generation_007/proposal_001 | family=None | phase=None | Q_rmd17=2.4636176274882366 | Q_iso17=3.039575705698899 | Q_total=2.6652029548619685 | G_delta=-0.4680593064167389 | status=terminal_success
- generation_007/proposal_004 | family=None | phase=None | Q_rmd17=2.7536850677446942 | Q_iso17=2.730948435297518 | Q_total=2.7457272463881828 | G_delta=-0.38753501489052455 | status=terminal_success
- generation_007/proposal_005 | family=None | phase=None | Q_rmd17=1.4897931255458434 | Q_iso17=2.7851130183693558 | Q_total=1.9431550880340727 | G_delta=-1.1901071732446347 | status=terminal_success
- generation_007/proposal_006 | family=None | phase=None | Q_rmd17=2.5588683862168615 | Q_iso17=2.8867518904216536 | Q_total=2.6736276126885388 | G_delta=-0.45963464859016856 | status=terminal_success
- generation_007/proposal_008 | family=None | phase=None | Q_rmd17=2.201867102394039 | Q_iso17=2.529855613775236 | Q_total=2.316663081377458 | G_delta=-0.8165991799012495 | status=terminal_success
- generation_007/proposal_009 | family=None | phase=None | Q_rmd17=0.879962316300981 | Q_iso17=0.9988255043781936 | Q_total=0.9215644321280054 | G_delta=-2.211697829150702 | status=terminal_success

## Evidence brief path
- /home/lmy/.openclaw/workspace/research_runtime/knowledge/briefs/evidence_brief_20260419T2020Z_generation008_proposal001_continuation.md

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
