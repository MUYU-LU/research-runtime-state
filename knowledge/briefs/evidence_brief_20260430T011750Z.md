# MLIP Evidence Delta Brief

## run_metadata

```json
{
  "version": "evidence-run.v7-package-deepread",
  "generated_at_utc": "2026-04-30T01:27:28.560890+00:00",
  "mode": "jump",
  "source_unit": "generation_016/proposal_002",
  "evidence_package_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z",
  "evidence_run_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/evidence_run.json"
}
```

## evidence_package_index

```json
{
  "evidence_quality": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/evidence_quality.json",
  "evidence_provenance": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/evidence_provenance.json",
  "current_code_profile": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/current_code_profile.json",
  "benchmark_diagnosis": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/benchmark_diagnosis.json",
  "generation_memory": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/generation_memory.json",
  "mechanism_cards": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/mechanism_cards.json",
  "patch_blueprints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/patch_blueprints.json",
  "proposal_constraints": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/proposal_constraints.json",
  "audit_report": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/audit_report.json",
  "source_plan": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/source_plan.json",
  "source_artifacts_index": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/source_artifacts_index.json",
  "source_novelty": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/source_novelty.json",
  "source_analysis_requirements": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/source_analysis_requirements.json",
  "paper_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts",
  "repo_artifacts_dir": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/repo_artifacts",
  "evidence_run": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/evidence_run.json"
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
  "fresh_repo_code_verified": false,
  "has_mechanism_cards": true,
  "has_strong_mechanism_cards": false,
  "strong_mechanism_card_count": 0,
  "min_strong_mechanism_cards": 3,
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
      "min_attempted_external_sources": 7,
      "min_new_sources": 5,
      "max_recent_reused_sources": 1
    },
    "source_discovery_budget": {
      "min_successful_pdf_sources": 4,
      "min_successful_repo_sources": 3,
      "min_strong_mechanism_cards": 3,
      "max_pdf_attempts": 6,
      "max_repo_attempts": 4,
      "max_external_source_attempts": 10,
      "max_source_expansion_rounds": 2,
      "source_expansion_round": 2
    },
    "pdf_attempted_source_count": 6,
    "pdf_successful_source_count": 6,
    "repo_attempted_source_count": 4,
    "repo_successful_source_count": 0,
    "attempted_external_source_count": 10,
    "successful_external_source_count": 6,
    "source_targets_met": false,
    "source_budget_exhausted": true,
    "new_source_count": 10,
    "recent_reused_source_count": 0,
    "new_source_ids": [
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu9759u7535_-_LESu901au7528u589eu5f3au6846u67b6_9cadc4e696.pdf#7ea8271d8ced",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_Neural_P3Mu51e0u4f55GNNu957fu7a0bu76f8u4e92u4f5cu7528u589eu5f3a_6482a13b6b.pdf#c8bc30315c4f",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu901au7528u52bf_-_CHGNetu7535u8377u611fu77e5u9884u8badu7ec3u795eu7ecfu7f51u7edcu52bf_7d8d76686d.pdf#9d970111678e",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu6ce8u610fu529b_-_EFAu6b27u6c0fu5febu901fu6ce8u610fu529bu5168u5c40u539fu5b50u8868u793a_0ef43a7c38.pdf#9b564004b09e",
      "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
      "repo:ChengUCB/les#1b749b5117af",
      "repo:klicperajo/dimenet#fb2d85d9a45f",
      "repo:mir-group/nequip#ba95170e90de",
      "repo:materialsvirtuallab/matgl#21eb6f305802"
    ],
    "recent_reused_source_ids": [],
    "all_sources_recent_repeats": false,
    "source_novelty_passed": false,
    "allow_recent_source_reuse": false
  },
  "external_attempted_source_count": 10,
  "external_successful_source_count": 6,
  "source_novelty_passed": false,
  "source_budget_exhausted": true,
  "needs_source_expansion": false,
  "hard_rules": [
    "No provenance -> no strong evidence.",
    "No mechanism card -> no proposal mechanism.",
    "No formula derivation/algorithm/repo path/code trace/current insertion point -> weak evidence only.",
    "No patch blueprint -> not implementation-ready.",
    "Benchmark diagnosis is not external mechanism evidence."
  ],
  "insufficient_for_broad_jump": true,
  "insufficiency_reason": "Source expansion round 2 exhausted the configured budget (6/6 PDFs succeeded; 4/4 repository deep-read attempts failed; min successful repo sources=3 not met), and no mechanism card could be promoted to strong evidence under the package hard rules.",
  "candidate_mechanisms_not_promoted": [
    "GEN018-W01-latent-ewald-energy-decomposition",
    "GEN018-W02-euclidean-fast-attention-global-representation",
    "GEN018-W03-high-order-cartesian-tensor-shadow-branch"
  ],
  "source_expansion_round": 2,
  "repo_attempted_source_count": 4,
  "repo_successful_source_count": 0,
  "pdf_attempted_source_count": 6,
  "pdf_successful_source_count": 6
}
```

