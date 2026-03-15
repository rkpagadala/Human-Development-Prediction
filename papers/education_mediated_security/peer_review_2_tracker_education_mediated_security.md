# Peer Review 2 Tracker

**Review recommendation:** Major Revision
**Source:** `papers/peer_review_2.md`
**Paper:** "Education-Mediated Security: Rethinking the Causal Drivers of Human Development"
**Last updated:** 2026-03-14

---

## Priority Summary

*Verified against paper content 2026-03-14. Items marked IN PAPER confirmed by full read.*

| # | Category | Item | Status |
|---|---|---|---|
| 1 | FATAL | Causal identification — Duflo absent | FIXED — paragraph added before Cambodia block; names Duflo (2001), explains why IV can't operate at 25yr timescales, frames three identification structures |
| 2 | FATAL | Higher R² ≠ causal primacy | IN PAPER — lag-decay shape contrast explicit in Fig A1 discussion |
| 3 | FATAL | Year FE defense weakest point | IN PAPER — global co-movement argument present |
| 4 | FATAL | "Sole primary driver" unfalsifiable | IN PAPER — necessary condition framing in abstract + appendix limitations |
| 5 | SIGNIFICANT | Threshold non-standard and convenient | IN PAPER — Table A4 exists with three specs |
| 6 | SIGNIFICANT | Cuba contradicts PTE (11 yrs ≠ 25 yrs) | IN PAPER — pre-existing base argument correct |
| 7 | SIGNIFICANT | Sen critique rhetorical, not empirical | IN PAPER — indirect tests in Sec 10 + Sec 8; provision endogeneity acknowledged as untestable directly |
| 8 | SIGNIFICANT | China/CR reinterpretation contested | IN PAPER — data quality caveat + sources |
| 9 | SIGNIFICANT | Uganda doing too much work | IN PAPER — AIDS as education-mediated, detailed |
| 10 | MODERATE | PTE vs simple persistence | IN PAPER (implicit) — Cambodia Sec 4 covers this; could be made explicit |
| 11 | MODERATE | Table A2 undermines 25-yr specificity | IN PAPER — multi-channel mechanism argument |
| 12 | MODERATE | Fiscal competition has no empirical evidence | IN PAPER — OECD DAC data in intro |
| M1 | MINOR | Kerala uncertainty | IN PAPER |
| M2 | MINOR | Deaton (2013) not cited | IN PAPER — Sec 2.2 |
| M3 | MINOR | Political system from 3 data points | IN PAPER |
| M4 | MINOR | Abstract/Bangladesh inconsistency | IN PAPER |
| M5 | MINOR | Qatar residual unsourced | IN PAPER |
| M6 | MINOR | 28-country panel not listed | IN PAPER |

## All Items Fixed — Ready for Submission

### A — Duflo (2001) citation ✓ FIXED

Paragraph added before the Cambodia block in Section 4. Explains why Duflo-style IV cannot operate at 25-year timescales, then frames three identification structures (temporal ordering, lag-decay shape contrast, natural experiments). Cambodia follows directly as the primary natural experiment.

### B — Extended family / sibling transmission ✓ FIXED

Three paragraphs added to Section 2.3 between the "runs beneath it" paragraph and the global PTE paragraph. Covers: sibling channel (2–20 yrs, self-limiting as fertility falls), extended family channel (2–25 yrs, strongest in South Asia/sub-Saharan Africa/East Asia), and crucially explains the smooth Figure A1 lag-decay curve as a theoretical prediction of the multi-channel structure — defeating reviewer #11 definitively.

---

## FATAL / NEAR-FATAL

### #1 — Causal identification doesn't support causal claim (Duflo 2001 absent)

**Status:** SUBSTANTIALLY ADDRESSED — needs to be made explicit in paper

**What exists:**
- Cambodia natural experiment: Khmer Rouge destroyed state education. Educated-parent cohorts recovered faster than state supply alone predicts. This distinguishes PTE (survives state collapse) from simple educational persistence (which would have collapsed with the state). Already in paper at Section 4.
- Pre/post colonization variation: missionary and administrative schools introduced formal education with timing exogenous to recipient populations. Not clean (colonization affects institutions/economics) but provides variation in educational rupture timing.
- Temporal ordering argument: parental cohort precedes child cohort by definition. This IS the identification structure that IV would otherwise supply.

**Still needed in paper:**
- One explicit paragraph framing Cambodia + colonial variation as natural experiments
- Explain why IV/discontinuity designs cannot operate at 25-year generational timescales across 189 countries
- Cite Duflo (2001) and distinguish: her instrument identifies short-run income returns; it cannot identify 25-year intergenerational transmission
- Section: likely Section 4 (identification) or methodology section

**Draft language:**
> "Duflo (2001) provides the canonical natural-experiment identification of education's effects on earnings in Indonesia. That design is appropriate for short-run individual returns; it cannot be replicated at 25-year generational timescales across 189 countries. Our identification rests on three structures: (1) temporal ordering — parental cohort precedes child cohort by definition, ruling out reverse causality; (2) the Cambodia natural experiment — Khmer Rouge systematic destruction of state education provides a test of PTE vs. simple persistence; cohorts born to educated parents showed faster recovery than state supply alone predicts; (3) colonial education variation — missionary and administrative schools introduced formal education at times exogenous to recipient populations, providing variation in rupture timing."

