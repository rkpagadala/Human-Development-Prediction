"""
Three-way comparison to test how interpolation affects conclusions:
  A) Original: all years 1960-2015, interpolated education features
  B) 5-year only: restrict to real WCDE observation years (1960,1965,...2015)
  C) Year-controlled: add 'year' as explicit feature, all years
"""

import math
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.inspection import permutation_importance

ROOT = "datasets/"

DATASETS = {
    "children_per_woman":           ROOT + "children_per_woman_total_fertility.csv",
    "co2_emissions_percapita":      ROOT + "co2_emissions_tonnes_per_person.csv",
    "gini_index":                   ROOT + "gini.csv",
    "gdppercapita":                 ROOT + "gdppercapita_us_inflation_adjusted.csv",
    "In_Primary_OL":                ROOT + "In_Primary_OL.csv",
    "Primary_OL":                   ROOT + "Primary_OL.csv",
    "population":                   ROOT + "converted_pop.csv",
    "female_In_Primary_OL":         ROOT + "female_In_Primary_OL.csv",
    "female_Primary_OL":            ROOT + "female_Primary_OL.csv",
    "life_expectancy":              ROOT + "life_expectancy_years.csv",
}

FEATURES = [
    "children_per_woman",
    "co2_emissions_percapita",
    "gini_index",
    "gdppercapita",
    "In_Primary_OL",
    "Primary_OL",
    "population",
    "female_In_Primary_OL",
    "female_Primary_OL",
    "gdppercapita_20yr_lag",
]
TARGET = "life_expectancy"

def load_wide(name):
    df = pd.read_csv(DATASETS[name])
    df["Country"] = df["Country"].str.lower()
    return df.set_index("Country")

def build_panel(years):
    dfs = {name: load_wide(name) for name in list(DATASETS.keys())}
    # find common countries
    common = set(dfs["life_expectancy"].index)
    for name, df in dfs.items():
        common &= set(df.index)
    common = sorted(common)

    rows = []
    for country in common:
        for year in years:
            yr = str(year)
            row = {"country": country, "year": year}
            for feat in DATASETS:
                try:
                    row[feat] = dfs[feat].loc[country, yr]
                except KeyError:
                    row[feat] = np.nan
            # 20-year lagged GDP
            lag_yr = str(year - 20)
            try:
                row["gdppercapita_20yr_lag"] = dfs["gdppercapita"].loc[country, lag_yr]
            except KeyError:
                row["gdppercapita_20yr_lag"] = np.nan
            rows.append(row)

    return pd.DataFrame(rows)

def compute_nrmse(y_true, y_pred):
    rmse = math.sqrt(np.mean((y_true - y_pred) ** 2))
    return rmse / (y_true.max() - y_true.min())

def run_experiment(label, df, extra_features=None):
    features = FEATURES.copy()
    if extra_features:
        features = features + extra_features

    df_clean = df[features + [TARGET]].dropna()
    X = df_clean[features].values
    y = df_clean[TARGET].values

    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"  Rows: {len(df_clean)}  |  Countries x years")
    print(f"{'='*60}")

    rf = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)

    # Cross-validated NRMSE
    cv_scores = cross_val_score(rf, X, y, cv=5, scoring="neg_mean_squared_error")
    rmse = math.sqrt(-cv_scores.mean())
    nrmse = rmse / (y.max() - y.min())
    print(f"  CV NRMSE: {nrmse:.5f}  (RMSE: {rmse:.3f} years)")

    # Fit on full data for permutation importance
    rf.fit(X, y)
    perm = permutation_importance(rf, X, y, n_repeats=10, random_state=42, n_jobs=-1)

    order = perm.importances_mean.argsort()[::-1]
    print(f"\n  Permutation importance (mean decrease in R²):")
    for rank, i in enumerate(order, 1):
        bar = "#" * int(perm.importances_mean[i] / perm.importances_mean[order[0]] * 20)
        print(f"    {rank:2}. {features[i]:<35} {perm.importances_mean[i]:.4f}  {bar}")

    return nrmse

# ── Build panels ──────────────────────────────────────────────────────────────
ALL_YEARS = list(range(1960, 2016))
FIVE_YEAR  = list(range(1960, 2016, 5))

print("Loading data...")
panel_all  = build_panel(ALL_YEARS)
panel_5yr  = build_panel(FIVE_YEAR)

# ── Experiment A: original (all years, no year control) ───────────────────────
nrmse_a = run_experiment("A) Original — all years, no year control", panel_all)

# ── Experiment B: 5-year only (removes interpolation smoothness) ──────────────
nrmse_b = run_experiment("B) 5-year only — real WCDE observations only", panel_5yr)

# ── Experiment C: all years + year as explicit feature ────────────────────────
panel_all["year_num"] = panel_all["year"]
nrmse_c = run_experiment("C) All years + year as control feature", panel_all, extra_features=["year_num"])

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print("  SUMMARY")
print(f"{'='*60}")
print(f"  A) Original (all years):        NRMSE = {nrmse_a:.5f}")
print(f"  B) 5-year only (no interp.):    NRMSE = {nrmse_b:.5f}")
print(f"  C) Year-controlled (all years): NRMSE = {nrmse_c:.5f}")
print(f"\n  If female education importance drops sharply in B or C,")
print(f"  the original conclusion is driven by interpolation / time trend.")
