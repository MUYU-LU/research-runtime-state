# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-05-01T01:14:20.001701+00:00",
  "mode": "balanced",
  "source_unit": "generation_020/proposal_003",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/evidence_run.json"
}
```

## package_contract

```json
[
  "This brief is an evidence-delta index, not a full proposal context dump.",
  "JSON files in evidence_package_index are the handoff source of truth.",
  "Full local_context/current_code_profile/benchmark_diagnosis are referenced by path and compact summary only.",
  "No provenance -> no strong evidence.",
  "No mechanism card -> no proposal mechanism.",
  "No formula derivation / algorithm / repo code path / code trace / current insertion point -> weak evidence only.",
  "Benchmark diagnosis is internal diagnosis, not external mechanism evidence.",
  "Reading artifacts is not enough: strong mechanisms require derivation, tensor/data-flow reasoning, code trace, and bounded edit mapping.",
  "Source novelty is tracked; repeated recent sources without new mechanism extraction downgrade proposal readiness."
]
```

## evidence_quality

```json
{
  "version": "evidence_quality.v1",
  "grade": "A",
  "fresh_local_pdf_verified": true,
  "fresh_repo_code_verified": true,
  "has_mechanism_cards": true,
  "has_strong_mechanism_cards": true,
  "strong_mechanism_card_count": 2,
  "min_strong_mechanism_cards": 1,
  "strong_card_target_met": true,
  "has_patch_blueprints": true,
  "has_implementation_ready_blueprints": true,
  "usable_for_proposal": true,
  "usable_for_implementation": true,
  "diagnosis_only": false,
  "require_external_evidence": true,
  "source_novelty": {
    "version": "source_novelty.v1",
    "history_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_source_history.jsonl",
    "policy": {
      "lookback_runs": 3,
      "min_attempted_external_sources": 2,
      "min_new_sources": 1,
      "max_recent_reused_sources": 1
    },
    "source_discovery_budget": {
      "min_successful_pdf_sources": 1,
      "min_successful_repo_sources": 1,
      "min_strong_mechanism_cards": 1,
      "max_pdf_attempts": 6,
      "max_repo_attempts": 4,
      "max_external_source_attempts": 10,
      "max_source_expansion_rounds": 2,
      "source_expansion_round": 1
    },
    "pdf_attempted_source_count": 2,
    "pdf_successful_source_count": 2,
    "repo_attempted_source_count": 1,
    "repo_successful_source_count": 1,
    "attempted_external_source_count": 3,
    "successful_external_source_count": 3,
    "source_targets_met": true,
    "source_budget_exhausted": false,
    "new_source_count": 2,
    "recent_reused_source_count": 1,
    "new_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu65e9u671fu67b6u6784_-_SchNetu8fdeu7eedu6ee4u6ce2u5377u79efu5206u5b50u52bf_e748cfccb3.pdf#21de6918484e"
    ],
    "recent_reused_source_ids": [
      "repo:atomistic-machine-learning/schnetpack#41e33adf8c61"
    ],
    "recent_attempted_reused_source_count": 1,
    "recent_attempted_reused_source_ids": [
      "repo:atomistic-machine-learning/schnetpack#41e33adf8c61"
    ],
    "reuse_semantics": "recent_reused_source_ids counts sources used as strong evidence in recent runs. recent_attempted_reused_source_ids is diagnostic only and does not fail novelty by itself.",
    "all_sources_recent_repeats": false,
    "source_novelty_passed": true,
    "allow_recent_source_reuse": false
  },
  "external_attempted_source_count": 3,
  "external_successful_source_count": 3,
  "source_novelty_passed": true,
  "source_budget_exhausted": false,
  "needs_source_expansion": false,
  "hard_rules": [
    "No provenance -> no strong evidence.",
    "No mechanism card -> no proposal mechanism.",
    "No formula derivation/algorithm/repo path/code trace/current insertion point -> weak evidence only.",
    "No patch blueprint -> not implementation-ready.",
    "Benchmark diagnosis is not external mechanism evidence."
  ]
}
```

## context_references

```json
{
  "source_unit": "generation_020/proposal_003",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_020/proposal_003",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/generation_memory.json",
  "generation_memory": {
    "version": "generation_memory.v1",
    "source_unit": "generation_020/proposal_003",
    "last_completed_generation": "generation_020",
    "ignored_legacy_source_count": 6,
    "completed_generation_count_for_source": 0,
    "recent_attempt_count_for_source": 0,
    "unit_card_count_for_source": 0,
    "negative_pattern_count_for_source": 0,
    "partial_positive_pattern_count_for_source": 0,
    "latest_generation": null,
    "latest_best_child": null,
    "latest_outcome_counts": {},
    "latest_lessons": [],
    "note": "Full generation memory, unit cards, code deltas, and attempts are in generation_memory.json, not expanded in this brief."
  },
  "benchmark_warnings": [],
  "note": "Full proposal context, current code profile, and benchmark dossier are referenced here, not repeated in the brief."
}
```

## source_attempt_summary

```json
{
  "by_type": {
    "local_code_profile": {
      "total": 1,
      "success": 1,
      "fresh": 1,
      "can_support_strong": 0
    },
    "local_runtime_context": {
      "total": 1,
      "success": 0,
      "fresh": 0,
      "can_support_strong": 0
    },
    "local_ledger": {
      "total": 2,
      "success": 1,
      "fresh": 2,
      "can_support_strong": 0
    },
    "prior_brief": {
      "total": 5,
      "success": 5,
      "fresh": 0,
      "can_support_strong": 0
    },
    "local_pdf": {
      "total": 2,
      "success": 2,
      "fresh": 2,
      "can_support_strong": 2
    },
    "repo_code": {
      "total": 1,
      "success": 1,
      "fresh": 1,
      "can_support_strong": 1
    }
  },
  "strong_capable_sources": [
    "paper_artifact:paper_001",
    "paper_artifact:paper_002",
    "repo_artifact:repo_001"
  ],
  "failed_sources": [
    {
      "source_id": "proposal_context",
      "type": "local_runtime_context",
      "notes": "Benchmark and history context. Useful for diagnosis, not external mechanism support."
    },
    {
      "source_id": "generation_memory",
      "type": "local_ledger",
      "notes": "Long-term generation memory supports diagnosis and avoids duplicate attempts; it is not external mechanism evidence."
    }
  ],
  "reused_sources": [
    "prior_brief:1",
    "prior_brief:2",
    "prior_brief:3",
    "prior_brief:4",
    "prior_brief:5"
  ]
}
```

## source_novelty

```json
{
  "version": "source_novelty.v1",
  "history_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_source_history.jsonl",
  "policy": {
    "lookback_runs": 3,
    "min_attempted_external_sources": 2,
    "min_new_sources": 1,
    "max_recent_reused_sources": 1
  },
  "source_discovery_budget": {
    "min_successful_pdf_sources": 1,
    "min_successful_repo_sources": 1,
    "min_strong_mechanism_cards": 1,
    "max_pdf_attempts": 6,
    "max_repo_attempts": 4,
    "max_external_source_attempts": 10,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 1
  },
  "pdf_attempted_source_count": 2,
  "pdf_successful_source_count": 2,
  "repo_attempted_source_count": 1,
  "repo_successful_source_count": 1,
  "attempted_external_source_count": 3,
  "successful_external_source_count": 3,
  "source_targets_met": true,
  "source_budget_exhausted": false,
  "new_source_count": 2,
  "recent_reused_source_count": 1,
  "new_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu65e9u671fu67b6u6784_-_SchNetu8fdeu7eedu6ee4u6ce2u5377u79efu5206u5b50u52bf_e748cfccb3.pdf#21de6918484e"
  ],
  "recent_reused_source_ids": [
    "repo:atomistic-machine-learning/schnetpack#41e33adf8c61"
  ],
  "recent_attempted_reused_source_count": 1,
  "recent_attempted_reused_source_ids": [
    "repo:atomistic-machine-learning/schnetpack#41e33adf8c61"
  ],
  "reuse_semantics": "recent_reused_source_ids counts sources used as strong evidence in recent runs. recent_attempted_reused_source_ids is diagnostic only and does not fail novelty by itself.",
  "all_sources_recent_repeats": false,
  "source_novelty_passed": true,
  "allow_recent_source_reuse": false
}
```

## source_artifacts

```json
{
  "papers": [
    {
      "artifact_ref": "paper_artifact:paper_001",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/paper_artifacts/paper_001.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_002",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu65e9u671fu67b6u6784_-_SchNetu8fdeu7eedu6ee4u6ce2u5377u79efu5206u5b50u52bf_e748cfccb3.pdf#21de6918484e",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/paper_artifacts/paper_002.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:atomistic-machine-learning/schnetpack#41e33adf8c61",
      "repo": "atomistic-machine-learning/schnetpack",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/repo_artifacts/repo_001.json",
      "success": true
    }
  ]
}
```

## source_analysis_requirements

```json
{
  "version": "source_analysis_requirements.v1",
  "instruction": "Reading artifacts is not enough. Promote a mechanism only after writing formula derivation / shape or data-flow reasoning / repo code trace / current insertion point / bounded edit. If no strong mechanism can be materialized and the source budget is not exhausted, expand the source plan with new PDFs/repos instead of writing a proposal-ready brief.",
  "required_for_strong_mechanism": [
    "mathematical_form or algorithmic update",
    "formula_derivation with reasoning steps from source expression to current-code implication",
    "tensor_shapes or data_flow for model-code mechanisms",
    "repo_code_trace with artifact, repo_file, class_or_function, implementation_pattern, mapped_current_insertion_point",
    "current_code_insertion_point",
    "bounded_edit",
    "benchmark expectation over energy/force/gap/Q/runtime/failure risk"
  ],
  "source_discovery_budget": {
    "min_successful_pdf_sources": 1,
    "min_successful_repo_sources": 1,
    "min_strong_mechanism_cards": 1,
    "max_pdf_attempts": 6,
    "max_repo_attempts": 4,
    "max_external_source_attempts": 10,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 1
  },
  "source_budget_exhausted": false,
  "source_targets_met": true,
  "artifact_index": {
    "papers": [
      {
        "artifact_ref": "paper_artifact:paper_001",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/paper_artifacts/paper_001.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_002",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu65e9u671fu67b6u6784_-_SchNetu8fdeu7eedu6ee4u6ce2u5377u79efu5206u5b50u52bf_e748cfccb3.pdf#21de6918484e",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/paper_artifacts/paper_002.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:atomistic-machine-learning/schnetpack#41e33adf8c61",
        "repo": "atomistic-machine-learning/schnetpack",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T011417Z/repo_artifacts/repo_001.json",
        "success": true
      }
    ]
  }
}
```

## what_is_new_for_proposal

```json
{
  "usable_for_proposal": true,
  "usable_for_implementation": true,
  "diagnosis_only": false,
  "strong_mechanisms": [
    "GEN021-M01-atomwise-energy-residual-calibration",
    "GEN021-M02-energy-force-loss-rebalancing-control"
  ],
  "weak_or_hypothesis_mechanisms": [],
  "proposal_allowed_mechanisms": [
    "GEN021-M01-atomwise-energy-residual-calibration",
    "GEN021-M02-energy-force-loss-rebalancing-control"
  ],
  "proposal_blocked_mechanisms": [
    "unproven model-family label without formula derivation and code trace",
    "force-only proposal when energy/gap/Q context is available",
    "implementation rewrite without patch blueprint"
  ]
}
```

## new_mechanism_cards_summary

```json
{
  "strong_mechanism_ids": [
    "GEN021-M01-atomwise-energy-residual-calibration",
    "GEN021-M02-energy-force-loss-rebalancing-control"
  ],
  "weak_or_hypothesis_ids": [],
  "cards": [
    {
      "mechanism_id": "GEN021-M01-atomwise-energy-residual-calibration",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_001",
        "paper_artifact:paper_002",
        "repo_artifact:repo_001",
        "current_unit_profile",
        "proposal_context"
      ],
      "concrete_mechanism": "Move the next bounded adaptation from another hidden-state vector mixer into a direct atomwise scalar energy residual head, while preserving forces as the negative derivative of the same scalar energy. The generation_020 late PaiNN mixer was source-recoverable but too weakly coupled to the objective: scalar_scale = 0.05*sigmoid(-6) ≈ 1.24e-4 and vector_scale = 0.025*sigmoid(-7) ≈ 2.28e-5, with a zero final context layer and only 8 epochs before LR reaches zero. SchNet evidence supports atomwise energy pooling as the direct scalar target path, and Forces-Are-Not-Enough evidence says force accuracy alone is not aligned with downstream/stability metrics; the current benchmark already includes energy, force, gap, and Q, so the next exploit should target energy/gap calibration directly instead of adding another very small vector feedback path.",
      "current_code_insertion_point": [
        "model/model.py::EvolutionMLIP.__init__: add self.energy_residual_head and self.energy_residual_scale_logit; optionally disable or leave final_tp_invariant_mixer unchanged for ablation clarity.",
        "model/model.py::EvolutionMLIP.forward_energy: after vector_norm/scalar_vector_input/readout_norm and before return, add beta * energy_residual.sum() to the scalar energy.",
        "model/train.py::train and run_epoch: no required change; optional companion ablation can slightly raise energy_weight after warmup but should be separate from the model-only card."
      ],
      "bounded_edit": [
        "Add <=25 lines in model/model.py: LayerNorm(hidden_dim*2), Linear(hidden_dim*2, hidden_dim//2), SiLU, Linear(hidden_dim//2,1), zero initialize final layer, and a capped scalar parameter beta <= 0.05.",
        "Use residual_input = torch.cat([scalar_state, vector_norm], dim=-1), not raw vector components, so the residual energy remains invariant.",
        "Initialize residual output exactly zero for source fallback, but avoid the generation_020 double attenuation: if final layer is zero, initialize beta around 0.005-0.02 rather than 1e-4 effective scale, or learn beta with a small positive floor/clamp.",
        "Do not change dataset sampling, benchmark metric fields, remote state, or create a force-only head."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "GEN021-M02-energy-force-loss-rebalancing-control",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_001",
        "paper_artifact:paper_002",
        "repo_artifact:repo_001",
        "current_unit_profile",
        "proposal_context"
      ],
      "concrete_mechanism": "Run a bounded training-objective control that tests whether the neutral generation_020 result is partly an objective-allocation issue: current MAE loss uses force_weight=20 and energy_weight=1 after warmup, so the force term dominates the scalar energy term; SchNet's evidence and SchNetPack's MD17 config explicitly separate energy and force losses, while Forces-Are-Not-Enough warns force accuracy alone is not sufficient. A next-generation exploit can modestly increase late energy emphasis or make the existing warmup less force-heavy without changing architecture.",
      "current_code_insertion_point": [
        "model/train.py::train: lines defining energy_warmup_epochs, warmup_ratio, epoch_energy_weight, epoch_force_weight.",
        "model/train.py::run_epoch: preserve loss_energy/loss_force definitions and only consume new weights.",
        "model/model.py::EvolutionMLIP.forward: preserve energy-to-force autograd."
      ],
      "bounded_edit": [
        "Change only constants/schedule in train.py; no dataset, metric, benchmark, or model architecture edits.",
        "Example bounded schedule: after warmup, set epoch_energy_weight = energy_weight*1.25 and epoch_force_weight = force_weight*0.9, or ramp linearly so final force_weight remains >=16.",
        "Record this as a control/diagnostic proposal, not as a broad architecture jump."
      ],
      "downgrade_reasons": []
    }
  ]
}
```

## new_patch_blueprints_summary

```json
{
  "implementation_ready_blueprints": [
    "GEN021-M01-atomwise-energy-residual-calibration",
    "GEN021-M02-energy-force-loss-rebalancing-control"
  ],
  "blueprints": [
    {
      "blueprint_id": "GEN021-M01-atomwise-energy-residual-calibration",
      "mechanism_id": "GEN021-M01-atomwise-energy-residual-calibration",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py::EvolutionMLIP.__init__: add self.energy_residual_head and self.energy_residual_scale_logit; optionally disable or leave final_tp_invariant_mixer unchanged for ablation clarity.",
        "model/model.py::EvolutionMLIP.forward_energy: after vector_norm/scalar_vector_input/readout_norm and before return, add beta * energy_residual.sum() to the scalar energy.",
        "model/train.py::train and run_epoch: no required change; optional companion ablation can slightly raise energy_weight after warmup but should be separate from the model-only card."
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "GEN021-M02-energy-force-loss-rebalancing-control",
      "mechanism_id": "GEN021-M02-energy-force-loss-rebalancing-control",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/train.py::train: lines defining energy_warmup_epochs, warmup_ratio, epoch_energy_weight, epoch_force_weight.",
        "model/train.py::run_epoch: preserve loss_energy/loss_force definitions and only consume new weights.",
        "model/model.py::EvolutionMLIP.forward: preserve energy-to-force autograd."
      ],
      "blocked_until": []
    }
  ]
}
```

## proposal_constraints

```json
{
  "version": "proposal_constraints.v1",
  "allowed_mechanisms": [
    "GEN021-M01-atomwise-energy-residual-calibration",
    "GEN021-M02-energy-force-loss-rebalancing-control"
  ],
  "weak_or_hypothesis_mechanisms": [],
  "blocked_mechanisms": [
    "unproven model-family label without formula derivation and code trace",
    "force-only proposal when energy/gap/Q context is available",
    "implementation rewrite without patch blueprint"
  ],
  "proposal_can_use_as_strong_evidence": true,
  "required_sections_in_proposal": [
    "mechanism_refs",
    "evidence_refs",
    "historical_relation",
    "why_not_duplicate",
    "files_to_edit",
    "code_insertion_points",
    "minimal_edit_plan",
    "implementation_checklist"
  ]
}
```

## audit_report

```json
{
  "version": "audit_report.v1",
  "issues": [],
  "mechanism_card_count": 2,
  "strong_mechanism_card_count": 2,
  "provenance_record_count": 12
}
```

## what_not_to_use_as_strong_evidence

```json
{
  "weak_or_hypothesis_mechanisms": [],
  "blocked_mechanisms": [
    "unproven model-family label without formula derivation and code trace",
    "force-only proposal when energy/gap/Q context is available",
    "implementation rewrite without patch blueprint"
  ],
  "diagnosis_only": false
}
```

## followup_queries

```json
[
  "Find MLIP papers/repos with lightweight angular features that do not require full equivariance.",
  "Search for compact equivariant MLIP repos with readable training loops."
]
```
