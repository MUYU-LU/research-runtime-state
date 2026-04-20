# Proposal context for generation_001/proposal_004

## Current unit
- unit: generation_001/proposal_004
- source unit: base_unit

## Current runtime summary
```json
{
  "implementation_status": {
    "implementation_state": "launch_ready",
    "source_unit": "base_unit",
    "proposal_file": "04_jump_minimal_equivariant_local.md",
    "control_replicate": false,
    "changed_files": [],
    "repair_attempts": 0,
    "same_failure_class_repairs": 0,
    "last_failure_class": null,
    "remote_synced": true,
    "remote_smoke_passed": true,
    "remote_path": "/public/home/lmy/MLIP_EVOLUTION/research_runtime/generations/generation_001/proposal_004",
    "smoke_log_local": null,
    "smoke_log_remote": null,
    "last_actor": "workspace_cleanup_terminal_sync",
    "last_updated_utc": "2026-04-17T03:04:05.976354+00:00"
  },
  "run_status": {
    "run_state": "terminal_success",
    "launch_count": 0,
    "retry_count": 0,
    "pid": null,
    "host": null,
    "launch_log_local": null,
    "launch_log_remote": null,
    "failure_class": null,
    "launched_at_utc": null,
    "finished_at_utc": "2026-04-17T02:59:38.050265Z",
    "last_actor": "remote_collect_unit.py",
    "last_state_change_utc": "2026-04-17T02:59:38.050342+00:00"
  },
  "unit_summary": {
    "unit": "generation_001/proposal_004",
    "unit_meta": {
      "source_unit": "base_unit",
      "generation_round": "generation_001",
      "proposal_unit": "proposal_004",
      "proposal_file": "04_jump_minimal_equivariant_local.md"
    },
    "proposal_metadata": {
      "family": null,
      "phase": null,
      "jump_type": null,
      "budget_class": null,
      "expected_capability_gain": [],
      "proposal_file": "04_jump_minimal_equivariant_local.md",
      "control_replicate": false
    },
    "runtime_summary": {
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
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
        "metrics_path": "generations/generation_001/proposal_004/outputs/rmd17/benchmark_metrics.json",
        "history_path": "generations/generation_001/proposal_004/outputs/rmd17/train_history.json",
        "metrics": {
          "mild_ood_energy_mae": 31.10732775878906,
          "mild_ood_force_mae": 0.22409957795776428,
          "hard_ood_energy_mae": 31.102521728515626,
          "hard_ood_force_mae": 0.22413658142276108,
          "mixed_force_mae": 0.22412178003676236,
          "mixed_energy_mae": 31.104444140625002,
          "gap_penalty": 0.00016512063670020657,
          "Q_dataset": 1.4697045905697588,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 132.45355056476592,
              "energy_mae": 127.70477868652344,
              "force_mae": 0.23743857373204083
            },
            "val": {
              "loss": 35.589319355010986,
              "energy_mae": 31.107327819824217,
              "force_mae": 0.22409957729745655
            },
            "device": "cuda",
            "energy_weight": 1.0,
            "force_weight": 20.0
          },
          "best_val_force_mae": 0.22409957729745655,
          "best_val_energy_mae": 31.107327819824217,
          "force_trend": "improving",
          "energy_trend": "improving"
        },
        "Q_dataset": 1.4697045905697588
      },
      "iso17": {
        "metrics_path": "generations/generation_001/proposal_004/outputs/iso17/benchmark_metrics.json",
        "history_path": "generations/generation_001/proposal_004/outputs/iso17/train_history.json",
        "metrics": {
          "within_energy_mae": 218.2653943958849,
          "within_force_mae": 0.28658473771987575,
          "other_energy_mae": 217.85158015324518,
          "other_force_mae": 0.292543678644758,
          "mixed_force_mae": 0.2901601022748051,
          "mixed_energy_mae": 218.01710585030105,
          "gap_penalty": 0.02079294582213958,
          "Q_dataset": 1.5903411219295698,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 8,
          "last_epoch": {
            "epoch": 8,
            "train": {
              "loss": 161.4331660029912,
              "energy_mae": 155.68944889484067,
              "force_mae": 0.28718586659040485
            },
            "val": {
              "loss": 221.37109375,
              "energy_mae": 216.3662109375,
              "force_mae": 0.250244140625
            },
            "device": "cuda",
            "energy_weight": 1.0,
            "force_weight": 20.0
          },
          "best_val_force_mae": 0.19005022943019867,
          "best_val_energy_mae": 19.801106770833332,
          "force_trend": "worsening",
          "energy_trend": "improving"
        },
        "Q_dataset": 1.5903411219295698
      }
    },
    "Q_rmd17": 1.4697045905697588,
    "Q_iso17": 1.5903411219295698,
    "Q_total": 1.5119273765456926,
    "G_delta": 1.5236616434277017,
    "generation_summary": "ledger/generation_001_summary.json",
    "frontier_record": "ledger/frontier.jsonl"
  }
}
```

