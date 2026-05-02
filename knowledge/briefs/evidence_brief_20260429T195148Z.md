# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-04-29T19:51:53.355906+00:00",
  "mode": "balanced",
  "source_unit": "generation_016/proposal_002",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/evidence_run.json"
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
      "max_pdf_attempts": 6,
      "max_repo_attempts": 4,
      "max_external_source_attempts": 10,
      "max_source_expansion_rounds": 2,
      "source_expansion_round": 1
    },
    "pdf_attempted_source_count": 4,
    "pdf_successful_source_count": 4,
    "repo_attempted_source_count": 2,
    "repo_successful_source_count": 1,
    "attempted_external_source_count": 6,
    "successful_external_source_count": 5,
    "source_targets_met": true,
    "source_budget_exhausted": false,
    "new_source_count": 6,
    "recent_reused_source_count": 0,
    "new_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu6a21u578bu67b6u6784_-_CAMPu7b1bu5361u5c14u539fu5b50u77e9u673au5668u5b66u4e60u52bf_d9eafc3a57.pdf#d98a73fcde4f",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_TACEu7b1bu5361u5c14u7a7au95f4u5f20u91cfu539fu5b50u7c07u5c55u5f00_e9ab8f4246.pdf#35cab3944e7c",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_PaiNNu5f20u91cfu6027u8d28u4e0eu5206u5b50u5149u8c31u6d88u606fu4f20u9012_97c39f1a80.pdf#b33702964a46",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u8badu7ec3_-_NequIPu9ad8u6027u80fdu8badu7ec3u63a8u7406u6df1u5ea6u7b49u53d8u539fu5b50u95f4u52bf_63e6df2008.pdf#a4fb3c313353",
      "repo:MaxH1996/PaiNN-in-PyG#55a1dfc4a439",
      "repo:atomistic-machine-learning/schnetpack#41e33adf8c61"
    ],
    "recent_reused_source_ids": [],
    "all_sources_recent_repeats": false,
    "source_novelty_passed": true,
    "allow_recent_source_reuse": false
  },
  "external_attempted_source_count": 6,
  "external_successful_source_count": 5,
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
  "source_unit": "generation_016/proposal_002",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_016/proposal_002",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/generation_memory.json",
  "generation_memory": {
    "version": "generation_memory.v1",
    "source_unit": "generation_016/proposal_002",
    "last_completed_generation": "generation_016",
    "ignored_legacy_source_count": 2,
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
      "total": 3,
      "success": 3,
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
      "total": 2,
      "success": 1,
      "fresh": 2,
      "can_support_strong": 1
    }
  },
  "strong_capable_sources": [
    "paper_artifact:paper_001",
    "paper_artifact:paper_002",
    "paper_artifact:paper_003",
    "paper_artifact:paper_004",
    "repo_artifact:repo_002"
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
    },
    {
      "source_id": "repo_artifact:repo_001",
      "type": "repo_code",
      "notes": "Repo deep-read failed: "
    }
  ],
  "reused_sources": [
    "prior_brief:1",
    "prior_brief:2",
    "prior_brief:3"
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
  "pdf_attempted_source_count": 4,
  "pdf_successful_source_count": 4,
  "repo_attempted_source_count": 2,
  "repo_successful_source_count": 1,
  "attempted_external_source_count": 6,
  "successful_external_source_count": 5,
  "source_targets_met": true,
  "source_budget_exhausted": false,
  "new_source_count": 6,
  "recent_reused_source_count": 0,
  "new_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu6a21u578bu67b6u6784_-_CAMPu7b1bu5361u5c14u539fu5b50u77e9u673au5668u5b66u4e60u52bf_d9eafc3a57.pdf#d98a73fcde4f",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_TACEu7b1bu5361u5c14u7a7au95f4u5f20u91cfu539fu5b50u7c07u5c55u5f00_e9ab8f4246.pdf#35cab3944e7c",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_PaiNNu5f20u91cfu6027u8d28u4e0eu5206u5b50u5149u8c31u6d88u606fu4f20u9012_97c39f1a80.pdf#b33702964a46",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u8badu7ec3_-_NequIPu9ad8u6027u80fdu8badu7ec3u63a8u7406u6df1u5ea6u7b49u53d8u539fu5b50u95f4u52bf_63e6df2008.pdf#a4fb3c313353",
    "repo:MaxH1996/PaiNN-in-PyG#55a1dfc4a439",
    "repo:atomistic-machine-learning/schnetpack#41e33adf8c61"
  ],
  "recent_reused_source_ids": [],
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
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu6a21u578bu67b6u6784_-_CAMPu7b1bu5361u5c14u539fu5b50u77e9u673au5668u5b66u4e60u52bf_d9eafc3a57.pdf#d98a73fcde4f",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/paper_artifacts/paper_001.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_002",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_TACEu7b1bu5361u5c14u7a7au95f4u5f20u91cfu539fu5b50u7c07u5c55u5f00_e9ab8f4246.pdf#35cab3944e7c",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/paper_artifacts/paper_002.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_003",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_PaiNNu5f20u91cfu6027u8d28u4e0eu5206u5b50u5149u8c31u6d88u606fu4f20u9012_97c39f1a80.pdf#b33702964a46",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/paper_artifacts/paper_003.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_004",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u8badu7ec3_-_NequIPu9ad8u6027u80fdu8badu7ec3u63a8u7406u6df1u5ea6u7b49u53d8u539fu5b50u95f4u52bf_63e6df2008.pdf#a4fb3c313353",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/paper_artifacts/paper_004.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:MaxH1996/PaiNN-in-PyG#55a1dfc4a439",
      "repo": "MaxH1996/PaiNN-in-PyG",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/repo_artifacts/repo_001.json",
      "success": false
    },
    {
      "artifact_ref": "repo_artifact:repo_002",
      "source_id": "repo:atomistic-machine-learning/schnetpack#41e33adf8c61",
      "repo": "atomistic-machine-learning/schnetpack",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/repo_artifacts/repo_002.json",
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
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu6a21u578bu67b6u6784_-_CAMPu7b1bu5361u5c14u539fu5b50u77e9u673au5668u5b66u4e60u52bf_d9eafc3a57.pdf#d98a73fcde4f",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/paper_artifacts/paper_001.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_002",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_TACEu7b1bu5361u5c14u7a7au95f4u5f20u91cfu539fu5b50u7c07u5c55u5f00_e9ab8f4246.pdf#35cab3944e7c",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/paper_artifacts/paper_002.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_003",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_PaiNNu5f20u91cfu6027u8d28u4e0eu5206u5b50u5149u8c31u6d88u606fu4f20u9012_97c39f1a80.pdf#b33702964a46",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/paper_artifacts/paper_003.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_004",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u8badu7ec3_-_NequIPu9ad8u6027u80fdu8badu7ec3u63a8u7406u6df1u5ea6u7b49u53d8u539fu5b50u95f4u52bf_63e6df2008.pdf#a4fb3c313353",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/paper_artifacts/paper_004.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:MaxH1996/PaiNN-in-PyG#55a1dfc4a439",
        "repo": "MaxH1996/PaiNN-in-PyG",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/repo_artifacts/repo_001.json",
        "success": false
      },
      {
        "artifact_ref": "repo_artifact:repo_002",
        "source_id": "repo:atomistic-machine-learning/schnetpack#41e33adf8c61",
        "repo": "atomistic-machine-learning/schnetpack",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T195148Z/repo_artifacts/repo_002.json",
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
    "GEN017-M01-painn-style-scalar-vector-mixing-gate"
  ],
  "weak_or_hypothesis_mechanisms": [
    "GEN017-M02-cartesian-tensor-contraction-background"
  ],
  "proposal_allowed_mechanisms": [
    "GEN017-M01-painn-style-scalar-vector-mixing-gate"
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
    "GEN017-M01-painn-style-scalar-vector-mixing-gate"
  ],
  "weak_or_hypothesis_ids": [
    "GEN017-M02-cartesian-tensor-contraction-background"
  ],
  "cards": [
    {
      "mechanism_id": "GEN017-M01-painn-style-scalar-vector-mixing-gate",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_003",
        "repo_artifact:repo_002",
        "paper_artifact:paper_001"
      ],
      "concrete_mechanism": null,
      "current_code_insertion_point": [
        "model/model.py::EvolutionMLIP.__init__ after body_order_readout/body_order_scale definitions: add tiny vector-to-body-order gate/projection modules initialized near zero",
        "model/model.py::EvolutionMLIP.forward_energy after the interaction loop and before body_order_residual = self.body_order_readout(body_order_descriptor): compute U/V projections of vector_state, norm_v, dot_uv, and a sigmoid/tanh-gated body_order_descriptor correction",
        "model/model.py::BalancedInteractionBlock.forward already exposes agg_norm/vector_alignment; do not rewrite it unless using this as the ablation variant",
        "model/train.py::TRAIN_ENERGY_WEIGHT/TRAIN_FORCE_WEIGHT and run_epoch loss remain unchanged for the primary ablation so benchmark semantics are preserved"
      ],
      "bounded_edit": [
        "Do not replace EvolutionMLIP or add external dependencies. Add at most two Linear layers plus a small MLP in EvolutionMLIP to produce a descriptor_dim-sized correction from [body_order_descriptor, norm_v, dot_uv].",
        "Initialize the final correction layer to zero or multiply by a new small learnable scale initialized negative, mirroring body_order_scale, so the starting model is close to generation_016/proposal_002.",
        "Keep existing cutoff, RBF, neighbor list, atomref, loss weights, and force-from-energy path unchanged.",
        "Use vector_state.transpose(1,2) only internally for PaiNN-like contractions; return no new public outputs."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "GEN017-M02-cartesian-tensor-contraction-background",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "paper_artifact:paper_001",
        "paper_artifact:paper_002",
        "paper_artifact:paper_004"
      ],
      "concrete_mechanism": null,
      "current_code_insertion_point": [
        "model/model.py::BodyOrderMessageBranch._angular_monomials",
        "model/model.py::BodyOrderMessageBranch._symmetrize"
      ],
      "bounded_edit": [
        "Do not add a full CAMP/TACE hierarchy in generation_017 without a fresh implementation repository trace; at most test one additional normalized contraction or keep this as proposal background."
      ],
      "downgrade_reasons": [
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
  "implementation_ready_blueprints": [
    "GEN017-M01-painn-style-scalar-vector-mixing-gate"
  ],
  "blueprints": [
    {
      "blueprint_id": "GEN017-M01-painn-style-scalar-vector-mixing-gate",
      "mechanism_id": "GEN017-M01-painn-style-scalar-vector-mixing-gate",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py::EvolutionMLIP.__init__ after body_order_readout/body_order_scale definitions: add tiny vector-to-body-order gate/projection modules initialized near zero",
        "model/model.py::EvolutionMLIP.forward_energy after the interaction loop and before body_order_residual = self.body_order_readout(body_order_descriptor): compute U/V projections of vector_state, norm_v, dot_uv, and a sigmoid/tanh-gated body_order_descriptor correction",
        "model/model.py::BalancedInteractionBlock.forward already exposes agg_norm/vector_alignment; do not rewrite it unless using this as the ablation variant",
        "model/train.py::TRAIN_ENERGY_WEIGHT/TRAIN_FORCE_WEIGHT and run_epoch loss remain unchanged for the primary ablation so benchmark semantics are preserved"
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "GEN017-M02-cartesian-tensor-contraction-background",
      "mechanism_id": "GEN017-M02-cartesian-tensor-contraction-background",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py::BodyOrderMessageBranch._angular_monomials",
        "model/model.py::BodyOrderMessageBranch._symmetrize"
      ],
      "blocked_until": [
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
  "allowed_mechanisms": [
    "GEN017-M01-painn-style-scalar-vector-mixing-gate"
  ],
  "weak_or_hypothesis_mechanisms": [
    "GEN017-M02-cartesian-tensor-contraction-background"
  ],
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
  "strong_mechanism_card_count": 1,
  "provenance_record_count": 13
}
```

## what_not_to_use_as_strong_evidence

```json
{
  "weak_or_hypothesis_mechanisms": [
    "GEN017-M02-cartesian-tensor-contraction-background"
  ],
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
