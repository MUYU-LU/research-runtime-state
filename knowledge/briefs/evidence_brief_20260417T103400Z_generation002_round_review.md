# MLIP Evidence Brief

## question
What benchmark-centric continuation choice should guide the next round after completed `generation_002`, given all selected units, cross-dataset Q metrics, train dynamics, runtime reliability, and the explicit rule that `proposal_007` is control-only and not an advancement candidate?

## local_context
- Active review target: completed `generation_002` under `/home/lmy/.openclaw/workspace/research_runtime`.
- Source unit for all generation_002 continuations: `generation_001/proposal_004`.
- Source benchmark profile (`generation_001/proposal_004`):
  - `Q_rmd17 = 1.4697`
  - `Q_iso17 = 1.5903`
  - `Q_total = 1.5119`
  - rMD17 mixed: force `0.2241`, energy `31.1044`, gap `0.00017`
  - ISO17 mixed: force `0.2902`, energy `218.0171`, gap `0.02079`
- Required policy: compare units with benchmark-centric evidence, not force-only summaries.
- Prior local evidence brief (`evidence_brief_20260417T032900Z_proposal004_continuation.md`) recommended winner-family exploit plus one bounded jump, with control replicate used only for variance estimation.

## current_unit_profile
- Current parent/frontier family: minimal local equivariant energy-first MLIP from `generation_001/proposal_004`.
- Present capabilities in `generation_001/proposal_004/model/model.py`:
  - atom embedding plus atomref baseline
  - dense cutoff neighbor construction
  - scalar and vector hidden states
  - one local equivariant-style interaction pass
  - scalar total-energy readout, forces from autograd
- Missing / limited capabilities:
  - only one interaction stage
  - no explicit higher-body contraction
  - no principled irreps stack
  - no sparse neighbor pipeline
  - no long-range branch
- Likely bottleneck entering generation_002: limited depth/capacity and limited scalar-vector coupling, not absence of local equivariance.
- Likely implementation surface: `model/model.py` with existing `train.py` contract preserved.

## benchmark_dossier
### Generation_002 selected-unit comparison
| unit | type | Q_rmd17 | Q_iso17 | Q_total | G_delta | rMD17 mixed F/E | ISO17 mixed F/E | key note |
|---|---:|---:|---:|---:|---:|---|---|---|
| proposal_001 | exploit | 1.4496 | 2.0374 | 1.6553 | +0.1434 | 0.2544 / 23.0382 | 0.2731 / 43.6037 | best balanced exploit, all trends improving |
| proposal_002 | exploit | 1.2997 | 1.9635 | 1.5320 | +0.0201 | 0.2182 / 66.4361 | 0.2587 / 68.7813 | force good, energy regressed badly |
| proposal_003 | jump | null | null | null | null | NaN / NaN | NaN / NaN | training/eval numerically invalid despite terminal_success |
| proposal_004 | jump | 0.8602 | 2.4556 | 1.4186 | -0.0933 | 0.3342 / 107.4205 | 0.1645 / 36.1584 | huge ISO17 win, severe rMD17 collapse |
| proposal_005 | jump | 1.5755 | 1.9680 | 1.7129 | +0.2010 | 0.2108 / 24.4736 | 0.2579 / 68.8842 | best non-control Q_total, rMD17 strong |
| proposal_006 | backward | 1.4227 | 1.8736 | 1.5805 | +0.0686 | 0.2662 / 22.4109 | 0.2879 / 71.9590 | simpler but weaker than top exploit/jump |
| proposal_007 | control | 1.8519 | 1.6615 | 1.7852 | +0.2733 | 0.2393 / 5.5319 | 0.2724 / 199.3388 | control replicate only, exclude from advancement |
| proposal_008 | exploit | 1.5179 | 1.8058 | 1.6186 | +0.1067 | 0.2362 / 21.8935 | 0.2595 / 128.6283 | low-risk gain, but ISO17 energy remains poor |

