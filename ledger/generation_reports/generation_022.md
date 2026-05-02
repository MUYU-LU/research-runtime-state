# generation_022 outcome report

- source_unit: `generation_021/proposal_001`
- parent_Q_total: `4.047536521538605`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_022/proposal_007",
  "Q_rmd17": 4.2218266077814475,
  "Q_iso17": 3.7376975105809342,
  "Q_total": 4.052381423761268,
  "outcome_class": "control_replicate"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 1,
  "control_replicate": 1,
  "negative_method": 3,
  "neutral_variance": 3
}
```

## Lessons

- No child beat parent generation_021/proposal_001; keep parent unless a reviewed override is chosen.
- Negative methods should not be repeated unless the proposal addresses the recorded failure pattern.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_022/proposal_001` | negative_method | terminal_success | 4.015889923933675 | -0.03164659760493027 | model/model.py +21/-0 | Q_total lost and no tracked component metric improved relative to parent |
| `generation_022/proposal_002` | negative_method | terminal_success | 4.003529942707198 | -0.04400657883140724 | model/model.py +28/-0 | Q_total lost and no tracked component metric improved relative to parent |
| `generation_022/proposal_003` | neutral_variance | terminal_success | 4.03039664406702 | -0.017139877471585407 | model/model.py +34/-0 | abs(delta_Q)=0.0171399 within margin=0.03 |
| `generation_022/proposal_004` | neutral_variance | terminal_success | 4.03341008908984 | -0.01412643244876488 | model/model.py +44/-0 | abs(delta_Q)=0.0141264 within margin=0.03 |
| `generation_022/proposal_005` | benchmark_tradeoff | terminal_success | 4.014571403323885 | -0.03296511821472059 | model/model.py +22/-0; model/train.py +5/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_022/proposal_006` | neutral_variance | terminal_success | 4.042395946355124 | -0.005140575183481211 | model/model.py +38/-0 | abs(delta_Q)=0.00514058 within margin=0.03 |
| `generation_022/proposal_007` | control_replicate | terminal_success | 4.052381423761268 | None | no tracked code diff | unit is marked as a control replicate |
| `generation_022/proposal_008` | negative_method | terminal_success | 3.9976753017846547 | -0.049861219753950525 | model/model.py +30/-2 | Q_total lost and no tracked component metric improved relative to parent |
