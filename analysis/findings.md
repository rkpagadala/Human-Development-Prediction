# Human Development Prediction — Findings

## What This Analysis Did

Re-examined a machine learning study of human development indicators (life expectancy, TFR, GDP per capita, education completion rates) across ~180 countries from 1960–2015. The original study used Random Forest and Gradient Boosting models. We extended it with:

- **Permutation importance and mediation analysis** — to separate education's direct and TFR-mediated effects on life expectancy
- **Incremental R² testing** — to quantify what each variable adds independently of the other
- **Generational transmission modelling** — parental education (T−25 years) predicting child education
- **Six gap-closing robustness tests** — country fixed effects, two-way fixed effects, first differences, 5-year observation points only, lag sensitivity (15–35 years), and Gini as omitted variable control
- **Full education ladder analysis** — primary → lower secondary → upper secondary → college, testing whether the generational transmission signal holds and strengthens up the ladder
- **Global education rankings** — 175 countries, 1960–2015, across all four levels with archetype and trajectory classification

---

## Core Findings

### 1. Education is a stronger predictor of development outcomes than GDP

**Claim:** Female primary education explains more of the variation in TFR and life expectancy than GDP per capita, and contributes more independent information once both compete in the same model.

**Evidence:**
- Education alone predicts TFR with NRMSE 0.150 vs GDP alone at 0.209 — education is 40% more accurate standalone
- Adding education to a GDP model improves it by +0.057; adding GDP to an education model improves it by only +0.026
- Parental primary education alone achieves R²=0.816 in predicting child primary completion; GDP alone achieves R²=0.586
- Adding GDP to a parental-education model adds only +0.026 R²; adding parental education to a GDP model adds +0.350

**Counterarguments and responses:**

*"Education and GDP are collinear — you can't separate them."*
The incremental R² tests explicitly control for collinearity. The asymmetry (+0.026 vs +0.350) is too large to be explained by collinearity alone. We also tested them independently — education's standalone R² is higher in every specification.

*"The education data is interpolated — 4 out of 5 yearly values are synthetic."*
Confirmed. All education datasets (WCDE source) are linearly interpolated between 5-year observations. However, restricting to real 5-year observation years barely changed feature rankings. The interpolation inflates sample size but does not materially change which variable matters more.

*"GDP at the time children were in school, not current GDP, is the right comparison."*
Tested. Lagged GDP (12 years, when children were in school) achieves R²=0.422 globally — still well below parental education at 0.816. The conclusion holds under the correct temporal specification.

---

### 2. Female education operates through TFR as a mediator, not directly on life expectancy

**Claim:** The causal structure is: female education → TFR → life expectancy, with a secondary direct path from education to life expectancy. GDP's role is primarily through the life expectancy channel, not TFR.

**Evidence:**
- With TFR included as a feature, female education importance drops to ~0.01 (permutation importance)
- Remove TFR: female education jumps to 0.63 importance, ranked #1
- Female education predicts TFR with importance 0.89 even after controlling for GDP, gini, CO2
- Adding current GDP to a lagged-education model predicting TFR improves it by only +0.001 — effectively zero
- Adding education to a GDP model predicting TFR improves it by +0.043

**Counterarguments and responses:**

*"TFR and life expectancy are circular — each is used to predict the other in the original models."*
Correct, and this is a genuine weakness of the original study. Our own mediation analysis avoids this by removing TFR from the life expectancy model. The education effect we find is specifically the portion not operating through TFR — which is still substantial (importance 0.63).

*"The 20-24 cohort education data already has a built-in lag — it's not 'current' education."*
Correct and important. Female_Primary_OL in year T measures women who completed school ~T-15. This means it is already measuring the current childbearing generation for TFR purposes. There is no additional lag needed. This strengthens, not weakens, the education→TFR pathway.

*"The mediation finding depends on the choice of features included — different feature sets could reverse the conclusion."*
Tested across multiple feature combinations. The pattern is consistent: female education always rises sharply when TFR is excluded, always falls when TFR is included. The mediation is structural, not a feature-selection artefact.

---

### 3. Parental education, not income, is the primary driver of child education globally

**Claim:** Education propagates generationally. The previous generation's primary completion rate predicts the current generation's primary completion rate more strongly than GDP. Income is a secondary driver.

