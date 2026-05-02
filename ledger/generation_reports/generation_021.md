# generation_021 outcome report

- source_unit: `generation_020/proposal_003`
- parent_Q_total: `4.047840586729483`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_021/proposal_007",
  "Q_rmd17": 4.205550155366414,
  "Q_iso17": 3.7556591302237874,
  "Q_total": 4.048088296566495,
  "outcome_class": "control_replicate"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 2,
  "control_replicate": 1,
  "negative_method": 1,
  "neutral_variance": 4
}
```

## Lessons

- No child beat parent generation_020/proposal_003; keep parent unless a reviewed override is chosen.
- Negative methods should not be repeated unless the proposal addresses the recorded failure pattern.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_021/proposal_001` | neutral_variance | terminal_success | 4.047536521538605 | -0.000304065190877445 | model/model.py +18/-1 | abs(delta_Q)=0.000304065 within margin=0.03 |
| `generation_021/proposal_002` | benchmark_tradeoff | terminal_success | 3.994747999311766 | -0.05309258741771661 | model/model.py +17/-1 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_021/proposal_003` | neutral_variance | terminal_success | 4.040912217036441 | -0.00692836969304178 | model/model.py +17/-1 | abs(delta_Q)=0.00692837 within margin=0.03 |
| `generation_021/proposal_004` | neutral_variance | terminal_success | 4.036724566415289 | -0.011116020314193342 | model/train.py +15/-3 | abs(delta_Q)=0.011116 within margin=0.03 |
| `generation_021/proposal_006` | neutral_variance | terminal_success | 4.040471609843766 | -0.007368976885716805 | model/model.py +17/-1; model/train.py +6/-2 | abs(delta_Q)=0.00736898 within margin=0.03 |
| `generation_021/proposal_007` | control_replicate | terminal_success | 4.048088296566495 | None | no tracked code diff | unit is marked as a control replicate |
| `generation_021/proposal_008` | benchmark_tradeoff | terminal_success | 3.9804917918049663 | -0.0673487949245164 | model/model.py +29/-2 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_021/proposal_009` | negative_method | terminal_success | 3.9833527877346557 | -0.06448779899482693 | model/train.py +6/-1 | Q_total lost and no tracked component metric improved relative to parent |
