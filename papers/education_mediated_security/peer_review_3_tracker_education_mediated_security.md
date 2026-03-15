# Peer Review 3 Tracker

**Review recommendation:** Minor Revision (conditional acceptance possible)
**Source:** `papers/education_mediated_security/peer_review_3_education_mediated_security.md`
**Paper:** "Education as the Sole Primary Driver of Human Development"
**Last updated:** 2026-03-15

---

## Priority Summary

| # | Category | Item | Section | Effort | Status |
|---|---|---|---|---|---|
| 1 | FATAL | Bangladesh 2011 vs. 2015 date inconsistency | Table 4 + Sec 7 | 5 min | FIXED |
| 2 | SIGNIFICANT | "33 million / 27 countries" — add country list or remove | Sec 9 | 30 min | FIXED (sentence removed) |
| 3 | SIGNIFICANT | Provision endogeneity indirect tests — name them explicitly | Sec 10 | 15 min | FIXED |
| 4 | MODERATE | PTE-vs-persistence sentence missing from Cambodia | Sec 4 | 10 min | FIXED |
| 5 | MODERATE | Nutrition/physical security necessary-condition qualifier | Sec 2 or Sec 11 | 10 min | FIXED (added to Sec 2.4) |
| 6 | MODERATE | Reverse-causality test for GDP not shown | Table 2 or Sec 6.2 | 30 min | FIXED (Panel B added; abstract reframed; R²≈0.29 both directions) |
| 7 | MODERATE | Korea benchmark circularity — acknowledge or use Korea+Singapore avg | Sec 7 | 15 min | FIXED (Option B: labeled calibration case; Korea–Singapore avg stated) |
| 8 | MINOR | "Rupture margin" — define in Sec 7 or remove from conclusion | Sec 7 + Sec 11 | 10 min | FIXED (defined formally in Sec 7) |
| 9 | MINOR | "Leapfrog effect" — define formally or drop named-term framing | Sec 7 | 5 min | FIXED (dropped "what we term" framing) |
| 10 | MINOR | Figure A1 outcome clarification sentence | Sec 6.1/A1 | 5 min | FIXED |
| 11 | MINOR | Section 8 undersells education-builds-institutions | Sec 8 | 20 min | FIXED (Glaeser et al. 2004 added; causal arrow paragraph added) |

Items 1 and 2 must be fixed before submission. Items 3–7 are strongly recommended. Items 8–11 are credibility fixes — minor but flagged by journal copy-editors.

---

## FATAL

### #1 — Bangladesh date inconsistency: Table 4 says 2011; Section 7 narrative says 2015

**What the reviewer found:**
- Table 4: "Developed by: **2011**" with "LE > 70.1: **2011**"
- Section 7 Bangladesh paragraph: "**Bangladesh crossed in 2015** — the most important case in the table" — 2015 used throughout that paragraph

**What is correct:**
The Round 1 tracker corrected Bangladesh to **2011** (when LE crossed 70.1). The table is right; the Section 7 narrative still has the old incorrect date. Confirm against World Bank WDI: Bangladesh LE crossed 70.1 in 2011, not 2015.

**Action:**
In Section 7's Bangladesh paragraph, replace every instance of "2015" (when referring to the development threshold crossing date) with "2011". The 2011 crossing is also the cleanest refutation of income-first: GDP per capita was only ~$820 in 2011. Make sure that figure is used, not the 2015 GDP figure.

---

## SIGNIFICANT

### #2 — "27 countries / 33 million" has no reproducible specification

**What the reviewer found:**
> "Approximately 33 million young people in those 27 countries alone are not completing lower secondary — authors' calculations from WCDE v3 completion rates and World Bank population data, 2015."

No selection criterion stated. No country list. Cannot be verified.

**Options (pick one):**
- **Option A (preferred):** Add a footnote listing the 27 countries and the selection criterion, e.g., "Countries with lower secondary completion below 30% in 2015: [list]. Population calculation: WCDE v3 completion rates × World Bank 15–24 age-group population, 2015."
- **Option B:** Replace with a reproducible aggregate: "Countries with lower secondary completion below 30% in 2015 had a combined young population of approximately X million not completing lower secondary — authors' calculations from WCDE v3 and World Bank population data." Drop the specific "27" if it requires a footnote that doesn't exist.

