# Peer Review: "Education as the Sole Primary Driver of Human Development"

*Reviewer perspective: skeptical, no prior context*

**Overall assessment:** Interesting and ambitious, but the central causal claim substantially outpaces the evidence presented. The paper argues for a strong, exclusive causal thesis while the empirics support a weaker (and still valuable) correlational claim. Several methodological choices require justification or revision before this can be published in a serious journal.

---

## 1. The Central Claim Is Overstated

The title and abstract claim education is the **sole primary driver** — a near-unfalsifiable maximalist position. The empirics show:

- Parental education predicts child education within countries (R²=0.464)
- Education at T predicts outcomes at T+25

Neither establishes that education is *causally prior* to everything else, nor that the pathway is *exclusive*. The paper repeatedly asserts that income is "downstream" of education and that provision is "endogenous" to education — but these are theoretical claims, not empirical results. The regressions show correlation with a lag structure; they do not identify the direction of causality between education and institutions/income.

**The paper needs to distinguish between:** "education is an important upstream predictor" (supportable) vs. "education is the sole primary driver and everything else is a consequence" (not established here).

---

## 2. Identification Strategy Has a Core Weakness

The authors defend excluding year fixed effects on the grounds that they "absorb the generational mechanism itself." This is circular. If a global education trend confounds the parental→child education correlation, that is exactly what year FEs are designed to control for. The CO2 placebo test is clever but insufficient — CO2 and education do not share the same *within-country* variation structure.

The authors show (Table A1) that with two-way FE, the coefficient collapses from β=0.485 to β=0.086. Rather than dismissing this as "over-controlled," the paper should explain why the identifying variation — after removing global trends — is still theoretically meaningful. Currently the argument is: "the result disappears when we control for confounds, but we argue those aren't really confounds." Reviewers will not accept this without much more careful argumentation.

---

## 3. The "Bad Control" Argument Is Applied Inconsistently

The paper correctly notes that including GDP as a control is a bad control if education causes GDP. But in Table 2, the paper controls for *initial outcomes* (initial LE, initial TFR, initial log GDP) when predicting T+25 outcomes. If education causes those outcomes too, these are also bad controls. The asymmetric application of the bad-control critique — used to exclude GDP from one spec but not when it favors the author — needs to be addressed.

---

## 4. Case Study Evidence Is Selective and Underdetermined

Table 4 is the empirical core of the argument against Sen, but it has significant weaknesses:

**The lags are fitted post-hoc.** Kerala's lag is "~60–70 years (gradual)"; Taiwan's is "~20 years"; China's is "~45 years." The range 20–70 years is so wide that nearly any observed development date could be "predicted" by some prior education investment. The P-25 label implies a 25-year mechanism, but the actual fits range 20–70 years. This requires formal justification — why does the mechanism produce such different lags across cases?

**The Kerala numbers are estimated.** The paper acknowledges Kerala figures come from India's Sample Registration System, not direct WCDE measurement. Given Kerala is one of Sen's three canonical cases, using estimated figures for the central test is a significant limitation.

**Counter-cases are not considered.** Bangladesh is listed as a policy over-performer (Table 3, +15.8pp residual) but has life expectancy of ~72 and TFR ~2.3 as of 2015 — which would mean it *has* crossed the development threshold. If so, it should appear in Table 4, not Table 3. Similarly, Cuba's 1961 literacy campaign is mentioned positively but Cuba's development trajectory is not analyzed, despite being an obvious test case with strong state provision and not obviously market-mediated.

---

## 5. The China Narrative Is Doing Too Much Work

The paper's treatment of China is sophisticated but pulls in two directions it doesn't fully resolve:

- It argues the CR *expanded* lower secondary education for rural populations (supporting P-25)
- It argues Deng's health dismantling *delayed* LE crossing by 10–15 years

But if state provision can delay development by 10–15 years when removed, that is not a "bounded perturbation" — it is evidence that provision has substantial independent effects on welfare outcomes, which is precisely Sen's claim. The paper cannot simultaneously argue (a) provision is inert/endogenous and (b) removal of provision caused a 10–15 year delay in a population-wide welfare indicator.

The "first-generation vulnerability" concept introduced to handle this is theoretically underdeveloped and introduced ad hoc to explain an inconvenient data point.

---

## 6. The Development Threshold Is Arbitrary

The USA 1960 benchmark (TFR < 3.67, LE > 70.1) is defended as theoretically motivated, but the defense conflates two different arguments:

1. "USA 1960 is the natural baseline for postcolonial development" — plausible
2. "Crossing both thresholds simultaneously is the right binary measure of development" — not established

Why simultaneously? A country that achieves LE > 70 but TFR = 3.8 has not "developed" by this measure, but intuitively has achieved substantial welfare gains. The binary threshold means small differences in TFR near 3.67 determine whether a country is coded as developed or not, creating discontinuities in Table 4 that may be sensitive to measurement error. The analysis should show robustness to alternative thresholds or a continuous measure.

---

## 7. Several Empirical Claims Lack Supporting Citations

- "education causes GDP — confirmed below (FE β=+0.0110)" — this is Table 2, which controls for *initial GDP*. This does not establish that education *causes* GDP rather than predicts it; the claim is not identified.
- "Qatar delivered 4.8 percentage points below its generational education baseline" — where does this number come from? No table shows Qatar-specific residuals.
- The 28-country long-run panel: which 28 countries? Survivorship bias is acknowledged but not quantified or bounded.

---

## 8. Minor Issues

- The paper claims the one-child policy "accelerated what was already underway" citing Miller et al. (2018), but then uses China's TFR crossing 1975 as evidence of education-driven fertility decline. This needs to be more carefully separated from the question of whether the OCP independently moved TFR below 3.67.
- "Near-unity" generational transmission (β=0.960) in a 28-country panel with survivorship bias and country FE: the high coefficient likely reflects regression toward common trend rather than structural transmission. More careful treatment needed.
- Section 9 (educational rupture) is largely descriptive history without quantification. The 40% threshold claim is stated but not formally derived or tested in this paper.

---

## Summary Recommendation

**Major revisions required.** The paper makes a genuinely interesting argument that education is causally upstream of both growth-mediated and support-led welfare gains — a contribution worth pursuing. But the jump from "education is an important upstream predictor" to "education is the *sole primary* driver and everything else is *consequence*" is not supported by the empirics presented. The identification strategy requires a more rigorous defense of why year FEs should be excluded. The China case study undermines rather than supports the claim that provision is inert. The case-study timing analysis needs to be formalized with explicit out-of-sample prediction rather than retrospective lag-fitting.

The paper would be stronger — and publishable — if it made a more modest claim: *education is a necessary upstream condition that existing frameworks underweight, and generational transmission is the mechanism*. That claim is well-supported. The "sole primary" framing is not.
