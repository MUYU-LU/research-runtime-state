# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-04-29T14:46:40.110581+00:00",
  "mode": "jump",
  "source_unit": "generation_015/proposal_004",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/evidence_run.json"
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
    "pdf_attempted_source_count": 3,
    "pdf_successful_source_count": 3,
    "repo_attempted_source_count": 2,
    "repo_successful_source_count": 1,
    "attempted_external_source_count": 5,
    "successful_external_source_count": 4,
    "source_targets_met": true,
    "source_budget_exhausted": false,
    "new_source_count": 5,
    "recent_reused_source_count": 0,
    "new_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_SpookyNetu542bu7535u5b50u81eau7531u5ea6u975eu5c40u57dfu529bu573a_8934a89dff.pdf#f2801ba411fd",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_sGDMLu80fdu91cfu5b88u6052u5206u5b50u529bu573a_da37fc9ebd.pdf#383aa22f0a4f",
      "repo:BingqingCheng/cace#a6c88223e724",
      "repo:OUnke/SpookyNet#7161f33a43a0"
    ],
    "recent_reused_source_ids": [],
    "all_sources_recent_repeats": false,
    "source_novelty_passed": true,
    "allow_recent_source_reuse": false
  },
  "external_attempted_source_count": 5,
  "external_successful_source_count": 4,
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
  "source_unit": "generation_015/proposal_004",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_015/proposal_004",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/generation_memory.json",
  "generation_memory": {
    "version": "generation_memory.v1",
    "source_unit": "generation_015/proposal_004",
    "last_completed_generation": "generation_015",
    "ignored_legacy_source_count": 1,
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
      "total": 2,
      "success": 2,
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
    },
    {
      "source_id": "repo_artifact:repo_002",
      "type": "repo_code",
      "notes": "Repo deep-read failed: Traceback (most recent call last):\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 143, in <module>\n    main()\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 138, in main\n    result = read_repo(args.repo, args.max_files, args.max_file_chars, Path(args.cache_root).expanduser())\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 96, in read_repo\n    repo_root, git_action, git_warning = ensure_repo(owner, name, cache_root)\n                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 67, in ensure_repo\n    result = run_git([\"clone\", \"--depth\", \"1\", url, str(target)])\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 43, in run_git\n    return subprocess.run(\n           ^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.12/subprocess.py\", line 550, in run\n    stdout, stderr = process.communicate(input, timeout=timeout)\n                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.12/subprocess.py\", line 1209, in communicate\n    stdout, stderr = self._communicate(input, endtime, timeout)\n                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.12/subprocess.py\", line 2116, in _communicate\n    self._check_timeout(endtime, orig_timeout, stdout, stderr)\n  File \"/usr/lib/python3.12/subprocess.py\", line 1253, in _check_timeout\n    raise TimeoutExpired(\nsubprocess.TimeoutExpired: Command '['git', 'clone', '--depth', '1', 'https://github.com/OUnke/SpookyNet.git', '/home/lmy/.openclaw/workspace/.cache/mlip_evidence/repos/OUnke__SpookyNet']' timed out after 180 seconds"
    }
  ],
  "reused_sources": [
    "prior_brief:1",
    "prior_brief:2"
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
  "pdf_attempted_source_count": 3,
  "pdf_successful_source_count": 3,
  "repo_attempted_source_count": 2,
  "repo_successful_source_count": 1,
  "attempted_external_source_count": 5,
  "successful_external_source_count": 4,
  "source_targets_met": true,
  "source_budget_exhausted": false,
  "new_source_count": 5,
  "recent_reused_source_count": 0,
  "new_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_SpookyNetu542bu7535u5b50u81eau7531u5ea6u975eu5c40u57dfu529bu573a_8934a89dff.pdf#f2801ba411fd",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_sGDMLu80fdu91cfu5b88u6052u5206u5b50u529bu573a_da37fc9ebd.pdf#383aa22f0a4f",
    "repo:BingqingCheng/cace#a6c88223e724",
    "repo:OUnke/SpookyNet#7161f33a43a0"
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
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/paper_artifacts/paper_001.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_002",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_SpookyNetu542bu7535u5b50u81eau7531u5ea6u975eu5c40u57dfu529bu573a_8934a89dff.pdf#f2801ba411fd",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/paper_artifacts/paper_002.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_003",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_sGDMLu80fdu91cfu5b88u6052u5206u5b50u529bu573a_da37fc9ebd.pdf#383aa22f0a4f",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/paper_artifacts/paper_003.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:BingqingCheng/cace#a6c88223e724",
      "repo": "BingqingCheng/cace",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/repo_artifacts/repo_001.json",
      "success": true
    },
    {
      "artifact_ref": "repo_artifact:repo_002",
      "source_id": "repo:OUnke/SpookyNet#7161f33a43a0",
      "repo": "OUnke/SpookyNet",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/repo_artifacts/repo_002.json",
      "success": false
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
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu8868u793au65b9u6cd5_-_u7b1bu5361u5c14u539fu5b50u7c07u5c55u5f00CACE_b50892f5fb.pdf#5b6c7ac07310",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/paper_artifacts/paper_001.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_002",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_SpookyNetu542bu7535u5b50u81eau7531u5ea6u975eu5c40u57dfu529bu573a_8934a89dff.pdf#f2801ba411fd",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/paper_artifacts/paper_002.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_003",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu5206u5b50u529bu573a_-_sGDMLu80fdu91cfu5b88u6052u5206u5b50u529bu573a_da37fc9ebd.pdf#383aa22f0a4f",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/paper_artifacts/paper_003.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:BingqingCheng/cace#a6c88223e724",
        "repo": "BingqingCheng/cace",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/repo_artifacts/repo_001.json",
        "success": true
      },
      {
        "artifact_ref": "repo_artifact:repo_002",
        "source_id": "repo:OUnke/SpookyNet#7161f33a43a0",
        "repo": "OUnke/SpookyNet",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260429T144330Z/repo_artifacts/repo_002.json",
        "success": false
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
    "GEN016-M01-cace-shadow-body-order-representation",
    "GEN016-M02-bounded-electrostatic-energy-decomposition"
  ],
  "weak_or_hypothesis_mechanisms": [
    "GEN016-W01-gradient-domain-physics-regularization-guardrail",
    "GEN016-W02-full-spookynet-nonlocal-transformer-rewrite"
  ],
  "proposal_allowed_mechanisms": [
    "GEN016-M01-cace-shadow-body-order-representation",
    "GEN016-M02-bounded-electrostatic-energy-decomposition"
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
    "GEN016-M01-cace-shadow-body-order-representation",
    "GEN016-M02-bounded-electrostatic-energy-decomposition"
  ],
  "weak_or_hypothesis_ids": [
    "GEN016-W01-gradient-domain-physics-regularization-guardrail",
    "GEN016-W02-full-spookynet-nonlocal-transformer-rewrite"
  ],
  "cards": [
    {
      "mechanism_id": "GEN016-M01-cace-shadow-body-order-representation",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_001",
        "repo_artifact:repo_001"
      ],
      "concrete_mechanism": "Add a compact Cartesian body-order invariant representation branch beside the existing learned scalar/vector message path, then feed a small residual scalar energy head from B-basis invariants. This is a representation/message-path departure, not another gate/norm/readout tweak around BalancedInteractionBlock.",
      "current_code_insertion_point": [
        "research_runtime/generations/generation_015/proposal_004/model/model.py: EvolutionMLIP.__init__ after RBF buffer setup and before self.interactions: add small CartesianBodyOrderBranch(hidden_dim, num_rbf or cace_rbf=6, l_max=2, max_nu=2) and residual scalar alpha parameter initialized near -4 sigmoid or 0 scalar.",
        "research_runtime/generations/generation_015/proposal_004/model/model.py: EvolutionMLIP.forward_energy after dij/unit/rbf/cutoff_weight are computed and before/after the existing interaction loop: compute cace_B = self.body_order_branch(numbers, i_idx, j_idx, rij, dij, unit, rbf, cutoff_weight), residual_per_atom = self.body_order_readout(cace_B), add alpha * residual_per_atom.sum() to atomref + existing per_atom_energy.sum().",
        "research_runtime/generations/generation_015/proposal_004/model/train.py: keep dataloader, losses, energy/force weights, split/eval semantics; optionally add no new CLI/config dependency."
      ],
      "bounded_edit": [
        "Implement only a minimal local module in model/model.py, not an external dependency: AngularMonomial(l_max=2), A scatter, nu=1/2 Symmetrizer, LayerNorm/MLP head.",
        "Reuse the current neighbor list and cutoff; do not alter _build_neighbor_list, benchmark sampling, main.py, eval.py, dataloader.py, metrics, or force target definitions.",
        "Initialize residual contribution small: body_order_scale = nn.Parameter(torch.tensor(-4.0)); residual multiplier sigmoid(body_order_scale) or 0.05*tanh(scale).",
        "Truncate aggressively (l_max=2, max_nu=2, radial channels <=8, element embedding <=4) to avoid runtime blow-up and avoid a rewrite-heavy full CACE port.",
        "Ablation/control: compare against generation_015/proposal_004 and control replicate; reject if ISO17 energy trend/gap worsens or RMD17 mixed_force_mae regresses beyond round tolerance."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "GEN016-M02-bounded-electrostatic-energy-decomposition",
      "claim_strength": "strong",
      "strong_ready": true,
      "source_refs": [
        "paper_artifact:paper_002",
        "repo_artifact:repo_001"
      ],
      "concrete_mechanism": "Add a separate learned charge/electrostatic residual energy term on top of the existing local atomic-energy sum: E_total = E_local + beta E_elec. This changes energy decomposition and introduces bounded nonlocal all-pair information without changing labels, splits, metrics, or the energy-to-force contract.",
      "current_code_insertion_point": [
        "research_runtime/generations/generation_015/proposal_004/model/model.py: EvolutionMLIP.__init__ after readout modules: add self.charge_head = nn.Linear(hidden_dim, 1), self.electrostatic_log_scale = nn.Parameter(torch.tensor(-5.0)), and buffers/constant sigma/eps.",
        "research_runtime/generations/generation_015/proposal_004/model/model.py: EvolutionMLIP.forward_energy after scalar_state is finalized and before return: compute local_energy = atomref + per_atom_energy.sum(); compute q from scalar_state; compute all-pair damped Coulomb residual from positions; return local_energy + sigmoid(electrostatic_log_scale)*E_elec.",
        "research_runtime/generations/generation_015/proposal_004/model/train.py: no benchmark semantic change; optionally leave TRAIN_ENERGY_WEIGHT/FORCE_WEIGHT unchanged for first test."
      ],
      "bounded_edit": [
        "Implement a small latent q_head and direct real-space damped pair energy; do not port full SpookyNet or full CACE ChargeEq/Ewald solve in the first proposal.",
        "Neutralize charges per sample: q = q_raw - q_raw.mean(); optionally divide by sqrt(N) or clamp/tanh q_raw to stabilize.",
        "Use beta initialized very small (sigmoid(-5) or learnable 0.01 multiplier) so source behavior is recoverable.",
        "Use all-pairs for small molecules; if runtime is high, use a smooth larger cutoff but avoid discontinuous top-k selection.",
        "Ablation/control: beta fixed zero should reproduce source; q_head without E_elec must not be counted as mechanism; compare energy/gap and force consistency."
      ],
      "downgrade_reasons": []
    },
    {
      "mechanism_id": "GEN016-W01-gradient-domain-physics-regularization-guardrail",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "paper_artifact:paper_003"
      ],
      "concrete_mechanism": "Use sGDML/GDML as a training-target guardrail: conserve force-from-energy and consider a small gradient-consistency or finite-difference sanity regularizer only if it can be implemented without changing benchmark labels or metrics.",
      "current_code_insertion_point": [
        "model/train.py: run_epoch after pred_energy,pred_forces if ever used; must be off or tiny by default",
        "model/model.py: keep forward returning forces from energy autograd"
      ],
      "bounded_edit": [
        "Do not add direct force head.",
        "Do not change benchmark loss targets or eval metrics.",
        "At most add a disabled-by-default finite-difference smoke check for candidate architecture debugging."
      ],
      "downgrade_reasons": [
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "mechanism_id": "GEN016-W02-full-spookynet-nonlocal-transformer-rewrite",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "paper_artifact:paper_002"
      ],
      "concrete_mechanism": "A full all-to-all transformer-style nonlocal interaction with charge/spin embeddings is scientifically relevant but not bounded for generation_016 because the SpookyNet repo clone failed and current benchmark samples lack charge/spin labels.",
      "current_code_insertion_point": [
        "model/model.py would need a new global interaction stack; too rewrite-heavy for current round."
      ],
      "bounded_edit": [
        "Do not use as strong evidence; query/clone SpookyNet again later only if a full nonlocal rewrite is intentionally in scope."
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
    "GEN016-M01-cace-shadow-body-order-representation",
    "GEN016-M02-bounded-electrostatic-energy-decomposition"
  ],
  "blueprints": [
    {
      "blueprint_id": "GEN016-M01-cace-shadow-body-order-representation",
      "mechanism_id": "GEN016-M01-cace-shadow-body-order-representation",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_015/proposal_004/model/model.py: EvolutionMLIP.__init__ after RBF buffer setup and before self.interactions: add small CartesianBodyOrderBranch(hidden_dim, num_rbf or cace_rbf=6, l_max=2, max_nu=2) and residual scalar alpha parameter initialized near -4 sigmoid or 0 scalar.",
        "research_runtime/generations/generation_015/proposal_004/model/model.py: EvolutionMLIP.forward_energy after dij/unit/rbf/cutoff_weight are computed and before/after the existing interaction loop: compute cace_B = self.body_order_branch(numbers, i_idx, j_idx, rij, dij, unit, rbf, cutoff_weight), residual_per_atom = self.body_order_readout(cace_B), add alpha * residual_per_atom.sum() to atomref + existing per_atom_energy.sum().",
        "research_runtime/generations/generation_015/proposal_004/model/train.py: keep dataloader, losses, energy/force weights, split/eval semantics; optionally add no new CLI/config dependency."
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "GEN016-M02-bounded-electrostatic-energy-decomposition",
      "mechanism_id": "GEN016-M02-bounded-electrostatic-energy-decomposition",
      "implementation_ready": true,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "research_runtime/generations/generation_015/proposal_004/model/model.py: EvolutionMLIP.__init__ after readout modules: add self.charge_head = nn.Linear(hidden_dim, 1), self.electrostatic_log_scale = nn.Parameter(torch.tensor(-5.0)), and buffers/constant sigma/eps.",
        "research_runtime/generations/generation_015/proposal_004/model/model.py: EvolutionMLIP.forward_energy after scalar_state is finalized and before return: compute local_energy = atomref + per_atom_energy.sum(); compute q from scalar_state; compute all-pair damped Coulomb residual from positions; return local_energy + sigmoid(electrostatic_log_scale)*E_elec.",
        "research_runtime/generations/generation_015/proposal_004/model/train.py: no benchmark semantic change; optionally leave TRAIN_ENERGY_WEIGHT/FORCE_WEIGHT unchanged for first test."
      ],
      "blocked_until": []
    },
    {
      "blueprint_id": "GEN016-W01-gradient-domain-physics-regularization-guardrail",
      "mechanism_id": "GEN016-W01-gradient-domain-physics-regularization-guardrail",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/train.py: run_epoch after pred_energy,pred_forces if ever used; must be off or tiny by default",
        "model/model.py: keep forward returning forces from energy autograd"
      ],
      "blocked_until": [
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "blueprint_id": "GEN016-W02-full-spookynet-nonlocal-transformer-rewrite",
      "mechanism_id": "GEN016-W02-full-spookynet-nonlocal-transformer-rewrite",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py would need a new global interaction stack; too rewrite-heavy for current round."
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
    "GEN016-M01-cace-shadow-body-order-representation",
    "GEN016-M02-bounded-electrostatic-energy-decomposition"
  ],
  "weak_or_hypothesis_mechanisms": [
    "GEN016-W01-gradient-domain-physics-regularization-guardrail",
    "GEN016-W02-full-spookynet-nonlocal-transformer-rewrite"
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
  "mechanism_card_count": 4,
  "strong_mechanism_card_count": 2,
  "provenance_record_count": 11
}
```

## what_not_to_use_as_strong_evidence

```json
{
  "weak_or_hypothesis_mechanisms": [
    "GEN016-W01-gradient-domain-physics-regularization-guardrail",
    "GEN016-W02-full-spookynet-nonlocal-transformer-rewrite"
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