## context_references

```json
{
  "source_unit": "generation_016/proposal_002",
  "context_path": null,
  "unit_root": "/home/lmy/.openclaw/workspace/research_runtime/generations/generation_016/proposal_002",
  "current_code_profile_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/current_code_profile.json",
  "benchmark_diagnosis_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/benchmark_diagnosis.json",
  "generation_memory_path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/generation_memory.json",
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
      "total": 6,
      "success": 6,
      "fresh": 6,
      "can_support_strong": 6
    },
    "repo_code": {
      "total": 4,
      "success": 0,
      "fresh": 4,
      "can_support_strong": 0
    }
  },
  "strong_capable_sources": [
    "paper_artifact:paper_001",
    "paper_artifact:paper_002",
    "paper_artifact:paper_003",
    "paper_artifact:paper_004",
    "paper_artifact:paper_005",
    "paper_artifact:paper_006"
  ],
  "failed_sources": [
    {
      "source_id": "proposal_context",
      "type": "local_runtime_context",
      "notes": "Benchmark and history context. Useful for diagnosis, not external mechanism support."
    },
    {
      "source_id": "repo_artifact:repo_001",
      "type": "repo_code",
      "notes": "Repo deep-read failed: Traceback (most recent call last):\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 143, in <module>\n    main()\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 138, in main\n    result = read_repo(args.repo, args.max_files, args.max_file_chars, Path(args.cache_root).expanduser())\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 96, in read_repo\n    repo_root, git_action, git_warning = ensure_repo(owner, name, cache_root)\n                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 69, in ensure_repo\n    raise RuntimeError(f\"git clone failed: {result.stderr.strip() or result.stdout.strip()}\")\nRuntimeError: git clone failed: Cloning into '/home/lmy/.openclaw/workspace/.cache/mlip_evidence/repos/ChengUCB__les'...\nfatal: unable to access 'https://github.com/ChengUCB/les.git/': Failed to connect to github.com port 443 after 138946 ms: Couldn't connect to server"
    },
    {
      "source_id": "repo_artifact:repo_002",
      "type": "repo_code",
      "notes": "Repo deep-read failed: Traceback (most recent call last):\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 143, in <module>\n    main()\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 138, in main\n    result = read_repo(args.repo, args.max_files, args.max_file_chars, Path(args.cache_root).expanduser())\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 96, in read_repo\n    repo_root, git_action, git_warning = ensure_repo(owner, name, cache_root)\n                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 69, in ensure_repo\n    raise RuntimeError(f\"git clone failed: {result.stderr.strip() or result.stdout.strip()}\")\nRuntimeError: git clone failed: Cloning into '/home/lmy/.openclaw/workspace/.cache/mlip_evidence/repos/klicperajo__dimenet'...\nfatal: unable to access 'https://github.com/klicperajo/dimenet.git/': Failed to connect to github.com port 443 after 138857 ms: Couldn't connect to server"
    },
    {
      "source_id": "repo_artifact:repo_003",
      "type": "repo_code",
      "notes": "Repo deep-read failed: Traceback (most recent call last):\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 143, in <module>\n    main()\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 138, in main\n    result = read_repo(args.repo, args.max_files, args.max_file_chars, Path(args.cache_root).expanduser())\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 96, in read_repo\n    repo_root, git_action, git_warning = ensure_repo(owner, name, cache_root)\n                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 69, in ensure_repo\n    raise RuntimeError(f\"git clone failed: {result.stderr.strip() or result.stdout.strip()}\")\nRuntimeError: git clone failed: Cloning into '/home/lmy/.openclaw/workspace/.cache/mlip_evidence/repos/mir-group__nequip'...\nfatal: unable to access 'https://github.com/mir-group/nequip.git/': GnuTLS recv error (-110): The TLS connection was non-properly terminated."
    },
    {
      "source_id": "repo_artifact:repo_004",
      "type": "repo_code",
      "notes": "Repo deep-read failed: Traceback (most recent call last):\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 143, in <module>\n    main()\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 138, in main\n    result = read_repo(args.repo, args.max_files, args.max_file_chars, Path(args.cache_root).expanduser())\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 96, in read_repo\n    repo_root, git_action, git_warning = ensure_repo(owner, name, cache_root)\n                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/lmy/.openclaw/workspace/skills/mlip-evidence/scripts/read_github_repo.py\", line 69, in ensure_repo\n    raise RuntimeError(f\"git clone failed: {result.stderr.strip() or result.stdout.strip()}\")\nRuntimeError: git clone failed: Cloning into '/home/lmy/.openclaw/workspace/.cache/mlip_evidence/repos/materialsvirtuallab__matgl'...\nfatal: unable to access 'https://github.com/materialsvirtuallab/matgl.git/': Failed to connect to github.com port 443 after 137151 ms: Couldn't connect to server"
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
    "min_attempted_external_sources": 7,
    "min_new_sources": 5,
    "max_recent_reused_sources": 1
  },
  "source_discovery_budget": {
    "min_successful_pdf_sources": 4,
    "min_successful_repo_sources": 3,
    "min_strong_mechanism_cards": 3,
    "max_pdf_attempts": 6,
    "max_repo_attempts": 4,
    "max_external_source_attempts": 10,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 2
  },
  "pdf_attempted_source_count": 6,
  "pdf_successful_source_count": 6,
  "repo_attempted_source_count": 4,
  "repo_successful_source_count": 0,
  "attempted_external_source_count": 10,
  "successful_external_source_count": 6,
  "source_targets_met": false,
  "source_budget_exhausted": true,
  "new_source_count": 10,
  "recent_reused_source_count": 0,
  "new_source_ids": [
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu9759u7535_-_LESu901au7528u589eu5f3au6846u67b6_9cadc4e696.pdf#7ea8271d8ced",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_Neural_P3Mu51e0u4f55GNNu957fu7a0bu76f8u4e92u4f5cu7528u589eu5f3a_6482a13b6b.pdf#c8bc30315c4f",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu901au7528u52bf_-_CHGNetu7535u8377u611fu77e5u9884u8badu7ec3u795eu7ecfu7f51u7edcu52bf_7d8d76686d.pdf#9d970111678e",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu6ce8u610fu529b_-_EFAu6b27u6c0fu5febu901fu6ce8u610fu529bu5168u5c40u539fu5b50u8868u793a_0ef43a7c38.pdf#9b564004b09e",
    "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
    "repo:ChengUCB/les#1b749b5117af",
    "repo:klicperajo/dimenet#fb2d85d9a45f",
    "repo:mir-group/nequip#ba95170e90de",
    "repo:materialsvirtuallab/matgl#21eb6f305802"
  ],
  "recent_reused_source_ids": [],
  "all_sources_recent_repeats": false,
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
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu9759u7535_-_LESu901au7528u589eu5f3au6846u67b6_9cadc4e696.pdf#7ea8271d8ced",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_001.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_002",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_Neural_P3Mu51e0u4f55GNNu957fu7a0bu76f8u4e92u4f5cu7528u589eu5f3a_6482a13b6b.pdf#c8bc30315c4f",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_002.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_003",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_003.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_004",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu901au7528u52bf_-_CHGNetu7535u8377u611fu77e5u9884u8badu7ec3u795eu7ecfu7f51u7edcu52bf_7d8d76686d.pdf#9d970111678e",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_004.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_005",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu6ce8u610fu529b_-_EFAu6b27u6c0fu5febu901fu6ce8u610fu529bu5168u5c40u539fu5b50u8868u793a_0ef43a7c38.pdf#9b564004b09e",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_005.json",
      "success": true
    },
    {
      "artifact_ref": "paper_artifact:paper_006",
      "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_006.json",
      "success": true
    }
  ],
  "repos": [
    {
      "artifact_ref": "repo_artifact:repo_001",
      "source_id": "repo:ChengUCB/les#1b749b5117af",
      "repo": "ChengUCB/les",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/repo_artifacts/repo_001.json",
      "success": false
    },
    {
      "artifact_ref": "repo_artifact:repo_002",
      "source_id": "repo:klicperajo/dimenet#fb2d85d9a45f",
      "repo": "klicperajo/dimenet",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/repo_artifacts/repo_002.json",
      "success": false
    },
    {
      "artifact_ref": "repo_artifact:repo_003",
      "source_id": "repo:mir-group/nequip#ba95170e90de",
      "repo": "mir-group/nequip",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/repo_artifacts/repo_003.json",
      "success": false
    },
    {
      "artifact_ref": "repo_artifact:repo_004",
      "source_id": "repo:materialsvirtuallab/matgl#21eb6f305802",
      "repo": "materialsvirtuallab/matgl",
      "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/repo_artifacts/repo_004.json",
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
    "min_successful_pdf_sources": 4,
    "min_successful_repo_sources": 3,
    "min_strong_mechanism_cards": 3,
    "max_pdf_attempts": 6,
    "max_repo_attempts": 4,
    "max_external_source_attempts": 10,
    "max_source_expansion_rounds": 2,
    "source_expansion_round": 2
  },
  "source_budget_exhausted": true,
  "source_targets_met": false,
  "artifact_index": {
    "papers": [
      {
        "artifact_ref": "paper_artifact:paper_001",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu9759u7535_-_LESu901au7528u589eu5f3au6846u67b6_9cadc4e696.pdf#7ea8271d8ced",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_001.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_002",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu76f8u4e92u4f5cu7528_-_Neural_P3Mu51e0u4f55GNNu957fu7a0bu76f8u4e92u4f5cu7528u589eu5f3a_6482a13b6b.pdf#c8bc30315c4f",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_002.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_003",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu7b49u53d8u67b6u6784_-_Eu28nu29u7b49u53d8u7b1bu5361u5c14u5f20u91cfu6d88u606fu4f20u9012u52bf_49ffe4f959.pdf#40e1f7ba9cb9",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_003.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_004",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu901au7528u52bf_-_CHGNetu7535u8377u611fu77e5u9884u8badu7ec3u795eu7ecfu7f51u7edcu52bf_7d8d76686d.pdf#9d970111678e",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_004.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_005",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu957fu7a0bu6ce8u610fu529b_-_EFAu6b27u6c0fu5febu901fu6ce8u610fu529bu5168u5c40u539fu5b50u8868u793a_0ef43a7c38.pdf#9b564004b09e",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_005.json",
        "success": true
      },
      {
        "artifact_ref": "paper_artifact:paper_006",
        "source_id": "local_pdf:/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/source_inputs/MLIPu529bu573au57fau51c6_-_Forces_Are_Not_Enoughu5206u5b50u6a21u62dfu8bc4u6d4b_1791e8e520.pdf#a6c222c86e12",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/paper_artifacts/paper_006.json",
        "success": true
      }
    ],
    "repos": [
      {
        "artifact_ref": "repo_artifact:repo_001",
        "source_id": "repo:ChengUCB/les#1b749b5117af",
        "repo": "ChengUCB/les",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/repo_artifacts/repo_001.json",
        "success": false
      },
      {
        "artifact_ref": "repo_artifact:repo_002",
        "source_id": "repo:klicperajo/dimenet#fb2d85d9a45f",
        "repo": "klicperajo/dimenet",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/repo_artifacts/repo_002.json",
        "success": false
      },
      {
        "artifact_ref": "repo_artifact:repo_003",
        "source_id": "repo:mir-group/nequip#ba95170e90de",
        "repo": "mir-group/nequip",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/repo_artifacts/repo_003.json",
        "success": false
      },
      {
        "artifact_ref": "repo_artifact:repo_004",
        "source_id": "repo:materialsvirtuallab/matgl#21eb6f305802",
        "repo": "materialsvirtuallab/matgl",
        "path": "/home/lmy/.openclaw/workspace/research_runtime/knowledge/evidence_runs/evidence_run_20260430T011750Z/repo_artifacts/repo_004.json",
        "success": false
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
    "GEN018-W01-latent-ewald-energy-decomposition",
    "GEN018-W02-euclidean-fast-attention-global-representation",
    "GEN018-W03-high-order-cartesian-tensor-shadow-branch"
  ],
  "proposal_allowed_mechanisms": [],
  "proposal_blocked_mechanisms": [
    "unproven model-family label without formula derivation and code trace",
    "force-only proposal when energy/gap/Q context is available",
    "implementation rewrite without patch blueprint",
    "round-2 broad jump package with zero strong mechanisms",
    "repository code support missing after concrete attempts",
    "source novelty/target failure due zero successful repo deep-reads"
  ]
}
```

