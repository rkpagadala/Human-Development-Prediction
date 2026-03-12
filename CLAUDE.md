# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a data science / ML research project that predicts human development indicators (life expectancy, fertility rate, GDP per capita, education completion rates) for countries using Random Forest and Gradient Boosting Tree algorithms. Notebooks are designed to run in **Google Colab**.

## Running the Code

There are no build/test/lint commands — this is a notebook-based research project. To work with it:

```bash
# Install dependencies (no requirements.txt — install manually)
pip install pandas numpy tensorflow tensorflow_decision_forests matplotlib seaborn scikit-learn

# Launch Jupyter locally
jupyter notebook

# Or open notebooks in Google Colab (intended environment)
```

Key notebooks to run in order:
1. `data_extract_code/` — extract and preprocess raw data
2. `interpolation_code/` — fill missing year gaps via linear interpolation
3. `models/` — train and evaluate ML models

## Architecture

### Data Pipeline
- **Raw data sources:** World Bank, WCDE (in `/raw_data/`)
- **Extraction scripts:** `/data_extract_code/` — parse raw CSVs, normalize country names, convert population strings (e.g. `1.2M` → numeric)
- **Interpolation:** `/interpolation_code/` — linear interpolation to fill missing yearly data points
- **Cleaned datasets:** `/datasets/` — 30+ CSVs, one per indicator, with standardized country names (lowercase)

### Models (`/models/`)
- 2 × 5 model matrix: 5 target indicators × (all countries / developing countries only)
- Each model notebook: loads relevant CSVs, merges on country+year, trains Random Forest + Gradient Tree, reports NRMSE and feature importances
- `All_Models.ipynb` — master notebook combining all models
- Individual notebooks: `life_expectancy_model.ipynb`, `tfr_model.ipynb`, `GDP_percaptia_model.ipynb`, `education_model.ipynb`, `primary_edu_OL_model.ipynb`

### Utility Scripts
- `data_clean.py` — normalizes country names to lowercase across datasets
- `cal_per.py` — converts raw feature importance scores to percentages
- `renaming_countries_mannual.ipynb` — manual country name reconciliation

### Key Design Decisions
- **Lagged features:** GDP and child mortality use 10–20 year lagged values to capture generational effects
- **Feature selection per model:** Not all 14 features are used in every model; selection is documented in `progress.md` and the linked report
- **Developing countries subset:** Defined as countries in bottom 50% on all indicators in 1960

## Key Files
- `progress.md` — detailed model assumptions, variable importance findings, and development notes
- `reference.md` — academic references (Preston Curve, education-health links)
- `Macro level Diagram.png` — architecture visualization
- `results/README.md` — legend for result PNG files in `/results/`

## Data Conventions
- Country names are stored in **lowercase** throughout datasets
- Education data targets age group **20–24** (reflects completed education, not enrollment)
- GDP is **US inflation-adjusted** per capita
- NRMSE is the evaluation metric (lower = better); reliable threshold is roughly < 0.10
