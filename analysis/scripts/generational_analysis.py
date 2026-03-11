"""
Generational transmission of education vs income.

The 20-24 cohort in year T had parents who were 20-24 roughly in year T-25.
So Primary_OL(T-25) represents the parental generation's education.

Key question: does parental education predict child education independently
of GDP? If yes — and if it's stronger than GDP — then income is not the
primary driver. Education propagates itself generationally.

Focus: PRIMARY completion first (the foundation), then secondary.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

ROOT = "datasets/"

DATASETS = {
    "Primary_OL":         ROOT + "Primary_OL.csv",
    "Lower_Secondary_OL": ROOT + "Lower_Secondary_OL.csv",
    "female_Primary_OL":  ROOT + "female_Primary_OL.csv",
    "gdp":                ROOT + "gdppercapita_us_inflation_adjusted.csv",
    "tfr":                ROOT + "children_per_woman_total_fertility.csv",
    "life_expectancy":    ROOT + "life_expectancy_years.csv",
}

PARENTAL_LAG = 25   # years between parental 20-24 cohort and child 20-24 cohort
SCHOOLING_LAG = 12  # years between schooling age and 20-24 measurement

def load(path):
    df = pd.read_csv(path)
    df["Country"] = df["Country"].str.lower()
    return df.set_index("Country")

print("Loading data...")
dfs = {name: load(path) for name, path in DATASETS.items()}
all_countries = sorted(set(dfs["gdp"].index) & set(dfs["Primary_OL"].index))

def get(name, country, year):
    try:
        return float(dfs[name].loc[country, str(year)])
    except (KeyError, ValueError):
        return np.nan

def comp(ol): return 100 - ol

def fit_and_report(label, X_cols, X_data, y):
    reg = LinearRegression().fit(X_data, y)
    r2  = reg.score(X_data, y)
    print(f"  {label:<55}  R² = {r2:.3f}")
    return reg, r2

# ── Build global panel ────────────────────────────────────────────────────────
print("Building global panel (1985-2015, need parental lag to 1960)...")
rows = []
for country in all_countries:
    for yr in range(1985, 2016):
        child_pri   = comp(get("Primary_OL",   country, yr))
        child_low   = comp(get("Lower_Secondary_OL", country, yr))
        parent_pri  = comp(get("Primary_OL",   country, yr - PARENTAL_LAG))
        parent_f_pri= comp(get("female_Primary_OL", country, yr - PARENTAL_LAG))
        gdp_school  = get("gdp", country, yr - SCHOOLING_LAG)   # GDP when child was in school
        gdp_parent  = get("gdp", country, yr - PARENTAL_LAG)    # GDP when parent was in school
        gdp_current = get("gdp", country, yr)
        if any(np.isnan(v) for v in [child_pri, parent_pri, gdp_school]):
            continue
        rows.append({
            "country":      country,
            "year":         yr,
            "child_pri":    child_pri,
            "child_low":    child_low,
            "parent_pri":   parent_pri,
            "parent_f_pri": parent_f_pri,
            "gdp_school":   gdp_school,
            "gdp_parent":   gdp_parent,
            "gdp_current":  gdp_current,
            "log_gdp_school":  np.log(gdp_school)  if gdp_school  > 0 else np.nan,
            "log_gdp_parent":  np.log(gdp_parent)  if not np.isnan(gdp_parent) and gdp_parent > 0 else np.nan,
            "log_gdp_current": np.log(gdp_current) if not np.isnan(gdp_current) and gdp_current > 0 else np.nan,
        })

panel = pd.DataFrame(rows).dropna(subset=["child_pri","parent_pri","log_gdp_school"])
print(f"  Panel: {len(panel)} observations, {panel['country'].nunique()} countries\n")

# ── Section 1: How much does GDP alone explain? ───────────────────────────────
print(f"{'='*72}")
print(f"  SECTION 1: What drives PRIMARY education? (target: ≥primary completion)")
print(f"  Global panel, all countries, 1985-2015")
print(f"{'='*72}")

p = panel.dropna(subset=["log_gdp_school","parent_pri","log_gdp_parent"])
y = p["child_pri"].values

print()
fit_and_report("GDP at schooling age only",
               ["log_gdp_school"], p[["log_gdp_school"]].values, y)

fit_and_report("Parental primary education only",
               ["parent_pri"], p[["parent_pri"]].values, y)

fit_and_report("GDP at schooling age + parental education",
               ["log_gdp_school","parent_pri"],
               p[["log_gdp_school","parent_pri"]].values, y)

fit_and_report("GDP when parent was in school only",
               ["log_gdp_parent"], p[["log_gdp_parent"]].values, y)

fit_and_report("GDP when parent schooled + parental education",
               ["log_gdp_parent","parent_pri"],
               p[["log_gdp_parent","parent_pri"]].values, y)

fit_and_report("Female parental education only",
               ["parent_f_pri"], p[["parent_f_pri"]].values, y)

fit_and_report("Female parental edu + GDP at schooling age",
               ["parent_f_pri","log_gdp_school"],
               p[["parent_f_pri","log_gdp_school"]].values, y)

fit_and_report("Female parental edu + parental edu + GDP",
               ["parent_f_pri","parent_pri","log_gdp_school"],
               p[["parent_f_pri","parent_pri","log_gdp_school"]].values, y)

# ── Section 2: Same for lower secondary ───────────────────────────────────────
print(f"\n{'='*72}")
print(f"  SECTION 2: What drives LOWER SECONDARY? (target: ≥lower sec completion)")
print(f"{'='*72}")

p2 = panel.dropna(subset=["child_low","log_gdp_school","parent_pri","log_gdp_parent"])
y2 = p2["child_low"].values

print()
fit_and_report("GDP at schooling age only",
               ["log_gdp_school"], p2[["log_gdp_school"]].values, y2)

fit_and_report("Parental primary education only",
               ["parent_pri"], p2[["parent_pri"]].values, y2)

fit_and_report("GDP + parental primary education",
               ["log_gdp_school","parent_pri"],
               p2[["log_gdp_school","parent_pri"]].values, y2)

fit_and_report("Female parental education only",
               ["parent_f_pri"], p2[["parent_f_pri"]].values, y2)

fit_and_report("Female parental edu + GDP",
               ["parent_f_pri","log_gdp_school"],
               p2[["parent_f_pri","log_gdp_school"]].values, y2)

# ── Section 3: Incremental value — parental edu vs GDP ───────────────────────
print(f"\n{'='*72}")
print(f"  SECTION 3: Incremental R² — what adds more: parental edu or GDP?")
print(f"{'='*72}")
p3 = panel.dropna(subset=["child_pri","log_gdp_school","parent_pri","parent_f_pri"])
y3 = p3["child_pri"].values

_, r2_base   = fit_and_report("Baseline (intercept only → mean)", [], np.ones((len(y3),1)), y3)
_, r2_gdp    = fit_and_report("+ GDP at schooling age", ["log_gdp_school"], p3[["log_gdp_school"]].values, y3)
_, r2_par    = fit_and_report("+ parental primary edu", ["parent_pri"], p3[["parent_pri"]].values, y3)
_, r2_both   = fit_and_report("+ both GDP and parental edu", ["log_gdp_school","parent_pri"], p3[["log_gdp_school","parent_pri"]].values, y3)
_, r2_fpar   = fit_and_report("+ female parental edu", ["parent_f_pri"], p3[["parent_f_pri"]].values, y3)
_, r2_fboth  = fit_and_report("+ female parental edu + GDP", ["parent_f_pri","log_gdp_school"], p3[["parent_f_pri","log_gdp_school"]].values, y3)

print(f"\n  Incremental gain from adding GDP to parental-edu model:          +{r2_both-r2_par:.3f}")
print(f"  Incremental gain from adding parental edu to GDP model:          +{r2_both-r2_gdp:.3f}")
print(f"  Incremental gain from adding female parental edu to GDP model:   +{r2_fboth-r2_gdp:.3f}")

# ── Section 4: Country-level generational momentum ───────────────────────────
print(f"\n{'='*72}")
print(f"  SECTION 4: Generational momentum — per-country residuals")
print(f"  After removing BOTH GDP and parental education effects,")
print(f"  which countries still over/under-perform? (pure policy signal)")
print(f"{'='*72}")

p4 = panel.dropna(subset=["child_pri","log_gdp_school","parent_pri"])
y4 = p4["child_pri"].values
X4 = p4[["log_gdp_school","parent_pri"]].values
reg4 = LinearRegression().fit(X4, y4)
p4 = p4.copy()
p4["residual"] = y4 - reg4.predict(X4)

country_res = p4.groupby("country")["residual"].mean().sort_values(ascending=False)

print(f"\n  TOP 15 over-performers (better edu than GDP+parental-edu predicts):")
for country, res in country_res.head(15).items():
    bar = "#" * int(abs(res) / country_res.abs().max() * 20)
    print(f"    {country:<30}  {res:>+6.1f}pp  {bar}")

print(f"\n  TOP 15 under-performers:")
for country, res in country_res.tail(15).items():
    bar = "#" * int(abs(res) / country_res.abs().max() * 20)
    print(f"    {country:<30}  {res:>+6.1f}pp  {bar}")

# Focus countries
print(f"\n  Focus countries:")
for c in ["china", "india", "south korea", "malaysia", "thailand",
          "singapore", "ghana", "kenya", "nigeria", "pakistan", "bangladesh"]:
    if c in country_res.index:
        res = country_res[c]
        print(f"    {c:<30}  {res:>+6.1f}pp")

# ── Section 5: Generational trace for China and India ────────────────────────
print(f"\n{'='*72}")
print(f"  SECTION 5: Generational trace — China vs India")
print(f"  Child primary edu vs parental primary edu vs GDP(schooling age)")
print(f"{'='*72}")

print(f"\n  {'Year':>5}  {'CHN child≥Pri':>14} {'CHN parent≥Pri':>15} {'CHN GDP-school':>15}  "
      f"{'IND child≥Pri':>14} {'IND parent≥Pri':>15} {'IND GDP-school':>15}")
print(f"  {'-'*5}  {'-'*14} {'-'*15} {'-'*15}  {'-'*14} {'-'*15} {'-'*15}")

for yr in range(1985, 2016, 5):
    c_child  = comp(get("Primary_OL", "china", yr))
    c_parent = comp(get("Primary_OL", "china", yr - PARENTAL_LAG))
    c_gdp    = get("gdp", "china", yr - SCHOOLING_LAG)
    i_child  = comp(get("Primary_OL", "india", yr))
    i_parent = comp(get("Primary_OL", "india", yr - PARENTAL_LAG))
    i_gdp    = get("gdp", "india", yr - SCHOOLING_LAG)
    print(f"  {yr:>5}  {c_child:>13.1f}% {c_parent:>14.1f}% {c_gdp:>15.0f}  "
          f"{i_child:>13.1f}% {i_parent:>14.1f}% {i_gdp:>15.0f}")
