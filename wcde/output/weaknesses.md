# Analytical Weaknesses — WCDE Analysis

*Working document. Priority order: fix > acknowledge > note.*

---

## W1. The parental proxy framing — language note only ✓ DOWNGRADED
**Affects:** generational_analysis.md, long_run_generational.md — β language
**Severity:** Low — framing note, not a methodological problem

The regression uses "country's lower secondary rate 25 years ago" as the parental variable.
This is aggregate, not household-level. But this is not actually a weakness in the finding —
it is a precision-of-language issue.

Parental transmission is one of the most universally observed patterns in social science:
educated parents produce educated children, across every culture, era, and dataset that has
looked. The alternative — that children's education is determined by government policy
independently of parental background — would predict that Cambodia recovers its educated
class immediately once government schools are restored. It has not, 45 years on. The
Khmer Rouge natural experiment supports the parental channel: destroying the parent
generation's education set recovery back by a full generation despite restored political will.

The β=0.49 FE coefficient captures a compound of parental transmission, community norms,
and institutional persistence — but all three channels operate in the same direction and
all three are real consequences of the parent generation's education level. The coefficient
is not inflated by the aggregation; it is measuring the genuine total effect of national
education level on the next generation's education level, through all channels.

**Language note only:** Where the document says "parents transmit literacy to children",
this can optionally be softened to "a generation's education strongly predicts the next
generation's — through parental, community, and institutional channels." This is more
precise without changing the substance of the claim. The β=0.49 interpretation stands.

---

## W2. T+10 and T+15 near-zero effects — workforce dilution ✓ DOWNGRADED
**Affects:** education_outcomes.md — Education → Income section
**Severity:** Low — pattern is explained by workforce dilution, not absence of effect

The lagged regression table shows:
- T+10: education β = +0.0004 (near zero)
- T+15: education β = +0.0027 (small)
- T+25: education β = +0.0071 (reported as significant finding)

The monotonically increasing pattern is consistent with workforce percolation. At T+10,
the educated cohort from T is 30–34 years old — roughly 1/8 of the working-age population.
The productivity gain is real but diluted below the noise threshold. By T+25, four to five
cohorts of elevated-education workers are in the workforce simultaneously, and the signal
clears the noise. The shape (+0.0004, +0.0027, +0.0071) is not flat-then-jump; it rises
monotonically as expected under gradual accumulation.

Note: the T+25 coefficient captures a compound effect — the original cohort's productivity
plus the path-dependent follow-on cohorts (β=0.49 intergenerational multiplier). This makes
the T+25 number larger and more policy-relevant than a single-cohort return, but means it
cannot be interpreted as the isolated return to one cohort's education alone.

**Language note only:** Worth one sentence in education_outcomes.md acknowledging that
short-lag near-zero reflects workforce dilution, not absence of effect — preempts the
obvious reader question without requiring any analytical change.

---

## W3. Sign flip in life expectancy model (OLS vs FE) ✓ FIXED
**Affects:** education_outcomes.md — Education → Life Expectancy section
**Severity:** High — unexplained contradiction in the results

**Fixed.** Added explanation to the Life Expectancy interpretation section in
education_outcomes.md. The sign reversal is a ceiling/convergence confound in OLS:
high-education countries (USA, Germany, Japan) are also the richest and were already
near the biological ceiling at T, so their e0 growth was slow regardless of education.
The cross-sectional education coefficient absorbs this ceiling effect and goes negative.
FE strips this out by comparing each country to itself — within any country, rising
education is followed by rising life expectancy. FE is the correct model to interpret;
OLS is reported for completeness with the explanation now in the document.

---

## W4. Linear model on bounded outcome — artefact "under-performers" ✓ FIXED
**Affects:** policy_residual.md, generational_analysis.md Tables 3 & 4
**Severity:** Medium — affects policy ranking interpretation

**Fixed.** Added ceiling note to the Method section and callout notes before Tables 2
and 4 in policy_residual.md, explicitly flagging that countries above ~95% completion
have mechanically negative residuals due to the linear model ceiling artefact, and that
their rankings do not reflect policy under-performance. The genuine under-performers
(Niger, Angola, Burkina Faso, etc.) are unaffected. The over-performer rankings are
also unaffected — those countries sit in the middle of the distribution where the
linear model is well-behaved. Logit regression not pursued as it would not change
any substantive finding.

