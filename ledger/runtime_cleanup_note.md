# Runtime Cleanup Note

- time_utc: 2026-04-18T12:34:01.687169+00:00
- deleted remote legacy state file: `/public/home/lmy/MLIP_EVOLUTION/research_runtime/ACTIVE_STATE.json`
- moved remote bad layout directory out of active runtime: `research_runtime/generations/generation_001/generation_001` -> `/public/home/lmy/MLIP_EVOLUTION/_quarantine_research_runtime_legacy/generation_001_nested_duplicate`
- rebuilt local and remote `ledger/frontier.jsonl` records for completed generation_003 and generation_004 units from existing outputs.
- added layout guard to `remote_sync_unit.py` to reject nested `generation_*` directories inside a generation directory after sync.
- current generation_005 unit code/status was not modified by this cleanup; OpenClaw's own current next step remains authoritative via `remote_inspect.py --json`.
