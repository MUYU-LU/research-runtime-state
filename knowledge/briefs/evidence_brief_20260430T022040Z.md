# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-04-30T02:21:59.077098+00:00",
  "mode": "jump",
  "source_unit": "generation_016/proposal_002",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/evidence_run.json"
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
  "strong_mechanism_card_count": 4,
  "min_strong_mechanism_cards": 3,
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
      "min_attempted_external_sources": 8,
      "min_new_sources": 3,
      "max_recent_reused_sources": 5,
      "reuse_justification": "Recent failed packages are explicitly diagnosis-only. Reuse is allowed only to re-deep-read repositories after the clone/cache fix and to extract mechanisms not promoted from those failed packages."
    },
    "source_discovery_budget": {
      "min_successful_pdf_sources": 3,
      "min_successful_repo_sources": 3,
      "min_strong_mechanism_cards": 3,
      "max_pdf_attempts": 4,
      "max_repo_attempts": 4,
      "max_external_source_attempts": 8,
      "max_source_expansion_rounds": 2,
      "source_expansion_round": 1
    },
    "pdf_attempted_source_count": 4,
    "pdf_successful_source_count": 4,
    "repo_attempted_source_count": 4,
    "repo_successful_source_count": 4,
    "attempted_external_source_count": 8,
    "successful_external_source_count": 8,
    "source_targets_met": true,
    "source_budget_exhausted": true,
    "new_source_count": 4,
    "recent_reused_source_count": 4,
    "new_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu57fau7840u6a21u578b_-_MACE-MPu539fu5b50u6750u6599u5316u5b66u57fau7840u6a21u578b_2500f8644a.pdf#5aaf69b35fb9",
      "repo:thorben-frank/euclidean_fast_attention#da8923302a31",
      "repo:ACESuit/mace#059fbdc41b25",
      "repo:CederGroupHub/chgnet#2248a04aa729"
    ],
    "recent_reused_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu6ce8u610fu529b_-_EFAu6b27u6c0fu5febu901fu6ce8u610fu529bu5168u5c40u539fu5b50u8868u793a_0ef43a7c38.pdf#9b564004b09e",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u8badu7ec3_-_NequIPu9ad8u6027u80fdu8badu7ec3u63a8u7406u6df1u5ea6u7b49u53d8u539fu5b50u95f4u52bf_63e6df2008.pdf#a4fb3c313353",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu901au7528u52bf_-_CHGNetu7535u8377u611fu77e5u9884u8badu7ec3u795eu7ecfu7f51u7edcu52bf_7d8d76686d.pdf#9d970111678e",
      "repo:mir-group/nequip#ba95170e90de"
    ],
    "all_sources_recent_repeats": false,
    "source_novelty_passed": true,
    "allow_recent_source_reuse": false
  },
  "external_attempted_source_count": 8,
  "external_successful_source_count": 8,
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
  "source_unit": "generation_016/proposal_002",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_016/proposal_002",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/generation_memory.json",
  "generation_memory": {
    "version": "generation_memory.v1",
    "source_unit": "generation_016/proposal_002",
    "last_completed_generation": "generation_017",
    "ignored_legacy_source_count": 3,
    "completed_generation_count_for_source": 1,
    "recent_attempt_count_for_source": 8,
    "unit_card_count_for_source": 8,
    "negative_pattern_count_for_source": 0,
    "partial_positive_pattern_count_for_source": 0,
    "latest_generation": "generation_017",
    "latest_best_child": {
      "unit": "generation_017/proposal_003",
      "Q_rmd17": 4.087588139313619,
      "Q_iso17": 3.602184007105058,
      "Q_total": 3.9176966930406225,
      "outcome_class": "neutral_variance"
    },
    "latest_outcome_counts": {
      "benchmark_tradeoff": 5,
      "control_replicate": 2,
      "neutral_variance": 1
    },
    "latest_lessons": [
      "No child beat parent generation_016/proposal_002; keep parent unless a reviewed override is chosen."
    ],
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
      "success": 2,
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
      "total": 4,
      "success": 4,
      "fresh": 4,
      "can_support_strong": 4
    },
    "repo_code": {
      "total": 4,
      "success": 4,
      "fresh": 4,
      "can_support_strong": 4
    }
  },
  "strong_capable_sources": [
    "paper_artifact:paper_001",
    "paper_artifact:paper_002",
    "paper_artifact:paper_003",
    "paper_artifact:paper_004",
    "repo_artifact:repo_001",
    "repo_artifact:repo_002",
    "repo_artifact:repo_003",
    "repo_artifact:repo_004"
  ],
  "failed_sources": [
    {
      "source_id": "proposal_context",
      "type": "local_runtime_context",
      "notes": "Benchmark and history context. Useful for diagnosis, not external mechanism support."
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
    "min_attempted_external_sources": 8,
    "min_new_sources": 3,
    "max_recent_reused_sources": 5,
    "reuse_justification": "Recent failed packages are explicitly diagnosis-only. Reuse is allowed only to re-deep-read repositories after the clone/cache fix and to extract mechanisms not promoted from those failed packages."
  },
  "source_discovery_budget": {
    "min_successful_pdf_sources": 3,
    "min_successful_repo_sources": 3,
    "min_strong_mechanism_cards": 3,
    "max_pdf_attempts": 4,
    "max_repo_attempts": 4,
    "max_external_source_attempts": 8,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 1
  },
  "pdf_attempted_source_count": 4,
  "pdf_successful_source_count": 4,
  "repo_attempted_source_count": 4,
  "repo_successful_source_count": 4,
  "attempted_external_source_count": 8,
  "successful_external_source_count": 8,
  "source_targets_met": true,
  "source_budget_exhausted": true,
  "new_source_count": 4,
  "recent_reused_source_count": 4,
  "new_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu57fau7840u6a21u578b_-_MACE-MPu539fu5b50u6750u6599u5316u5b66u57fau7840u6a21u578b_2500f8644a.pdf#5aaf69b35fb9",
    "repo:thorben-frank/euclidean_fast_attention#da8923302a31",
    "repo:ACESuit/mace#059fbdc41b25",
    "repo:CederGroupHub/chgnet#2248a04aa729"
  ],
  "recent_reused_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu6ce8u610fu529b_-_EFAu6b27u6c0fu5febu901fu6ce8u610fu529bu5168u5c40u539fu5b50u8868u793a_0ef43a7c38.pdf#9b564004b09e",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u8badu7ec3_-_NequIPu9ad8u6027u80fdu8badu7ec3u63a8u7406u6df1u5ea6u7b49u53d8u539fu5b50u95f4u52bf_63e6df2008.pdf#a4fb3c313353",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu901au7528u52bf_-_CHGNetu7535u8377u611fu77e5u9884u8badu7ec3u795eu7ecfu7f51u7edcu52bf_7d8d76686d.pdf#9d970111678e",
    "repo:mir-group/nequip#ba95170e90de"
  ],
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
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu6ce8u610fu529b_-_EFAu6b27u6c0fu5febu901fu6ce8u610fu529bu5168u5c40u539fu5b50u8868u793a_0ef43a7c38.pdf#9b564004b09e",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/paper_artifacts/paper_001.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_002",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu57fau7840u6a21u578b_-_MACE-MPu539fu5b50u6750u6599u5316u5b66u57fau7840u6a21u578b_2500f8644a.pdf#5aaf69b35fb9",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/paper_artifacts/paper_002.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_003",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u8badu7ec3_-_NequIPu9ad8u6027u80fdu8badu7ec3u63a8u7406u6df1u5ea6u7b49u53d8u539fu5b50u95f4u52bf_63e6df2008.pdf#a4fb3c313353",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/paper_artifacts/paper_003.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_004",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu901au7528u52bf_-_CHGNetu7535u8377u611fu77e5u9884u8badu7ec3u795eu7ecfu7f51u7edcu52bf_7d8d76686d.pdf#9d970111678e",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/paper_artifacts/paper_004.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:thorben-frank/euclidean_fast_attention#da8923302a31",
      "repo": "thorben-frank/euclidean_fast_attention",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/repo_artifacts/repo_001.json",
      "success": true
    },
    {
      "artifact_ref": "repo_artifact:repo_002",
      "source_id": "repo:ACESuit/mace#059fbdc41b25",
      "repo": "ACESuit/mace",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/repo_artifacts/repo_002.json",
      "success": true
    },
    {
      "artifact_ref": "repo_artifact:repo_003",
      "source_id": "repo:mir-group/nequip#ba95170e90de",
      "repo": "mir-group/nequip",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/repo_artifacts/repo_003.json",
      "success": true
    },
    {
      "artifact_ref": "repo_artifact:repo_004",
      "source_id": "repo:CederGroupHub/chgnet#2248a04aa729",
      "repo": "CederGroupHub/chgnet",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/repo_artifacts/repo_004.json",
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
    "min_successful_pdf_sources": 3,
    "min_successful_repo_sources": 3,
    "min_strong_mechanism_cards": 3,
    "max_pdf_attempts": 4,
    "max_repo_attempts": 4,
    "max_external_source_attempts": 8,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 1
  },
  "source_budget_exhausted": true,
  "source_targets_met": true,
  "artifact_index": {
    "papers": [
      {
        "artifact_ref": "paper_artifact:paper_001",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu6ce8u610fu529b_-_EFAu6b27u6c0fu5febu901fu6ce8u610fu529bu5168u5c40u539fu5b50u8868u793a_0ef43a7c38.pdf#9b564004b09e",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/paper_artifacts/paper_001.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_002",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu57fau7840u6a21u578b_-_MACE-MPu539fu5b50u6750u6599u5316u5b66u57fau7840u6a21u578b_2500f8644a.pdf#5aaf69b35fb9",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/paper_artifacts/paper_002.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_003",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u8badu7ec3_-_NequIPu9ad8u6027u80fdu8badu7ec3u63a8u7406u6df1u5ea6u7b49u53d8u539fu5b50u95f4u52bf_63e6df2008.pdf#a4fb3c313353",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/paper_artifacts/paper_003.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_004",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu901au7528u52bf_-_CHGNetu7535u8377u611fu77e5u9884u8badu7ec3u795eu7ecfu7f51u7edcu52bf_7d8d76686d.pdf#9d970111678e",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/paper_artifacts/paper_004.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:thorben-frank/euclidean_fast_attention#da8923302a31",
        "repo": "thorben-frank/euclidean_fast_attention",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/repo_artifacts/repo_001.json",
        "success": true
      },
      {
        "artifact_ref": "repo_artifact:repo_002",
        "source_id": "repo:ACESuit/mace#059fbdc41b25",
        "repo": "ACESuit/mace",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/repo_artifacts/repo_002.json",
        "success": true
      },
      {
        "artifact_ref": "repo_artifact:repo_003",
        "source_id": "repo:mir-group/nequip#ba95170e90de",
        "repo": "mir-group/nequip",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/repo_artifacts/repo_003.json",
        "success": true
      },
      {
        "artifact_ref": "repo_artifact:repo_004",
        "source_id": "repo:CederGroupHub/chgnet#2248a04aa729",
        "repo": "CederGroupHub/chgnet",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T022040Z/repo_artifacts/repo_004.json",
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
    "G018-MECH-001",
    "G018-MECH-002",
    "G018-MECH-003",
    "G018-MECH-004"
  ],
  "weak_or_hypothesis_mechanisms": [],
  "proposal_allowed_mechanisms": [
    "G018-MECH-001",
    "G018-MECH-002",
    "G018-MECH-003",
    "G018-MECH-004"
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
    "G018-MECH-001",
    "G018-MECH-002",
    "G018-MECH-003",
    "G018-MECH-004"
  ],
  "weak_or_hypothesis_ids": [],
  "cards": [
    {
      "mechanism_id": "G018-MECH-001",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_001",
        "repo_artifact:repo_001"
      ],
      "concrete_mechanism": null,
      "current_code_insertion_point": [
        "research_runtime/generations/generation_016/proposal_002/model/model.py: add a small GlobalRoPEAttentionSideChannel class after BalancedInteractionBlock or before EvolutionMLIP.",
        "model.py __init__ lines 258-260: add ModuleList/global_context modules parallel to self.interactions plus fixed direction/frequency buffers.",
        "model.py forward_energy lines 323-332: after each local interaction, call global_context(scalar_state, positions) and damped-residual add into scalar_state.",
        "model.py forward lines 344-348: preserve energy-to-force autograd path; do not detach positions inside the side-channel."
      ],
      "bounded_edit": [
        "Implement a PyTorch-only small-M global attention module using fixed directions and sinusoidal RoPE; avoid adding JAX/e3x dependencies.",
        "Keep Dq,Dv <= hidden_dim/2, M <= 14, and initialize residual scale at -5 sigmoid so the parent behavior is recovered at start.",
        "Use centered positions for translation invariance; no pairwise O(N^2) attention table.",
        "Wire module in as a side-channel only; keep current neighbor graph, body_order_branch, readout, and training contract intact."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "G018-MECH-002",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_002",
        "repo_artifact:repo_002"
      ],
      "concrete_mechanism": null,
      "current_code_insertion_point": [
        "research_runtime/generations/generation_016/proposal_002/model/model.py: BodyOrderMessageBranch._symmetrize lines 159-177 is the direct replacement point.",
        "model.py BodyOrderMessageBranch.__init__ lines 120-128: add correlation/order config and learned contraction weights; update descriptor_dim accordingly.",
        "model.py BodyOrderMessageBranch.forward lines 196-216: keep atom_a construction, then pass atom_a and atomic numbers into the learned contraction before descriptor message aggregation.",
        "model.py lines 247-254 and 340-342: reuse damped residual readout and scale."
      ],
      "bounded_edit": [
        "Do not import e3nn/MACE; implement a low-l scalar-only PyTorch contraction over current atom_a with correlation=2 or 3 and small rank.",
        "Replace only _symmetrize and descriptor_dim; leave the main BalancedInteractionBlock unchanged.",
        "Initialize new contraction output projection near zero and preserve body_order_scale damping.",
        "Limit descriptor_dim growth to <= current 4*radial_dim*type_dim*2 to avoid runtime blowup."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "G018-MECH-003",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_003",
        "repo_artifact:repo_003"
      ],
      "concrete_mechanism": null,
      "current_code_insertion_point": [
        "research_runtime/generations/generation_016/proposal_002/model/model.py BalancedInteractionBlock.forward lines 57-99: add explicit tensor-product branch terms rather than more scalar/vector gates.",
        "model.py __init__ lines 14-40: add tp_edge_mlp and residual scale parameters or create a separate TPInteractionBranch class.",
        "model.py forward_energy lines 323-332: call the branch in the existing interaction loop.",
        "model.py train.py lines 126-140: no loss change; forces remain from autograd."
      ],
      "bounded_edit": [
        "Implement only l=0/l=1 couplings expressible with dot(unit, vector), scalar*unit, and vector residual; no e3nn dependency or full irreps rewrite.",
        "Initialize TP branch output projection/residual scale near zero to preserve parent behavior.",
        "Keep hidden_dim and num_interactions unchanged; compare replacing one existing gate versus additive sibling branch.",
        "Preserve current neighbor normalization and cutoff weighting."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "G018-MECH-004",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_004",
        "repo_artifact:repo_004"
      ],
      "concrete_mechanism": null,
      "current_code_insertion_point": [
        "research_runtime/generations/generation_016/proposal_002/model/model.py __init__ lines 261-279: add latent_q_head, global_gate, conditioned_readout, aux scale.",
        "model.py forward_energy lines 334-342: compute q/global context after readout_norm and before per_atom_energy; optionally replace self.readout(scalar_state).",
        "model.py forward lines 344-348: return energy, forces and optionally store aux loss without detaching energy path.",
        "model/train.py run_epoch lines 126-130: add model auxiliary regularization term with small weight from config; keep benchmark output fields unchanged."
      ],
      "bounded_edit": [
        "Use latent q only; do not require external charge/mag labels or alter dataset schema.",
        "Initialize conditioned_readout to match old readout as closely as practical or add a damped residual conditioned head instead of replacing the readout.",
        "Set lambda_aux small (1e-4 to 1e-3) and enforce zero mean q per molecule for charge-neutral molecular data.",
        "Keep AtomRef least-squares initialization in train.py lines 53-99 unchanged."
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
    "G018-MECH-001",
    "G018-MECH-002",
    "G018-MECH-003",
    "G018-MECH-004"
  ],
  "blueprints": [
    {
      "blueprint_id": "G018-MECH-001",
      "mechanism_id": "G018-MECH-001",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_016/proposal_002/model/model.py: add a small GlobalRoPEAttentionSideChannel class after BalancedInteractionBlock or before EvolutionMLIP.",
        "model.py __init__ lines 258-260: add ModuleList/global_context modules parallel to self.interactions plus fixed direction/frequency buffers.",
        "model.py forward_energy lines 323-332: after each local interaction, call global_context(scalar_state, positions) and damped-residual add into scalar_state.",
        "model.py forward lines 344-348: preserve energy-to-force autograd path; do not detach positions inside the side-channel."
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "G018-MECH-002",
      "mechanism_id": "G018-MECH-002",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_016/proposal_002/model/model.py: BodyOrderMessageBranch._symmetrize lines 159-177 is the direct replacement point.",
        "model.py BodyOrderMessageBranch.__init__ lines 120-128: add correlation/order config and learned contraction weights; update descriptor_dim accordingly.",
        "model.py BodyOrderMessageBranch.forward lines 196-216: keep atom_a construction, then pass atom_a and atomic numbers into the learned contraction before descriptor message aggregation.",
        "model.py lines 247-254 and 340-342: reuse damped residual readout and scale."
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "G018-MECH-003",
      "mechanism_id": "G018-MECH-003",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_016/proposal_002/model/model.py BalancedInteractionBlock.forward lines 57-99: add explicit tensor-product branch terms rather than more scalar/vector gates.",
        "model.py __init__ lines 14-40: add tp_edge_mlp and residual scale parameters or create a separate TPInteractionBranch class.",
        "model.py forward_energy lines 323-332: call the branch in the existing interaction loop.",
        "model.py train.py lines 126-140: no loss change; forces remain from autograd."
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "G018-MECH-004",
      "mechanism_id": "G018-MECH-004",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_016/proposal_002/model/model.py __init__ lines 261-279: add latent_q_head, global_gate, conditioned_readout, aux scale.",
        "model.py forward_energy lines 334-342: compute q/global context after readout_norm and before per_atom_energy; optionally replace self.readout(scalar_state).",
        "model.py forward lines 344-348: return energy, forces and optionally store aux loss without detaching energy path.",
        "model/train.py run_epoch lines 126-130: add model auxiliary regularization term with small weight from config; keep benchmark output fields unchanged."
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
    "G018-MECH-001",
    "G018-MECH-002",
    "G018-MECH-003",
    "G018-MECH-004"
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
  "mechanism_card_count": 4,
  "strong_mechanism_card_count": 4,
  "provenance_record_count": 17
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