The number must be reproducible from stated criteria before submission. This is the kind of thing journal copy-editors check.

---

### #3 — Provision endogeneity indirect tests: name them explicitly as tests

**Residual from R2#7 — partially addressed but connection left implicit.**

**What exists in the paper:** Section 10 contains acknowledgment that direct test is infeasible + two indirect tests in proximity. But the two tests are not framed *as* tests of provision endogeneity. A reader following the Section 10 argument can miss what they are evidence of.

**Action — one sentence needed in Section 10:**
> "Two indirect tests bear on provision endogeneity: first, Figure A1 shows education outperforming income at short lags — lags where provision demand would be the operative channel if Sen's framing were correct; second, the over-performers in Table 3 achieve above-income welfare outcomes without above-income provision expenditure, consistent with provision being downstream of education rather than independently supplied. Neither constitutes direct causal identification of provision endogeneity, but both are inconsistent with the alternative in which provision operates as an independent primary input."

This single addition converts a limitations acknowledgment into an evidential argument.

---

## MODERATE

### #4 — PTE-vs-persistence sentence missing from Cambodia analysis

**Residual from R2#10 — still implicit, not explicit.**

**What exists:** Section 4's Cambodia analysis establishes provision-independence ("The mechanism is transmitted through households, not through buildings"). It does not explicitly state the persistence-vs.-PTE distinction.

**Action — one sentence needed in Section 4:**
> "Simple educational persistence — education as an autocorrelated stock — predicts that Cambodian attainment would track state supply: collapsing when state infrastructure was destroyed, recovering when it was rebuilt. PTE predicts recovery through the household channel independently of state supply. Cambodia shows the latter: the plateau persists through substantial external school reconstruction from 1991 onward and ends when the post-KR parental cohort, not the rebuilt infrastructure, becomes the dominant influence on school-age enrolment patterns."

This is the sentence the R2 tracker flagged as needed and the R3 reviewer confirms is absent.

---

### #5 — Nutrition / physical security as non-education necessary conditions

**Residual from R2#4 — still absent from current text.**