### Cross-unit findings
- All units reached `terminal_success`, `launch_ready`, `remote_synced=true`, `remote_smoke_passed=true`, with `launch_count=2`, `retry_count=0`, `repair_attempts=0`.
- Reliability did not separate candidates this round. Benchmark quality did.
- `proposal_003` is the main exception: terminal state is recorded, but benchmark outputs are NaN on both datasets, so it is not a usable continuation signal.
- Best non-control `Q_total` is `proposal_005`, then `proposal_001`, then `proposal_008`.
- Best ISO17 `Q_dataset` is `proposal_004`, but it loses too much on rMD17 and ends with negative `G_delta`.
- Best rMD17 `Q_dataset` is control `proposal_007`, but it is a variance anchor, not an advancement candidate.

### Control comparison
- `proposal_007` outscored all units on `Q_total`, driven by exceptional rMD17 energy (`5.53`) and `Q_rmd17 = 1.8519`.
- But `proposal_007` also had poor ISO17 mixed energy (`199.34`) and worsening ISO17 energy trend.
- This reinforces its role as variance estimator, not architecture evidence. The round should not select it for advancement.

### Train-history trend summary
- `proposal_001`: improving force and energy trends on both datasets, no obvious instability.
- `proposal_005`: improving on rMD17, ISO17 force improving but ISO17 energy worsening, suggesting higher-capacity benefit with incomplete cross-dataset calibration.
- `proposal_008`: improving on both datasets, but final ISO17 mixed energy remains very high.
- `proposal_002`: strong force but worsening rMD17 energy and worsening ISO17 force, indicating miscalibrated coupling.
- `proposal_004`: both trends improving, yet final behavior remains highly dataset-skewed, so optimization trend alone overstates viability.
- `proposal_003`: NaN train histories, unusable.

## mathematical_evidence
- Parent unit uses one-pass local message aggregation over cutoff neighbors, with radial basis expansion, scalar edge filtering, vector messages aligned to normalized relative displacement, scalar update from aggregated scalar context, and scalar readout from scalar state plus vector norms.
- `proposal_001` mathematically preserves that form and repeats the interaction block twice, a clean depth exploit.
- `proposal_005` adds low-rank scalar-vector mixing inside a two-stage equivariant pathway, increasing representational composition without explicit triplets.
- `proposal_004` is the strongest evidence that a cleaner NequIP-like interaction can produce a large ISO17 gain, but not yet with stable cross-dataset balance.
- Benchmark consequence this round: richer forms can help, but they must be judged by `Q_total`, not isolated force or one-dataset wins.

## physical_evidence
- All successful candidates preserve energy-first force consistency via autograd, so physical consistency of the force path remained intact.
- rMD17 and ISO17 both reward local geometry, but the round shows that improved directional structure can still over-specialize by dataset.
- `proposal_004` likely captures local angular structure beneficial to ISO17 while overfitting or destabilizing rMD17 energy/force balance.
- `proposal_001` and `proposal_005` keep locality and bounded changes while avoiding the catastrophic numeric failure seen in the explicit triplet bridge.

## chemical_evidence
- Benchmark regime remains short-range molecular chemistry, where angular dependence matters but stable energy calibration across molecules/configurations matters too.
- `proposal_005` improved rMD17 materially while staying competitive on ISO17, suggesting better composition capacity for conformational molecular force fields.
- `proposal_001` improved both datasets relative to parent, making it the clearest chemistry-safe continuation.
- `proposal_004` hints that stronger equivariant interaction structure may matter for ISO17-like transfer, but the chemistry fit is incomplete unless rMD17 degradation is fixed.

## textual_evidence
- Prior local evidence brief argued for two bounded axes after the parent win: deeper winner-family exploit and one disciplined jump.
- That prediction largely held:
  - deeper exploit (`proposal_001`) worked cleanly
  - disciplined higher-capacity jump (`proposal_005`) produced the best non-control `Q_total`
  - heavier body-order triplet bridge (`proposal_003`) failed numerically
- Earlier textual evidence from NequIP/MACE remains relevant as qualitative background, but this round's decision is dominated by local benchmark evidence.

