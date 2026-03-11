"""
Incremental value of lagged education vs current GDP for life expectancy and TFR.
Mirrors edu_vs_gdp.py but replaces current education with 20-year lagged education.

Key question: if education takes 20 years to have effect, does lagged education
still outperform current GDP as an independent predictor?
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
        for year in range(1980, 2016):  # start 1980 so lag reaches back to 1960
            yr     = str(year)
            lag_yr = str(year - 20)
            row    = {"country": country, "year": year}
            for name in DATASETS:
                try:
                    row[name] = dfs[name].loc[country, yr]
                except KeyError:
                    row[name] = np.nan
            for name in ["female_Primary_OL", "female_In_Primary_OL", "Primary_OL", "gdppercapita"]:
                try:
                    row[name + "_20lag"] = dfs[name].loc[country, lag_yr]
                except KeyError:
                    row[name + "_20lag"] = np.nan
            rows.append(row)
    return pd.DataFrame(rows)

def nrmse(features, target, df):
    clean = df[features + [target]].dropna()
    X = clean[features].values
    y = clean[target].values
    rf = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
    cv = cross_val_score(rf, X, y, cv=5, scoring="neg_mean_squared_error")
    return math.sqrt(-cv.mean()) / (y.max() - y.min()), len(clean)

def section(title, target, panel, edu_cur, edu_lag, gdp_cur, gdp_lag, ctrl):
    print(f"\n{'='*62}")
    print(f"  Predicting: {target}  —  {title}")
    print(f"{'='*62}")

    r = {}
    r["current edu alone"],       _ = nrmse(edu_cur,                   target, panel)
    r["lagged edu alone"],        _ = nrmse(edu_lag,                   target, panel)
    r["current gdp alone"],       _ = nrmse(gdp_cur,                   target, panel)
    r["lagged gdp alone"],        _ = nrmse(gdp_lag,                   target, panel)
    r["cur edu + ctrl"],          _ = nrmse(edu_cur + ctrl,            target, panel)
    r["lag edu + ctrl"],          _ = nrmse(edu_lag + ctrl,            target, panel)
    r["cur gdp + ctrl"],          _ = nrmse(gdp_cur + ctrl,            target, panel)
    r["lag edu + cur gdp + ctrl"],_ = nrmse(edu_lag + gdp_cur + ctrl,  target, panel)
    r["cur edu + cur gdp + ctrl"],_ = nrmse(edu_cur + gdp_cur + ctrl,  target, panel)
    r["lag edu + lag gdp + ctrl"],_ = nrmse(edu_lag + gdp_lag + ctrl,  target, panel)

    r["lag edu+ctrl → +cur gdp"] = r["lag edu + ctrl"] - r["lag edu + cur gdp + ctrl"]
    r["cur gdp+ctrl → +lag edu"] = r["cur gdp + ctrl"] - r["lag edu + cur gdp + ctrl"]

    print(f"  Standalone predictors:")
    print(f"    Current education:           NRMSE = {r['current edu alone']:.5f}")
    print(f"    Lagged  education (20yr):    NRMSE = {r['lagged edu alone']:.5f}")
    print(f"    Current GDP:                 NRMSE = {r['current gdp alone']:.5f}")
    print(f"    Lagged  GDP (20yr):          NRMSE = {r['lagged gdp alone']:.5f}")
    print(f"\n  With controls:")
    print(f"    Current edu + ctrl:          NRMSE = {r['cur edu + ctrl']:.5f}")
    print(f"    Lagged  edu + ctrl:          NRMSE = {r['lag edu + ctrl']:.5f}")
    print(f"    Current GDP + ctrl:          NRMSE = {r['cur gdp + ctrl']:.5f}")
    print(f"\n  Combined (lagged edu vs current GDP):")
    print(f"    Lagged edu + cur GDP + ctrl: NRMSE = {r['lag edu + cur gdp + ctrl']:.5f}")
    print(f"    Cur   edu + cur GDP + ctrl:  NRMSE = {r['cur edu + cur gdp + ctrl']:.5f}")
    print(f"    Lagged edu + lag GDP + ctrl: NRMSE = {r['lag edu + lag gdp + ctrl']:.5f}")
    print(f"\n  Incremental value of adding current GDP to lagged-edu model:")
    print(f"    {r['lag edu+ctrl → +cur gdp']:+.5f}  ({'improvement' if r['lag edu+ctrl → +cur gdp'] > 0 else 'no improvement'})")
    print(f"  Incremental value of adding lagged edu to current-GDP model:")
    print(f"    {r['cur gdp+ctrl → +lag edu']:+.5f}  ({'improvement' if r['cur gdp+ctrl → +lag edu'] > 0 else 'no improvement'})")
    return r

print("Loading data...")
panel = load_panel()

EDU_CUR = ["female_Primary_OL",       "female_In_Primary_OL",       "Primary_OL"]
EDU_LAG = ["female_Primary_OL_20lag", "female_In_Primary_OL_20lag", "Primary_OL_20lag"]
GDP_CUR = ["gdppercapita"]
GDP_LAG = ["gdppercapita_20lag"]
CTRL    = ["co2_emissions_percapita", "gini_index"]

section("lagged edu vs current GDP", "life_expectancy",   panel, EDU_CUR, EDU_LAG, GDP_CUR, GDP_LAG, CTRL)
section("lagged edu vs current GDP", "children_per_woman", panel, EDU_CUR, EDU_LAG, GDP_CUR, GDP_LAG, CTRL)