## Source runtime summary
```json
{
  "implementation_status": {
    "implementation_state": "implementation_needed",
    "source_unit": "base_unit",
    "proposal_file": null,
    "control_replicate": false,
    "changed_files": [],
    "repair_attempts": 0,
    "same_failure_class_repairs": 0,
    "last_failure_class": null,
    "remote_synced": false,
    "remote_smoke_passed": false,
    "remote_path": null,
    "smoke_log_local": null,
    "smoke_log_remote": null,
    "last_actor": "create_unit.py",
    "last_updated_utc": "2026-04-17T02:47:42.406238+00:00"
  },
  "run_status": {
    "run_state": "terminal_success",
    "launch_count": 0,
    "retry_count": 0,
    "pid": null,
    "host": null,
    "launch_log_local": null,
    "launch_log_remote": null,
    "failure_class": null,
    "launched_at_utc": null,
    "finished_at_utc": null,
    "last_actor": "create_unit.py",
    "last_state_change_utc": "2026-04-17T02:47:42.406772+00:00"
  },
  "unit_summary": {
    "unit": "base_unit",
    "unit_meta": {},
    "proposal_metadata": {
      "family": null,
      "phase": null,
      "jump_type": null,
      "budget_class": null,
      "expected_capability_gain": [],
      "proposal_file": null,
      "control_replicate": false
    },
    "runtime_summary": {
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
      "retry_count": 0,
      "implementation_state": "implementation_needed",
      "remote_synced": false,
      "remote_smoke_passed": false,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null
    },
    "datasets": {
      "rmd17": {
        "metrics_path": "base_unit/outputs/rmd17/benchmark_metrics.json",
        "history_path": null,
        "metrics": {
          "mild_ood_energy_mae": 651.4705227050781,
          "mild_ood_force_mae": 0.5771036948170513,
          "hard_ood_energy_mae": 647.3704008789063,
          "hard_ood_force_mae": 0.5781588028315455,
          "mixed_force_mae": 0.5777367596257479,
          "mixed_energy_mae": 649.010449609375,
          "gap_penalty": 0.0018282815098366672,
          "Q_dataset": -0.00018282815098366674,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 0,
          "last_epoch": null,
          "best_val_force_mae": null,
          "best_val_energy_mae": null,
          "force_trend": "unknown",
          "energy_trend": "unknown"
        },
        "Q_dataset": -0.00018282815098366674
      },
      "iso17": {
        "metrics_path": "base_unit/outputs/iso17/benchmark_metrics.json",
        "history_path": null,
        "metrics": {
          "within_energy_mae": 744.1677951926052,
          "within_force_mae": 1.3586197245239031,
          "other_energy_mae": 702.5220068359375,
          "other_force_mae": 1.809504021176925,
          "mixed_force_mae": 1.6291503025157161,
          "mixed_energy_mae": 719.1803221786047,
          "gap_penalty": 0.3318693881105635,
          "Q_dataset": -0.03318693881105635,
          "device": "cuda"
        },
        "history_summary": {
          "epochs": 0,
          "last_epoch": null,
          "best_val_force_mae": null,
          "best_val_energy_mae": null,
          "force_trend": "unknown",
          "energy_trend": "unknown"
        },
        "Q_dataset": -0.03318693881105635
      }
    },
    "Q_rmd17": -0.00018282815098366674,
    "Q_iso17": -0.03318693881105635,
    "Q_total": -0.011734266882009105,
    "G_delta": null,
    "frontier_record": "ledger/frontier.jsonl"
  }
}
```