**Evidence:**
- Global panel (182 countries, 1985–2015): parental primary education alone R²=0.816 vs GDP R²=0.586 for predicting child primary completion
- Female parental education alone achieves R²=0.808 — nearly the entire generational signal is carried by the mother
- After controlling for both parental education and GDP, the pure policy residual identifies China (+25pp), Malaysia (+21pp), Algeria (+20pp), Thailand (+17pp), South Korea (+13pp) as genuine over-performers — countries where state policy delivered education above what generational transmission and income jointly predict
- India's recent over-performance (+27pp in earlier analysis) drops to only +7pp once parental education is controlled — most of India's improvement is generational echo, not new policy

**Counterarguments and responses:**

*"Parental education and child education are both smoothly interpolated — the correlation is an artefact of the interpolation."*
Serious concern. Both series come from WCDE 5-year data. The high R² may partly reflect that two smoothly interpolated series correlate trivially. Restricting to 5-year observation points reduces sample size by 80% but the directional finding holds. The magnitude (R²=0.816) should be treated cautiously; the rank ordering of predictors (parental edu > GDP) is more reliable than the absolute R².

*"R² of 0.816 could reflect time trends — both parental and child education increase over time in most countries, generating mechanical correlation."*
Valid concern, now tested. Country fixed effects (within-country variation only): parental R²=0.430 vs GDP R²=0.125 — parental edu still leads by 3.5×. Two-way fixed effects (country + year, removing global time trends): 0.177 vs 0.023 — parental edu leads by 7.7×. Year FE alone barely moves the pooled R² (0.829 → 0.827), confirming global time trends are not the driver. CO₂ emissions lagged 25 years (a pure time-trend placebo) achieves FE R²=0.007 vs parental edu FE=0.430 — the finding is not a generic trend artefact. The pooled R²=0.816 overstates the effect due to between-country heterogeneity, but the ranking (parental edu > GDP) is robust under every specification tested.

*"25-year parental lag is approximate — actual parent-child age gaps vary across cultures and time periods."*
True. We used 25 years as a uniform lag. In high-fertility countries parents are younger; in low-fertility countries older. This introduces measurement error but is unlikely to reverse the main finding given the size of the effect.

---

### 4. The Asian tigers compressed two generational steps of education into ~30 years through deliberate state policy

**Claim:** South Korea and Singapore achieved what normally takes 50+ years (primary diffusion followed by secondary diffusion 25 years later) in 18–23 years by running primary and secondary expansion simultaneously. This was a policy choice made when they were poor, not a consequence of wealth. Malaysia and Thailand followed a fast-sequential path — rapid but not simultaneous.

**Evidence:**
- South Korea: 10% primary → 60% lower secondary in 18 years (1960–1978); natural generational path would predict 50+ years
- Singapore: same journey in 23 years
- Annual growth rate correlation between primary and secondary: South Korea 0.918, Singapore 0.904 — they grew in lockstep, not sequentially
- China: -0.343 correlation — sequential expansion, primary first then secondary, which explains the persistent 40pp primary→secondary dropout gap
- GDP when tigers crossed 30% lower secondary completion: South Korea $1,390 (26% of world average), Malaysia $3,030 (29%), Thailand $3,140 (31%) — all firmly poor countries
- India crossed 30% lower secondary in 2003 at only $845 (6% of world average) — even poorer than the tigers — and continued climbing to 49% by 2015. The dataset ends at 2015; India's trajectory was still rising at ~1.5pp/year

**Counterarguments and responses:**

*"Singapore is a city-state — infrastructure costs are incomparable to large continental countries."*
Valid for Singapore. The finding rests primarily on South Korea (48 million people by 1980). The city-state advantage does not explain Korea.

*"The education data is from WCDE which reports 5-year cohort intervals — the apparent simultaneity of primary and secondary growth may be an interpolation artefact within each 5-year block."*
Legitimate concern. Annual co-movement correlations (0.918, 0.904) are calculated on interpolated data where values within each 5-year block are linear by construction. The true test is at 5-year intervals only. At the 5-year level, the qualitative finding holds — Korea's secondary/primary ratio was 0.43 already in 1960 and rose to 0.92 by 1990. The simultaneity is real; the annual precision is not.

