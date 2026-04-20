# Proposal context for generation_003/proposal_004

## Current unit
- unit: generation_003/proposal_004
- source unit: generation_002/proposal_005

## Current runtime summary
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

## Source runtime summary
```json
{
  "implementation_status": {
    "implementation_state": "launch_ready",
    "source_unit": "generation_001/proposal_004",
    "proposal_file": "06_jump_multi_stage_low_rank_equivariant_mix.md",
    "control_replicate": false,
    "changed_files": [
      {
        "path": "model/model.py",
        "sha256": "05d954b468e27920503e2fab6e039925b2c31829c33516158fcd53ce2e4a08af"
      },
      {
        "path": "model/train.py",
        "sha256": "98bbc0d295ed9abe2ae86ebe718f55e1e6a7fa610b359bf4bbac9c13f6facb4a"
      }
    ],
    "repair_attempts": 0,
    "same_failure_class_repairs": 0,
    "last_failure_class": "unknown_failure",
    "remote_synced": true,
    "remote_smoke_passed": true,
    "remote_path": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_002/proposal_005",
    "smoke_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_002/proposal_005/outputs/smoke_rmd17.log",
    "smoke_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_002/proposal_005/outputs/smoke_rmd17.log",
    "last_actor": "remote_collect_unit.py",
    "last_updated_utc": "2026-04-17T07:27:00.189352+00:00",
    "notes": [
      "Implemented 2-stage low-rank equivariant mix stack via LowRankEquivariantStage blocks.",
      "Added low-rank scalar/vector mixing per edge with learned rank-space projections and radial gating while preserving scalar total-energy, local cutoff graph, and force-from-autograd contract.",
      "Local import/forward sanity check was attempted by subagent but did not run in that session because torch was unavailable there."
    ]
  },
  "run_status": {
    "run_state": "terminal_success",
    "launch_count": 2,
    "retry_count": 0,
    "pid": "2769384",
    "host": "210.45.70.177",
    "launch_log_local": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_002/proposal_005/outputs/launch.log",
    "launch_log_remote": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_002/proposal_005/outputs/launch.log",
    "failure_class": null,
    "launched_at_utc": "2026-04-17T07:30:20.410958Z",
    "finished_at_utc": "2026-04-17T10:05:01.218968+00:00",
    "last_actor": "remote_collect_unit.py",
    "last_state_change_utc": "2026-04-17T10:05:01.219013+00:00"
  },
  "unit_summary": {
    "unit": "generation_002/proposal_005",
    "unit_meta": {
      "source_unit": "generation_001/proposal_004",
      "generation_round": "generation_002",
      "proposal_unit": "proposal_005",
      "proposal_file": "06_jump_multi_stage_low_rank_equivariant_mix.md",
      "control_replicate": false
    },
    "proposal_metadata": {
      "family": null,
      "phase": null,
      "jump_type": null,
      "budget_class": null,
      "expected_capability_gain": [],
      "proposal_file": "06_jump_multi_stage_low_rank_equivariant_mix.md",
      "control_replicate": false
    },
    "runtime_summary": {
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 2,
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
        "metrics_path": "generations/generation_002/proposal_005/outputs/rmd17/benchmark_metrics.json",
        "history_path": "generations/generation_002/proposal_005/outputs/rmd17/train_history.json",
        "metrics": {
          "mild_ood_energy_mae": 24.4689345703125,
          "mild_ood_force_mae": 0.2108615520070307,
          "hard_ood_energy_mae": 24.47663366699219,
          "hard_ood_force_mae": 0.2107955724238418,
          "mixed_force_mae": 0.21082196425711736,
          "mixed_energy_mae": 24.473554028320315,
          "gap_penalty": 0.0,
          "Q_dataset": 1.5755421719438902,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 92.49480907683075,
              "energy_mae": 88.05652728271484,
              "force_mae": 0.2219140895274468
            },
            "val": {
              "loss": 28.686161748409273,
              "energy_mae": 24.468930725097657,
              "force_mae": 0.2108615515572019
            },
            "device": "cuda",
            "energy_weight": 1.0,
            "force_weight": 20.0
          },
          "best_val_force_mae": 0.2108615515572019,
          "best_val_energy_mae": 6.631689086914062,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 1.5755421719438902
      },
      "iso17": {
        "metrics_path": "generations/generation_002/proposal_005/outputs/iso17/benchmark_metrics.json",
        "history_path": "generations/generation_002/proposal_005/outputs/iso17/train_history.json",
        "metrics": {
          "within_energy_mae": 69.02865969214109,
          "within_force_mae": 0.25652010944662706,
          "other_energy_mae": 68.78793043870192,
          "other_force_mae": 0.25880236335671863,
          "mixed_force_mae": 0.257889461792682,
          "mixed_energy_mae": 68.88422214007758,
          "gap_penalty": 0.008896978544902463,
          "Q_dataset": 1.9679936593168936,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 80.11548589887005,
              "energy_mae": 73.97539183361695,
              "force_mae": 0.30700470456798185
            },
            "val": {
              "loss": 72.69505055745442,
              "energy_mae": 67.98209635416667,
              "force_mae": 0.2356476734081904
            },
            "device": "cuda",
            "energy_weight": 1.0,
            "force_weight": 20.0
          },
          "best_val_force_mae": 0.2345629334449768,
          "best_val_energy_mae": 7.027669270833333,
          "force_trend": "improving",
          "energy_trend": "worsening"
        },
        "Q_dataset": 1.9679936593168936
      }
    },
    "Q_rmd17": 1.5755421719438902,
    "Q_iso17": 1.9679936593168936,
    "Q_total": 1.7129001925244414,
    "G_delta": 0.20097281597874872,
    "generation_summary": "ledger/generation_002_summary.json",
    "frontier_record": "ledger/frontier.jsonl"
  }
}
```

