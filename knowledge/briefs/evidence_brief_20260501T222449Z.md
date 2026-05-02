# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-05-01T22:24:50.589809+00:00",
  "mode": "balanced",
  "source_unit": "generation_023/proposal_004",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/evidence_run.json"
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
  "strong_mechanism_card_count": 1,
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
      "max_pdf_attempts": 4,
      "max_repo_attempts": 3,
      "max_external_source_attempts": 6,
      "max_source_expansion_rounds": 2,
      "source_expansion_round": 1
    },
    "pdf_attempted_source_count": 1,
    "pdf_successful_source_count": 1,
    "repo_attempted_source_count": 1,
    "repo_successful_source_count": 1,
    "attempted_external_source_count": 2,
    "successful_external_source_count": 2,
    "source_targets_met": true,
    "source_budget_exhausted": false,
    "new_source_count": 2,
    "recent_reused_source_count": 0,
    "new_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu4f53u7cfb_-_Sum-of-Gaussiansu957fu7a0bu673au5668u5b66u4e60u52bf_68a044b310.pdf#6ead2254c93b",
      "repo:DuktigYajie/SOG-Net#f5e17730da3e"
    ],
    "recent_reused_source_ids": [],
    "recent_attempted_reused_source_count": 0,
    "recent_attempted_reused_source_ids": [],
    "reuse_semantics": "recent_reused_source_ids counts sources used as strong evidence in recent runs. recent_attempted_reused_source_ids is diagnostic only and does not fail novelty by itself.",
    "all_sources_recent_repeats": false,
    "source_novelty_passed": true,
    "allow_recent_source_reuse": false
  },
  "external_attempted_source_count": 2,
  "external_successful_source_count": 2,
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
  "source_unit": "generation_023/proposal_004",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_023/proposal_004",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/generation_memory.json",
  "generation_memory": {
    "version": "generation_memory.v1",
    "source_unit": "generation_023/proposal_004",
    "last_completed_generation": "generation_023",
    "ignored_legacy_source_count": 9,
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
      "total": 1,
      "success": 1,
      "fresh": 1,
      "can_support_strong": 1
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
    "max_pdf_attempts": 4,
    "max_repo_attempts": 3,
    "max_external_source_attempts": 6,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 1
  },
  "pdf_attempted_source_count": 1,
  "pdf_successful_source_count": 1,
  "repo_attempted_source_count": 1,
  "repo_successful_source_count": 1,
  "attempted_external_source_count": 2,
  "successful_external_source_count": 2,
  "source_targets_met": true,
  "source_budget_exhausted": false,
  "new_source_count": 2,
  "recent_reused_source_count": 0,
  "new_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu4f53u7cfb_-_Sum-of-Gaussiansu957fu7a0bu673au5668u5b66u4e60u52bf_68a044b310.pdf#6ead2254c93b",
    "repo:DuktigYajie/SOG-Net#f5e17730da3e"
  ],
  "recent_reused_source_ids": [],
  "recent_attempted_reused_source_count": 0,
  "recent_attempted_reused_source_ids": [],
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
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu4f53u7cfb_-_Sum-of-Gaussiansu957fu7a0bu673au5668u5b66u4e60u52bf_68a044b310.pdf#6ead2254c93b",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/paper_artifacts/paper_001.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:DuktigYajie/SOG-Net#f5e17730da3e",
      "repo": "DuktigYajie/SOG-Net",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/repo_artifacts/repo_001.json",
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
    "max_pdf_attempts": 4,
    "max_repo_attempts": 3,
    "max_external_source_attempts": 6,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 1
  },
  "source_budget_exhausted": false,
  "source_targets_met": true,
  "artifact_index": {
    "papers": [
      {
        "artifact_ref": "paper_artifact:paper_001",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu4f53u7cfb_-_Sum-of-Gaussiansu957fu7a0bu673au5668u5b66u4e60u52bf_68a044b310.pdf#6ead2254c93b",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/paper_artifacts/paper_001.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:DuktigYajie/SOG-Net#f5e17730da3e",
        "repo": "DuktigYajie/SOG-Net",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T222449Z/repo_artifacts/repo_001.json",
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
    "GEN024-M01-adaptive-sog-realspace-latent-tail"
  ],
  "weak_or_hypothesis_mechanisms": [],
  "proposal_allowed_mechanisms": [
    "GEN024-M01-adaptive-sog-realspace-latent-tail"
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
    "GEN024-M01-adaptive-sog-realspace-latent-tail"
  ],
  "weak_or_hypothesis_ids": [],
  "cards": [
    {
      "mechanism_id": "GEN024-M01-adaptive-sog-realspace-latent-tail",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_001",
        "repo_artifact:repo_001",
        "current_unit_profile",
        "generation_memory"
      ],
      "concrete_mechanism": "Continue from generation_023/proposal_004 by treating its fixed two-sigma LES all-pair latent-charge tail as an ablation baseline, then test a bounded nonperiodic real-space Sum-of-Gaussians (SOG) q_i q_j tail with a few log-spaced Gaussian bandwidths and tiny capped trainable amplitudes. This transfers SOG-Net's adaptive LR-decay mechanism while avoiding the paper/repo's full periodic FFT/NUFFT machinery, cell inputs, and large-system assumptions that are outside the current molecule benchmark contract.",
      "current_code_insertion_point": [
        "model/model.py::EvolutionMLIP.__init__ lines 469-475: current proposal_004 defines les_tail_beta_logits, les_tail_beta_caps, and fixed les_tail_sigmas=[0.8,2.0]. A proposal may add sog_tail_log_widths and capped sog_tail_weight_logits or replace the two fixed sigmas with M=3-4 log-spaced Gaussian widths under a total near-zero gate.",
        "model/model.py::EvolutionMLIP.forward_energy lines 566-594: reuse charge_raw/neutral charge and the all_rij/all_dij/nonself tensors; replace les_kernels=torch.erf(...)/d with a small Gaussian-bank kernel exp(-d^2/s_l^2) and a tiny capped sum over l.",
        "model/model.py final energy return lines 596-603: add E_sog exactly where les_tail_energy is now added, preserving autograd force consistency.",
        "model/train.py: no semantic change; keep the same RMD17/ISO17 train/eval fields and energy/force losses."
      ],
      "bounded_edit": [
        "Do not add cell, periodic PBC, reciprocal grids, NUFFT/FINUFFT/TensorFlow dependencies, charge labels, or a new data contract.",
        "Keep the source fallback exact: the new SOG tail must have a zero or near-zero capped gate so proposal_004 behavior is recovered when the gate is zero.",
        "Use a small M (3 or 4) log-spaced Gaussian bank instead of the repo's 12-bandwidth/default large-system setting; this is evidence for a bounded molecule benchmark probe, not a full SOG-Net port.",
        "Prefer replacing the current fixed two-sigma LES all-pair tail or adding the SOG branch behind a separate tiny cap; do not simultaneously introduce unrelated architecture/loss changes.",
        "Keep total LR scale no larger than the current combined LES caps until a proposal writer justifies otherwise from controls; monitor runtime due to O(N^2*M) all-pair work."
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
    "GEN024-M01-adaptive-sog-realspace-latent-tail"
  ],
  "blueprints": [
    {
      "blueprint_id": "GEN024-M01-adaptive-sog-realspace-latent-tail",
      "mechanism_id": "GEN024-M01-adaptive-sog-realspace-latent-tail",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py::EvolutionMLIP.__init__ lines 469-475: current proposal_004 defines les_tail_beta_logits, les_tail_beta_caps, and fixed les_tail_sigmas=[0.8,2.0]. A proposal may add sog_tail_log_widths and capped sog_tail_weight_logits or replace the two fixed sigmas with M=3-4 log-spaced Gaussian widths under a total near-zero gate.",
        "model/model.py::EvolutionMLIP.forward_energy lines 566-594: reuse charge_raw/neutral charge and the all_rij/all_dij/nonself tensors; replace les_kernels=torch.erf(...)/d with a small Gaussian-bank kernel exp(-d^2/s_l^2) and a tiny capped sum over l.",
        "model/model.py final energy return lines 596-603: add E_sog exactly where les_tail_energy is now added, preserving autograd force consistency.",
        "model/train.py: no semantic change; keep the same RMD17/ISO17 train/eval fields and energy/force losses."
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
    "GEN024-M01-adaptive-sog-realspace-latent-tail"
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
  "mechanism_card_count": 1,
  "strong_mechanism_card_count": 1,
  "provenance_record_count": 11
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