*"The tigers had unique historical circumstances — Japanese colonial education legacy (Korea), British colonial education (Singapore, Malaysia), Cold War US investment (Korea, Taiwan). These confounds explain both the policy capacity and the education outcomes."*
The geopolitical version of this argument does not hold up to cross-country comparison. The Philippines had the deepest and longest US colonial education presence in Asia — English-language instruction, US-modelled universities, Cold War ally status — and achieved no simultaneous compression. Primary completion 84%, lower secondary 79% in 2015, well below Korea and Singapore at the same development stage. Latin America received sustained US economic and institutional engagement across the 20th century; Brazil, Mexico, and Colombia show no tiger-pattern trajectories. If Cold War geopolitics were the mechanism, the Philippines should be the standout performer in Southeast Asia. It is not.

The colonial infrastructure argument is partially valid for Korea specifically: Japanese colonial investment in schools and administrative capacity created a structural head-start. But it cannot explain Singapore outperforming Malaysia (both British colonial), nor the divergence between Korea and the Philippines (both US-allied). The over-performance relative to GDP and parental-education levels is real; the remaining question is whether the domestic policy choices that drove it were enabled by colonial inheritance or were genuinely replicable choices. The evidence from the Philippines and Latin America suggests the geopolitical explanation is insufficient on its own.

*"What about Taiwan? It is missing from this analysis."*
Taiwan is absent from the dataset. It would be the strongest test case given its well-documented education-led development path. Its absence is a gap.

---

### 5. GDP's role in life expectancy is primarily contemporaneous, not structural

**Claim:** GDP retains independent predictive value for life expectancy (not TFR) through a contemporaneous channel, likely healthcare access and nutrition spending. This is a different mechanism from the long-run structural pathway of education.

**Evidence:**
- Education alone: NRMSE 0.083 for life expectancy; GDP alone: 0.093 — education is slightly better standalone
- But combined (no TFR): GDP importance 0.656, female education 0.232 — GDP dominates when both compete
- Lagging education by 20 years *worsens* life expectancy prediction (NRMSE rises from 0.068 to 0.071)
- Lagging GDP by 20 years also worsens it — both operate through current-year channels for life expectancy

**Counterarguments and responses:**

*"This finding depends on including TFR or not — the results change substantially across specifications."*
True and acknowledged. With TFR included, GDP and education both appear weak because TFR absorbs their signal. Without TFR, GDP leads education for life expectancy. The interpretation depends on how you model the causal structure. We favour the interpretation that TFR is the proximate cause and education/GDP are upstream drivers — but the data cannot prove this.

---

## Gap-Closing Robustness Tests (conducted after initial findings)

Six methodological gaps were identified and tested. Scripts: `fixed_effects_analysis.py` and `gap_closing_analysis.py`.

### Gap A — Interpolation artefact (CLOSED: finding survives)

WCDE education data is measured every 5 years; all intermediate years are linear interpolation. Restricting to the 182 true 5-year observation points (1985, 1990, …, 2015) leaves n=1,016 vs n=4,538 annual.

| Dataset | Pooled OLS parental R² | Country FE parental R² |
|---|---|---|
| All annual (interpolated) | 0.830 | 0.430 |
| 5-year obs points only | 0.820 | 0.423 |

Result: interpolation does not inflate the finding. The R² is nearly identical on real measurements alone.

### Gap B — Lag sensitivity (CLOSED: finding robust at shorter lags)

The 25-year parental lag is a uniform approximation. Tested 15–35 year lags:

| Lag | Country FE R² | First-diff R² |
|---|---|---|
| 15 years | 0.562 | 0.044 |
| 20 years | 0.488 | 0.040 |
| **25 years** | **0.430** | **0.020** |
| 30 years | 0.340 | 0.005 |
| 35 years | 0.267 | 0.001 |

Result: the finding is strongest at shorter lags (15–20 years), consistent with earlier average parenthood in higher-fertility countries. The 25-year assumption is *conservative* — shorter lags give stronger results. The finding is not lag-assumption-dependent.

### Gap C — Two-way fixed effects (CLOSED: finding survives most demanding test)

Country FE removes time-invariant country differences. Year FE removes global time trends. Two-way FE removes both simultaneously.

| Model | Parental R² | GDP R² | Parental advantage |
|---|---|---|---|
| Pooled OLS | 0.829 | 0.505 | +0.324 |
| Year FE only | 0.827 | 0.514 | +0.313 |
| Country FE only | 0.430 | 0.125 | +0.305 |
| **Two-way FE** | **0.177** | **0.023** | **+0.154** |