## rmd17 benchmark dossier
```json
{
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
  "history": [
    {
      "epoch": 6,
      "train": {
        "loss": 17.122951533921064,
        "energy_mae": 14.264244873046875,
        "force_mae": 0.14293533291434868
      },
      "val": {
        "loss": 16.838496948063373,
        "energy_mae": 14.148597229003906,
        "force_mae": 0.13449498588428832
      },
      "device": "cuda",
      "learning_rate": 0.0001464466094067263,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 5.0
    },
    {
      "epoch": 7,
      "train": {
        "loss": 9.64272145679593,
        "energy_mae": 7.217515197753906,
        "force_mae": 0.12126031273673289
      },
      "val": {
        "loss": 3.8898900472670794,
        "energy_mae": 1.4970237426757813,
        "force_mae": 0.11964331542444416
      },
      "device": "cuda",
      "learning_rate": 3.8060233744356646e-05,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 5.0
    },
    {
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
    }
  ],
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
    "best_val_energy_mae": 1.4970237426757813
  }
}
```

## iso17 benchmark dossier
```json
{
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
  "history": [
    {
      "epoch": 6,
      "train": {
        "loss": 16.494677424578384,
        "energy_mae": 12.728089829246597,
        "force_mae": 0.18832938009780822
      },
      "val": {
        "loss": 13.137791315714518,
        "energy_mae": 9.443359375,
        "force_mae": 0.18472160398960114
      },
      "device": "cuda",
      "learning_rate": 0.0001464466094067263,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 5.0
    },
    {
      "epoch": 7,
      "train": {
        "loss": 9.340480196948098,
        "energy_mae": 5.889193634939666,
        "force_mae": 0.1725643281354615
      },
      "val": {
        "loss": 11.073963165283203,
        "energy_mae": 7.683919270833333,
        "force_mae": 0.16950220863024393
      },
      "device": "cuda",
      "learning_rate": 3.8060233744356646e-05,
      "energy_weight": 1.0,
      "force_weight": 20.0,
      "grad_clip": 5.0
    },
    {
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
    }
  ],
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
    "best_val_energy_mae": 0.24772135416666666
  }
}
```