## rmd17 benchmark dossier
```json
{
  "metrics": {
    "mild_ood_energy_mae": 31.10732775878906,
    "mild_ood_force_mae": 0.22409957795776428,
    "hard_ood_energy_mae": 31.102521728515626,
    "hard_ood_force_mae": 0.22413658142276108,
    "mixed_force_mae": 0.22412178003676236,
    "mixed_energy_mae": 31.104444140625002,
    "gap_penalty": 0.00016512063670020657,
    "Q_dataset": 1.4697045905697588,
    "device": "cuda"
  },
  "history": [
    {
      "epoch": 6,
      "train": {
        "loss": 122.86707294273377,
        "energy_mae": 117.61344454956054,
        "force_mae": 0.2626813974706456
      },
      "val": {
        "loss": 95.56742486190795,
        "energy_mae": 90.48811999511719,
        "force_mae": 0.2539652531230822
      },
      "device": "cuda",
      "energy_weight": 1.0,
      "force_weight": 20.0
    },
    {
      "epoch": 7,
      "train": {
        "loss": 118.22032309532166,
        "energy_mae": 113.25608120727539,
        "force_mae": 0.24821208366099745
      },
      "val": {
        "loss": 39.19629244422912,
        "energy_mae": 34.499584533691404,
        "force_mae": 0.23483539693849162
      },
      "device": "cuda",
      "energy_weight": 1.0,
      "force_weight": 20.0
    },
    {
      "epoch": 8,
      "train": {
        "loss": 132.45355056476592,
        "energy_mae": 127.70477868652344,
        "force_mae": 0.23743857373204083
      },
      "val": {
        "loss": 35.589319355010986,
        "energy_mae": 31.107327819824217,
        "force_mae": 0.22409957729745655
      },
      "device": "cuda",
      "energy_weight": 1.0,
      "force_weight": 20.0
    }
  ],
  "history_summary": {
    "epochs": 8,
    "last_epoch": {
      "epoch": 8,
      "train": {
        "loss": 132.45355056476592,
        "energy_mae": 127.70477868652344,
        "force_mae": 0.23743857373204083
      },
      "val": {
        "loss": 35.589319355010986,
        "energy_mae": 31.107327819824217,
        "force_mae": 0.22409957729745655
      },
      "device": "cuda",
      "energy_weight": 1.0,
      "force_weight": 20.0
    },
    "best_val_force_mae": 0.22409957729745655,
    "best_val_energy_mae": 31.107327819824217
  }
}
```

## iso17 benchmark dossier
```json
{
  "metrics": {
    "within_energy_mae": 218.2653943958849,
    "within_force_mae": 0.28658473771987575,
    "other_energy_mae": 217.85158015324518,
    "other_force_mae": 0.292543678644758,
    "mixed_force_mae": 0.2901601022748051,
    "mixed_energy_mae": 218.01710585030105,
    "gap_penalty": 0.02079294582213958,
    "Q_dataset": 1.5903411219295698,
    "device": "cuda"
  },
  "history": [
    {
      "epoch": 6,
      "train": {
        "loss": 193.40257905780678,
        "energy_mae": 187.2517607131807,
        "force_mae": 0.3075409300477788
      },
      "val": {
        "loss": 294.6613464355469,
        "energy_mae": 289.8313802083333,
        "force_mae": 0.24149885276953378
      },
      "device": "cuda",
      "energy_weight": 1.0,
      "force_weight": 20.0
    },
    {
      "epoch": 7,
      "train": {
        "loss": 181.11661013707075,
        "energy_mae": 175.17465445641244,
        "force_mae": 0.29709778935233555
      },
      "val": {
        "loss": 24.32199478149414,
        "energy_mae": 19.801106770833332,
        "force_mae": 0.2260443220535914
      },
      "device": "cuda",
      "energy_weight": 1.0,
      "force_weight": 20.0
    },
    {
      "epoch": 8,
      "train": {
        "loss": 161.4331660029912,
        "energy_mae": 155.68944889484067,
        "force_mae": 0.28718586659040485
      },
      "val": {
        "loss": 221.37109375,
        "energy_mae": 216.3662109375,
        "force_mae": 0.250244140625
      },
      "device": "cuda",
      "energy_weight": 1.0,
      "force_weight": 20.0
    }
  ],
  "history_summary": {
    "epochs": 8,
    "last_epoch": {
      "epoch": 8,
      "train": {
        "loss": 161.4331660029912,
        "energy_mae": 155.68944889484067,
        "force_mae": 0.28718586659040485
      },
      "val": {
        "loss": 221.37109375,
        "energy_mae": 216.3662109375,
        "force_mae": 0.250244140625
      },
      "device": "cuda",
      "energy_weight": 1.0,
      "force_weight": 20.0
    },
    "best_val_force_mae": 0.19005022943019867,
    "best_val_energy_mae": 19.801106770833332
  }
}
```