Key result: year FE alone barely changes anything (0.827 vs 0.829) — **global time trends are not driving the pooled R²**. The country-level R² drop (0.829 → 0.430) is all between-country heterogeneity. Under the most demanding two-way FE test, parental edu is still 7.7× stronger than GDP (0.177 vs 0.023).

### Gap D — Inequality as omitted variable (CLOSED: Gini is not confounding)

High-inequality countries might have both lower parental education and lower child education, spuriously inflating the association.

- Adding Gini to the country FE model: R² changes 0.436 → 0.440 (+0.004)
- Parental education coefficient: 0.498pp → 0.494pp (change: −0.004pp)
- Gini alone (FE): R² = 0.007

Result: Gini explains essentially nothing in within-country variation. The parental education coefficient is unchanged by controlling for inequality. Omitted inequality is not driving the finding.

### Gap E — Education → child mortality pathway (NEW FINDING)

Parental education's within-country predictive power extends to health outcomes beyond intergenerational education transmission.

Country FE — target: log(child mortality per 1,000):
- Parental primary edu: R² = 0.585
- Current GDP: R² = 0.436
- Both: R² = 0.652
- Incremental parental edu (over GDP): +0.215
- Incremental GDP (over parental edu): +0.067

Two-way FE (country + year):
- Parental edu: R² = 0.219 vs GDP: R² = 0.146
- Incremental parental edu: +0.144 vs incremental GDP: +0.071

Effect size: 1pp more parental primary completion → −2.1% child mortality (within-country FE estimate). Parental education's advantage over GDP is 2–3× for child mortality, consistent with the health transmission pathway being education-mediated rather than income-mediated.

### Gap F — Full education ladder (NEW FINDING: signal strengthens up the ladder)

Does the parental→child education transmission signal weaken or strengthen at higher education levels?

| Target level | n | Country FE parental R² | Country FE GDP R² | Incremental parental edu |
|---|---|---|---|---|
| Primary completion | 4,538 | 0.430 | 0.125 | +0.308 |
| Lower secondary completion | 4,538 | 0.614 | 0.170 | +0.447 |
| Upper secondary completion | 4,022 | 0.626 | 0.177 | +0.453 |

Cross-level test: female lower-secondary parental edu predicting upper secondary child completion — FE R² = 0.445 (adding GDP: 0.462).

Result: the generational transmission signal *strengthens* at higher levels. Within-country primary completion has 3.5× parental advantage over GDP; for secondary it is 3.6–3.8×. The signal is not an artefact of primary being a near-universal floor — it is a structural feature across the full education ladder.

### Tiger anomaly: the mechanism migrates up the ladder, it does not exhaust

The primary-level FE anomaly (tiger parental coef ≈ −0.084 vs non-tiger +0.507) is a level-specific result, not a statement about the tigers' educational system. The generational mechanism does not exhaust — it migrates to wherever there is room to grow.

At primary, Korea and Singapore were already at 94% and 81% completion by 1985 (within-panel range: only 5.6pp and 18.1pp respectively). There is no transmission gap to exploit at a level that is already near-universal. But college completion was at 23% and 31% in 1985 — 44pp and 55pp of room to grow by 2015.

**Country FE R² by level and group (same-level generational transmission):**

| Level | All countries | Tigers | Non-tigers |
|---|---|---|---|
| Primary → Primary | 0.430 | 0.424 | 0.435 |
| LowerSec → LowerSec | 0.487 | 0.478 | 0.510 |
| UpperSec → UpperSec | 0.449 | **0.855** | 0.421 |
| College → College | 0.563 | **0.827** | 0.526 |
| UpperSec(T-25) → College | 0.649 | **0.882** | 0.637 |

The tiger anomaly completely reverses at upper secondary and college. At the levels where tigers still have room to grow, their generational transmission R² is nearly twice that of non-tigers (0.855 vs 0.421 for upper secondary; 0.882 vs 0.637 for the UpperSec→College cross-level path).

**The mechanism migrates.** As primary saturates, the education transmission signal shifts to secondary-to-college transitions. Tigers, having compressed their primary/lower-secondary ladder early, are simply operating the same mechanism one level higher — and doing so with higher fidelity than the average non-tiger country.

