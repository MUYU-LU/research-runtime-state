# MLIP Evidence Brief

## Question

For the next MLIP round starting from the current remote-derived base_unit under the fixed benchmark contract, what evidence-backed exploit angles and next-phase jump angles are justified now?

## Mode

balanced

## Source Unit

base_unit at `/home/lmy/.openclaw/workspace/research_runtime/base_unit`

## Current Capability Profile

```json
{
  "phase_guess": "relative geometry pair model",
  "present": [
    "atom embedding",
    "pairwise distance RBFs",
    "cutoff-local pair scoring",
    "atomref baseline",
    "forces from autograd",
    "benchmark-aligned train/eval loop for rMD17 and ISO17"
  ],
  "missing": [
    "neighbor message passing",
    "angular/triplet structure",
    "equivariance",
    "periodic/cell handling",
    "long-range head",
    "uncertainty or test-time adaptation"
  ],
  "verified_notes": [
    "model.py sums pair energies from [emb_i, emb_j, rbf(d_ij)] under a hard cutoff.",
    "No directional features or graph updates are present.",
    "train.py keeps a simple energy-plus-force L1 objective.",
    "eval.py is tightly aligned to rMD17 and ISO17 anchored benchmark reporting."
  ]
}
```

## Strong Papers

### 1) Verified local paper evidence
- **NequIP high-performance paper**  
  Local PDF verified: `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP等变训练 - NequIP高性能训练推理深度等变原子间势.pdf`  
  Extraction succeeded. Confirms deep equivariant MLIPs improve data efficiency and generalization, and that practical implementations center on interaction layers, spherical harmonics, tensor products, and compiled train/inference.

### 2) Verified local paper evidence
- **MACE-MP foundation model paper**  
  Local PDF verified: `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP基础模型 - MACE-MP原子材料化学基础模型.pdf`  
  Extraction succeeded. Confirms higher-order equivariant message passing and ACE-style body-order structure as the key leap beyond simpler local models, with stable MD and fine-tuning value.

### 3) Verified local paper evidence
- **LES long-range paper**  
  Local PDF verified: `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP长程相互作用 - 从能量和力学习电荷与长程作用.pdf`  
  Extraction succeeded. Confirms latent-charge long-range augmentation can improve electrostatic/charged systems and can wrap short-range MLIPs, but this is not the most immediate gap for the current benchmark.

### 4) Verified local paper evidence
- **TAIP test-time adaptation paper**  
  Local PDF verified: `/mnt/c/Users/1/Desktop/文献/MLIP/MLIP泛化 - TAIP在线测试时适应分布外数据.pdf`  
  Extraction succeeded. Reports strong gains on MD17 and ISO17-style OOD settings through self-supervised test-time adaptation, but requires a much richer encoder/adaptation setup than the current base_unit has.

## Strong Repos

### Verified repo evidence
- **NequIP**: `https://github.com/mir-group/nequip`  
  Verified by reading `README.md`, `nequip/model/nequip_models.py`, `nequip/nn/interaction_block.py`.  
  Confirms E(3)-equivariant GNN design with spherical harmonic edge attrs, radial embeddings, interaction layers, tensor-product message passing, and autograd forces.

- **MACE**: `https://github.com/ACEsuit/mace`  
  Verified by reading `README.md`, `mace/modules/models.py`, `mace/modules/blocks.py`, `mace/modules/radial.py`.  
  Confirms higher-order equivariant message passing, ACE/product-basis structure, radial embedding blocks, and foundation/fine-tuning workflows.

- **CACE**: `https://github.com/BingqingCheng/cace`  
  Verified by reading `README.md`, `cace/modules/les_wrapper.py`, `cace/modules/ewald.py`, `cace/modules/interaction.py`.  
  Confirms Cartesian atomic cluster expansion, message passing, and optional LES/Ewald long-range modules.

### Not verified in this run
- TAIP repository details were **not** verified. Only the TAIP paper itself was verified.

## Exploit Angles

```json
[
  {
    "angle": "Add lightweight local neighbor message passing while keeping scalar outputs and autograd force supervision.",
    "why_now": "This is the smallest justified structural fix to the current pair-only model, and it is strongly supported by verified NequIP/MACE paper plus repo evidence.",
    "confidence": "medium_high"
  },
  {
    "angle": "Add angular or triplet structure on top of current distance features before attempting full equivariance.",
    "why_now": "The sharpest current capability gap is missing directional chemistry/body-order information; verified MACE and CACE evidence supports this.",
    "confidence": "medium_high"
  },
  {
    "angle": "Upgrade local interaction parameterization rather than only tuning optimizer or loss weights.",
    "why_now": "Evidence points to architectural locality/body-order changes as the justified exploit lever, not shallow hyperparameter search.",
    "confidence": "medium"
  }
]
```

## Jump Angles

```json
[
  {
    "angle": "Minimal E(3)-equivariant local model in the NequIP/MACE family.",
    "why_now": "Verified local papers and repos consistently identify equivariant interaction layers as the next major phase jump beyond pairwise invariant models.",
    "confidence": "medium"
  },
  {
    "angle": "CACE-style higher-body Cartesian expansion as a bridge jump.",
    "why_now": "Verified repo evidence suggests a potentially more incremental route to body-order structure than a full irreps-heavy stack.",
    "confidence": "medium"
  },
  {
    "angle": "Keep LES-style long-range latent-charge augmentation for a later branch, not the default next round.",
    "why_now": "Verified paper evidence is strong, but it looks less aligned to the dominant current benchmark gap than missing local geometry structure.",
    "confidence": "medium"
  },
  {
    "angle": "Treat TAIP-style test-time adaptation as a research branch rather than the main next-round candidate.",
    "why_now": "The verified paper is benchmark-relevant, but implementation fit to the current minimalist base_unit is poor.",
    "confidence": "medium"
  }
]
```

## Implementation Fit

```json
{
  "best_near_term": [
    "scalar neighbor message passing",
    "angular/triplet augmentation",
    "richer local interaction/readout under same benchmark contract"
  ],
  "best_next_phase": [
    "minimal NequIP/MACE-like equivariant model",
    "CACE-style higher-body expansion"
  ],
  "poorer_fit_for_immediate_round": [
    "long-range LES augmentation",
    "TAIP-style test-time adaptation"
  ]
}
```

## Risks Or Mismatches

```json
[
  "frontier.jsonl was missing in this run, so no fresh frontier-outcome linkage was available",
  "TAIP repo evidence is not verified in this run",
  "long-range evidence is real but likely not the first-order bottleneck for rMD17/ISO17 from this base_unit",
  "full foundation-model complexity should not be mistaken for immediate round implementation fit"
]
```

## Followup Queries

```json
[
  "Find smallest public angular/triplet MLIPs that beat pairwise baselines on MD17/ISO17 without full equivariance",
  "Inspect whether any fresh frontier record later appears that confirms directionality/OOD as the actual failure mode",
  "If desired, verify a TAIP code repo specifically before recommending an adaptation branch"
]
```

## Confidence

```json
{
  "current_code_profile": "high",
  "verified_local_paper_evidence": "medium_high",
  "verified_repo_evidence": "medium_high",
  "strongest_exploit_direction": "lightweight message passing plus angular/body-order augmentation",
  "strongest_jump_direction": "minimal equivariant local model",
  "overall": "medium_high"
}
```