## Generation summary
```json
{
  "generation": "generation_001",
  "created_at_utc": "2026-04-17T10:03:07.670201+00:00",
  "units": [
    {
      "unit": "generation_001/proposal_001",
      "proposal_file": "01_exploit_neighbor_message_passing.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 1,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 0.631172829692333,
      "Q_iso17": 1.966366518343365,
      "Q_total": 1.098490620720194,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 140.00287213134766,
      "rmd17_mild_ood_force_mae": 0.41414512604288756,
      "rmd17_hard_ood_energy_mae": 139.92787573242188,
      "rmd17_hard_ood_force_mae": 0.4156753925327212,
      "rmd17_mixed_force_mae": 0.41506328593678776,
      "rmd17_mixed_energy_mae": 139.9578742919922,
      "rmd17_gap_penalty": 0.0036950006014834906,
      "rmd17_Q_dataset": 0.631172829692333,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.4141451278217137,
      "rmd17_best_val_energy_mae": 28.06105938720703,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 18.903125483446782,
      "iso17_within_force_mae": 0.40726443166927534,
      "iso17_other_energy_mae": 16.017423753004806,
      "iso17_other_force_mae": 0.41254535522598484,
      "iso17_mixed_force_mae": 0.410432985803301,
      "iso17_mixed_energy_mae": 17.171704445181597,
      "iso17_gap_penalty": 0.012966817492633348,
      "iso17_Q_dataset": 1.966366518343365,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.1946235050757726,
      "iso17_best_val_energy_mae": 14.776041666666666
    },
    {
      "unit": "generation_001/proposal_002",
      "proposal_file": "02_exploit_angular_triplet_head.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 0.5885258127252502,
      "Q_iso17": 1.3215743424786996,
      "Q_total": 0.8450927981389574,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 158.1576350097656,
      "rmd17_mild_ood_force_mae": 0.4205563422366977,
      "rmd17_hard_ood_energy_mae": 158.1170658569336,
      "rmd17_hard_ood_force_mae": 0.42257104540430007,
      "rmd17_mixed_force_mae": 0.4217651641372591,
      "rmd17_mixed_energy_mae": 158.1332935180664,
      "rmd17_gap_penalty": 0.004790566602521183,
      "rmd17_Q_dataset": 0.5885258127252502,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.39254336929135025,
      "rmd17_best_val_energy_mae": 158.1576350097656,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 271.56422300433167,
      "iso17_within_force_mae": 0.38795811705069966,
      "iso17_other_energy_mae": 241.01429987980768,
      "iso17_other_force_mae": 0.39901185762996855,
      "iso17_mixed_force_mae": 0.394590361398261,
      "iso17_mixed_energy_mae": 253.23426912961725,
      "iso17_gap_penalty": 0.028492097712176128,
      "iso17_Q_dataset": 1.3215743424786996,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.21114557484785715,
      "iso17_best_val_energy_mae": 39.640950520833336
    },
    {
      "unit": "generation_001/proposal_003",
      "proposal_file": "03_exploit_residual_pair_graph.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 0.90210068306928,
      "Q_iso17": 1.366300627809506,
      "Q_total": 1.0645706637283592,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 96.69731335449218,
      "rmd17_mild_ood_force_mae": 0.32745184243936093,
      "rmd17_hard_ood_energy_mae": 96.39558331298828,
      "rmd17_hard_ood_force_mae": 0.3275510432301089,
      "rmd17_mixed_force_mae": 0.3275113629138097,
      "rmd17_mixed_energy_mae": 96.51627532958983,
      "rmd17_gap_penalty": 0.0003029477251026802,
      "rmd17_Q_dataset": 0.90210068306928,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.32745184102654457,
      "rmd17_best_val_energy_mae": 72.99180975341797,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 242.71950852800123,
      "iso17_within_force_mae": 0.37385978785039176,
      "iso17_other_energy_mae": 245.5685175030048,
      "iso17_other_force_mae": 0.37893804577107615,
      "iso17_mixed_force_mae": 0.37690674260280244,
      "iso17_mixed_energy_mae": 244.42891391300338,
      "iso17_gap_penalty": 0.013583322105513489,
      "iso17_Q_dataset": 1.366300627809506,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "worsening",
      "iso17_energy_trend": "worsening",
      "iso17_best_val_force_mae": 0.18580262859662375,
      "iso17_best_val_energy_mae": 15.429036458333334
    },
    {
      "unit": "generation_001/proposal_004",
      "proposal_file": "04_jump_minimal_equivariant_local.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 1.4697045905697588,
      "Q_iso17": 1.5903411219295698,
      "Q_total": 1.5119273765456926,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 31.10732775878906,
      "rmd17_mild_ood_force_mae": 0.22409957795776428,
      "rmd17_hard_ood_energy_mae": 31.102521728515626,
      "rmd17_hard_ood_force_mae": 0.22413658142276108,
      "rmd17_mixed_force_mae": 0.22412178003676236,
      "rmd17_mixed_energy_mae": 31.104444140625002,
      "rmd17_gap_penalty": 0.00016512063670020657,
      "rmd17_Q_dataset": 1.4697045905697588,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.22409957729745655,
      "rmd17_best_val_energy_mae": 31.107327819824217,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 218.2653943958849,
      "iso17_within_force_mae": 0.28658473771987575,
      "iso17_other_energy_mae": 217.85158015324518,
      "iso17_other_force_mae": 0.292543678644758,
      "iso17_mixed_force_mae": 0.2901601022748051,
      "iso17_mixed_energy_mae": 218.01710585030105,
      "iso17_gap_penalty": 0.02079294582213958,
      "iso17_Q_dataset": 1.5903411219295698,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "worsening",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.19005022943019867,
      "iso17_best_val_energy_mae": 19.801106770833332
    },
    {
      "unit": "generation_001/proposal_005",
      "proposal_file": "05_jump_cace_body_order_bridge.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 0.9441950186098212,
      "Q_iso17": 1.816600428348992,
      "Q_total": 1.249536912018531,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 73.57701043701172,
      "rmd17_mild_ood_force_mae": 0.3391681952457875,
      "rmd17_hard_ood_energy_mae": 73.05043377685547,
      "rmd17_hard_ood_force_mae": 0.3395546536417678,
      "rmd17_mixed_force_mae": 0.33940007028337565,
      "rmd17_mixed_energy_mae": 73.26106444091798,
      "rmd17_gap_penalty": 0.0011394299388805765,
      "rmd17_Q_dataset": 0.9441950186098212,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.3391681952131912,
      "rmd17_best_val_energy_mae": 36.010086547851564,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 40.741789139851484,
      "iso17_within_force_mae": 0.3742518058950358,
      "iso17_other_energy_mae": 39.589672475961535,
      "iso17_other_force_mae": 0.3800960376686775,
      "iso17_mixed_force_mae": 0.3777583449592208,
      "iso17_mixed_energy_mae": 40.05051914151751,
      "iso17_gap_penalty": 0.015615774410625463,
      "iso17_Q_dataset": 1.816600428348992,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.1891689250866572,
      "iso17_best_val_energy_mae": 7.178059895833333
    },
    {
      "unit": "generation_001/proposal_006",
      "proposal_file": "06_jump_equivariant_triplet_hybrid.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 0.5641251237740994,
      "Q_iso17": 1.8459469948983962,
      "Q_total": 1.0127627786676032,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 48.64187133789063,
      "rmd17_mild_ood_force_mae": 0.6421745787896216,
      "rmd17_hard_ood_energy_mae": 49.3634165649414,
      "rmd17_hard_ood_force_mae": 0.6446221184656024,
      "rmd17_mixed_force_mae": 0.6436431025952101,
      "rmd17_mixed_energy_mae": 49.074798474121096,
      "rmd17_gap_penalty": 0.003811330682989836,
      "rmd17_Q_dataset": 0.5641251237740994,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.5967964364178479,
      "rmd17_best_val_energy_mae": 48.64187316894531,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 21.424124961324257,
      "iso17_within_force_mae": 0.44352122439753894,
      "iso17_other_energy_mae": 21.3470458984375,
      "iso17_other_force_mae": 0.4506398164652861,
      "iso17_mixed_force_mae": 0.44779237963818724,
      "iso17_mixed_energy_mae": 21.377877523592204,
      "iso17_gap_penalty": 0.01605017229423627,
      "iso17_Q_dataset": 1.8459469948983962,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.31076844533284503,
      "iso17_best_val_energy_mae": 2.8271484375
    },
    {
      "unit": "generation_001/proposal_007",
      "proposal_file": "07_backward_simplify_atomwise_local_baseline.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": 0.6699802032157187,
      "Q_iso17": 2.0316753558640994,
      "Q_total": 1.146573506642652,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 96.05946423339844,
      "rmd17_mild_ood_force_mae": 0.44559492137376217,
      "rmd17_hard_ood_energy_mae": 96.35261059570313,
      "rmd17_hard_ood_force_mae": 0.4471873637950048,
      "rmd17_mixed_force_mae": 0.4465503868265077,
      "rmd17_mixed_energy_mae": 96.23535205078124,
      "rmd17_gap_penalty": 0.003573744548814818,
      "rmd17_Q_dataset": 0.6699802032157187,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "improving",
      "rmd17_energy_trend": "improving",
      "rmd17_best_val_force_mae": 0.44559492111112925,
      "rmd17_best_val_energy_mae": 54.478027893066404,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 20.064335647431932,
      "iso17_within_force_mae": 0.3554765443695654,
      "iso17_other_energy_mae": 18.771963641826922,
      "iso17_other_force_mae": 0.3650635276390956,
      "iso17_mixed_force_mae": 0.36122873433128355,
      "iso17_mixed_energy_mae": 19.288912444068927,
      "iso17_gap_penalty": 0.026969383553859198,
      "iso17_Q_dataset": 2.0316753558640994,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "improving",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.1910510535041491,
      "iso17_best_val_energy_mae": 12.420572916666666
    },
    {
      "unit": "generation_001/proposal_008",
      "proposal_file": "08_control_replicate_base_unit.md",
      "control_replicate": false,
      "run_state": "terminal_success",
      "failure_class": null,
      "launch_count": 0,
      "retry_count": 0,
      "implementation_state": "launch_ready",
      "remote_synced": true,
      "remote_smoke_passed": true,
      "repair_attempts": 0,
      "same_failure_class_repairs": 0,
      "last_failure_class": null,
      "Q_rmd17": -0.011980764669461678,
      "Q_iso17": -0.17750563109147202,
      "Q_total": -0.0699144679171653,
      "rmd17_metrics_present": true,
      "rmd17_history_present": true,
      "rmd17_mild_ood_energy_mae": 824.6456911010742,
      "rmd17_mild_ood_force_mae": 0.5416401309333742,
      "rmd17_hard_ood_energy_mae": 831.4332929077149,
      "rmd17_hard_ood_force_mae": 0.5407502312399447,
      "rmd17_mixed_force_mae": 0.5411061911173165,
      "rmd17_mixed_energy_mae": 828.7182521850586,
      "rmd17_gap_penalty": 0.0,
      "rmd17_Q_dataset": -0.011980764669461678,
      "rmd17_device": "cuda",
      "rmd17_epochs": 8,
      "rmd17_force_trend": "worsening",
      "rmd17_energy_trend": "worsening",
      "rmd17_best_val_force_mae": 0.5210017480198293,
      "rmd17_best_val_energy_mae": 790.7902130126953,
      "iso17_metrics_present": true,
      "iso17_history_present": true,
      "iso17_within_energy_mae": 740.6420796913676,
      "iso17_within_force_mae": 1.6752869960842747,
      "iso17_other_energy_mae": 659.6675916466346,
      "iso17_other_force_mae": 2.219974552324185,
      "iso17_mixed_force_mae": 2.0020995298282207,
      "iso17_mixed_energy_mae": 692.0573868645279,
      "iso17_gap_penalty": 0.32513089250540866,
      "iso17_Q_dataset": -0.17750563109147202,
      "iso17_device": "cuda",
      "iso17_epochs": 8,
      "iso17_force_trend": "worsening",
      "iso17_energy_trend": "improving",
      "iso17_best_val_force_mae": 0.27482137084007263,
      "iso17_best_val_energy_mae": 482.7887369791667
    }
  ],
  "best_control_Q_total": null
}
```

