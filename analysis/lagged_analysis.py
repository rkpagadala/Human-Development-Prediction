"""
Test whether lagged education (20 years prior) predicts life expectancy and TFR
better than current GDP, which is volatile year-to-year.

Experiments:
  1. Current education vs current GDP predicting life expectancy
  2. 20-year lagged education vs current GDP predicting life expectancy
  3. 20-year lagged education vs current GDP predicting TFR
  4. Stability check: GDP volatility vs education volatility within countries
"""

import math
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.inspection import permutation_importance

ROOT = "datasets/"

DATASETS = {
    "children_per_woman":      ROOT + "children_per_woman_total_fertility.csv",
    "co2_emissions_percapita": ROOT + "co2_emissions_tonnes_per_person.csv",
    "gini_index":              ROOT + "gini.csv",
    "gdppercapita":            ROOT + "gdppercapita_us_inflation_adjusted.csv",
    "female_Primary_OL":       ROOT + "female_Primary_OL.csv",
    "female_In_Primary_OL":    ROOT + "female_In_Primary_OL.csv",
    "life_expectancy":         ROOT + "life_expectancy_years.csv",
}

def load_panel(years=None):
    if years is None:
        years = list(range(1980, 2016))  # start 1980 so 20yr lag reaches back to 1960
    dfs = {}
    for name, path in DATASETS.items():
        df = pd.read_csv(path)
        df["Country"] = df["Country"].str.lower()
        dfs[name] = df.set_index("Country")

    common = set(dfs["life_expectancy"].index)
    for df in dfs.values():
        common &= set(df.index)
    common = sorted(common)

    rows = []
    for country in common:
        for year in years:
            yr     = str(year)
            lag_yr = str(year - 20)
            row    = {"country": country, "year": year}
            for name in DATASETS:
                try:
                    row[name] = dfs[name].loc[country, yr]
                except KeyError:
                    row[name] = np.nan
            # 20-year lags
            for name in ["gdppercapita", "female_Primary_OL", "female_In_Primary_OL"]:
                try:
                    row[name + "_20lag"] = dfs[name].loc[country, lag_yr]
                except KeyError:
                    row[name + "_20lag"] = np.nan
            rows.append(row)
    return pd.DataFrame(rows), dfs, common

def run(label, df, features, target):
    df_clean = df[features + [target]].dropna()
    X = df_clean[features].values
    y = df_clean[target].values

    rf = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
    cv = cross_val_score(rf, X, y, cv=5, scoring="neg_mean_squared_error")
    nrmse = math.sqrt(-cv.mean()) / (y.max() - y.min())

    rf.fit(X, y)
    perm = permutation_importance(rf, X, y, n_repeats=10, random_state=42, n_jobs=-1)
    order = perm.importances_mean.argsort()[::-1]

    print(f"\n{'='*64}")
    print(f"  {label}")
    print(f"  Target: {target}  |  Rows: {len(df_clean)}  |  NRMSE: {nrmse:.5f}")
    print(f"{'='*64}")
    max_imp = perm.importances_mean[order[0]]
    for rank, i in enumerate(order, 1):
        bar = "#" * int(perm.importances_mean[i] / max_imp * 24)
        print(f"    {rank:2}. {features[i]:<40} {perm.importances_mean[i]:.4f}  {bar}")
    return nrmse

print("Loading data...")
panel, dfs, common = load_panel()

CONTROLS = ["co2_emissions_percapita", "gini_index"]

# ── 1. Current education + current GDP → life expectancy ─────────────────────
nrmse1 = run(
    "1) Life expectancy ~ current edu + current GDP",
    panel,
    ["female_Primary_OL", "female_In_Primary_OL", "gdppercapita"] + CONTROLS,
    "life_expectancy",
)

# ── 2. Lagged education + current GDP → life expectancy ──────────────────────
nrmse2 = run(
    "2) Life expectancy ~ 20yr-lagged edu + current GDP",
    panel,
    ["female_Primary_OL_20lag", "female_In_Primary_OL_20lag", "gdppercapita"] + CONTROLS,
    "life_expectancy",
)

# ── 3. Lagged education vs lagged GDP → life expectancy ──────────────────────
nrmse3 = run(
    "3) Life expectancy ~ 20yr-lagged edu + 20yr-lagged GDP",
    panel,
    ["female_Primary_OL_20lag", "female_In_Primary_OL_20lag", "gdppercapita_20lag"] + CONTROLS,
    "life_expectancy",
)

# ── 4. Lagged education + current GDP → TFR ──────────────────────────────────
nrmse4 = run(
    "4) TFR ~ 20yr-lagged edu + current GDP",
    panel,
    ["female_Primary_OL_20lag", "female_In_Primary_OL_20lag", "gdppercapita"] + CONTROLS,
    "children_per_woman",
)

# ── 5. Stability: within-country std dev of GDP vs education ─────────────────
print(f"\n{'='*64}")
print(f"  5) Within-country volatility: GDP vs female education")
print(f"{'='*64}")

gdp_df  = dfs["gdppercapita"]
edu_df  = dfs["female_Primary_OL"]
years   = [str(y) for y in range(1980, 2016)]

gdp_cols = [c for c in years if c in gdp_df.columns]
edu_cols = [c for c in years if c in edu_df.columns]

gdp_cv  = gdp_df.loc[common, gdp_cols].apply(pd.to_numeric, errors='coerce')
edu_cv  = edu_df.loc[common, edu_cols].apply(pd.to_numeric, errors='coerce')

# Coefficient of variation (std/mean) within each country
gdp_cv_vals = (gdp_cv.std(axis=1) / gdp_cv.mean(axis=1)).dropna()
edu_cv_vals = (edu_cv.std(axis=1) / edu_cv.mean(axis=1)).dropna()

print(f"  Coefficient of variation (std/mean) within countries, 1980–2015:")
print(f"    GDP per capita:          mean={gdp_cv_vals.mean():.3f}  median={gdp_cv_vals.median():.3f}")
print(f"    Female primary edu:      mean={edu_cv_vals.mean():.3f}  median={edu_cv_vals.median():.3f}")
print(f"\n  GDP is ~{gdp_cv_vals.median()/edu_cv_vals.median():.1f}x more volatile than female education within countries.")

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n{'='*64}")
print(f"  NRMSE COMPARISON")
print(f"{'='*64}")
print(f"  1) Current edu + current GDP  → life exp:  {nrmse1:.5f}")
print(f"  2) Lagged edu  + current GDP  → life exp:  {nrmse2:.5f}")
print(f"  3) Lagged edu  + lagged GDP   → life exp:  {nrmse3:.5f}")
print(f"  4) Lagged edu  + current GDP  → TFR:       {nrmse4:.5f}")