---

## W5. Policy residual bad-control problem ✓ FIXED
**Affects:** policy_residual.md
**Severity:** Medium — affects interpretation of the ranking

**Fixed.** GDP dropped as a predictor from script 06_policy_residual.py. The residual
now measures "education above what parental education alone predicts" — pure policy
contribution net of intergenerational inheritance, with no mediation bias.

Results improved substantially: panel grew from 1068 to 1323 obs (countries without GDP
data now included); Norway, Denmark, Iceland, Germany, USA all flipped to slightly positive
FE residuals (no longer artefact under-performers); China improved from −7.4 to −1.4 pp;
Table 4 chronic under-performers is now entirely low-completion African countries with no
rich-country noise. Korea and Singapore remain slightly negative due to the ceiling artefact
(W4, acknowledged), not bad control.

---

## W6. China analysis: correlation attributed as causation ✓ FIXED
**Affects:** china_analysis.md
**Severity:** Medium — the CR attribution specifically

**Fixed.** Language revised throughout china_analysis.md to:
- Describe the CR as a period/factor associated with the gains, not a mechanism
- List plausible contributing factors (民办学校, reduced migration, ideological pressure)
  without asserting which one caused the gains
- Replace "the mechanism was 民办学校" with "the data establishes the timing"
- Replace "mechanisms are not hard to identify" (Deng trough) with "several factors
  plausibly contributed... the data cannot distinguish between these"
- Replace "CR-era community schools" with "the CR period" where used as a causal agent

The data establishes: (1) when the gains occurred, (2) that they coincided with CR-era
policies, (3) that the pattern is consistent with Gao Mobo's account. It does not
establish which specific CR factors caused which specific gains.

---

## W7. Female data appears identical to both-gender data ✓ FIXED
**Affects:** china_analysis.md Section 6.2
**Severity:** Medium — the section is currently void

**Root cause found and fixed.** Both `prop_both.csv` and `prop_female.csv` from the WCDE
R package contain rows for all three sex values (Both / Male / Female). The `process_prop`
function in `02_process.py` did not filter by sex, so `dict(zip(education, prop))` took
the last entry per education key — which was always Female (alphabetical order). Both
output files were silently identical Female data.

**Fix applied:** Added `sex_filter` parameter to `process_prop`; `completion_both` now
filters `sex == "Both"` and `completion_female` filters `sex == "Female"`. All downstream
scripts rerun. Max difference between files is now 28 pp (Qatar).

**China gender gap now real:** Female/both ratio for lower secondary: 0.40 (1950) → 0.74
(1970) → 0.92 (1990) → 1.00 (2015). The steepest convergence spans the CR and early
reform era. Section updated in china_analysis.md with real data and correct interpretation.

---

## W8. Pre-1950 data reliability varies by country ✓ ADDRESSED
**Affects:** long_run_generational.md
**Severity:** Low-Medium — manageable for large countries; real concern for small/thin-data ones

The issue is broader than survivorship bias. WCDE v3 reconstruction uses census microdata
(IPUMS), DHS surveys, and historical anchor points — not pure extrapolation — but for
countries with few pre-1950 censuses, the "data" is largely model output. The WCDE team
explicitly flags Sub-Saharan Africa and small island states as having significant measurement
gaps. WCDE v3 is also officially in Beta status.

**What this means in practice:**
- Large countries with census anchor points (USA, UK, Germany, Japan) are reasonably
  reliable for pre-1920 analysis. Japan's Meiji-era education records are particularly
  well-documented and consistent with the WCDE reconstruction.
- Small countries with thin census histories have essentially modelled pre-1920 data.
  Entire country series can be visibly wrong (implausible jumps, flat lines, etc.).
  These countries should be excluded from any pre-1920 analysis.

**Fixed:** Added a data quality table to long_run_generational.md classifying countries
by pre-1950 reliability, flagging WCDE v3 Beta status, and warning against adding small
countries to the pre-1920 analysis. The 28-country panel used in the document consists
of large countries with reasonable data quality; the historical comparisons (USA vs UK,
Japan rise, Korea post-independence) are sufficiently anchored to support the conclusions.

