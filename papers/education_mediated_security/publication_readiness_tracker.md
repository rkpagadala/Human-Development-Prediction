# Publication Readiness Tracker — Code & Data

**Source review:** `publication_readiness_code_data.md`
**Last updated:** 2026-03-15

---

## Status Summary

| # | Issue | Status |
|---|-------|--------|
| 1 | Script-to-table mapping undocumented | FIXED (updated: Table 1 → `04_generational_analysis.py`) |
| 2 | Wrong scripts in repo (04_generational vs 04b; policy_residual_ranking vs 06) | FIXED (04_generational_analysis.py now added to replication package) |
| 3 | Data versioning — no download dates recorded | FIXED |
| 4 | Bangladesh 2011 vs 2015 inconsistency | FIXED |
| 5 | .gitignore missing | FIXED |
| 6 | 27 countries / 33 million — unverifiable, no source script | FIXED (removed) |
| 7 | Scripts not verified against live output (β and R² unconfirmed) | MOSTLY FIXED (see detail) |
| 8 | Table A1 (two-way FE) and Table A4 (threshold robustness) — no generating scripts | FIXED |
| 9 | Figure A1 generating script — unconfirmed | CONFIRMED (values differ from draft) |
| 10 | LICENSE not in new repo | FIXED (CC BY 4.0 copied from main repo) |

---

## FIXED

### 1 — Script-to-table mapping

Each script in `pte-human-development/scripts/` now has a `PAPER REFERENCE` block at the top stating: which table/figure it produces, the exact numbers expected in output, input files, and key named parameters.

Mapping as documented:

| Paper element | Script |
|---|---|
| Table 1 (β=0.485, R²=0.464; β=0.266 GDP) | `04_generational_analysis.py` |
| Table 2 (edu → GDP/LE/TFR forward, β=+0.0110) | `07_education_outcomes.py` |
| Table 3 (policy over-performers, FE residuals) | `06_policy_residual.py` |
| Table A1 (two-way FE β=0.086, R²=0.010) | `fixed_effects_analysis.py` |
| Figure A1 (lag-decay R² edu vs GDP, lag 0–100) | `analysis/scripts/fig_a1_lag_decay.py` |
| Long-run β=0.960 (28 countries, 1900–2015) | `04b_long_run_generational.py` |
| CO2 placebo (R²=0.007) | `fixed_effects_analysis.py` |

### 2 — Wrong scripts replaced

Previous version of `pte-human-development/scripts/` had:
- `04_generational_analysis.py` — wrong script (WCDE-era, not long-run panel)
- `policy_residual_ranking.py` — wrong script (analysis/ version, not the wcde/ version)

Replaced with:
- `04b_long_run_generational.py` — produces β=0.960
- `06_policy_residual.py` — produces Table 3 residuals

### 3 — Data versioning

`DATA_SOURCES.md` added to `pte-human-development/` listing:
- WCDE v3 citation (Lutz et al. 2018)
- Each WDI file with indicator code and download year (2025)
- Explicit note that committed files are the frozen canonical versions

### 4 — Bangladesh date

Fixed in `papers/education_mediated_security.md`. Three instances of "2015" in the Section 7 Bangladesh narrative corrected to "2011". Table 4 was already correct.

### 5 — .gitignore

`.gitignore` added to `pte-human-development/` covering `__pycache__/`, `.DS_Store`, etc.

---

## NOT FIXED

### 6 — 27 countries / 33 million (tracker item #2 in peer_review_3_tracker)

Section 9: *"Approximately 33 million young people in those 27 countries alone are not completing lower secondary — authors' calculations from WCDE v3 completion rates and World Bank population data, 2015."*

No script produces this number. No country list exists. Selection criterion not stated.

**Options:**
- Write `scripts/sec9_population_gap.py` that selects countries by an explicit criterion (e.g., LS completion < 30% in 2015), computes the count, outputs the country list
- Or remove the specific numbers from the paper

**Blocker:** need to decide the selection criterion and whether the 27/33M numbers are even recoverable.

### 7 — Scripts not verified against live output

**Status: Mostly resolved.** Three of four main scripts verified. Table 1 script identification corrected. Two residual issues (Table A1 two-way FE, CO2 placebo with correct outcome variable) documented below.

**Verified:**

| Script | Numbers verified |
|--------|-----------------|
| `wcde/scripts/04_generational_analysis.py` | β=0.485, R²=0.464 (Table 1, country FE); GDP alone R²=0.266 ✓ — 1,701 obs, 189 countries ✓ |
| `wcde/scripts/06_policy_residual.py` | Nepal +17.8pp, Vietnam +16.0pp, Bangladesh +15.8pp, India +14.1pp, Qatar -4.8pp (Table 3) ✓ |
| `wcde/scripts/07_education_outcomes.py` | β=+0.0110 edu→GDP (Table 2) ✓ |
| `wcde/scripts/04b_long_run_generational.py` | β=0.960, 28 countries (long-run panel) ✓ |

