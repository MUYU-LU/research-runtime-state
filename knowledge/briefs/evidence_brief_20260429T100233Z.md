# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-04-29T10:04:53.181054+00:00",
  "mode": "balanced",
  "source_unit": "generation_014/proposal_009",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/evidence_run.json"
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
    "pdf_attempted_source_count": 2,
    "pdf_successful_source_count": 2,
    "repo_attempted_source_count": 1,
    "repo_successful_source_count": 1,
    "attempted_external_source_count": 3,
    "successful_external_source_count": 3,
    "source_targets_met": true,
    "source_budget_exhausted": false,
    "new_source_count": 3,
    "recent_reused_source_count": 0,
    "new_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_u6b27u6c0fTransformeru5febu901fu7a33u5b9au529bu573a_9a21144d7b.pdf#ba57cf3104e9",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu80fdu91cfu5b88u6052_-_ESENu5e73u6ed1u8868u8fbeu539fu5b50u95f4u52bf_9f8f7f5e6c.pdf#77f70452391e",
      "repo:torchmd/torchmd-net#e0cf6c6d162e"
    ],
    "recent_reused_source_ids": [],
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
  "source_unit": "generation_014/proposal_009",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_014/proposal_009",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/generation_memory.json",
  "generation_memory": {
    "version": "generation_memory.v1",
    "source_unit": "generation_014/proposal_009",
    "last_completed_generation": "generation_014",
    "ignored_legacy_source_count": 0,
    "completed_generation_count_for_source": 1,
    "recent_attempt_count_for_source": 0,
    "unit_card_count_for_source": 1,
    "negative_pattern_count_for_source": 0,
    "partial_positive_pattern_count_for_source": 0,
    "latest_generation": "generation_014",
    "latest_best_child": {
      "unit": "generation_014/proposal_009",
      "Q_rmd17": 4.054452268569513,
      "Q_iso17": 3.609934903921426,
      "Q_total": 3.8988711909426823,
      "outcome_class": "frontier_win"
    },
    "latest_outcome_counts": {
      "frontier_win": 7,
      "neutral_variance": 1
    },
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
      "total": 1,
      "success": 1,
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
      "total": 2,
      "success": 2,
      "fresh": 2,
      "can_support_strong": 2
    }
  },
  "strong_capable_sources": [
    "paper_artifact:paper_001",
    "paper_artifact:paper_002",
    "repo_artifact:repo_001",
    "repo_artifact:repo_001_supplemental"
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
    "prior_brief:1"
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
  "new_source_count": 3,
  "recent_reused_source_count": 0,
  "new_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_u6b27u6c0fTransformeru5febu901fu7a33u5b9au529bu573a_9a21144d7b.pdf#ba57cf3104e9",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu80fdu91cfu5b88u6052_-_ESENu5e73u6ed1u8868u8fbeu539fu5b50u95f4u52bf_9f8f7f5e6c.pdf#77f70452391e",
    "repo:torchmd/torchmd-net#e0cf6c6d162e"
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
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_u6b27u6c0fTransformeru5febu901fu7a33u5b9au529bu573a_9a21144d7b.pdf#ba57cf3104e9",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/paper_artifacts/paper_001.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_002",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu80fdu91cfu5b88u6052_-_ESENu5e73u6ed1u8868u8fbeu539fu5b50u95f4u52bf_9f8f7f5e6c.pdf#77f70452391e",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/paper_artifacts/paper_002.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:torchmd/torchmd-net#e0cf6c6d162e",
      "repo": "torchmd/torchmd-net",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/repo_artifacts/repo_001.json",
      "success": true
    },
    {
      "artifact_ref": "repo_artifact:repo_001_supplemental",
      "source_id": "repo:torchmd/torchmd-net#e0cf6c6d162e",
      "repo": "torchmd/torchmd-net",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/repo_artifacts/repo_001_supplemental_trace.json",
      "success": true,
      "supplemental_to": "repo_artifact:repo_001"
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
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_u6b27u6c0fTransformeru5febu901fu7a33u5b9au529bu573a_9a21144d7b.pdf#ba57cf3104e9",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/paper_artifacts/paper_001.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_002",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu80fdu91cfu5b88u6052_-_ESENu5e73u6ed1u8868u8fbeu539fu5b50u95f4u52bf_9f8f7f5e6c.pdf#77f70452391e",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/paper_artifacts/paper_002.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:torchmd/torchmd-net#e0cf6c6d162e",
        "repo": "torchmd/torchmd-net",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T100233Z/repo_artifacts/repo_001.json",
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
    "GEN015-M01-gated-invariant-vector-readout-damping"
  ],
  "weak_or_hypothesis_mechanisms": [
    "GEN015-W01-conservative-smoothness-guardrail"
  ],
  "proposal_allowed_mechanisms": [
    "GEN015-M01-gated-invariant-vector-readout-damping"
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
    "GEN015-M01-gated-invariant-vector-readout-damping"
  ],
  "weak_or_hypothesis_ids": [
    "GEN015-W01-conservative-smoothness-guardrail"
  ],
  "cards": [
    {
      "mechanism_id": "GEN015-M01-gated-invariant-vector-readout-damping",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_001",
        "paper_artifact:paper_002",
        "repo_artifact:repo_001",
        "repo_artifact:repo_001_supplemental"
      ],
      "concrete_mechanism": "Continue the generation_014 vector-norm readout family, but change the raw concatenation into a learned, damped invariant-vector readout gate so the scalar head can use vector magnitudes without letting the new vector channel dominate ISO17 energy/gap behavior.",
      "current_code_insertion_point": [
        "research_runtime/generations/generation_014/proposal_009/model/model.py: EvolutionMLIP.__init__ after self.vector_norm_layer and before self.readout",
        "research_runtime/generations/generation_014/proposal_009/model/model.py: EvolutionMLIP.forward_energy immediately after vector_norm = self.vector_norm_layer(torch.linalg.norm(vector_state, dim=-1)) and before readout_input construction"
      ],
      "bounded_edit": [
        "Add either self.vector_readout_logit = nn.Parameter(torch.tensor(-1.5)) for a scalar gate, or self.vector_readout_gate = nn.Sequential(nn.Linear(hidden_dim * 2, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, hidden_dim)) with final bias initialized negative if initialization helpers are available.",
        "Replace readout_input = torch.cat([scalar_state, vector_norm], dim=-1) with gated_vector_norm = torch.sigmoid(gate) * vector_norm and readout_input = torch.cat([scalar_state, gated_vector_norm], dim=-1).",
        "Do not change dataloaders, benchmark splits, metrics, main.py entrypoint, force target definitions, or energy/force loss semantics.",
        "Keep force computation as -torch.autograd.grad(energy, positions, create_graph=True)[0]; do not add a direct-force head."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "GEN015-W01-conservative-smoothness-guardrail",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "paper_artifact:paper_002",
        "repo_artifact:repo_001",
        "repo_artifact:repo_001_supplemental"
      ],
      "concrete_mechanism": "Guardrail for proposal selection: generation_015 should not trade the current conservative energy-to-force contract for direct force heads, top-k neighbor discontinuities, or high-frequency/sparse readout changes when the target issue is ISO17 energy/gap robustness.",
      "current_code_insertion_point": [
        "model/model.py: EvolutionMLIP.forward must continue returning (energy, forces) from autograd",
        "model/model.py: _cutoff_weight and _build_neighbor_list should not be replaced with top-k/ranked discontinuous neighbor selection in this evidence-backed path"
      ],
      "bounded_edit": [
        "No direct implementation move recommended from this card alone; use it as a proposal constraint/audit checklist alongside GEN015-M01.",
        "If any model edit changes edge construction or force computation, add a local finite-difference/autograd consistency sanity check before benchmark launch; do not alter benchmark semantics."
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
    "GEN015-M01-gated-invariant-vector-readout-damping"
  ],
  "blueprints": [
    {
      "blueprint_id": "GEN015-M01-gated-invariant-vector-readout-damping",
      "mechanism_id": "GEN015-M01-gated-invariant-vector-readout-damping",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_014/proposal_009/model/model.py: EvolutionMLIP.__init__ after self.vector_norm_layer and before self.readout",
        "research_runtime/generations/generation_014/proposal_009/model/model.py: EvolutionMLIP.forward_energy immediately after vector_norm = self.vector_norm_layer(torch.linalg.norm(vector_state, dim=-1)) and before readout_input construction"
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "GEN015-W01-conservative-smoothness-guardrail",
      "mechanism_id": "GEN015-W01-conservative-smoothness-guardrail",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py: EvolutionMLIP.forward must continue returning (energy, forces) from autograd",
        "model/model.py: _cutoff_weight and _build_neighbor_list should not be replaced with top-k/ranked discontinuous neighbor selection in this evidence-backed path"
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
    "GEN015-M01-gated-invariant-vector-readout-damping"
  ],
  "weak_or_hypothesis_mechanisms": [
    "GEN015-W01-conservative-smoothness-guardrail"
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
  "provenance_record_count": 9
}
```

## what_not_to_use_as_strong_evidence

```json
{
  "weak_or_hypothesis_mechanisms": [
    "GEN015-W01-conservative-smoothness-guardrail"
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