## code_evidence
- `generation_001/proposal_004/model/model.py`: one interaction pass, scalar/vector hidden state, vector contribution enters via norms, energy-first contract.
- `generation_002/proposal_001/model/model.py`: introduces `InteractionBlock` and `num_interactions=2`, a low-friction exploit.
- `generation_002/proposal_005/model/model.py`: introduces `LowRankEquivariantStage`, low-rank scalar/vector projection and gating, then stacks two stages.
- Code-fit judgment:
  - `proposal_001` is drop-in to moderate-change within current family.
  - `proposal_005` is moderate-change but still bounded and runnable-unit fit.
  - `proposal_004` is moderate-to-higher friction and needs dataset-balance repair before being a default continuation.
  - `proposal_003` shows that bounded-on-paper body-order augmentation can still be numerically fragile in this codebase.

## relevant_papers
- `SE(3)-Equivariant Graph Neural Networks for Data-Efficient and Accurate Interatomic Potentials` (NequIP), from prior brief.
- `Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields` (MACE), from prior brief.
- In this round review, these remain background support, not primary ranking evidence.

## local_literature
- Read local literature guidance from `mlip-evidence/references/local_mlip_literature.md`.
- No new local PDF extraction was needed for this round-complete benchmark review because the decisive evidence is in completed generation artifacts and the prior locally grounded brief.
- Prior local brief used as nearby evidence: `research_runtime/knowledge/briefs/evidence_brief_20260417T032900Z_proposal004_continuation.md`.

## relevant_repos
- No new repository deep-read was required for this local round review.
- Prior brief's repo evidence remains the relevant background:
  - NequIP (`mir-group/nequip`)
  - MACE (`ACEsuit/mace`)

## capability_gap
- Current validated capabilities after generation_002:
  - bounded multi-stage equivariant local interaction is viable
  - low-rank scalar-vector mixing is viable
  - exact control variance can be large, especially in energy terms
- Missing pieces for the next tier:
  - more reliable cross-dataset energy calibration
  - better separation between genuine architecture gain and seed/training variance
  - safer bounded path toward stronger ISO17 transfer without rMD17 collapse
- Integration risk by direction:
  - exploit around `proposal_001`: low
  - exploit-plus-jump around `proposal_005`: medium
  - revive NequIP-style `proposal_004`: medium to high until dataset balance improves
  - revive triplet bridge from `proposal_003`: high

## implementable_design_moves
1. **Primary exploit move around `proposal_001`**
   - principle: keep the best-balanced two-stage residual winner-family design
   - mathematical form: two repeated local scalar/vector interaction blocks
   - physical rationale: preserve local equivariant geometry while adding depth
   - chemistry relevance: improves both rMD17 and ISO17 versus parent
   - code pattern: reuse `InteractionBlock` stack
   - implementation friction: low
   - expected effect: stable cross-dataset improvement and cleaner baseline for further branching
   - bounded control/ablation: compare directly against control replicate and parent under same budget
2. **Primary jump move around `proposal_005`**
   - principle: keep two-stage locality but use low-rank scalar/vector mixing to lift capacity
   - mathematical form: low-rank latent coupling gated by radial features inside each stage
   - physical rationale: richer directional composition without explicit triplet machinery
   - chemistry relevance: strongest non-control overall, especially strong on rMD17
   - code pattern: `LowRankEquivariantStage`
   - implementation friction: medium
   - expected effect: higher ceiling than plain depth, but needs ISO17 energy calibration
   - bounded control/ablation: remove low-rank pathway while keeping two-stage depth
3. **Deprioritized jump repair around `proposal_004`**
   - principle: recover the ISO17 advantage without severe rMD17 regression
   - mathematical form: cleaner NequIP-like interaction, but with stricter calibration focus
   - physical rationale: directional quality is promising, balance is not
   - chemistry relevance: useful only if cross-dataset collapse is corrected
   - code pattern: keep isolated refactor, no extra body-order branch
   - implementation friction: medium to high
   - expected effect: potential specialized jump branch, not default continuation
   - bounded control/ablation: same structure with tighter energy calibration and direct parent comparison

## exploit_angles
- Best exploit candidate: `proposal_001`.
- Secondary exploit candidate: `proposal_008`, but only as a calibration branch, not the main frontier.
- `proposal_002` should not be the default exploit because its force gains came with clear energy degradation and mixed trend warnings.

