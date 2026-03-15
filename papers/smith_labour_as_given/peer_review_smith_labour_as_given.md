# Peer Review: "Labour as Given: Adam Smith's Unexamined Assumption and the Two-Hundred-and-Fifty-Year Error It Founded"

**Reviewer:** Skeptical peer, no prior context
**Date:** 2026-03-15
**Verdict:** Major revisions required — unsuitable for publication in current form

---

## Overall Assessment

The paper has a genuinely interesting core argument but is currently unsuitable for publication in any serious economics journal and would face serious resistance even in interdisciplinary outlets. The problems are both structural and empirical.

---

## 1. The Central Intellectual Move

The paper's thesis — that Smith treated educated labour as a natural given, that this assumption propagated through the tradition, and that the data show education causes income rather than the reverse — is interesting and defensible. The Knox/Scotland historical framing is the paper's strongest contribution: it is specific, documented, and connects Smith's personal biography to his analytical blind spot.

The problem is that the paper treats this as a discovery when it is closer to an emphasis. Economists have been writing about education-first development since at least Schultz (1961) and Easterlin (1981). The paper cites them but never explains why *those papers* did not resolve the "250-year error." If the argument is correct and the evidence exists, why hasn't the tradition absorbed it? That question demands an answer and does not get one.

---

## 2. Empirical Section (Section 5): Critically Insufficient

This is the paper's most serious problem. The empirical claims are enormous:

> "Education predicts GDP one PTE interval forward... GDP does not predict education forward across a PTE interval with comparable strength."

But the evidence presented is three paragraphs with no tables, no standard errors, no robustness checks, and no engagement with identification concerns.

**2.1 Fixed effects with lagged variables does not establish causation.** The paper presents FE β=0.0110 as if it settles the causal question. But fixed effects removes time-invariant country heterogeneity; it does not address reverse causation within the time series, nor omitted time-varying confounders (institutional reform, trade openness, political stability). The claim "the causal arrow runs from education to income" requires instrumental variable estimation or a genuine natural experiment — not OLS with country FEs.

**2.2 The R² comparison is not a causal test.** Showing that education FE R²=0.464 outperforms GDP FE R²=0.266 demonstrates that education is a stronger predictor, not that it is causally prior. A confounding third factor (state capacity, institutional quality, culture) could generate both patterns simultaneously.

**2.3 The lag-decay argument is asserted, not shown.** The paper describes "smooth curves reflecting overlapping timescales" with no figures, no tables, and no specification details. Reviewers cannot evaluate a claim they cannot see.

**2.4 The Cambodia natural experiment has fatal confounders.** Cambodia 1975–2000 also experienced: total infrastructure destruction, land mine contamination of agricultural land, continued armed conflict (the Khmer Rouge held UN Security Council recognition until 1982 and fought guerrilla warfare until 1998), near-total international isolation until 1991, and a Vietnamese occupation that constrained institutional development. The Vietnam comparison is not clean — Vietnam had a different political trajectory, different aid flows, and had completed its own education expansion under different conditions. Attributing Cambodia's educational plateau specifically to parental education destruction when every other development input was simultaneously destroyed is not defensible as a natural experiment.

**2.5 The 40% threshold is stated as precise policy guidance with no derivation.** "Below approximately 40% female lower-secondary completion, the binding constraint is the parental education base" — where does this number come from empirically? It appears in the policy section as if it were established earlier, but it is not.

---

## 3. The "Smith Committed an Error" Framing

This framing is intellectually unfair and will alienate reviewers.

Smith was writing *The Wealth of Nations* as a theory of market mechanisms and the sources of national wealth *given* an operating economy. He was not writing a development economics textbook. Every theoretical model abstracts from something; the question is whether the abstraction was appropriate for the purposes at hand. Calling this the "founding error" and "the most consequential omission in the history of a discipline" requires demonstrating that:

