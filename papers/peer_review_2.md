# Peer Review 2: "Education as the Sole Primary Driver of Human Development"

**Recommendation: Major Revision**

The core intuition — that both of Sen's pathways (growth-mediated and support-led) are downstream of education — is genuinely interesting and worth developing. But the paper's ambitions exceed its evidence at several critical junctures.

---

## Fatal or Near-Fatal Problems

**1. The causal identification doesn't support the causal claim.**

The paper repeatedly asserts causal primacy but identifies only correlational structure. Country FE with a 25-year lag establishes that parental education predicts child education — this is unsurprising, potentially tautological, and does not establish that education *causes* development outcomes through the proposed mechanism. There is no instrumental variable, no natural experiment, no discontinuity design. The paper acknowledges this implicitly in the CO2 placebo, but a placebo test establishes absence of a time-trend artefact — it doesn't establish causal direction.

The Duflo (2001) Indonesia school construction paper is directly relevant and conspicuously absent. That's the gold standard for what causal identification of education effects looks like. By omission, the paper signals it cannot meet that bar.

**2. Higher R² is not causal primacy.**

"Parental education alone (R²=0.464) explains within-country educational variation at 1.74 times the rate of GDP alone (R²=0.266)." Education is a slow-moving, highly autocorrelated stock. Any lagged slow-moving variable will mechanically produce high within-country R² compared to a more volatile variable like GDP. The comparison is not informative about which is causally prior.

**3. The year fixed effects defense is the paper's weakest point.**

The paper argues year FEs should be excluded because they "absorb the global education expansion" — i.e., the very phenomenon under study. But this conflates the signal with a confounder. If global trends (WHO disease eradication, Green Revolution, antibiotic diffusion, international aid) simultaneously raised both education and health outcomes across countries, the within-country correlation between parental education and development outcomes would be spuriously inflated. Year FEs are not "conditioning away the signal" — they are standard procedure for removing common shocks that threaten identification. The two-way FE coefficient dropping to 0.086 is a warning the paper waves away.

**4. "Sole primary driver" is defined in a way that makes it unfalsifiable.**

The necessary condition framing ("remove education and nothing else works") is not a falsifiable empirical claim — it's almost definitionally true of any foundational input. Remove nutrition and education doesn't work. Remove physical security and education doesn't work. Remove state capacity and education doesn't work. The paper never explains why education wins the "necessary condition" contest over these alternatives. The asymmetry test ("remove income, education still works; remove education, income doesn't sustain") is rhetorically powerful but doesn't actually establish that education is the *sole* necessary condition — only that it's *a* necessary condition that can operate at low income levels.

---

## Significant Problems

**5. The development threshold definition is non-standard and convenient.**

USA 1960 TFR < 3.67 and LE > 70.1 are presented as theoretically motivated, but the motivation is post-hoc: these thresholds produce the crossing dates the theory needs. The paper claims robustness to alternative thresholds but never shows the table. "The ordering across all cases is perfectly preserved" needs to be demonstrated, not asserted — this belongs in Appendix Table A4, not a parenthetical.

**6. Cuba contradicts the P-25 mechanism.**

Cuba crossed in 1972, 11 years after the 1961 literacy campaign. The paper's own mechanism is 25 years (one generational interval). Eleven years is not P-25 — it's not even close. The paper handles this by noting lower secondary was already 49.7% in 1960, but this makes Cuba an example of a prior-education story, not the 1961 campaign. The paper can't simultaneously claim the 1961 campaign as the rupture and credit the pre-existing educational base. Pick one.

**7. The Sen critique is rhetorical, not empirical.**

The claim that "direct provision is endogenous to education" (educated populations demand it) is theoretical and not tested anywhere in the paper. The paper would need to show that provision expansions are predicted by prior education levels — not just that educated populations have better outcomes. This is the core of the rebuttal against Sen, and it has zero empirical support in the paper itself.

**8. China/Cultural Revolution reinterpretation is contested and oversimplified.**

Describing the CR as net-positive for rural lower secondary enrollment ignores: teacher quality collapse (urban-trained teachers sent to re-education camps), curriculum dismantlement, school closures at the university and middle school levels that bottlenecked future teachers, and the contested nature of the completion data itself (did "community schools" produce genuine lower secondary attainment?). The WCDE data may be recording enrollment, not attainment. The claim that "barefoot teachers" were the mechanism and Sen credited the wrong CR-era workers is interesting but requires direct evidence, not inference from aggregate completion rates.

**9. Uganda is doing too much work.**

Uganda's trajectory is attributed entirely to the absence of an educational rupture. But Uganda also experienced the AIDS epidemic (which depressed LE independently of education), persistent multi-actor conflict after Amin, and structural factors not shared with India. The counterfactual — "if Uganda had the same education trajectory as India, it would have followed India's LE path" — is not demonstrated. This is selection on the dependent variable.

---

## Moderate Problems

**10. The P-25 mechanism is asserted, not demonstrated.**

β=0.960 in the long-run panel is consistent with education being a slow-moving persistent stock (any 25-year autocorrelation would be high), not specifically with a generational transmission mechanism. What distinguishes P-25 from simple educational persistence? The paper needs a test that distinguishes "parents transmit education" from "education levels are sticky." One approach: show that cohorts born to educated mothers in disrupted countries (where state education collapsed) maintain higher completion than the state supply would predict.

**11. Table A2 undermines the 25-year specificity claim.**

Robustness across 15, 20, 25, and 30-year lags is presented as a strength, but it actually weakens the theoretical case. If P-25 is specifically generational, the 25-year lag should be the strongest — coefficients strengthening "between T+15 and T+25–30" is consistent with simple persistence, not the discrete generational mechanism the title implies.

**12. The "provision competes with education for fiscal resources" claim has no evidence.**

"A state that prioritises health clinics over schools is spending on effects while starving the cause. In the long run, provision-first is net negative." This is the paper's most direct policy implication and has zero empirical support. There is no analysis of fiscal allocation, no comparison of provision-heavy vs. education-heavy spending strategies, no attempt to identify the tradeoff empirically. This claim should either be supported or removed.

---

## Minor Issues

- Kerala estimates carry more uncertainty than country-level data; the paper's most qualitative case rests on the most uncertain numbers
- Deaton (2013) *The Great Escape* is directly relevant (health technology diffusion independent of income) and not cited
- "The mechanism does not care what political system delivers the education" is stated as a conclusion from three data points (Korea, Cuba, Taiwan), which is insufficient
- The abstract states the threshold is "both lower total fertility than the United States in 1960 (TFR < 3.67) *and* higher life expectancy" but the body defines development as crossing *both* simultaneously — the abstract should reflect that Bangladesh's TFR crossed in 2000 but development wasn't achieved until 2011 (when LE crossed)

---

## What's Worth Keeping

The Uganda-India comparison is the paper's most compelling illustration. The policy over-performer table (Table 3) is genuinely interesting — Nepal at $902, Bangladesh at $1,250. The bad control problem discussion is methodologically sophisticated and important. The reinterpretation of the Preston Curve as an education story is well-grounded in Lutz & Kebede.

The core claim — that Sen's typology describes fiscal routing, not causal mechanism — is a real insight. But the paper needs to make this as a bounded, testable claim rather than as "education is the *sole* primary driver," which is unsupportable with this evidence.

---

## Path to Publication

Narrow the claim. "Education is the primary upstream mechanism in Sen's canonical cases, and the timing of development crossing dates is predicted by prior educational investment rather than by provision" is publishable with the existing evidence. "Sole primary driver" is not.
