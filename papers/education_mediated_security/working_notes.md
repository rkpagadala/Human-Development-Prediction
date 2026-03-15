# Working Notes — education_mediated_security.md

*Active session log. Updated as edits are made.*

---

## Open Issues from Claude Peer Review

### Issue 1 — "Sole primary driver" overstated
**Reviewer:** The claim is near-unfalsifiable. "Education is the sole primary driver" outpaces the empirics.
**Decision:** DISPUTE but sharpen. The necessary-condition argument is already in the paper (para 3 of Section 1) and is the right framing. The problem is the title and abstract lead with "sole primary driver" before the argument is made — it reads as assertion, not conclusion. The necessary-condition test IS the falsifiable claim: *remove education and nothing else works; remove income and education still works; remove provision and education still works.* No other variable survives the asymmetry test. This needs to be the front-and-centre framing, not buried in paragraph 3.
**Fix needed:** Strengthen the necessary-condition framing in abstract and intro. Make the asymmetry test the headline claim, not a parenthetical.
**Status:** OPEN

---

### Issue 2 — Year FE defense still reads as circular
**Reviewer:** Result collapses from β=0.485 to β=0.086 with two-way FE. Defense is: "that's not a confounder, that's the signal." Reviewer says this is circular.
**Decision:** DISPUTE but reframe. The paper's defense is substantively correct but rhetorically weak. The key move the paper hasn't made explicitly: *the reviewer's framing assumes global time trends are confounders; the paper's claim is that the global educational expansion IS the causal process being studied.* The CO2 placebo already handles spurious trend. The deeper issue is that the year FE debate is about what counts as signal vs. noise — and that depends on the research question. Ours is: does PTE operate? Year FEs condition out the PTE-driven global trend to ask "does PTE operate within what's left after removing the global trend?" That's the wrong question for our purpose.
**Additional argument to add:** The long-run 28-country panel (1900–2015) produces β=0.960 in a period with NO global education trend — countries were moving slowly and unevenly. If β=0.485 were a trend artefact, the pre-trend period should produce a weaker result. It produces a stronger one.
**Status:** Already in paper (year FE section). May need a single sentence that directly names the circularity charge and shows it's wrong.

---

### Issue 3 — Bad control applied inconsistently
**Reviewer:** If education causes initial LE, TFR, GDP, then controlling for initial conditions in Table 2 is also a bad control.
**Decision:** DISPUTE with clarification. This is a misunderstanding of the bad-control critique. A bad control is one that is *caused by the treatment variable in the same regression* — i.e., on the causal path from treatment to outcome. Initial conditions at time T cannot be caused by education at time T; they are caused by education at T−25 (prior generation). The temporal ordering solves this: $O_{it}$ is predetermined relative to $E_{it}$. The paper has this argument (one sentence in methodology) but it needs to be stated as a direct response to the expected objection.
**Fix needed:** Add a clear sentence in the methodology section making this explicit. "Initial outcomes at T are caused by prior education (at T−PTE), not by current education (at T). Conditioning on initial outcomes is therefore not a bad control — it is a conservative adjustment that absorbs prior trajectory and makes our education coefficient a lower bound."
**Status:** Argument exists, needs surfacing. LOW PRIORITY.

---

### Issue 4 — Lag range 20–70 years looks post-hoc
**Reviewer:** If lags range from 20 to 70 years, nearly any development date could be "predicted." The PTE label implies 25 years but fits are 20–70.
**Decision:** DISPUTE. The paper already addresses this: "The lag length is not a free parameter fitted to match each case — it is the number of generational cycles required to compound from the starting educational base to the threshold." Two parameters determine depth: (1) rupture speed relative to starting base, (2) LE pathway disruption. Both are independently measurable. The 20–70 range is exactly what the multi-generational theory predicts: one, two, or three complete generational cycles of ~25 years each. The range IS the theory. Taiwan is one cycle (fast rupture, high base). Kerala is three cycles (gradual accumulation, low starting base in early 20th century). A theory that predicted only 25-year lags would be wrong.
**Fix needed:** The two-parameter test needs to be demonstrably applied to each case before the crossing date is "predicted." Currently the paper presents the parameters and the results but doesn't explicitly walk through the prediction for each case. Add a brief table or prose showing: for Taiwan, rupture speed = fast (46.5pp gain 1965–1980), base = moderate → 1 cycle predicted → PTE. For Kerala, rupture = gradual (over decades of social reform), base = very low in 1900 → 3 cycles predicted → GGPTE. Make the prediction explicit, then show the data confirms it.
**Status:** OPEN — medium priority.

---

