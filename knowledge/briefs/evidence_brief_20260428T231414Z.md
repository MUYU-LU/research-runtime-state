# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-04-28T23:14:15.660711+00:00",
  "mode": "balanced",
  "source_unit": "generation_013/proposal_007",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/evidence_run.json"
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
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu67b6u6784_-_AlphaNetu5c40u90e8u6846u67b6u795eu7ecfu7f51u7edcu539fu5b50u95f4u52bf_a87ab20bd7.pdf#4ad46b498dc7",
      "repo:ACEsuit/mace#99833dea34c0"
    ],
    "recent_reused_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12"
    ],
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
  "source_unit": "generation_013/proposal_007",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_013/proposal_007",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/generation_memory.json",
  "generation_memory": {
    "version": "generation_memory.v1",
    "source_unit": "generation_013/proposal_007",
    "last_completed_generation": "generation_013",
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
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu67b6u6784_-_AlphaNetu5c40u90e8u6846u67b6u795eu7ecfu7f51u7edcu539fu5b50u95f4u52bf_a87ab20bd7.pdf#4ad46b498dc7",
    "repo:ACEsuit/mace#99833dea34c0"
  ],
  "recent_reused_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12"
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
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu67b6u6784_-_AlphaNetu5c40u90e8u6846u67b6u795eu7ecfu7f51u7edcu539fu5b50u95f4u52bf_a87ab20bd7.pdf#4ad46b498dc7",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/paper_artifacts/paper_001.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_002",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/paper_artifacts/paper_002.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:ACEsuit/mace#99833dea34c0",
      "repo": "ACEsuit/mace",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/repo_artifacts/repo_001.json",
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
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu67b6u6784_-_AlphaNetu5c40u90e8u6846u67b6u795eu7ecfu7f51u7edcu539fu5b50u95f4u52bf_a87ab20bd7.pdf#4ad46b498dc7",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/paper_artifacts/paper_001.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_002",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/paper_artifacts/paper_002.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:ACEsuit/mace#99833dea34c0",
        "repo": "ACEsuit/mace",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/repo_artifacts/repo_001.json",
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
    "GEN014-M01-invariant-vector-readout-repair",
    "GEN014-M02-atomref-energy-safeguard"
  ],
  "weak_or_hypothesis_mechanisms": [],
  "proposal_allowed_mechanisms": [
    "GEN014-M01-invariant-vector-readout-repair",
    "GEN014-M02-atomref-energy-safeguard"
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
    "GEN014-M01-invariant-vector-readout-repair",
    "GEN014-M02-atomref-energy-safeguard"
  ],
  "weak_or_hypothesis_ids": [],
  "cards": [
    {
      "mechanism_id": "GEN014-M01-invariant-vector-readout-repair",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_001",
        "repo_artifact:repo_001",
        "paper_artifact:paper_002"
      ],
      "concrete_mechanism": "generation_013/proposal_007 removed vector_norm from the final per-atom readout. External evidence supports conservative energy models that transform equivariant/geometric features into invariant atomic energy contributions, then compute forces as -grad(E). A bounded repair is to re-introduce vector-derived invariant scalars (at minimum ||vector_state|| per atom, optionally with a small learned gate) into the readout while preserving the existing energy-summed autograd force contract.",
      "current_code_insertion_point": [
        "research_runtime/generations/generation_013/proposal_007/model/model.py: EvolutionMLIP.__init__ readout input dimension currently hidden_dim; restore hidden_dim*2 or gated compact variant.",
        "research_runtime/generations/generation_013/proposal_007/model/model.py: EvolutionMLIP.forward_energy after interaction loop where proposal_007 changed per_atom_energy = self.readout(scalar_state).squeeze(-1)."
      ],
      "bounded_edit": [
        "Change readout first layer back to nn.Linear(hidden_dim * 2, hidden_dim) and compute vector_norm = torch.linalg.norm(vector_state, dim=-1).",
        "Set per_atom_energy = self.readout(torch.cat([scalar_state, vector_norm], dim=-1)).squeeze(-1).",
        "Optional only if proposal budget allows: multiply vector_norm by a learned scalar gate initialized small (e.g. sigmoid bias < 0) to control runtime/variance; do not add new losses or entrypoints."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "GEN014-M02-atomref-energy-safeguard",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "repo_artifact:repo_001",
        "paper_artifact:paper_002"
      ],
      "concrete_mechanism": "MACE represents baseline atomic energies as a registered AtomicEnergiesBlock added to learned interaction/readout energies. Its README warns that fitted average E0s correspond to deviations from average and can be less stable for MD than isolated atom energies; for foundation fine-tuning it uses estimated corrections. In the current lightweight model, proposal_007 freezes least-squares atomref after fitting. Given ISO17 val energy worsened and mixed_energy_mae regressed, the next evidence-backed move is a one-factor atomref-freeze ablation or soft trainable atomref with small regularization, not a blanket freeze.",
      "current_code_insertion_point": [
        "research_runtime/generations/generation_013/proposal_007/model/train.py: after initialize_atomref_lstsq call, lines that set model.atomref.weight.requires_grad_(False).",
        "research_runtime/generations/generation_013/proposal_007/model/train.py: optimizer construction and energy_weight/force_weight warmup schedule."
      ],
      "bounded_edit": [
        "Run a one-factor proposal that removes the freeze line (keep fitted initialization but allow atomref to train) OR gates freeze by config default false; do not change model architecture in the same unit if isolating atomref effect.",
        "Optional bounded control if not combined with M01: add tiny L2 regularization to atomref deviation from fitted values rather than hard freeze.",
        "Do not alter benchmark metrics, splits, max epochs, output schema, or main.py entrypoint."
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
    "GEN014-M01-invariant-vector-readout-repair",
    "GEN014-M02-atomref-energy-safeguard"
  ],
  "blueprints": [
    {
      "blueprint_id": "GEN014-M01-invariant-vector-readout-repair",
      "mechanism_id": "GEN014-M01-invariant-vector-readout-repair",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_013/proposal_007/model/model.py: EvolutionMLIP.__init__ readout input dimension currently hidden_dim; restore hidden_dim*2 or gated compact variant.",
        "research_runtime/generations/generation_013/proposal_007/model/model.py: EvolutionMLIP.forward_energy after interaction loop where proposal_007 changed per_atom_energy = self.readout(scalar_state).squeeze(-1)."
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "GEN014-M02-atomref-energy-safeguard",
      "mechanism_id": "GEN014-M02-atomref-energy-safeguard",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_013/proposal_007/model/train.py: after initialize_atomref_lstsq call, lines that set model.atomref.weight.requires_grad_(False).",
        "research_runtime/generations/generation_013/proposal_007/model/train.py: optimizer construction and energy_weight/force_weight warmup schedule."
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
    "GEN014-M01-invariant-vector-readout-repair",
    "GEN014-M02-atomref-energy-safeguard"
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

## generation_013_outcome_memory_addendum

```json
{
  "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260428T231414Z/generation_013_outcome_memory.json",
  "canonical_source": "/home/lmy/.openclaw/workspace/research_runtime/ledger/generation_summaries/generation_013.json",
  "summary": {
    "did_any_child_beat_parent": false,
    "best_child": "generation_013/proposal_001",
    "best_child_outcome_class": "neutral_variance",
    "outcome_counts": {"benchmark_tradeoff": 2, "negative_method": 2, "neutral_variance": 4},
    "source_unit": "generation_013/proposal_007",
    "source_unit_outcome_class": "benchmark_tradeoff",
    "source_unit_Q_total": 3.75578478119853,
    "source_unit_delta_Q_vs_parent": -0.07451670430602064
  },
  "proposal_time_implication": "generation_014 continuation should not repeat proposal_007 as-is; isolate scalar-only readout removal and fitted-atomref freeze while preserving benchmark semantics and checking energy/Q, not force or gap alone."
}
```