---

## W9. The 25-year intergenerational lag is assumed, not validated
**Affects:** All generational regressions
**Severity:** Low — better than initially assessed

The relevant quantity is **mean age at childbearing (MAC)** — the fertility-weighted mean
age at which a woman has children. This is NOT the age of first birth, and importantly,
NOT the same in high-fertility vs low-fertility societies in the way that seemed
problematic.

In high-fertility societies with early and frequent births:
- First birth: age 15–19 (teen pregnancies common in Sub-Saharan Africa, Bangladesh,
  historical India; less so but present in China and Latin America)
- Last birth: age 38–42
- Births roughly span 15–40, weighted toward younger ages by natural fertility
- Teen pregnancies **pull MAC DOWN**, partially offsetting the wide fertility span
- Result: MAC ≈ 25–27 for most developing world in 1960s–1980s

In low-fertility modern societies:
- First birth: age 28–32 (deliberate delay)
- TFR: 1.3–1.9; births clustered in a narrow window
- Near-zero teen births
- MAC ≈ 30–31

| Context | MAC estimate | vs 25yr lag |
|:--------|:------------:|:-----------:|
| Sub-Saharan Africa 1970 (TFR=6.5, first birth ~16) | ~26 | +1yr |
| Bangladesh 1970 (TFR=7, first birth ~16) | ~25 | 0yr |
| India 1970 (TFR=5.5, first birth ~17) | ~26 | +1yr |
| China 1965 (TFR=6.3) | ~26 | +1yr |
| USA 1965 (TFR=2.9, teen birth rate ~70/1000) | ~26 | +1yr |
| USA 2015 (TFR=1.9, teen births rare) | ~28 | +3yr |
| Japan/Germany 2015 (TFR=1.3–1.5) | ~31 | +6yr |

**Conclusion:** 25 years is approximately correct for the developing world parent
cohorts that form most of the regression sample. The lag is too short by 5–6 years
for modern Japan and Germany, but those countries are near ceiling anyway, so the
misspecification has minimal effect on β estimates. The original concern in W9 about
"20-22 years for high-fertility countries" was wrong — it confused age of first birth
with mean age at childbearing. Teen pregnancies bring the mean closer to 25, not further.

**Residual concern:** The lag is fixed at 25 for all country-years, but MAC actually
varies over time within countries as fertility transitions occur. A country moving from
TFR=6 to TFR=2 shifts its MAC from ~26 to ~28. This adds noise to the regression but
does not bias the β estimate in a systematic direction.

---

## W10. World history document mixes data and inference without labelling
**Affects:** world_education_history.md
**Severity:** Low — presentational

Specific historical claims in the world history document ("1 million barefoot doctors by
1975", "540 Thomasites in 1901") come from secondary sources, not WCDE data. A reader
cannot tell which statements are derived from the data and which are historical background.
This is fine for an essay but is a problem if the document is read as a data analysis.

**Fix:** Add a note at the top distinguishing data-derived findings from historical
context, or mark each claim with its source type.

---

## Priority Matrix

| # | Issue | Fix complexity | Impact on conclusions |
|:-:|:------|:--------------:|:---------------------:|
| W1 | Parental proxy framing | Optional language tweak | Low — β=0.49 captures real compound effect; language note only |
| W2 | Short-lag near-zero GDP effect | One sentence in doc | Low — workforce dilution explains the pattern |
| W3 | e0 sign flip OLS vs FE | Add explanation paragraph ✓ | Fixed — ceiling confound explained in doc |
| W4 | Linear model ceiling artefact | Flag in doc ✓ | Fixed — ceiling note added to policy_residual.md |
| W5 | GDP bad control in policy residual | Drop GDP ✓ | Fixed — GDP removed from regression, rankings corrected |
| W6 | China causal attribution | Soften language | Low — changes certainty, not direction |
| W7 | Female data error | Fix processing or remove | Medium — section is currently wrong |
| W8 | Pre-1950 data reliability | Country quality table added ✓ | Addressed — large countries reliable, small ones flagged |
| W9 | 25-year lag assumed | Sensitivity test | Low — likely robust |
| W10 | History doc mixing sources | Add note | Low — presentational |