---

### #2 — Higher R² is not causal primacy

**Status:** ADDRESSED — needs sharper framing in paper

**The argument:**
- Key evidence is not R² level but lag-decay *shape* difference
- PTE weakens slowly (β=0.960 → β=0.485; slow decay across 100-year lags) — structural floor exists
- GDP collapses rapidly beyond lag 50 — no independent generational transmission mechanism
- Two autocorrelated slow-moving variables cannot both be persistence if their lag-decay shapes are fundamentally different

**Additional insight:**
- PTE's weakening over time is partly the sibling channel diminishing as fertility falls — fewer siblings, shorter gaps, less within-family compression. The β decline is the fertility transition showing up in the transmission coefficient. This is a *prediction* of the theory, not a weakness.
- GDP's collapse confirms it is downstream — no independent generational transmission mechanism, so predictive power disappears as lag increases.

**Still needed in paper:**
- Frame the contrast explicitly: "the lag-decay shape is the causal structure test, not the R² level"
- Add the sibling/fertility-transition explanation for the β decline

---

### #3 — Year FE defense weakest point

**Status:** SUBSTANTIALLY STRENGTHENED

**What was added:**
- Global co-movement argument: global welfare improvements and global educational rupture are the same process at different institutional scales. Year FEs absorb a genuine causal signal (global PTE), not a spurious confounder. Deaton's health diffusion itself required educated institutions.

**Remaining concern:**
- The two-way FE coefficient (β=0.086) cannot simply be waved away — reviewer's "this is a warning" point needs direct acknowledgment
- Possible frame: "the coefficient reduction in two-way FE reflects both absorbed genuine signal (global PTE as a real mechanism) and legitimate common-shock control; the within-country FE without year FEs is the appropriate specification for identifying generational transmission because the global expansion is the outcome we are studying, not a confounder of it"

---

### #4 — "Sole primary driver" unfalsifiable

**Status:** ADDRESSED

**What exists:**
- Necessary condition framing with asymmetry test: remove education → nothing else works; remove income → education still works (Bangladesh $1,250); remove provision → education still works (Korea, Taiwan)

**Still needed:**
- One sentence: "Education is the only necessary condition that is (a) policy-actionable at low income and (b) compounds intergenerationally. Nutrition and physical security are also necessary conditions, but neither can be deliberately delivered at scale by the policy interventions available to low-income governments, and neither compounds generationally in the way that education does."

---

## SIGNIFICANT

### #5 — Development threshold non-standard and convenient

**Status:** ADDRESSED — Table A4 confirmation needed

**What exists:**
- Three threshold specifications run; ordering preserved; robustness sentence in Section 3

**Action needed:**
- Confirm Table A4 exists in appendix with crossing dates across three threshold specs
- If missing, create it

---

### #6 — Cuba contradicts PTE (11 years ≠ 25 years)

**Status:** ADDRESSED

**Resolution:**
- Paper correctly picks "prior educational base" not 1961 campaign
- Cuba was already at 49.7% lower secondary in 1960; 1961 campaign completed what was in motion
- Rupture margin concept handles this — pre-existing high base means PTE was already generating demand; campaign removed the last access barriers

**No further action needed.**

---

### #7 — Sen critique is rhetorical, not empirical

**Status:** NOT ADDRESSED

**The gap:**
- "Direct provision is endogenous to education" has zero empirical support in the paper
- Need to show provision expansions are predicted by prior education levels, or explicitly acknowledge test is infeasible with available data

**Indirect tests that exist in paper:**
- Figure A1: education outperforms income at short lags where provision demand would be the channel — this is indirect evidence that provision is not the independent variable
- Table 3: over-performers achieve above-income welfare outcomes without above-income provision spending — consistent with provision being downstream

**Action needed:**
- Frame these explicitly as indirect tests of provision endogeneity
- Add sentence: "A direct test of provision endogeneity — regressing health provision spending on lagged education — is not feasible with available data. The indirect evidence is: (1) education outperforms income at short lags (Figure A1), where provision demand would be the operative channel if Sen's framing were correct; (2) over-performers in Table 3 achieve above-income welfare outcomes without above-income provision spending. These patterns are consistent with provision being downstream but do not constitute direct causal identification."

---

### #8 — China/CR reinterpretation contested

**Status:** ADDRESSED

**What exists:**
- Data quality caveat: WCDE estimates for CR-era China carry greater uncertainty; community school data may capture registration rather than genuine completion; Pepper (1996) and Unger (1982) cited
- Claim limited to: "basic literacy and numeracy transmission from a parent with some secondary schooling is sufficient to shift the household baseline"

**No further action needed.**

---

### #9 — Uganda doing too much work

**Status:** ADDRESSED