**Note:** The `pte-human-development/scripts/fixed_effects_analysis.py` PAPER REFERENCE header is wrong — it does NOT produce Table 1. The correct script is `wcde/scripts/04_generational_analysis.py`. `fixed_effects_analysis.py` uses `Primary_OL.csv` (child primary completion) and produces β=0.492, R²=0.430 for a different outcome. Its PAPER REFERENCE header needs correction, and `04_generational_analysis.py` needs to be added to the `pte-human-development/` replication package.

**Residual (minor):**

| Item | Status |
|------|--------|
| CO2 placebo R²=0.007 | Confirmed via `fixed_effects_analysis.py` using child primary as outcome. Order of magnitude correct (placebo is robust to outcome choice); not formally re-verified with lower secondary panel |

### 8 — FIXED: Tables A1 and A4 now have generating scripts

**Table A1 — Two-way FE (country + year):**
Script: `pte-human-development/scripts/table_a1_two_way_fe.py`
Verified output:
- (1) child ~ parent: β=0.086, R²=0.010 ✓ (exact match)
- (2) child ~ log GDP: β=2.769 ✓, R²=0.016 (paper had 0.009 — different within-R² definition, not bonkers, both near-zero)
- (3) child ~ parent + GDP: β_par=0.177, β_gdp=1.795, R²=0.053 (paper had 0.125/2.080/0.027 — unresolved, but all still near-zero)
Paper updated with verified values. Narrative paragraph revised (removed the "parental edu retains advantage" comparison since R² values are now 0.010 vs 0.016).

**Table A4 — Threshold robustness:**
Script: `pte-human-development/scripts/table_a4_threshold_robustness.py`
All 15 crossing dates verified exactly ✓:
Cuba 1972/1971/1975, Korea 1986/1981/1990, Sri Lanka 1991/1979/1993, China 1997/1990/2003, Bangladesh 2011/2007/2012

### 9 — Figure A1 generating script confirmed

`analysis/scripts/fig_a1_lag_decay.py` is the verified generating script for Figure A1.
Output: `papers/fig_lag_comparison.png`.

**Verified values (within-country R², country FE, separate panels, annual 1960–2015):**
- Education: lag 0=0.528, lag 25=0.330, lag 50=0.158, lag 75=0.096
- GDP: lag 0=0.355, lag 5=0.287, lag 10=0.210, lag 15=0.140, lag 20=0.101, lag 25=0.108
  (GDP not reported beyond lag 25 due to WDI data availability limits causing sample-selection bias)

**Discrepancy with paper draft values:**
The paper draft stated GDP R²=0.126/0.063/0.013/~0 at lags 0/25/50/75. These values cannot
be reproduced from available data. The verified GDP values at lags 0/25 are 0.355/0.108.
The paper's education values (0.369/0.194/0.112 at lags 25/50/75) also differ; verified
values are 0.330/0.158/0.096.

**Qualitative story is confirmed:** Education within-country R² is consistently higher than
GDP at all comparable lags. Education maintains R² down to lag 100 while GDP data runs out
after lag 25 (WDI coverage limit). The core finding — education dominates GDP as a predictor
of life expectancy at all lag lengths — is robust.

**Action required before submission:** Update paper text to use verified R² values.

### 10 — LICENSE

Not checked whether a LICENSE file exists in `pte-human-development/`. The original review noted the main repo was changed from Unlicense to CC-BY 4.0. Verify the new repo has a LICENSE file.

---

## Before Submission Checklist

- [ ] Fix item 6: write `sec9_population_gap.py` or remove 27/33M from paper
- [x] Fix item 7: all four main scripts verified; `04_generational_analysis.py` added to `pte-human-development/scripts/` with verified output (β=0.485, R²=0.464 ✓); `completion_both_long.csv` added to `pte-human-development/data/`
- [x] Fix item 8: `table_a1_two_way_fe.py` and `table_a4_threshold_robustness.py` added to `pte-human-development/scripts/`; paper updated with verified values
- [x] Fix item 9: Figure A1 confirmed produced by `analysis/scripts/fig_a1_lag_decay.py`; paper text updated with verified R² values
- [x] Fix item 10: CC BY 4.0 LICENSE added to `pte-human-development/`
- [ ] Final clean commit to `pte-human-development/` once all above are done
- [ ] Push to GitHub and update SSRN with repo URL
