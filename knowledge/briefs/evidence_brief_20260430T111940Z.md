# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-04-30T11:19:46.551034+00:00",
  "mode": "balanced",
  "source_unit": "generation_018/proposal_005",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/evidence_run.json"
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
  "min_strong_mechanism_cards": 2,
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
      "min_strong_mechanism_cards": 2,
      "max_pdf_attempts": 6,
      "max_repo_attempts": 4,
      "max_external_source_attempts": 10,
      "max_source_expansion_rounds": 2,
      "source_expansion_round": 2
    },
    "pdf_attempted_source_count": 3,
    "pdf_successful_source_count": 3,
    "repo_attempted_source_count": 3,
    "repo_successful_source_count": 3,
    "attempted_external_source_count": 6,
    "successful_external_source_count": 6,
    "source_targets_met": true,
    "source_budget_exhausted": true,
    "new_source_count": 6,
    "recent_reused_source_count": 0,
    "new_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_TACEu7b1bu5361u5c14u7a7au95f4u5f20u91cfu539fu5b50u7c07u5c55u5f00_e9ab8f4246.pdf#35cab3944e7c",
      "repo:torchmd/torchmd-net#e0cf6c6d162e",
      "repo:BingqingCheng/cace#a6c88223e724",
      "repo:ACEsuit/mace#99833dea34c0"
    ],
    "recent_reused_source_ids": [],
    "recent_attempted_reused_source_count": 3,
    "recent_attempted_reused_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
      "repo:ACEsuit/mace#99833dea34c0"
    ],
    "reuse_semantics": "recent_reused_source_ids counts sources used as strong evidence in recent runs. recent_attempted_reused_source_ids is diagnostic only and does not fail novelty by itself.",
    "all_sources_recent_repeats": false,
    "source_novelty_passed": true,
    "allow_recent_source_reuse": false
  },
  "external_attempted_source_count": 6,
  "external_successful_source_count": 6,
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
  "source_unit": "generation_018/proposal_005",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_018/proposal_005",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/generation_memory.json",
  "generation_memory": {
    "version": "generation_memory.v1",
    "source_unit": "generation_018/proposal_005",
    "last_completed_generation": "generation_018",
    "ignored_legacy_source_count": 4,
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
      "total": 3,
      "success": 3,
      "fresh": 3,
      "can_support_strong": 3
    },
    "repo_code": {
      "total": 3,
      "success": 3,
      "fresh": 3,
      "can_support_strong": 3
    }
  },
  "strong_capable_sources": [
    "paper_artifact:paper_001",
    "paper_artifact:paper_002",
    "paper_artifact:paper_003",
    "repo_artifact:repo_001",
    "repo_artifact:repo_002",
    "repo_artifact:repo_003"
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
    "min_strong_mechanism_cards": 2,
    "max_pdf_attempts": 6,
    "max_repo_attempts": 4,
    "max_external_source_attempts": 10,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 2
  },
  "pdf_attempted_source_count": 3,
  "pdf_successful_source_count": 3,
  "repo_attempted_source_count": 3,
  "repo_successful_source_count": 3,
  "attempted_external_source_count": 6,
  "successful_external_source_count": 6,
  "source_targets_met": true,
  "source_budget_exhausted": true,
  "new_source_count": 6,
  "recent_reused_source_count": 0,
  "new_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_TACEu7b1bu5361u5c14u7a7au95f4u5f20u91cfu539fu5b50u7c07u5c55u5f00_e9ab8f4246.pdf#35cab3944e7c",
    "repo:torchmd/torchmd-net#e0cf6c6d162e",
    "repo:BingqingCheng/cace#a6c88223e724",
    "repo:ACEsuit/mace#99833dea34c0"
  ],
  "recent_reused_source_ids": [],
  "recent_attempted_reused_source_count": 3,
  "recent_attempted_reused_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
    "repo:ACEsuit/mace#99833dea34c0"
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
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/paper_artifacts/paper_001.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_002",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/paper_artifacts/paper_002.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_003",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_TACEu7b1bu5361u5c14u7a7au95f4u5f20u91cfu539fu5b50u7c07u5c55u5f00_e9ab8f4246.pdf#35cab3944e7c",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/paper_artifacts/paper_003.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:torchmd/torchmd-net#e0cf6c6d162e",
      "repo": "torchmd/torchmd-net",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/repo_artifacts/repo_001.json",
      "success": true
    },
    {
      "artifact_ref": "repo_artifact:repo_002",
      "source_id": "repo:BingqingCheng/cace#a6c88223e724",
      "repo": "BingqingCheng/cace",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/repo_artifacts/repo_002.json",
      "success": true
    },
    {
      "artifact_ref": "repo_artifact:repo_003",
      "source_id": "repo:ACEsuit/mace#99833dea34c0",
      "repo": "ACEsuit/mace",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/repo_artifacts/repo_003.json",
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
    "min_strong_mechanism_cards": 2,
    "max_pdf_attempts": 6,
    "max_repo_attempts": 4,
    "max_external_source_attempts": 10,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 2
  },
  "source_budget_exhausted": true,
  "source_targets_met": true,
  "artifact_index": {
    "papers": [
      {
        "artifact_ref": "paper_artifact:paper_001",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/paper_artifacts/paper_001.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_002",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/paper_artifacts/paper_002.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_003",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_TACEu7b1bu5361u5c14u7a7au95f4u5f20u91cfu539fu5b50u7c07u5c55u5f00_e9ab8f4246.pdf#35cab3944e7c",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/paper_artifacts/paper_003.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:torchmd/torchmd-net#e0cf6c6d162e",
        "repo": "torchmd/torchmd-net",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/repo_artifacts/repo_001.json",
        "success": true
      },
      {
        "artifact_ref": "repo_artifact:repo_002",
        "source_id": "repo:BingqingCheng/cace#a6c88223e724",
        "repo": "BingqingCheng/cace",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/repo_artifacts/repo_002.json",
        "success": true
      },
      {
        "artifact_ref": "repo_artifact:repo_003",
        "source_id": "repo:ACEsuit/mace#99833dea34c0",
        "repo": "ACEsuit/mace",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T111940Z/repo_artifacts/repo_003.json",
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
    "GEN019-M01-rank2-cartesian-tp-sibling",
    "GEN019-M02-cace-nu2-ab-consistency"
  ],
  "weak_or_hypothesis_mechanisms": [],
  "proposal_allowed_mechanisms": [
    "GEN019-M01-rank2-cartesian-tp-sibling",
    "GEN019-M02-cace-nu2-ab-consistency"
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
    "GEN019-M01-rank2-cartesian-tp-sibling",
    "GEN019-M02-cace-nu2-ab-consistency"
  ],
  "weak_or_hypothesis_ids": [],
  "cards": [
    {
      "mechanism_id": "GEN019-M01-rank2-cartesian-tp-sibling",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_001",
        "repo_artifact:repo_001",
        "current_unit_profile",
        "proposal_context"
      ],
      "concrete_mechanism": "Exploit generation_018/proposal_005 by preserving TPInteractionBranch's explicit l=0/l=1 scalar-vector tensor-product messages and adding a near-zero, separately-scaled rank-2 Cartesian symmetric-traceless sibling. External HotPP/TensorNet evidence supports Cartesian tensor contraction as a direct generalization: scalar I, vector/antisymmetric A, and symmetric traceless S channels are produced from radial edge weights and unit-vector geometry. The generation_019 edit should keep the existing w_ss/w_vs/w_sv/w_vp/w_vself branch unchanged, add an S-channel residual with its own logit initialized near zero, and gate its scalar/readout influence from the existing scalar state so the frontier TP win is not overwritten.",
      "current_code_insertion_point": [
        "research_runtime/generations/generation_018/proposal_005/model/model.py:TPInteractionBranch.__init__ add rank2_edge_mlp or extend edge_mlp output and rank2_residual_logit",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:TPInteractionBranch.forward after radial_weights.unbind compute S(unit), agg_rank2, and rank2-gated scalar delta",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:EvolutionMLIP.forward_energy loop keep existing scalar/vector residual combine; add rank2 scalar residual only if returned by branch",
        "research_runtime/generations/generation_018/proposal_005/model/train.py no required contract change; preserve energy_weight=1.0, force_weight=20.0, grad_clip=3.0, metrics names"
      ],
      "bounded_edit": [
        "Do not remove or reinitialize existing TPInteractionBranch scalar/vector paths; add rank2 path as near-zero residual with independent logit and tiny output init.",
        "Keep hidden_dim=96, num_rbf=32, cutoff=5.0, num_interactions=2 unless proposal explicitly budgets a runtime increase.",
        "Use pure torch operations shaped [E,H,5] -> [N,H,5] -> [N,H]; avoid adding Warp/e3nn dependencies.",
        "Add an ablation switch by setting rank2_residual_logit very negative or exposing a config flag; control must compare against generation_018/proposal_005."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "GEN019-M02-cace-nu2-ab-consistency",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_002",
        "repo_artifact:repo_002",
        "repo_artifact:repo_003",
        "current_unit_profile",
        "proposal_context"
      ],
      "concrete_mechanism": "Branch-diversifying alternative: keep the winning TPInteractionBranch unchanged but audit and tighten BodyOrderMessageBranch into a CACE-consistent ν=2 Cartesian A/B descriptor path. The current unit already has a CACE-inspired side path and a damped body_order_readout; generation_019 should make the angular monomial set and symmetrization match external CACE evidence, optionally adding a tiny product-basis/symmetric-contraction block, while preserving the small body_order_multiplier. This targets ISO17 energy/gap generalization rather than repeating generation_017's PaiNN/body-order/norm-dot/readout-damping local repairs.",
      "current_code_insertion_point": [
        "research_runtime/generations/generation_018/proposal_005/model/model.py:BodyOrderMessageBranch._angular_monomials audit the l<=2 Cartesian basis to exactly [1,x,y,z,x^2,y^2,z^2,xy,xz,yz] and keep num_angular consistent",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:BodyOrderMessageBranch._symmetrize replace ad-hoc slices only if needed with documented CACE ν=1/ν=2 contractions; preserve descriptor_dim or add a projection back to descriptor_dim",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:BodyOrderMessageBranch.forward after atom_a normalization optionally apply a tiny product-basis/symmetric-contraction projection before message_norm",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:EvolutionMLIP.forward_energy body_order_readout/body_order_multiplier keep damped scalar energy residual",
        "research_runtime/generations/generation_018/proposal_005/model/train.py preserve loss schedule and metric logging; no evaluator-specific ISO17-only weighting change"
      ],
      "bounded_edit": [
        "Do not remove TPInteractionBranch or change the main BalancedInteractionBlock; this is a side-branch diversification only.",
        "If fixing angular basis changes descriptor shape, project back to the existing descriptor_dim=128 and initialize added projection near zero.",
        "Keep body_order_multiplier small/learnable; do not add readout damping-only repairs or ISO17-only loss hacks.",
        "Use local PyTorch loops/einsum for at most ν=2 or a tiny selected product basis; avoid e3nn dependency and avoid increasing num_interactions."
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
    "GEN019-M01-rank2-cartesian-tp-sibling",
    "GEN019-M02-cace-nu2-ab-consistency"
  ],
  "blueprints": [
    {
      "blueprint_id": "GEN019-M01-rank2-cartesian-tp-sibling",
      "mechanism_id": "GEN019-M01-rank2-cartesian-tp-sibling",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_018/proposal_005/model/model.py:TPInteractionBranch.__init__ add rank2_edge_mlp or extend edge_mlp output and rank2_residual_logit",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:TPInteractionBranch.forward after radial_weights.unbind compute S(unit), agg_rank2, and rank2-gated scalar delta",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:EvolutionMLIP.forward_energy loop keep existing scalar/vector residual combine; add rank2 scalar residual only if returned by branch",
        "research_runtime/generations/generation_018/proposal_005/model/train.py no required contract change; preserve energy_weight=1.0, force_weight=20.0, grad_clip=3.0, metrics names"
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "GEN019-M02-cace-nu2-ab-consistency",
      "mechanism_id": "GEN019-M02-cace-nu2-ab-consistency",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_018/proposal_005/model/model.py:BodyOrderMessageBranch._angular_monomials audit the l<=2 Cartesian basis to exactly [1,x,y,z,x^2,y^2,z^2,xy,xz,yz] and keep num_angular consistent",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:BodyOrderMessageBranch._symmetrize replace ad-hoc slices only if needed with documented CACE ν=1/ν=2 contractions; preserve descriptor_dim or add a projection back to descriptor_dim",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:BodyOrderMessageBranch.forward after atom_a normalization optionally apply a tiny product-basis/symmetric-contraction projection before message_norm",
        "research_runtime/generations/generation_018/proposal_005/model/model.py:EvolutionMLIP.forward_energy body_order_readout/body_order_multiplier keep damped scalar energy residual",
        "research_runtime/generations/generation_018/proposal_005/model/train.py preserve loss schedule and metric logging; no evaluator-specific ISO17-only weighting change"
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
    "GEN019-M01-rank2-cartesian-tp-sibling",
    "GEN019-M02-cace-nu2-ab-consistency"
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
  "provenance_record_count": 15
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