## jump_angles
- Best non-control jump candidate: `proposal_005`.
- Secondary, specialized jump candidate: `proposal_004` only if the round deliberately pursues ISO17-focused upside with explicit rMD17-balance safeguards.
- `proposal_003` should be excluded from advancement due to NaN outputs.

## risks_or_mismatches
- Control variance is large enough that small gains should not be overclaimed.
- `proposal_007` demonstrates that the highest `Q_total` in this round can come from a control replicate, so round advancement must exclude it by policy.
- `proposal_005` has the best non-control aggregate score, but ISO17 energy remains weak and its ISO17 energy trend worsened.
- `proposal_001` is more balanced, but it still does not match the ISO17 upside glimpsed by `proposal_004`.
- `proposal_004` is attractive if judged by ISO17 alone, but benchmark-centric ranking rejects it as the main continuation because `G_delta` is negative.
- `proposal_003` indicates numeric fragility for the bounded triplet/body-order bridge in the current codebase.

## implementation_fit
- `proposal_001` has the strongest fit to next-round bounded work.
- `proposal_005` also fits bounded continuation, but should be handled as a targeted higher-capacity branch, not the only path.
- `proposal_004` is still implementable, but benchmark evidence says it is not yet the safest continuation center.
- Overall fit judgment: keep the next round centered on winner-family local equivariant models with one exploit anchor and one bounded higher-capacity jump.

## strong_evidence
- Best non-control `Q_total`: `proposal_005 = 1.7129` with `G_delta = +0.2010`.
- Best balanced non-control cross-dataset profile: `proposal_001 = 1.6553` with both datasets improving and all trends improving.
- Control-only `proposal_007` confirms meaningful variance and must not be treated as advancement evidence.
- Explicit triplet/body-order bridge (`proposal_003`) produced NaN outputs and should not drive the next round.

## weak_but_relevant
- `proposal_004` suggests a cleaner NequIP-like refactor may hold real ISO17 upside.
- `proposal_008` suggests there is still some training-budget headroom in the family, though less compelling than structural exploit/jump branches.
- `proposal_006` shows backward simplification is viable but not frontier-leading.

## background_context
- Generation_001 established `proposal_004` as the first strong local equivariant winner.
- Generation_002 tested exploit, jump, backward, and control continuations around that winner.
- The completed results support a mixed continuation strategy rather than a force-only or single-dataset strategy.

## key_findings
- Excluding control, the best continuation candidates are `proposal_005` and `proposal_001`.
- `proposal_005` is the highest-scoring non-control candidate overall.
- `proposal_001` is the most balanced and lowest-risk continuation anchor.
- The next round should be **balanced**, centered on `proposal_001` as exploit anchor and `proposal_005` as bounded higher-capacity jump.
- `proposal_007` is explicitly excluded from advancement choice because it is the required control replicate.

## useful_patterns
- Two-stage depth works.
- Low-rank scalar/vector mixing can outperform plain depth overall.
- Force improvements without energy balance are not enough.
- Specialized one-dataset wins do not beat cross-dataset `Q_total` plus positive `G_delta`.
- Terminal-success bookkeeping can still hide unusable NaN outcomes, so output validity must be checked directly.

## exploit_angles
- Anchor on `proposal_001`.
- Use `proposal_008` only as a low-risk calibration side branch if needed.

## jump_angles
- Promote `proposal_005` as the main non-control jump continuation.
- Keep `proposal_004` as optional evidence for future specialized ISO17-oriented exploration, not as default next step.

## followup_queries
- Can `proposal_005` be made more ISO17-energy-stable without losing its rMD17 gain?
- Does `proposal_001` retain its balanced advantage under another seed/control comparison?
- Is the `proposal_004` ISO17 gain recoverable with tighter calibration, or is it inherently dataset-skewed in the current implementation?
- What specific numerical instability caused NaNs in `proposal_003`?

## confidence
Medium-high. The local benchmark evidence is strong enough to exclude several paths and identify the best non-control candidates. Confidence is lower only on whether the next frontier should center purely on `proposal_001` or jointly on `proposal_001` plus `proposal_005`; that uncertainty is why the recommendation is balanced rather than purely exploit or purely jump.