## new_mechanism_cards_summary

```json
{
  "strong_mechanism_ids": [],
  "weak_or_hypothesis_ids": [
    "GEN018-W01-latent-ewald-energy-decomposition",
    "GEN018-W02-euclidean-fast-attention-global-representation",
    "GEN018-W03-high-order-cartesian-tensor-shadow-branch"
  ],
  "cards": [
    {
      "mechanism_id": "GEN018-W01-latent-ewald-energy-decomposition",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "paper_artifact:paper_001",
        "paper_artifact:paper_002"
      ],
      "concrete_mechanism": "Add a separate differentiable long-range energy term E_lr from latent per-atom charges q_i predicted from current hidden states, then train total E = E_short + lambda_lr E_lr under the unchanged energy/force loss. LES provides reciprocal-space and finite-system Coulomb forms; Neural P3M provides mesh/FFT decomposition as a scalable alternative.",
      "current_code_insertion_point": [
        "model/model.py: EvolutionMLIP.__init__ after current energy/readout heads: add self.charge_head and scalar lambda_lr/buffer.",
        "model/model.py: EvolutionMLIP.forward_energy after final hidden states and before returning energy: compute E_lr and add to short-range energy.",
        "train.py: keep TRAIN_ENERGY_WEIGHT/TRAIN_FORCE_WEIGHT unchanged; optionally expose lambda_lr as model constant for ablation."
      ],
      "bounded_edit": [
        "Add <=60 lines: charge_head, per-batch charge centering helper, pairwise erfc Coulomb term with eps and distance clamp, lambda_lr default small (e.g. 0.02-0.1).",
        "No dataset/split/eval change; no external labels; no change to output signature.",
        "Ablate with lambda_lr=0 or charge_head disabled against parent generation_016/proposal_002."
      ],
      "downgrade_reasons": [
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "mechanism_id": "GEN018-W02-euclidean-fast-attention-global-representation",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "paper_artifact:paper_005"
      ],
      "concrete_mechanism": "Attach a lightweight global additive context branch inspired by Euclidean Fast Attention (EFA): project hidden states to q/k/v, encode positions with distance/direction Fourier features, and add an unnormalized global context to each atom before the energy head. This targets non-local correlations without repeating failed PaiNN/body-order/readout-damping directions.",
      "current_code_insertion_point": [
        "model/model.py: after the final BalancedInteractionBlock stack in EvolutionMLIP.forward_energy, before the energy readout.",
        "model/model.py: add a small GlobalContextBlock module near BalancedInteractionBlock, gated by a scalar alpha initialized small.",
        "train.py: no loss or benchmark semantic changes; alpha=0 ablation."
      ],
      "bounded_edit": [
        "Add one GlobalContextBlock with d<=32, B<=8 fixed direction/Fourier features and residual scale alpha.",
        "Do not add quadratic full attention; use graph-level sum aggregation only.",
        "Keep hidden_dim=96 and existing force autograd path unchanged."
      ],
      "downgrade_reasons": [
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "mechanism_id": "GEN018-W03-high-order-cartesian-tensor-shadow-branch",
      "claim_strength": "weak_hypothesis",
      "strong_ready": false,
      "source_refs": [
        "paper_artifact:paper_003"
      ],
      "concrete_mechanism": "Use a very small Cartesian tensor shadow branch that accumulates second-order relative-position moments per atom and feeds rotational invariants into the scalar hidden state. This is a broader representation jump than scalar/vector gates but remains bounded; however it is not strong because no HotPP/NequIP repo code trace succeeded.",
      "current_code_insertion_point": [
        "model/model.py: inside/adjacent to BalancedInteractionBlock.forward where edge vectors/distances are available; or after interaction stack if edge_index is retained.",
        "model/model.py: add TensorMomentBranch module returning delta_h; feed before final energy head.",
        "train.py: unchanged loss; branch disabled for ablation."
      ],
      "bounded_edit": [
        "Add <=80 lines computing rank-2 moment invariants with torch.einsum/index_add; avoid e3nn dependency and no full equivariant rewrite.",
        "Keep tensor branch width tiny and residual scale initialized near zero.",
        "Ablate with branch scale=0; compare to parent/control."
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
  "implementation_ready_blueprints": [],
  "blueprints": [
    {
      "blueprint_id": "GEN018-W01-latent-ewald-energy-decomposition",
      "mechanism_id": "GEN018-W01-latent-ewald-energy-decomposition",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py: EvolutionMLIP.__init__ after current energy/readout heads: add self.charge_head and scalar lambda_lr/buffer.",
        "model/model.py: EvolutionMLIP.forward_energy after final hidden states and before returning energy: compute E_lr and add to short-range energy.",
        "train.py: keep TRAIN_ENERGY_WEIGHT/TRAIN_FORCE_WEIGHT unchanged; optionally expose lambda_lr as model constant for ablation."
      ],
      "blocked_until": [
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "blueprint_id": "GEN018-W02-euclidean-fast-attention-global-representation",
      "mechanism_id": "GEN018-W02-euclidean-fast-attention-global-representation",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py: after the final BalancedInteractionBlock stack in EvolutionMLIP.forward_energy, before the energy readout.",
        "model/model.py: add a small GlobalContextBlock module near BalancedInteractionBlock, gated by a scalar alpha initialized small.",
        "train.py: no loss or benchmark semantic changes; alpha=0 ablation."
      ],
      "blocked_until": [
        "missing repo_code_path",
        "missing_repo_code_trace"
      ]
    },
    {
      "blueprint_id": "GEN018-W03-high-order-cartesian-tensor-shadow-branch",
      "mechanism_id": "GEN018-W03-high-order-cartesian-tensor-shadow-branch",
      "implementation_ready": false,
      "target_files": [
        "model/model.py",
        "model/train.py"
      ],
      "target_insertion_points": [
        "model/model.py: inside/adjacent to BalancedInteractionBlock.forward where edge vectors/distances are available; or after interaction stack if edge_index is retained.",
        "model/model.py: add TensorMomentBranch module returning delta_h; feed before final energy head.",
        "train.py: unchanged loss; branch disabled for ablation."
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
  "allowed_mechanisms": [],
  "weak_or_hypothesis_mechanisms": [
    "GEN018-W01-latent-ewald-energy-decomposition",
    "GEN018-W02-euclidean-fast-attention-global-representation",
    "GEN018-W03-high-order-cartesian-tensor-shadow-branch"
  ],
  "blocked_mechanisms": [
    "unproven model-family label without formula derivation and code trace",
    "force-only proposal when energy/gap/Q context is available",
    "implementation rewrite without patch blueprint",
    "round-2 broad jump package with zero strong mechanisms",
    "repository code support missing after concrete attempts",
    "source novelty/target failure due zero successful repo deep-reads"
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
    "No fresh repository code deep-read was recorded in this package.",
    "No mechanism card passed strong-evidence validation.",
    "Source novelty policy failed; the run did not add enough new external sources or repeated recent sources too heavily.",
    "Package is not proposal-ready; it lacks at least one mechanism with provenance, formula derivation, code trace, insertion point, and bounded edit."
  ],
  "mechanism_card_count": 3,
  "strong_mechanism_card_count": 0,
  "provenance_record_count": 19,
  "insufficient_for_broad_jump": true,
  "insufficiency_reason": "Source expansion round 2 exhausted the configured budget (6/6 PDFs succeeded; 4/4 repository deep-read attempts failed; min successful repo sources=3 not met), and no mechanism card could be promoted to strong evidence under the package hard rules."
}
```

## what_not_to_use_as_strong_evidence

```json
{
  "weak_or_hypothesis_mechanisms": [
    "GEN018-W01-latent-ewald-energy-decomposition",
    "GEN018-W02-euclidean-fast-attention-global-representation",
    "GEN018-W03-high-order-cartesian-tensor-shadow-branch"
  ],
  "blocked_mechanisms": [
    "unproven model-family label without formula derivation and code trace",
    "force-only proposal when energy/gap/Q context is available",
    "implementation rewrite without patch blueprint",
    "round-2 broad jump package with zero strong mechanisms",
    "repository code support missing after concrete attempts",
    "source novelty/target failure due zero successful repo deep-reads"
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