### Issue 5 — China/provision contradiction ← HIGHEST PRIORITY
**Reviewer:** If Deng's health dismantling caused a 10–15 year LE delay, provision has substantial independent effects. You can't simultaneously argue (a) provision is inert/endogenous AND (b) removing provision caused a 10–15 year delay.
**Decision:** This is the strongest objection in the review. The current text resolves it with "first-generation vulnerability" — an underdeveloped concept. The correct resolution:

**The asymmetry argument:** Provision removal causes a delay measured in *years*. Education removal causes a delay measured in *generations*. Uganda's LE fell to 47.8 by 1993 — below its 1960 level — and has not recovered after 65 years. China stalled for 15 years and then crossed. The recovery time asymmetry is itself the evidence for primacy. This is not a "provision is inert" argument — it is a "provision is a short-run perturbation; education is the long-run trajectory-setter" argument.

**The mechanism distinction:** When Deng dismantled the barefoot doctor system, China had an increasingly educated population. That population did two things over the next 15 years: (1) exerted political pressure to rebuild health infrastructure, and (2) made better individual health decisions than an uneducated population would. Both are PTE effects operating after a provision shock. The 15-year delay is how long it took an educated population to rebuild the provision they had lost. An uneducated population (Uganda) cannot do this — it cannot rebuild what it has lost because it lacks the political organization and individual health knowledge that educated populations have.

**Fix needed:** Rewrite the China paragraph to make this explicit. The claim is not "provision is inert" — it is "provision shock recovery time is determined by the underlying educational base." China recovered in 15 years; Uganda has not recovered in 65 years. The mechanism explains the differential recovery, not the initial shock.
**Status:** OPEN — fix this first.

---

### Issue 6 — Development threshold arbitrary
**Reviewer:** Binary threshold creates discontinuities; why simultaneously?
**Decision:** PARTIALLY ACCEPT. The three-spec robustness (Table A4) exists and handles the sensitivity concern. The simultaneity requirement is theoretically motivated — both thresholds must cross together because the demographic transition (fertility) and the epidemiological transition (mortality) are co-produced by the same mechanism, and we want to capture that both have fired. A country with LE > 70 but TFR = 3.8 is in a transitional state, not a completed development transition. This should be stated explicitly.
**Fix needed:** Add one sentence explaining why simultaneous crossing is the right definition. Already have Table A4. LOW PRIORITY.

---

### Issue 7 — One-child policy and China TFR
**Reviewer:** Paper can't use China's TFR crossing 1975 as evidence of education-driven fertility decline if the OCP (1979+) is in play.
**Decision:** ACCEPT. Need to be careful: China's TFR crossed 3.67 in *1975* — four years before the OCP began in 1979. The OCP is not in play for the TFR crossing date. This should be stated explicitly in the China discussion to preempt the objection.
**Fix needed:** One sentence in China discussion: "China's TFR crossed 3.67 in 1975, four years before the one-child policy was enacted in 1979; the fertility decline that determined the development crossing date is therefore education-driven, not policy-forced."
**Status:** OPEN — easy fix.

---

## Edits Made This Session

**Issue 5 — China/provision contradiction** ✓ FIXED
- Rewrote China paragraph to add: (a) OCP sentence (TFR crossed 1975, four years before 1979 OCP — fertility decline is education-driven); (b) explicit paragraph naming and answering the reviewer's objection with the asymmetry argument: provision removal = years-scale perturbation; education removal = generations-scale failure. "Remove the accelerator and you lose speed temporarily. Remove the engine and you stop permanently."

**Issue 1 — Sole primary driver in abstract** ✓ IMPROVED
- Abstract now states the asymmetry test explicitly: remove education → nothing works; remove income → education still works (Bangladesh $1,250); remove provision → education still works (Korea/Taiwan). The falsifiable claim is now in the abstract, not just Section 1.

**Issue 4 — Lags look post-hoc** ✓ FIXED
- Added paragraph after "crossing dates are the test, not the inputs" that explicitly applies the two-parameter rule to all cases *before* revealing the crossing dates. Makes the prediction character explicit: margin+disruption → predicted depth → observed depth confirmed.

---

## Decisions NOT to Change

- **β=0.960 "near-unity" in survivorship-biased panel:** Reviewer says this reflects regression to common trend. The paper already acknowledges survivorship bias slightly overstates β. The long-run coefficient is directionally correct even if slightly upward-biased. Stated as "conservative" in methodology. No change.

- **40% threshold not formally derived:** Reviewer correct that it's stated not derived. Paper already notes "companion work." No change for this paper.

- **Kerala figures estimated:** Acknowledged in Table 4 footnote. Kerala is illustrative, not load-bearing. The case works without exact numbers. No change.

- **"Sole primary driver" in title:** Keep. It's the thesis. Make the necessary-condition argument do the work of justifying it, rather than softening the title.
