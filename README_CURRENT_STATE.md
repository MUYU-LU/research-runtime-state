# Current MLIP Evolution State

This file is the first local state note for new OpenClaw sessions.

## Active runtime

Local staging runtime:
`/home/lmy/.openclaw/workspace/research_runtime`

Active remote runtime:
`/public/home/lmy/MLIP_EVOLUTION/research_runtime`

Old remote archive, do not use for active work:
`/public/home/lmy/MLIP_EVOLUTION_G1`

## Current round state

`generation_001` is complete.

`generation_002` has been materialized, implemented, synced, smoke-checked, and launched.
The eight selected runnable units are currently mirrored locally and remotely.

Latest verified inspection after script fix:
- `status_mismatch = false`
- `current_generation = generation_002`
- remote status files are readable
- remote PIDs were alive when inspected
- `next_safe_step.kind = timeout_stop`
- `next_safe_step.unit = generation_002/proposal_001`

The timeout recommendation comes from the configured wall-clock budget, not from a code implementation failure.
Use `remote_inspect.py --json` again before taking action, then follow its current `next_safe_step`.

## Important script note

`runtime_common.py` was fixed so remote commands are executed as one quoted `bash -lc` command through ssh.
Without this fix, `fetch_remote_json()` could falsely report existing remote JSON files as missing.

## What not to do

Do not restart, sync, smoke, or launch `generation_001` again.
Do not relaunch `generation_002` while its current remote PIDs may still be alive.
Do not use stale memory files that say generation_001 is the active round.
Do not use `/home/lmy/.openclaw/workspace/temp_pdfs`; it was a temporary cache and has been removed.
Do not use `/public/home/lmy/MLIP_EVOLUTION_G1` as active runtime.
Do not handwrite ssh/scp/nohup/kill for normal orchestration; use bundled scripts.

## Next valid actions

1. Run `remote_inspect.py --json`.
2. If `status_mismatch == true`, reconcile first.
3. If `next_safe_step.kind == timeout_stop`, use `remote_stop_unit.py` for the indicated unit.
4. If a unit is no longer alive, collect through `remote_collect_unit.py`.
5. Do not advance a new round until all selected `generation_002` units are terminal.

Updated: 2026-04-17T08:32:48.750200+00:00