**Resolution:**
- AIDS prevalence is itself education-mediated: educated populations have lower HIV transmission rates, follow prevention guidance, access treatment earlier, build political demand for response infrastructure
- Uganda's AIDS epidemic is a downstream consequence of educational absence — not an independent confounder to control for
- Mechanism explains the shock; the shock is not a separate variable

**Confirm in paper:**
- This argument should be stated explicitly, not assumed
- If not already in paper, add: "Uganda's AIDS epidemic was itself education-mediated: educated populations have substantially lower HIV transmission rates and faster health-system response. AIDS mortality is downstream of the same educational absence that explains Uganda's development trajectory — not an independent variable requiring separate control."

---

## MODERATE

### #10 — PTE mechanism vs. simple persistence

**Status:** NOT ADDRESSED

**The test:**
- What distinguishes "parents transmit education" from "education levels are sticky"?
- Reviewer's suggested test: show that cohorts born to educated mothers in disrupted countries maintain higher completion than state supply predicts

**The test exists in the data:**
- Cambodia: Khmer Rouge destroyed state education; educated-parent cohorts showed faster recovery
- This test is already in paper (Section 4) as the natural experiment for #1
- Need to make explicit that Cambodia also addresses this specific #10 question

**Action needed:**
- Add sentence in Section 4 or Section 2.3: "The Cambodia test simultaneously addresses both the causal identification question and the PTE-vs-persistence distinction. Simple persistence predicts that educational levels would track state supply — collapsing with it when state infrastructure is destroyed. PTE predicts that household transmission survives state collapse. Cambodia shows the latter: recovery in educated-parent cohorts exceeds what state-supply recovery would predict."

---

### #11 — Table A2 undermines 25-year specificity

**Status:** ADDRESSED by mechanism argument

**Resolution:**
- Multiple lag lengths working is the mechanism's multi-channel structure showing up in data
- Sibling transmission: 2–20 years; PTE: 25 years; GPTE: 50 years; GGPTE: 75 years
- The decisive test is not "which lag is strongest" but "why does PTE decay slowly while GDP collapses"
- Shape difference rules out persistence as explanation for both

**No further action needed beyond what's in paper.**

---

### #12 — Fiscal competition has no empirical evidence

**Status:** FIXED

**What was added:**
- OECD DAC data: health receives 2–3× education aid allocation
- SDG/MDG reframe in Introduction: revealed institutional preference of international system is provision-first
- Countries that developed fastest ignored this allocation

**No further action needed.**

---

## MINOR

| # | Item | Status | Note |
|---|---|---|---|
| M1 | Kerala uncertainty | Acknowledged | No action needed |
| M2 | Deaton (2013) not cited | Fixed | Section 2.2 |
| M3 | Political system from 3 data points | Fixed | Framed as supporting evidence |
| M4 | Abstract/Bangladesh inconsistency | Fixed | TFR vs LE split explicit |
| M5 | Qatar residual unsourced | Fixed | Sourced to FE residuals, WCDE v3 |
| M6 | 28-country panel not listed | Fixed | Survivorship bias caveat included |
| Cambodia NE | Already in paper | Done | Section 4 |

---

## Mechanism Updates Needed in Paper

### Vision docs P-25 → PTE (pending)
- `vision/for_the_leader.md` — still uses "P-25" throughout. Replace with PTE.
- `vision/for_the_philanthropist.md` — still uses "P-25" throughout. Replace with PTE.

### Extended family + sibling channel — Update Section 2.3

**Full transmission network (all channels simultaneous):**
- Extended family network: aunts, uncles, grandparents in child-rearing (2–25 years). Especially powerful in South Asia, sub-Saharan Africa, East Asia — precisely the low-education societies where development intervention matters most.
- Sibling channel: 2–20 years, variable by family size. In high-fertility societies, siblings spaced up to 20 years apart — oldest educated sibling transmits at near-PTE timescales within same family.
- PTE: ~25 years (base unit)
- GPTE: ~50 years
- GGPTE: ~75 years

**Smooth decay explanation — Add to Section 2.3 and Section 6.1:**
The smooth R² decay (0.528 at lag 0 → 0.369 at lag 25 → 0.194 at lag 50 → 0.112 at lag 75 → 0.061 at lag 100) is a direct prediction of the multi-channel structure. A single 25-year mechanism would show a step pattern. The overlapping channels produce the smooth aggregate curve. The smoothness is not a weakness — it is the empirical signature of multi-channel household transmission.

**Policy implication to add:** Educating any member of an extended family has downstream effects beyond that individual's own children. The return on educating one woman ripples through the kin network.

**Defeats reviewer #11:** Smooth decay is a theoretical prediction, not evidence against 25-year specificity.

---

## Next Paper Submission Steps

1. Address #1, #7, #10 in paper (see action items above)
2. Confirm Table A4 exists for #5
3. Add one sentence for #4 necessary-condition qualifier
4. Add explicit Cambodia/persistence distinction for #10
5. Update Section 2.3 with full transmission network (sibling/extended family)
6. Add lag-decay shape framing for #2
7. **Post to SSRN as working paper** — immediate credibility signal for platform
8. **Submit to Journal of Development Economics or World Development**