## Diff vs source: model.py
- +
- +import math
- -class LowRankEquivariantStage(nn.Module):
- -    def __init__(self, hidden_dim: int, num_rbf: int, rank: int):
- +class BalancedInteractionBlock(nn.Module):
- +    def __init__(self, hidden_dim: int, num_rbf: int):
- -        self.rank = rank
- -        self.edge_filter = nn.Sequential(
- +        self.edge_mlp = nn.Sequential(
- -            nn.Linear(hidden_dim, hidden_dim * 2),
- -        )
- -        self.message_mlp = nn.Sequential(
- -            nn.Linear(hidden_dim * 2 + num_rbf, hidden_dim),
- -            nn.SiLU(),
- -            nn.Linear(hidden_dim, hidden_dim),
- -            nn.SiLU(),
- +            nn.Linear(hidden_dim, hidden_dim * 4),
- -        self.scalar_to_rank = nn.Linear(hidden_dim, rank, bias=False)
- -        self.vector_to_rank = nn.Linear(hidden_dim, rank, bias=False)
- -        self.rank_gate = nn.Sequential(

## Diff vs source: train.py
- +    grad_clip: float | None = None,
- +            if grad_clip is not None and grad_clip > 0:
- +                torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
- -    optimizer = torch.optim.Adam(model.parameters(), lr=float(lr if lr is not None else CONFIG.get("learning_rate", 1e-3)))
- +    learning_rate = float(lr if lr is not None else CONFIG.get("learning_rate", 1e-3))
- +    optimizer = torch.optim.AdamW(
- +        model.parameters(),
- +        lr=learning_rate,
- +        weight_decay=float(CONFIG.get("weight_decay", 1e-5)),
- +    )
- +    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(epochs, 1))
- -    energy_weight = float(CONFIG.get("energy_weight", 1.0))
- -    force_weight = float(CONFIG.get("force_weight", 20.0))
- +    energy_weight = float(CONFIG.get("energy_weight", 2.0))
- +    force_weight = float(CONFIG.get("force_weight", 12.0))
- +    grad_clip = float(CONFIG.get("grad_clip", 5.0))
- +    energy_warmup_epochs = max(1, int(CONFIG.get("energy_warmup_epochs", 2)))
- +        epoch_energy_weight = energy_weight * min(1.0, epoch / energy_warmup_epochs)
- +        epoch_force_weight = force_weight
- +

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

## Latest evidence brief
- knowledge/briefs/evidence_brief_20260417T103400Z_generation002_round_review.md

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

        self_vector = self._apply_linear_to_vector(self.self_vector, vector_state)
        mixed_agg_vector = self._apply_linear_to_vector(self.agg_vector, agg_vector)

        agg_norm = torch.linalg.norm(agg_vector, dim=-1)
        vector_alignment = torch.sum(self_vector * mixed_agg_vector, dim=-1)
        scalar_input = torch.cat([scalar_state, agg_scalar, agg_norm, vector_alignment], dim=-1)
        delta_scalar = self.scalar_update(scalar_input)
        scalar_gate = torch.sigmoid(self.scalar_residual_gate(torch.cat([scalar_state, agg_scalar], dim=-1)))
        new_scalar = self.layer_norm(scalar_state + scalar_gate * delta_scalar)

        vector_mix = torch.tanh(self.vector_gate(torch.cat([new_scalar, agg_scalar], dim=-1)))
        self_mix, agg_mix = vector_mix.chunk(2, dim=-1)
        delta_vector = self_mix.unsqueeze(-1) * self_vector + agg_mix.unsqueeze(-1) * mixed_agg_vector
        new_vector = vector_state + 0.5 * delta_vector
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
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(epochs, 1))

    energy_weight = float(CONFIG.get("energy_weight", 2.0))
    force_weight = float(CONFIG.get("force_weight", 12.0))
    grad_clip = float(CONFIG.get("grad_clip", 5.0))
    energy_warmup_epochs = max(1, int(CONFIG.get("energy_warmup_epochs", 2)))

    history = []
    for epoch in range(1, epochs + 1):
        epoch_energy_weight = energy_weight * min(1.0, epoch / energy_warmup_epochs)
        epoch_force_weight = force_weight

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
