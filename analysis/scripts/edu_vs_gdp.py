"""
Test whether GDP adds anything once education is in the model, and vice versa.
Uses incremental R² (how much does adding each variable improve the model?)
"""

import math
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

ROOT = "datasets/"

DATASETS = {
    "children_per_woman":      ROOT + "children_per_woman_total_fertility.csv",
    "co2_emissions_percapita": ROOT + "co2_emissions_tonnes_per_person.csv",
    "gini_index":              ROOT + "gini.csv",
    "gdppercapita":            ROOT + "gdppercapita_us_inflation_adjusted.csv",
    "female_Primary_OL":       ROOT + "female_Primary_OL.csv",
    "female_In_Primary_OL":    ROOT + "female_In_Primary_OL.csv",
    "Primary_OL":              ROOT + "Primary_OL.csv",
    "life_expectancy":         ROOT + "life_expectancy_years.csv",
}

def load_panel():
    dfs = {}
    for name, path in DATASETS.items():
        df = pd.read_csv(path)
        df["Country"] = df["Country"].str.lower()
        dfs[name] = df.set_index("Country")

    common = set(dfs["life_expectancy"].index)
    for df in dfs.values():
        common &= set(df.index)

    rows = []
    for country in sorted(common):
        for year in range(1960, 2016):
            yr = str(year)
            row = {"country": country, "year": year}
            for name in DATASETS:
                try:
                    row[name] = dfs[name].loc[country, yr]
                except KeyError:
                    row[name] = np.nan
            rows.append(row)
    return pd.DataFrame(rows)

def nrmse(features, target, df):
    clean = df[features + [target]].dropna()
    X = clean[features].values
    y = clean[target].values
    rf = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
    cv = cross_val_score(rf, X, y, cv=5, scoring="neg_mean_squared_error")
    return math.sqrt(-cv.mean()) / (y.max() - y.min()), len(clean)

print("Loading data...")
panel = load_panel()

EDU     = ["female_Primary_OL", "female_In_Primary_OL", "Primary_OL"]
GDP     = ["gdppercapita"]
CTRL    = ["co2_emissions_percapita", "gini_index"]
TARGET  = "life_expectancy"

results = {}

print("\nRunning models (this takes a few minutes)...")

# Baselines
results["edu alone"],       n1 = nrmse(EDU,            TARGET, panel)
results["gdp alone"],       n2 = nrmse(GDP,            TARGET, panel)
results["ctrl alone"],      n3 = nrmse(CTRL,           TARGET, panel)

# Education + controls, no GDP
results["edu + ctrl"],      n4 = nrmse(EDU + CTRL,     TARGET, panel)

# GDP + controls, no education
results["gdp + ctrl"],      n5 = nrmse(GDP + CTRL,     TARGET, panel)

# Full: education + GDP + controls
results["edu + gdp + ctrl"],n6 = nrmse(EDU + GDP + CTRL, TARGET, panel)

# Incremental value of GDP given education
results["edu+ctrl → +gdp"] = results["edu + ctrl"] - results["edu + gdp + ctrl"]

# Incremental value of education given GDP
results["gdp+ctrl → +edu"] = results["gdp + ctrl"] - results["edu + gdp + ctrl"]

print(f"\n{'='*56}")
print(f"  Predicting: {TARGET}")
print(f"{'='*56}")
print(f"  Education alone:              NRMSE = {results['edu alone']:.5f}")
print(f"  GDP alone:                    NRMSE = {results['gdp alone']:.5f}")
print(f"  Controls alone:               NRMSE = {results['ctrl alone']:.5f}")
print(f"  Education + controls:         NRMSE = {results['edu + ctrl']:.5f}")
print(f"  GDP + controls:               NRMSE = {results['gdp + ctrl']:.5f}")
print(f"  Education + GDP + controls:   NRMSE = {results['edu + gdp + ctrl']:.5f}")
print(f"\n  Incremental gain from adding GDP to education model:")
print(f"    {results['edu+ctrl → +gdp']:+.5f}  ({'improvement' if results['edu+ctrl → +gdp'] > 0 else 'no improvement'})")
print(f"\n  Incremental gain from adding education to GDP model:")
print(f"    {results['gdp+ctrl → +edu']:+.5f}  ({'improvement' if results['gdp+ctrl → +edu'] > 0 else 'no improvement'})")

# Now repeat for TFR
TARGET2 = "children_per_woman"
results2 = {}
print(f"\n{'='*56}")
print(f"  Predicting: {TARGET2}")
print(f"{'='*56}")

results2["edu alone"],        _ = nrmse(EDU,               TARGET2, panel)
results2["gdp alone"],        _ = nrmse(GDP,               TARGET2, panel)
results2["edu + ctrl"],       _ = nrmse(EDU + CTRL,        TARGET2, panel)
results2["gdp + ctrl"],       _ = nrmse(GDP + CTRL,        TARGET2, panel)
results2["edu + gdp + ctrl"], _ = nrmse(EDU + GDP + CTRL,  TARGET2, panel)
results2["edu+ctrl → +gdp"]    = results2["edu + ctrl"] - results2["edu + gdp + ctrl"]
results2["gdp+ctrl → +edu"]    = results2["gdp + ctrl"] - results2["edu + gdp + ctrl"]

print(f"  Education alone:              NRMSE = {results2['edu alone']:.5f}")
print(f"  GDP alone:                    NRMSE = {results2['gdp alone']:.5f}")
print(f"  Education + controls:         NRMSE = {results2['edu + ctrl']:.5f}")
print(f"  GDP + controls:               NRMSE = {results2['gdp + ctrl']:.5f}")
print(f"  Education + GDP + controls:   NRMSE = {results2['edu + gdp + ctrl']:.5f}")
print(f"\n  Incremental gain from adding GDP to education model:")
print(f"    {results2['edu+ctrl → +gdp']:+.5f}  ({'improvement' if results2['edu+ctrl → +gdp'] > 0 else 'no improvement'})")
print(f"\n  Incremental gain from adding education to GDP model:")
print(f"    {results2['gdp+ctrl → +edu']:+.5f}  ({'improvement' if results2['gdp+ctrl → +edu'] > 0 else 'no improvement'})")