## Diff vs source: model.py
- -        self.pair_mlp = nn.Sequential(
- +        self.edge_filter = nn.Sequential(
- +            nn.Linear(num_rbf, hidden_dim),
- +            nn.SiLU(),
- +            nn.Linear(hidden_dim, hidden_dim * 2),
- +        )
- +        self.message_mlp = nn.Sequential(
- +        )
- +        self.scalar_update = nn.Sequential(
- +            nn.Linear(hidden_dim * 2, hidden_dim),
- +            nn.SiLU(),
- +        )
- +        self.vector_update = nn.Sequential(
- +            nn.Linear(hidden_dim * 2, hidden_dim),
- +            nn.Linear(hidden_dim, hidden_dim),
- -        self.pair_out = nn.Linear(hidden_dim, 1)
- +        self.energy_mlp = nn.Sequential(
- +            nn.Linear(hidden_dim * 2, hidden_dim),
- +            nn.SiLU(),
- +            nn.Linear(hidden_dim, 1),

## Diff vs source: train.py
- -    # The seed model is single-structure forward only. Keep honest batch semantics
- -    # instead of pretending the model consumes a vectorized structure batch.
- -    effective_batch_size = 1
- -    train_loader = make_dataloader(dataset, train_dir, batch_size=effective_batch_size, shuffle=True, max_samples=max_samples)
- -    val_loader = make_dataloader(dataset, val_dir, batch_size=effective_batch_size, shuffle=False, max_samples=max_samples)
- +    train_loader = make_dataloader(dataset, train_dir, batch_size=batch_size, shuffle=True, max_samples=max_samples)
- +    val_loader = make_dataloader(dataset, val_dir, batch_size=batch_size, shuffle=False, max_samples=max_samples)
- -            "requested_batch_size": batch_size,
- -            "effective_batch_size": effective_batch_size,

## Frontier tail
- base_unit | family=None | phase=None | Q_rmd17=-0.00018282815098366674 | Q_iso17=-0.03318693881105635 | Q_total=-0.011734266882009105 | G_delta=None | status=terminal_success
- generation_001/proposal_001 | family=None | phase=None | Q_rmd17=0.631172829692333 | Q_iso17=1.966366518343365 | Q_total=1.098490620720194 | G_delta=1.1102248876022032 | status=terminal_success
- generation_001/proposal_002 | family=None | phase=None | Q_rmd17=0.5885258127252502 | Q_iso17=1.3215743424786996 | Q_total=0.8450927981389574 | G_delta=0.8568270650209665 | status=terminal_success
- generation_001/proposal_003 | family=None | phase=None | Q_rmd17=0.90210068306928 | Q_iso17=1.366300627809506 | Q_total=1.0645706637283592 | G_delta=1.0763049306103682 | status=terminal_success
- generation_001/proposal_004 | family=None | phase=None | Q_rmd17=1.4697045905697588 | Q_iso17=1.5903411219295698 | Q_total=1.5119273765456926 | G_delta=1.5236616434277017 | status=terminal_success
- generation_001/proposal_005 | family=None | phase=None | Q_rmd17=0.9441950186098212 | Q_iso17=1.816600428348992 | Q_total=1.249536912018531 | G_delta=1.26127117890054 | status=terminal_success
- generation_001/proposal_006 | family=None | phase=None | Q_rmd17=0.5641251237740994 | Q_iso17=1.8459469948983962 | Q_total=1.0127627786676032 | G_delta=1.0244970455496123 | status=terminal_success
- generation_001/proposal_007 | family=None | phase=None | Q_rmd17=0.6699802032157187 | Q_iso17=2.0316753558640994 | Q_total=1.146573506642652 | G_delta=1.158307773524661 | status=terminal_success
- generation_001/proposal_008 | family=None | phase=None | Q_rmd17=-0.011980764669461678 | Q_iso17=-0.17750563109147202 | Q_total=-0.0699144679171653 | G_delta=-0.05818020103515619 | status=terminal_success

## Latest evidence brief
- knowledge/briefs/evidence_brief_20260417T032900Z_proposal004_continuation.md

## Proposal writing rule
- proposal decisions must be benchmark-centric, not force-only
- discuss energy, force, gap_penalty, Q fields, train trends, runtime/failure, and control comparison when relevant

## Current model.py
```python
from __future__ import annotations

import torch
from torch import nn


class EvolutionMLIP(nn.Module):
    def __init__(
        self,
        max_atomic_number: int = 100,
        hidden_dim: int = 96,
        num_rbf: int = 32,
        cutoff: float = 5.0,
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

        self.edge_filter = nn.Sequential(
            nn.Linear(num_rbf, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim * 2),
        )
        self.message_mlp = nn.Sequential(
            nn.Linear(hidden_dim * 2 + num_rbf, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
        )
        self.scalar_update = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        self.vector_update = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        self.energy_mlp = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, 1),
        )

    def _rbf(self, distances: torch.Tensor) -> torch.Tensor:
        diff = distances.unsqueeze(-1) - self.rbf_centers
        return torch.exp(-0.5 * (diff / self.rbf_widths) ** 2)

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

        filter_out = self.edge_filter(rbf)
        scalar_filter, vector_filter = filter_out.chunk(2, dim=-1)

        edge_input = torch.cat([scalar_state[i_idx], scalar_state[j_idx], rbf], dim=-1)
        edge_hidden = self.message_mlp(edge_input)

        scalar_message = edge_hidden * scalar_filter
        vector_message = vector_filter.unsqueeze(-1) * unit.unsqueeze(1)

        agg_scalar = torch.zeros_like(scalar_state)
        agg_vector = torch.zeros_like(vector_state)
        agg_scalar.index_add_(0, i_idx, scalar_message)
        agg_vector.index_add_(0, i_idx, vector_message)

        scalar_state = scalar_state + self.scalar_update(torch.cat([scalar_state, agg_scalar], dim=-1))
        vector_context = agg_vector + vector_state
        vector_norm = torch.linalg.norm(vector_context, dim=-1)
        scalar_state = scalar_state + self.vector_update(torch.cat([scalar_state, vector_norm], dim=-1))
        vector_state = vector_context

        per_atom_energy = self.energy_mlp(torch.cat([scalar_state, torch.linalg.norm(vector_state, dim=-1)], dim=-1)).squeeze(-1)
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

    optimizer = torch.optim.Adam(model.parameters(), lr=float(lr if lr is not None else CONFIG.get("learning_rate", 1e-3)))

    energy_weight = float(CONFIG.get("energy_weight", 1.0))
    force_weight = float(CONFIG.get("force_weight", 20.0))

    history = []
    for epoch in range(1, epochs + 1):
        model.train()
        train_metrics = run_epoch(
            model,
            train_loader,
            optimizer=optimizer,
            energy_weight=energy_weight,
            force_weight=force_weight,
            device=device,
        )

        model.eval()
        with torch.enable_grad():
            val_metrics = run_epoch(
                model,
                val_loader,
                optimizer=None,
                energy_weight=energy_weight,
                force_weight=force_weight,
                device=device,
            )

        row = {
            "epoch": epoch,
            "train": train_metrics,
            "val": val_metrics,
            "device": str(device),
            "energy_weight": energy_weight,
            "force_weight": force_weight,
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
