# Notes on Peer Review — education_mediated_security.md

*Reviewer: fresh Claude instance, skeptical, no prior context*
*Status: working through objections in order of severity*

---

## Resolved

**#8 One-child policy** — Reviewer flagged that the paper needed to separate OCP from education-driven fertility decline. Fixed: cited Cai (2010) showing OCP had no independent demographic effect; China mirrors South Korea and Thailand which achieved equivalent TFRs without compulsory policy.

**#3 Bad control inconsistency** — Reviewer claimed controlling for initial outcomes (O_it) in Table 2 is inconsistent with the bad-control argument used to exclude GDP. Fixed: added sentence to Section 5.2 explaining O_it is caused by prior education (E_{i,t-25}), not by E_it itself — T+25 mechanism means E_it has not yet had time to affect O_it. Conservative lower-bound control, not a bad control in Pearl's sense.

---

## Open — Serious

**#1 Central claim overstated** ✓ RESOLVED
Added paragraph to introduction defining "sole primary" precisely: not "explains all variance" but "necessary condition — the asymmetric input without which no other mechanism operates independently." Test: remove education → nothing else works. Remove income → education still works (Bangladesh $1,250). Remove provision → education still works (Korea, Taiwan). The asymmetry defines primacy. No other variable survives this test.

**#2 Year FE / identification** ✓ FIXED
Added to Section 5.2: explicit argument that the global education trend is the signal not the confounder (rain/crops analogy); direct pre-emption of CO2 within-country variation objection — CO2's within-country variation is driven by industrialisation patterns not generational transmission, making it a valid null precisely because it doesn't share the same variation structure.

**#5 China provision delay** ✓ RESOLVED
- "Inert" replaced with "unsustainable without education" throughout
- 10–15 year delay claim removed entirely
- Crossing dates explained mechanically by starting LE distance (Taiwan 68.1, Korea 61.4, China ~53 in 1965)
- China's depressed 1965 baseline attributed to GLF famine — Sen's baseline is famine-depressed, not a normal trajectory
- Post-1980 deceleration attributed to epidemiological ceiling (standard) alongside possible provision effect — data cannot cleanly separate them
- Barefoot teachers named as the mechanism Sen missed
- GLF famine recovery now identified as what Sen misreads as provision-led welfare gain

**#6 Development threshold robustness** ✓ RESOLVED
Ran three threshold specifications (strict USA 1960, loose TFR/LE, strict alt). Ordering perfectly preserved across all. Absolute dates shift 3–12 years. Robustness sentence added to Section 3. Also corrected Cuba crossing to 1972 (same year as Taiwan) and Bangladesh to 2011.

---

## Open — Weaker

**#4a Case study lags post-hoc fitted** ✓ RESOLVED
Added paragraph to Section 7 opening: two parameters (speed/depth of rupture; market mechanisms open) determine lag length independently of crossing dates. Both are measurable from education data and historical record without reference to the dates. "The crossing dates are the test of the theory, not its inputs."

**#4b Bangladesh / Cuba** ✓ RESOLVED
Both added to Table 4 with narrative paragraphs.
- Cuba: crossed 1975 (14 years after 1961 literacy campaign); started from 50% lower secondary base; consistent with P-25 on an adequate base; confirms regime-independence.
- Bangladesh: crossed 2015 at $1,250 GDP; 11.4% lower secondary in 1960 → 54.6% in 2015; policy over-performer in Table 3 (+15.8pp) → the over-performance was the rupture, the 2015 crossing was its result ~25 years later. Cleanest refutation of income-first account.

**#7 Qatar residual unsourced; 28-country panel not listed**
Reviewer: Qatar -4.8pp residual has no table reference. 28-country panel — which countries?

*To fix:* Add Qatar to a residuals table or footnote source. List 28-country panel in appendix or footnote.

**#8b Near-unity coefficient (β=0.960)** ✓ RESOLVED
Pre-1950, mass education was not a state priority anywhere — no global trend to confound. Near-unity in exactly the period where the confound cannot exist is structural evidence, not artefact. The decline to β=0.485 post-1975 is the rupture working: states delivering above parental baselines (Table 3 over-performers) compete with the parental signal and mechanically reduce the coefficient. β=0.485 is P-25 with the rupture operating on top of it.

---

## Reviewer's Summary Recommendation

Major revisions. Core suggestion: weaken claim to "education is a necessary upstream condition that existing frameworks underweight" — drop "sole primary."

*Our view:* The weaker framing concedes too much to Sen. The point is not that nothing else matters at the margin — it's that education is the necessary condition without which nothing else works. The framing is adversarial by design. Defend it, don't retreat from it.