**The gap:** The asymmetry test ("remove education → nothing works; remove income → education still works") is applied to education and income, but the same test would pass for physical security (remove it: Cambodia, Uganda, Amin's Uganda — nothing works) and nutrition (remove it: famine populations cannot learn). The "sole" in "sole primary driver" is unsupported without explaining why education wins the necessary-condition contest over these others.

**Action — one sentence, Section 2 or abstract:**
> "Nutrition and physical security are also necessary conditions for development, but neither can be deliberately delivered at scale by the policy interventions available to low-income governments without prior educational infrastructure, and neither compounds intergenerationally in the way that education does."

This is the sentence that appeared in the R2 tracker as "still needed" and has been raised again in R3. It must be in the paper before submission.

---

### #6 — Reverse-causality test for GDP not shown

**New issue. The abstract claims:**
> "Education predicts GDP, life expectancy, and fertility one PTE interval forward; GDP does not predict education forward with comparable strength."

The first half is shown in Table 2 (β=+0.0110 for education predicting GDP). The symmetric regression — GDP predicting education one PTE interval forward — is never shown. The asymmetry claim rests on assertion.

**Action:**
Add a column to Table 2 or a note in Section 6.2 showing: GDP at time *t* predicting education at time *t+25*. If the coefficient is small and/or the R² substantially lower than the reverse direction, the asymmetry claim is empirically demonstrated. If the coefficient is not small, the abstract claim needs revision.

This is the difference between claiming asymmetry and showing it. At *Journal of Development Economics* or *World Development*, stating it without showing it will be the first objection.

---

### #7 — Korea benchmark circularity

**New issue (also raised in skeptical R3).**

**The problem:** Korea is used to calibrate the "maximum educational expansion pace" benchmark (2.14 pp/yr). Every other case in Table 4 is then described relative to Korea. Korea itself is in Table 4 as a case the theory predicts. This is circular — the benchmark is set from Korea's expansion; Korea's predicted crossing date is then presented as consistent with the benchmark.

**Action (choose one):**
- **Option A (preferred):** Use Korea+Singapore average as benchmark (average ≈ 1.94 pp/yr). Korea then becomes a partial independent test rather than the calibration case by definition.
- **Option B:** Label Korea explicitly as the calibration case in Table 4 with a footnote: "Korea is the benchmark calibration case; the independent tests are all other rows." This is honest and sufficient.

Neither option invalidates the argument. Both prevent a reviewer from making the circularity objection stick.

---

## MINOR

### #8 — "Rupture margin" defined only in conclusion

**The problem:** Section 11 introduces "the rupture margin" as a named concept. Section 7, where the concept does all its work (comparing Bangladesh at half-Korea pace, Sri Lanka, India at a third), describes it without naming it.

**Action (choose one):**
- Introduce the term in Section 7: "We define the rupture margin as the speed of educational expansion relative to the starting base: the ratio of pp/yr gain to the gap remaining to universal completion."
- Or remove the term from Section 11 entirely and use the descriptive phrase consistently.

Named concepts that appear once create the impression of false precision. Either commit to the term or don't use it.

---

### #9 — "Leapfrog effect" named once without definition

**The problem:** Section 7 introduces "what we term the leapfrog effect: development timescales of 20–33 years against the 40–70 years seen in cases of gradual or sequential expansion." The term never appears again.

**Action (choose one):**
- Define it formally in Section 2 and use it consistently throughout Section 7 and the conclusion.
- Drop "what we term" and just describe the phenomenon: "In cases of rapid educational rupture, development timescales compress to 20–33 years, against 40–70 years in gradual expansion cases."

The second option is simpler and loses nothing. The first option would require committing to the term as a theoretical contribution throughout the paper. If you want it to be a named contribution, name it properly. If not, drop the framing.

---

### #10 — Figure A1 outcome clarification

**The problem:** Table 1 predicts *child education* from parental education and GDP. Figure A1 plots *life expectancy* predicted by education and GDP at different lag lengths. Both appear in close proximity with the same predictors but different outcomes.

**Action — one sentence before the Figure A1 discussion:**
> "Figure A1 switches the outcome from educational attainment (Table 1) to life expectancy, examining the same two predictors at every lag from 0 to 100 years to assess whether the predictive advantage of education over income is lag-dependent."

Five minutes. Prevents reader confusion.

---

### #11 — Section 8 undersells education-builds-institutions

**The reviewer's point:** The paper presents Acemoglu & Robinson as the challenge and spends three paragraphs deflecting, when the paper's own account (educated populations build institutions through political pressure — Kerala, Korea) is itself an original empirical argument. The defence receives less space than the methodological footnotes.

**Action:**
Add one paragraph to Section 8 explicitly tracing the causal arrow:
> "The mechanism runs: education → literate electorate → political demand for institutional quality → institutional development. This is not a theoretical assertion — it has empirical support. Glaeser et al. (2004) show that human capital predicts subsequent democratisation more reliably than initial institutional quality predicts subsequent human capital levels, directly inverting Acemoglu & Robinson's assumed causal direction. Kerala and Korea are not exceptions to the institutions-first account; they are evidence for the education-first account that the institutions-first literature has not yet engaged."

Citing Glaeser et al. (2004) also preempts the literature gap objection raised in the skeptical review.

---

## Reviewer's Positive Assessment (to preserve in revision)

The reviewer specifically praised:
- **Duflo paragraph (Section 4):** "well-executed" — do not alter
- **Sibling/extended family transmission (Section 2.3):** "genuinely valuable"
- **Smooth Figure A1 decay as theoretical prediction:** "most satisfying methodological move in the paper"
- **CO2 placebo:** "works"
- **Cuba handling:** "improved substantially"
- **Provision endogeneity acknowledgment (Section 10):** "honest and appropriate"

---

## Submission Target

Reviewer recommends: **Population and Development Review** as first target (methodology quantitative, directly engages Lutz & Kebede 2018, policy-relevant conclusion).

Second option: *World Development*.

Reviewer explicitly rules out AER/QJE for current framing — provision endogeneity gap requires direct test not feasible with available data.

**Do not submit to AER/QJE until R6 (reverse-causality GDP regression) is added and provision endogeneity is either directly tested or the claim is reframed.**
