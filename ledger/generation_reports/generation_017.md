# generation_017 outcome report

- source_unit: `generation_016/proposal_002`
- parent_Q_total: `3.9425481167873127`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_017/proposal_003",
  "Q_rmd17": 4.087588139313619,
  "Q_iso17": 3.602184007105058,
  "Q_total": 3.9176966930406225,
  "outcome_class": "neutral_variance"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 5,
  "control_replicate": 2,
  "neutral_variance": 1
}
```

## Lessons

- No child beat parent generation_016/proposal_002; keep parent unless a reviewed override is chosen.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_017/proposal_001` | benchmark_tradeoff | terminal_success | 3.8834835496867095 | -0.05906456710060315 | model/model.py +22/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_017/proposal_002` | benchmark_tradeoff | terminal_success | 3.8704915109905977 | -0.07205660579671491 | model/model.py +18/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_017/proposal_003` | neutral_variance | terminal_success | 3.9176966930406225 | -0.024851423746690138 | model/model.py +22/-0 | abs(delta_Q)=0.0248514 within margin=0.03 |
| `generation_017/proposal_004` | benchmark_tradeoff | terminal_success | 3.905862960647675 | -0.03668515613963752 | model/model.py +28/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_017/proposal_005` | benchmark_tradeoff | terminal_success | 3.889639743009369 | -0.05290837377794366 | model/model.py +56/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_017/proposal_007` | control_replicate | terminal_success | 3.8868060502667934 | None | no tracked code diff | unit is marked as a control replicate |
| `generation_017/proposal_008` | control_replicate | terminal_success | 3.912585595964674 | None | no tracked code diff | unit is marked as a control replicate |
| `generation_017/proposal_010` | benchmark_tradeoff | terminal_success | 3.8824281784035946 | -0.0601199383837181 | model/train.py +4/-4 | some component metrics improved but other tracked metrics regressed strongly |
