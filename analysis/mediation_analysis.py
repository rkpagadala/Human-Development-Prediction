"""
Mediation analysis: does female education predict life_expectancy and children_per_woman,
or does its apparent unimportance reflect mediation through children_per_woman?

Tests:
  1. Predict life_expectancy WITH children_per_woman (original setup)
  2. Predict life_expectancy WITHOUT children_per_woman (removes mediator)
  3. Predict children_per_woman using education features only (is education upstream?)
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

    print(f"\n{'='*62}")
    print(f"  {label}")
    print(f"  Target: {target}  |  Rows: {len(df_clean)}  |  NRMSE: {nrmse:.5f}")
    print(f"{'='*62}")
    print(f"  Permutation importance:")
    max_imp = perm.importances_mean[order[0]]
    for rank, i in enumerate(order, 1):
        bar = "#" * int(perm.importances_mean[i] / max_imp * 24)
        print(f"    {rank:2}. {features[i]:<32} {perm.importances_mean[i]:.4f}  {bar}")
    return nrmse

print("Loading panel data...")
panel = load_panel()

EDU_FEATURES = [
    "In_Primary_OL",
    "Primary_OL",
    "female_In_Primary_OL",
    "female_Primary_OL",
]

ALL_NON_EDU = [
    "children_per_woman",
    "co2_emissions_percapita",
    "gini_index",
    "gdppercapita",
    "population",
]

# ── Test 1: predict life expectancy WITH children_per_woman ───────────────────
run(
    "1) Life expectancy ~ all features (children_per_woman included)",
    panel,
    features=ALL_NON_EDU + EDU_FEATURES,
    target="life_expectancy",
)

# ── Test 2: predict life expectancy WITHOUT children_per_woman ────────────────
run(
    "2) Life expectancy ~ all features EXCEPT children_per_woman",
    panel,
    features=[f for f in ALL_NON_EDU if f != "children_per_woman"] + EDU_FEATURES,
    target="life_expectancy",
)

# ── Test 3: predict children_per_woman using only education features ──────────
run(
    "3) children_per_woman ~ education features only",
    panel,
    features=EDU_FEATURES,
    target="children_per_woman",
)

# ── Test 4: predict children_per_woman using all non-edu features + edu ───────
run(
    "4) children_per_woman ~ all features (is education still useful?)",
    panel,
    features=[f for f in ALL_NON_EDU if f != "children_per_woman"] + EDU_FEATURES,
    target="children_per_woman",
)