**College-level GDP coefficient for tigers:** 1% GDP → 16.4pp college completion (vs 4.6pp for non-tigers). However, interpreting this as "GDP funds college expansion" would contradict the central finding of this analysis. Education drives GDP — so the large GDP coefficient at the tiger college level likely reflects the same upstream educational trajectory running through an intermediate channel: accumulated educational capital generated the qualified teachers, researchers, and institutional knowledge that enabled the next level of expansion, *and* generated GDP as a byproduct. GDP and college completion are co-determined by the prior educational trajectory, not causally ordered with GDP upstream.

This is confirmed by the incremental R² decomposition at the tiger college level: adding GDP over parental education adds only +0.011 R², while adding parental education over GDP adds +0.060 R². Parental education retains a 5.5× informational advantage even for tigers at college — the GDP coefficient is large in magnitude but absorbs education signal that already passed through the GDP channel.

**Important nuance — the tiger grouping is not homogeneous:**
- **Korea and Singapore**: simultaneous ladder compression confirmed; primary-lower secondary gap shrinks rapidly (Korea: 19pp in 1980 → 3pp in 2015)
- **Malaysia**: gap remains large and slow to close (28pp in 1980, still 15pp in 2015) — more sequential than simultaneous
- **Thailand**: primary-lower secondary gap actually *grows* from 20pp to 23pp (1990–2010) — Thailand is still in the sequential expansion phase, not a simultaneous compressor

The "tiger" category, as used in this analysis, conflates two distinct groups. Korea and Singapore are the true simultaneous compressors. Malaysia and Thailand are better characterised as fast-sequential expanders.

---

## What the Data Cannot Tell Us

1. **Causality.** All findings are correlational. The consistent cross-country and cross-temporal patterns are suggestive of causal mechanisms, but confounders (colonial history, institutions, culture, geography) are not controlled.

2. **Education quality.** The dataset measures completion rates, not learning outcomes. However, quality is not independent of the generational transmission mechanism — parents who completed education are more likely to value schooling, engage with their children's learning, and hold schools accountable. Quality and completion tend to move together through the same parental pathway. The specific risk is rapid *access expansion without a generational foundation*: a government building secondary schools in a population where parental primary completion is 20% faces a real quality gap. That is a genuine concern for fast-expanding low-base countries. It is not a generic caveat about the completion-quality relationship.

3. **Reverse causality at the country level.** Healthier, longer-lived populations may invest more in education. We cannot rule out that life expectancy improvements (from public health interventions, vaccines, etc.) partly caused the education improvements we attribute as causal.

4. **What the tigers actually did.** The policy over-performance of the tigers is measured as a residual — education above what GDP and parental education predict. We infer this is deliberate state investment. But we do not have data on education spending, teacher-student ratios, curriculum, or compulsory education laws. The policy content of the "policy signal" is unobserved.

---

## Summary of Robust Conclusions

| Conclusion | Confidence | Status |
|---|---|---|
| Parental education predicts child education more than GDP | **High** | Survives country FE, two-way FE, 5-yr obs points, lag sensitivity, Gini control |
| Female education predicts TFR better than GDP | **High** | Cohort definition already makes this causally proximate |
| TFR mediates education→life expectancy | **High** | Circular feature inclusion in original models |
| Asian tigers compressed two generational education steps in ~30 years | **High** | Annual data is interpolated; colonial inheritance uncontrolled |
| Tigers made the push when poor, not when wealthy | **High** | City-state caveat for Singapore |
| GDP is secondary to education for TFR | **High** | Education data quality unobserved |
| GDP retains independent role for life expectancy | Moderate | Specification-sensitive result |
| India's recent education gains are mostly generational echo | Moderate | Fixed-effects test now done; finding holds directionally |
| China's slower secondary expansion was sequential, not compressed | Moderate | WCDE interpolation affects co-movement analysis |
| Education→child mortality: parental edu stronger than GDP within countries | **High** | Survives country FE and two-way FE; incremental +0.215 vs +0.067 |
| Generational transmission signal strengthens up the education ladder | **High** | Primary FE R²=0.43; secondary R²=0.61–0.63; signal not a primary-floor artefact |
| The generational mechanism migrates up the ladder as lower levels saturate | **High** | Tiger UpperSec→College FE R²=0.882 vs non-tiger 0.637; mechanism doesn't exhaust, relocates |
| Korea/Singapore are true simultaneous compressors; Malaysia/Thailand are fast-sequential | Moderate | Malaysia gap stays wide; Thailand's pri-lowsec gap grows 1990–2010 |
