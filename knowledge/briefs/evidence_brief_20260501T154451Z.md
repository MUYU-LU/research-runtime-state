# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-05-01T15:44:52.856547+00:00",
  "mode": "balanced",
  "source_unit": "generation_022/proposal_006",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/evidence_run.json"
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
      "source_expansion_round": 2
    },
    "pdf_attempted_source_count": 1,
    "pdf_successful_source_count": 1,
    "repo_attempted_source_count": 1,
    "repo_successful_source_count": 1,
    "attempted_external_source_count": 2,
    "successful_external_source_count": 2,
    "source_targets_met": true,
    "source_budget_exhausted": true,
    "new_source_count": 2,
    "recent_reused_source_count": 0,
    "new_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4e25u683cu957fu7a0bu8272u6563u795eu7ecfu7f51u7edcu52bf_cb12dadd9e.pdf#e677ecc459d6",
      "repo:RowleyGroup/MLXDM#067f251ba795"
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
  "source_budget_exhausted": true,
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
  "source_unit": "generation_022/proposal_006",
  "context_path": "/home/lmy/.openclaw/workspace/research_runtime/proposals/generation_023_from_generation_022_proposal_006_continuation/context.md",
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_022/proposal_006",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/generation_memory.json",
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
      "success": 1,
      "fresh": 1,
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
    "source_expansion_round": 2
  },
  "pdf_attempted_source_count": 1,
  "pdf_successful_source_count": 1,
  "repo_attempted_source_count": 1,
  "repo_successful_source_count": 1,
  "attempted_external_source_count": 2,
  "successful_external_source_count": 2,
  "source_targets_met": true,
  "source_budget_exhausted": true,
  "new_source_count": 2,
  "recent_reused_source_count": 0,
  "new_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4e25u683cu957fu7a0bu8272u6563u795eu7ecfu7f51u7edcu52bf_cb12dadd9e.pdf#e677ecc459d6",
    "repo:RowleyGroup/MLXDM#067f251ba795"
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
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4e25u683cu957fu7a0bu8272u6563u795eu7ecfu7f51u7edcu52bf_cb12dadd9e.pdf#e677ecc459d6",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/paper_artifacts/paper_001.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:RowleyGroup/MLXDM#067f251ba795",
      "repo": "RowleyGroup/MLXDM",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/repo_artifacts/repo_001.json",
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
    "source_expansion_round": 2
  },
  "source_budget_exhausted": true,
  "source_targets_met": true,
  "artifact_index": {
    "papers": [
      {
        "artifact_ref": "paper_artifact:paper_001",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_u4e25u683cu957fu7a0bu8272u6563u795eu7ecfu7f51u7edcu52bf_cb12dadd9e.pdf#e677ecc459d6",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/paper_artifacts/paper_001.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:RowleyGroup/MLXDM#067f251ba795",
        "repo": "RowleyGroup/MLXDM",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260501T154451Z/repo_artifacts/repo_001.json",
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
    "GEN023-M01-mlxmd-damped-dispersion-tail"
  ],
  "weak_or_hypothesis_mechanisms": [],
  "proposal_allowed_mechanisms": [
    "GEN023-M01-mlxmd-damped-dispersion-tail"
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
    "GEN023-M01-mlxmd-damped-dispersion-tail"
  ],
  "weak_or_hypothesis_ids": [],
  "cards": [
    {
      "mechanism_id": "GEN023-M01-mlxmd-damped-dispersion-tail",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_001",
        "repo_artifact:repo_001",
        "current_unit_profile",
        "proposal_context"
      ],
      "concrete_mechanism": "Add a bounded MLXDM-style damped London-dispersion residual after the existing learned neutral electrostatic q_i q_j term, using positive atomwise coefficient heads from the current residual_input and an i<j pair sum. This is deliberately not another charge-shell edit: it targets missing dispersion tail capacity with a separate attractive pair energy.",
      "current_code_insertion_point": [
        "research_runtime/generations/generation_022/proposal_006/model/model.py::EvolutionMLIP.__init__ around existing charge_head / charge_shell_beta_logits to add dispersion_head, dispersion_scale_logit, and small damping parameters.",
        "research_runtime/generations/generation_022/proposal_006/model/model.py::EvolutionMLIP.forward_energy after charge/electrostatic_pair_energy lines 557-572 and before the final return to compute all-pair damped dispersion_pair_energy.",
        "No required dataloader or benchmark semantic changes; train.py can remain unchanged because force autograd follows from total energy. Optional but not required: add a small log field only if existing training logging already supports extra components."
      ],
      "bounded_edit": [
        "In __init__, add self.dispersion_head = nn.Sequential(nn.LayerNorm(hidden_dim*2), nn.Linear(hidden_dim*2, hidden_dim//2), nn.SiLU(), nn.Linear(hidden_dim//2, 3)); initialize final layer near zero; add self.dispersion_scale_logit initialized to a negative value and cap scale around 1e-4 to 1e-3 in current energy units.",
        "In forward_energy, compute coeff_atom = softplus(self.dispersion_head(residual_input)) + 1e-6; split c6_atom,c8_atom,c10_atom; form i_pair,j_pair = torch.triu_indices(N,N,1,device=positions.device); d_pair = norm(positions[i_pair]-positions[j_pair]); pair coefficients = sqrt(cn_i*cn_j + eps).",
        "Compute rcrit/rvdw with eps-clamped ratios; e_disp_raw = -sum(c6/(d^6+rvdw^6)+c8/(d^8+rvdw^8)+c10/(d^10+rvdw^10)); dispersion_pair_energy = disp_cap*sigmoid(scale_logit)*e_disp_raw; add it after electrostatic_pair_energy.",
        "Guardrails: if N<2 return zero dispersion; clamp d_pair >= 1e-4; cap global scale; do not alter Q metric, dataset split, force loss, or neighbor-list semantics used by the existing message passing.",
        "Ablate with full term enabled vs scale forced to zero; if instability appears, fallback to C6-only by zeroing C8/C10 scale while retaining the same code path."
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
    "GEN023-M01-mlxmd-damped-dispersion-tail"
  ],
  "blueprints": [
    {
      "blueprint_id": "GEN023-M01-mlxmd-damped-dispersion-tail",
      "mechanism_id": "GEN023-M01-mlxmd-damped-dispersion-tail",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_022/proposal_006/model/model.py::EvolutionMLIP.__init__ around existing charge_head / charge_shell_beta_logits to add dispersion_head, dispersion_scale_logit, and small damping parameters.",
        "research_runtime/generations/generation_022/proposal_006/model/model.py::EvolutionMLIP.forward_energy after charge/electrostatic_pair_energy lines 557-572 and before the final return to compute all-pair damped dispersion_pair_energy.",
        "No required dataloader or benchmark semantic changes; train.py can remain unchanged because force autograd follows from total energy. Optional but not required: add a small log field only if existing training logging already supports extra components."
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
    "GEN023-M01-mlxmd-damped-dispersion-tail"
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
