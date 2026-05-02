# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-05-01T15:43:03.761221+00:00",
  "mode": "balanced",
  "source_unit": "generation_022/proposal_006",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/evidence_run.json"
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
  "grade": "C",
  "fresh_local_pdf_verified": true,
  "fresh_repo_code_verified": true,
  "has_mechanism_cards": true,
  "has_strong_mechanism_cards": false,
  "strong_mechanism_card_count": 0,
  "min_strong_mechanism_cards": 1,
  "strong_card_target_met": false,
  "has_patch_blueprints": true,
  "has_implementation_ready_blueprints": false,
  "usable_for_proposal": false,
  "usable_for_implementation": false,
  "diagnosis_only": true,
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
    "new_source_count": 0,
    "recent_reused_source_count": 2,
    "new_source_ids": [],
    "recent_reused_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4eceu80fdu91cfu548cu529bu5b66u4e60u7535u8377u4e0eu957fu7a0bu4f5cu7528_2fa85a146f.pdf#11bc8f1e3595",
      "repo:BingqingCheng/cace#a6c88223e724"
    ],
    "recent_attempted_reused_source_count": 2,
    "recent_attempted_reused_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4eceu80fdu91cfu548cu529bu5b66u4e60u7535u8377u4e0eu957fu7a0bu4f5cu7528_2fa85a146f.pdf#11bc8f1e3595",
      "repo:BingqingCheng/cace#a6c88223e724"
    ],
    "reuse_semantics": "recent_reused_source_ids counts sources used as strong evidence in recent runs. recent_attempted_reused_source_ids is diagnostic only and does not fail novelty by itself.",
    "all_sources_recent_repeats": true,
    "source_novelty_passed": false,
    "allow_recent_source_reuse": false
  },
  "external_attempted_source_count": 2,
  "external_successful_source_count": 2,
  "source_novelty_passed": false,
  "source_budget_exhausted": false,
  "needs_source_expansion": true,
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
  "source_unit": "generation_022/proposal_006",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_022/proposal_006",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/generation_memory.json",
  "generation_memory": {
    "version": "generation_memory.v1",
    "source_unit": "generation_022/proposal_006",
    "last_completed_generation": "generation_022",
    "ignored_legacy_source_count": 8,
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
  "new_source_count": 0,
  "recent_reused_source_count": 2,
  "new_source_ids": [],
  "recent_reused_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4eceu80fdu91cfu548cu529bu5b66u4e60u7535u8377u4e0eu957fu7a0bu4f5cu7528_2fa85a146f.pdf#11bc8f1e3595",
    "repo:BingqingCheng/cace#a6c88223e724"
  ],
  "recent_attempted_reused_source_count": 2,
  "recent_attempted_reused_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4eceu80fdu91cfu548cu529bu5b66u4e60u7535u8377u4e0eu957fu7a0bu4f5cu7528_2fa85a146f.pdf#11bc8f1e3595",
    "repo:BingqingCheng/cace#a6c88223e724"
  ],
  "reuse_semantics": "recent_reused_source_ids counts sources used as strong evidence in recent runs. recent_attempted_reused_source_ids is diagnostic only and does not fail novelty by itself.",
  "all_sources_recent_repeats": true,
  "source_novelty_passed": false,
  "allow_recent_source_reuse": false
}
```

## source_artifacts

```json
{
  "papers": [
    {
      "artifact_ref": "paper_artifact:paper_001",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4eceu80fdu91cfu548cu529bu5b66u4e60u7535u8377u4e0eu957fu7a0bu4f5cu7528_2fa85a146f.pdf#11bc8f1e3595",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/paper_artifacts/paper_001.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:BingqingCheng/cace#a6c88223e724",
      "repo": "BingqingCheng/cace",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/repo_artifacts/repo_001.json",
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
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4eceu80fdu91cfu548cu529bu5b66u4e60u7535u8377u4e0eu957fu7a0bu4f5cu7528_2fa85a146f.pdf#11bc8f1e3595",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/paper_artifacts/paper_001.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:BingqingCheng/cace#a6c88223e724",
        "repo": "BingqingCheng/cace",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154302Z/repo_artifacts/repo_001.json",
        "success": true
      }
    ]
  }
}
```

## what_is_new_for_proposal

```json
{
  "usable_for_proposal": false,
  "usable_for_implementation": false,
  "diagnosis_only": true,
  "strong_mechanisms": [],
  "weak_or_hypothesis_mechanisms": [
    "HYP-B001",
    "HYP-B002",
    "HYP-B003"
  ],
  "proposal_allowed_mechanisms": [],
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
  "strong_mechanism_ids": [],
  "weak_or_hypothesis_ids": [
    "HYP-B001",
    "HYP-B002",
    "HYP-B003"
  ],
  "cards": [
    {
      "mechanism_id": "HYP-B001",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "current_unit_profile",
        "proposal_context"
      ],
      "concrete_mechanism": "Use current profile to target loss, data mix, and evaluation gaps.",
      "current_code_insertion_point": [
        "model/model.py",
        "model/train.py"
      ],
      "bounded_edit": [
        "Requires key-file repo evidence before implementation."
      ],
      "downgrade_reasons": [
        "no strong provenance source",
        "no current-run artifact source_ref",
        "missing formula_derivation",
        "missing tensor_shapes_or_data_flow",
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "mechanism_id": "HYP-B002",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "current_unit_profile",
        "proposal_context"
      ],
      "concrete_mechanism": "Evaluate angular or three-body features for force accuracy on chemically distinct local environments.",
      "current_code_insertion_point": [
        "model/model.py",
        "model/train.py"
      ],
      "bounded_edit": [
        "Requires key-file repo evidence before implementation."
      ],
      "downgrade_reasons": [
        "no strong provenance source",
        "no current-run artifact source_ref",
        "missing formula_derivation",
        "missing tensor_shapes_or_data_flow",
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "mechanism_id": "HYP-B003",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "current_unit_profile",
        "proposal_context"
      ],
      "concrete_mechanism": "Compare a minimal E(3)-equivariant candidate against the current invariant baseline.",
      "current_code_insertion_point": [
        "model/model.py",
        "model/train.py"
      ],
      "bounded_edit": [
        "Requires key-file repo evidence before implementation."
      ],
      "downgrade_reasons": [
        "no strong provenance source",
        "no current-run artifact source_ref",
        "missing formula_derivation",
        "missing tensor_shapes_or_data_flow",
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    }
  ]
}
```

## new_patch_blueprints_summary

```json
{
  "implementation_ready_blueprints": [],
  "blueprints": [
    {
      "blueprint_id": "PB-B001",
      "mechanism_id": "HYP-B001",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py",
        "model/train.py"
      ],
      "blocked_until": [
        "no strong provenance source",
        "no current-run artifact source_ref",
        "missing formula_derivation",
        "missing tensor_shapes_or_data_flow",
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "blueprint_id": "PB-B002",
      "mechanism_id": "HYP-B002",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py",
        "model/train.py"
      ],
      "blocked_until": [
        "no strong provenance source",
        "no current-run artifact source_ref",
        "missing formula_derivation",
        "missing tensor_shapes_or_data_flow",
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "blueprint_id": "PB-B003",
      "mechanism_id": "HYP-B003",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py",
        "model/train.py"
      ],
      "blocked_until": [
        "no strong provenance source",
        "no current-run artifact source_ref",
        "missing formula_derivation",
        "missing tensor_shapes_or_data_flow",
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    }
  ]
}
```

## proposal_constraints

```json
{
  "version": "proposal_constraints.v1",
  "allowed_mechanisms": [],
  "weak_or_hypothesis_mechanisms": [
    "HYP-B001",
    "HYP-B002",
    "HYP-B003"
  ],
  "blocked_mechanisms": [
    "unproven model-family label without formula derivation and code trace",
    "force-only proposal when energy/gap/Q context is available",
    "implementation rewrite without patch blueprint"
  ],
  "proposal_can_use_as_strong_evidence": false,
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
  "issues": [
    "No mechanism card passed strong-evidence validation.",
    "Source novelty policy failed; the run did not add enough new external sources or repeated recent sources too heavily.",
    "Package is not proposal-ready; it lacks at least one mechanism with provenance, formula derivation, code trace, insertion point, and bounded edit."
  ],
  "mechanism_card_count": 3,
  "strong_mechanism_card_count": 0,
  "provenance_record_count": 11
}
```

## what_not_to_use_as_strong_evidence

```json
{
  "weak_or_hypothesis_mechanisms": [
    "HYP-B001",
    "HYP-B002",
    "HYP-B003"
  ],
  "blocked_mechanisms": [
    "unproven model-family label without formula derivation and code trace",
    "force-only proposal when energy/gap/Q context is available",
    "implementation rewrite without patch blueprint"
  ],
  "diagnosis_only": true
}
```

## followup_queries

```json
[
  "Find MLIP papers/repos with lightweight angular features that do not require full equivariance.",
  "Search for compact equivariant MLIP repos with readable training loops."
]
```