1. Smith was trying to explain why some countries develop and others do not (debatable — that is more Malthus's project)
2. The omission, rather than subsequent misapplication of Smith's framework by others, generated the policy errors described

Neither is demonstrated. The paper slides between "Smith didn't theorize this" and "Smith's framework caused a 250-year error" as if these are equivalent.

The Book V passage — where Smith proposes education as a corrective for industrial degradation — is quoted and called "exactly backwards." But this is also uncharitable: Smith's Book V argument (the state should fund basic education) actually supports the paper's policy conclusion. Calling the framing backwards while agreeing with the conclusion is confusing rather than compelling.

---

## 4. The Intellectual Genealogy (Section 4)

The genealogy Smith → Marshall → Becker → Lewis → Washington Consensus → Sen has a missing-evidence problem: it proves too much. If the error propagated uninterrupted, why does the paper also cite Easterlin (1981) and Lutz & Kebede (2018) as having identified education as the answer? The paper's own references show the tradition has been partially correcting itself. The genealogy needs to explain the *selective* persistence of the error, not its total persistence.

The treatment of Sen is the weakest link. The paper claims Sen "does not ask what made provision effective" — but Sen's capabilities framework explicitly includes education as a fundamental capability, and *Development as Freedom* (1999) treats education as constitutive of development rather than downstream of it. Dismissing this by saying he "described fiscal routing" without engaging with the later work is a citation gap a reviewer will flag.

A significant omission: the paper does not engage with Mankiw-Romer-Weil (1992), which augmented the Solow model with human capital and was enormously influential in the mainstream. If the "error" persisted after MRW, why? That is a more tractable and interesting puzzle than blaming Smith.

---

## 5. Structural Issues

**5.1 Two-claim conflation.** The paper is effectively two papers running in parallel:

- A historical/intellectual-history paper about Smith's assumption and its genealogy
- An empirical paper about education-income causality using WCDE data

These require different journals, different evidentiary standards, and different argumentative structures. Running them together means neither is fully convincing on its own terms.

**5.2 The title is too polemical.** "The Two-Hundred-and-Fifty-Year Error" will trigger defensive reactions in reviewers who work in the tradition being characterized as error-ridden. Strong titles are fine; adversarial titles create unnecessary friction before the argument begins.

**5.3 The England section (2.3) is underdeveloped.** The Knox/Scotland argument is tight and specific. The Tyndale/England chain is weaker institutionally — the paper itself acknowledges it was "less institutionally structured" — and reads as appended rather than integrated. Either develop it to the same evidentiary standard as the Scotland argument, or cut it.

**5.4 The South Korea/Japan/Bangladesh comparisons (Section 5.2) are illustrative, not systematic.** South Korea's development also involved massive US aid, land reform, Cold War strategic positioning, and specific industrial policy. Japan's Meiji transformation was driven by state-building imperatives well beyond education. Bangladesh's trajectory involved specific export-sector dynamics. Using three cherry-picked cases as confirmation of the PTE mechanism, in a paper that also claims 189-country panel evidence, is redundant and will look weak to reviewers.

---

## 6. What Would Make This Publishable

**Empirical strengthening:**
- IV estimation is required. Colonial missionary school presence is a standard instrument for historical education; Reformation-exposure instruments exist in the literature and are directly relevant here. Without IV, the causal claim cannot stand peer review.
- Publish actual regression tables with standard errors, sample sizes, and robustness specifications.
- The lag-decay figures described in the text must be shown.
- The Cambodia analysis needs a proper synthetic control or at minimum a clear accounting of confounders, with an explicit argument for why parental education destruction is the residual explanation.

**Framing correction:**
- Replace "error" with "omission that constrained the tradition" — less alienating, equally forceful, more accurate.
- Engage with MRW (1992) and the post-Becker human capital growth literature. The paper's genealogy stops too early and misses the most relevant prior work.
- The Sen critique needs to engage with *Development as Freedom* (1999) and the capabilities literature, not just *Hunger and Public Action* (1989).

**Structural decision:**
- Either split into two papers — one intellectual history, one empirical — or write a single paper where the intellectual history serves strictly as motivation for the empirical contribution and is not itself a co-equal claim.

---

## 7. Summary

| Dimension | Assessment |
|---|---|
| Core historical argument (Knox/Scotland) | Strong — publishable with development |
| Causal empirical claim | Underdeveloped — identification not established |
| Cambodia natural experiment | Fatally confounded as presented |
| Genealogy (Smith → Sen) | Selective and uncharitable to Sen |
| Policy implications | Reasonable but threshold number unsupported |
| Structure | Two papers in one; neither fully convincing |
| Title/framing | Unnecessarily adversarial |

The historical argument about Knox and Smith is publishable in a history of economic thought journal if developed with less polemical framing. The empirical argument about education-income causality is publishable in a development economics journal if the identification strategy is strengthened substantially. As a combined paper making both claims simultaneously, it currently satisfies neither standard.
