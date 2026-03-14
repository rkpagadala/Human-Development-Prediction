# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A research project studying the causal drivers of human development — life expectancy, fertility, GDP per capita, education completion — using longitudinal global data. Started as a collaborative undergraduate ML project (with Jaya Shankar) and extended into causal analysis, generational education effects, and policy work.

## Running the Code

Analysis scripts are plain Python. No notebooks.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels

# Run any analysis script directly, e.g.:
python analysis/scripts/lagged_analysis.py
python wcde/scripts/07_education_outcomes.py
```

## Repository Structure

### `analysis/`
Research outputs and scripts.
- `scripts/` — Python analysis scripts (rankings, causal tests, gap analysis, etc.)
- `findings.md` — main findings summary
- `leapfrog_brief.md` — countries that leapfrogged development
- `costing.md` — intervention cost analysis
- `education_gap_all_countries.md` — education gap tables by country

### `wcde/`
WCDE v3 data pipeline and long-run generational analysis.
- `scripts/` — download, process, and analyse WCDE education data back to 1875
- `data/` — processed WCDE outputs

### `datasets/`
Cleaned CSVs used by analysis scripts. One file per indicator, sourced from World Bank and WCDE. Country names are lowercase throughout.

Key files: `gdppercapita_us_inflation_adjusted.csv`, `children_per_woman_total_fertility.csv`, `child_mortality_0_5_year_olds_dying_per_1000_born.csv`, `life_expectancy_years.csv`, `gini.csv`, education completion CSVs by level and sex.

### `vision/`
Policy and philanthropist vision documents.

## Key Design Decisions
- **Education age group 20–24** — reflects completed education, not enrollment
- **Lagged features** — GDP and child mortality use 10–20 year lags to capture generational effects
- **GDP is US inflation-adjusted** per capita
- **P-25 mechanism** — parental transmission of education; below ~25% lower secondary completion, intergenerational progress is slow
- **NRMSE < 0.10** — reliable model threshold

## Key Files
- `reference.md` — academic references (Preston Curve, Lutz & Kebede, education-health links)
- `analysis/findings.md` — main research conclusions
