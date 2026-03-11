"""
Explore the relationship between female education and GDP:
  1. Does female education predict GDP?
  2. Does GDP predict female education?
  3. Life expectancy ~ education without GDP (does education rise further?)
  4. Life expectancy ~ GDP without education (how much does GDP alone explain?)
  5. Partial: education → life_expectancy controlling for GDP (and vice versa)
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
    "In_Primary_OL":           ROOT + "In_Primary_OL.csv",
    "Primary_OL":              ROOT + "Primary_OL.csv",
    "population":              ROOT + "converted_pop.csv",
    "female_In_Primary_OL":    ROOT + "female_In_Primary_OL.csv",
    "female_Primary_OL":       ROOT + "female_Primary_OL.csv",
    "life_expectancy":         ROOT + "life_expectancy_years.csv",
}

def load_panel(years=None):
    if years is None:
        years = list(range(1960, 2016))
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
            yr = str(year)
            row = {"country": country, "year": year}
            for name in DATASETS:
                try:
                    row[name] = dfs[name].loc[country, yr]
                except KeyError:
                    row[name] = np.nan
            # 20-year lagged GDP
            lag_yr = str(year - 20)
            try:
                row["gdppercapita_20yr_lag"] = dfs["gdppercapita"].loc[country, lag_yr]
            except KeyError:
                row["gdppercapita_20yr_lag"] = np.nan
            rows.append(row)
    return pd.DataFrame(rows)

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
        print(f"    {rank:2}. {features[i]:<35} {perm.importances_mean[i]:.4f}  {bar}")
    return nrmse

print("Loading data...")
panel = load_panel()

EDU = ["female_Primary_OL", "female_In_Primary_OL", "Primary_OL", "In_Primary_OL"]
NON_EDU = ["co2_emissions_percapita", "gini_index", "population", "children_per_woman"]

# ── 1. Does female education predict GDP? ─────────────────────────────────────
run("1) GDP ~ education only", panel, EDU, "gdppercapita")

# ── 2. Does GDP predict female education? ─────────────────────────────────────
run("2) female_Primary_OL ~ GDP + controls", panel,
    ["gdppercapita", "gdppercapita_20yr_lag", "co2_emissions_percapita", "gini_index", "population"],
    "female_Primary_OL")

# ── 3. Life expectancy ~ education only (no GDP, no TFR) ──────────────────────
run("3) Life expectancy ~ education only", panel, EDU, "life_expectancy")

# ── 4. Life expectancy ~ GDP only (no education, no TFR) ──────────────────────
run("4) Life expectancy ~ GDP only", panel,
    ["gdppercapita", "gdppercapita_20yr_lag"], "life_expectancy")

# ── 5. Life expectancy ~ education + controls, no GDP, no TFR ────────────────
run("5) Life expectancy ~ education + non-GDP controls", panel,
    EDU + ["co2_emissions_percapita", "gini_index", "population"], "life_expectancy")

# ── 6. Life expectancy ~ GDP + controls, no education, no TFR ────────────────
run("6) Life expectancy ~ GDP + non-edu controls", panel,
    ["gdppercapita", "gdppercapita_20yr_lag"] + NON_EDU, "life_expectancy")

# ── 7. Life expectancy ~ education + GDP together (no TFR) ───────────────────
run("7) Life expectancy ~ education + GDP together (no TFR)", panel,
    EDU + ["gdppercapita", "gdppercapita_20yr_lag", "co2_emissions_percapita", "gini_index", "population"],
    "life_expectancy")
