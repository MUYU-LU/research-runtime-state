# generation_015 outcome report

- source_unit: `generation_014/proposal_009`
- parent_Q_total: `3.8988711909426823`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_015/proposal_004",
  "Q_rmd17": 4.075989472741923,
  "Q_iso17": 3.623719881734134,
  "Q_total": 3.9176951158891966,
  "outcome_class": "neutral_variance"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 3,
  "control_replicate": 1,
  "negative_method": 2,
  "neutral_variance": 2
}
```

## Lessons

- No child beat parent generation_014/proposal_009; keep parent unless a reviewed override is chosen.
- Negative methods should not be repeated unless the proposal addresses the recorded failure pattern.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_015/proposal_001` | neutral_variance | terminal_success | 3.887328540650824 | -0.011542650291858525 | model/model.py +11/-1; model/train.py +17/-7 | abs(delta_Q)=0.0115427 within margin=0.03 |
| `generation_015/proposal_002` | benchmark_tradeoff | terminal_success | 3.868785674771593 | -0.03008551617108912 | model/model.py +3/-1; model/train.py +17/-7 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_015/proposal_003` | negative_method | terminal_success | 3.8543139745676527 | -0.04455721637502963 | model/model.py +12/-1; model/train.py +17/-7 | Q_total lost and no tracked component metric improved relative to parent |
| `generation_015/proposal_004` | neutral_variance | terminal_success | 3.9176951158891966 | 0.018823924946514303 | model/model.py +17/-3; model/train.py +17/-7 | abs(delta_Q)=0.0188239 within margin=0.03 |
| `generation_015/proposal_005` | benchmark_tradeoff | terminal_success | 3.864848583636104 | -0.034022607306578134 | model/model.py +8/-1; model/train.py +17/-7 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_015/proposal_007` | benchmark_tradeoff | terminal_success | 3.827418352240584 | -0.07145283870209829 | model/model.py +2/-1; model/train.py +17/-7 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_015/proposal_008` | control_replicate | terminal_success | 3.906487680290021 | None | no tracked code diff | unit is marked as a control replicate |
| `generation_015/proposal_009` | negative_method | terminal_success | 3.857973765444215 | -0.04089742549846731 | model/model.py +6/-2; model/train.py +17/-7 | Q_total lost and no tracked component metric improved relative to parent |
