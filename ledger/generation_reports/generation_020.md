# generation_020 outcome report

- source_unit: `generation_019/proposal_003`
- parent_Q_total: `4.02603007293594`
- margin: `0.03`
- did_any_child_beat_parent: `False`

## Best child

```json
{
  "unit": "generation_020/proposal_003",
  "Q_rmd17": 4.198151719111425,
  "Q_iso17": 3.7686913408773046,
  "Q_total": 4.047840586729483,
  "outcome_class": "neutral_variance"
}
```

## Outcome counts

```json
{
  "benchmark_tradeoff": 2,
  "control_replicate": 1,
  "neutral_variance": 5
}
```

## Lessons

- No child beat parent generation_019/proposal_003; keep parent unless a reviewed override is chosen.

## Units

| unit | outcome_class | run_state | Q_total | delta_Q_vs_parent | code_delta | notes |
|---|---|---|---:|---:|---|---|
| `generation_020/proposal_001` | neutral_variance | terminal_success | 4.019916294362016 | -0.006113778573924478 | model/model.py +59/-1 | abs(delta_Q)=0.00611378 within margin=0.03 |
| `generation_020/proposal_002` | neutral_variance | terminal_success | 4.0422869429257755 | 0.01625686998983511 | model/model.py +63/-1 | abs(delta_Q)=0.0162569 within margin=0.03 |
| `generation_020/proposal_003` | neutral_variance | terminal_success | 4.047840586729483 | 0.021810513793542263 | model/model.py +58/-1 | abs(delta_Q)=0.0218105 within margin=0.03 |
| `generation_020/proposal_004` | benchmark_tradeoff | terminal_success | 3.9955239619246834 | -0.030506111011256998 | model/model.py +64/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_020/proposal_005` | neutral_variance | terminal_success | 4.01585076696343 | -0.010179305972510377 | model/model.py +60/-2; model/train.py +1/-1 | abs(delta_Q)=0.0101793 within margin=0.03 |
| `generation_020/proposal_006` | benchmark_tradeoff | terminal_success | 3.9823875207011303 | -0.04364255223481006 | model/model.py +58/-1; model/train.py +10/-0 | some component metrics improved but other tracked metrics regressed strongly |
| `generation_020/proposal_007` | neutral_variance | terminal_success | 3.9968023701849615 | -0.029227702750978857 | model/model.py +12/-11 | abs(delta_Q)=0.0292277 within margin=0.03 |
| `generation_020/proposal_008` | control_replicate | terminal_success | 3.9806335007424267 | None | no tracked code diff | unit is marked as a control replicate |
