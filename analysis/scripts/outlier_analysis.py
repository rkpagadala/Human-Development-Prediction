"""
Which countries improved education fastest over 1960-2015?
Is GDP a predictor of education improvement, or is something else driving it?
Sorted by education level: primary → lower secondary → higher secondary (dropout cascade).
"""

import pandas as pd
import numpy as np

ROOT = "datasets/"

# Education levels — "OL" means "or less" so HIGH value = LOW education
# improvement = value_1960 - value_2015 (positive = got better)
# Higher secondary completes: HIGH value = HIGH education
# improvement = value_2015 - value_1960

EDU_LEVELS = {
    "In_Primary_OL":        (ROOT + "In_Primary_OL.csv",              "decrease"),  # % stuck below primary
    "Primary_OL":           (ROOT + "Primary_OL.csv",                 "decrease"),  # % with primary or less
    "Lower_Secondary_OL":   (ROOT + "Lower_Secondary_OL.csv",         "decrease"),  # % with lower sec or less
    "Higher_Secondary":     (ROOT + "Higher_Secondary_fin_complete.csv", "increase"),  # % completed higher sec
}

GDP_PATH = ROOT + "gdppercapita_us_inflation_adjusted.csv"

def load(path):
    df = pd.read_csv(path)
    df["Country"] = df["Country"].str.lower()
    return df.set_index("Country")

def get_val(df, country, year):
    try:
        return float(df.loc[country, str(year)])
    except (KeyError, ValueError):
        return np.nan

print("Loading data...")
edu_dfs = {name: load(path) for name, (path, _) in EDU_LEVELS.items()}
gdp_df  = load(GDP_PATH)

# Common countries across all datasets
common = set(gdp_df.index)
for df in edu_dfs.values():
    common &= set(df.index)
common = sorted(common)

START, END = 1960, 2015

# Build summary table per country
rows = []
for country in common:
    row = {"country": country}
    for level, (_, direction) in EDU_LEVELS.items():
        v0 = get_val(edu_dfs[level], country, START)
        v1 = get_val(edu_dfs[level], country, END)
        if direction == "decrease":
            row[f"{level}_1960"] = v0
            row[f"{level}_2015"] = v1
            row[f"{level}_improvement"] = v0 - v1   # positive = improved
        else:
            row[f"{level}_1960"] = v0
            row[f"{level}_2015"] = v1
            row[f"{level}_improvement"] = v1 - v0   # positive = improved

    row["gdp_1960"] = get_val(gdp_df, country, START)
    row["gdp_2015"] = get_val(gdp_df, country, END)
    row["gdp_growth"] = (row["gdp_2015"] / row["gdp_1960"]) if row["gdp_1960"] > 0 else np.nan
    rows.append(row)

summary = pd.DataFrame(rows).set_index("country")
summary = summary.dropna(subset=[f"{l}_improvement" for l in EDU_LEVELS])

# ── Dropout cascade: show average completion rates across levels ──────────────
print(f"\n{'='*62}")
print(f"  DROPOUT CASCADE — average 20-24 cohort completion rates")
print(f"{'='*62}")
print(f"  (shows what fraction of each cohort reaches each level)")
for year in [1960, 1980, 2000, 2015]:
    vals = {}
    for level, (_, direction) in EDU_LEVELS.items():
        col = f"{level}_{year}" if year in [1960, 2015] else None
        if col and col in summary.columns:
            v = summary[col].dropna().mean()
        else:
            # compute on the fly
            v = np.nanmean([get_val(edu_dfs[level], c, year) for c in common])
        vals[level] = v

    # Convert OL (or less) to "still at this level" by differencing
    stuck_below  = vals["In_Primary_OL"]
    stuck_primary = vals["Primary_OL"] - vals["In_Primary_OL"]
    stuck_lower  = vals["Lower_Secondary_OL"] - vals["Primary_OL"]
    completed_higher = vals["Higher_Secondary"]
    # rough: rest = lower secondary finished but not higher
    finished_lower_only = 100 - vals["Lower_Secondary_OL"] - completed_higher

    print(f"\n  Year {year}:")
    print(f"    Never completed primary:        {stuck_below:5.1f}%")
    print(f"    Primary only (stopped there):   {stuck_primary:5.1f}%")
    print(f"    Lower secondary only:           {stuck_lower:5.1f}%")
    print(f"    Finished lower sec, not higher: {max(finished_lower_only,0):5.1f}%")
    print(f"    Completed higher secondary:     {completed_higher:5.1f}%")

# ── Top 20 fastest improvers at each level ────────────────────────────────────
def show_top(level, n=20):
    col = f"{level}_improvement"
    df  = summary[[f"{level}_1960", f"{level}_2015", col,
                   "gdp_1960", "gdp_2015", "gdp_growth"]].dropna()
    df  = df.sort_values(col, ascending=False).head(n)

    print(f"\n{'='*72}")
    print(f"  TOP {n} FASTEST IMPROVERS — {level}")
    direction = EDU_LEVELS[level][1]
    print(f"  (improvement = {'decrease in OL %' if direction=='decrease' else 'increase in completion %'})")
    print(f"{'='*72}")
    print(f"  {'Country':<28} {'Start':>6} {'End':>6} {'Δ':>7}  {'GDP 1960':>9} {'GDP 2015':>9} {'GDP×':>6}")
    print(f"  {'-'*28} {'-'*6} {'-'*6} {'-'*7}  {'-'*9} {'-'*9} {'-'*6}")
    for country, r in df.iterrows():
        print(f"  {country:<28} {r[f'{level}_1960']:>6.1f} {r[f'{level}_2015']:>6.1f} "
              f"{r[col]:>7.1f}  "
              f"{r['gdp_1960']:>9.0f} {r['gdp_2015']:>9.0f} {r['gdp_growth']:>6.1f}x")

for level in EDU_LEVELS:
    show_top(level)

# ── Correlation: does starting GDP predict education improvement? ─────────────
print(f"\n{'='*62}")
print(f"  CORRELATION: starting GDP vs education improvement (1960-2015)")
print(f"{'='*62}")
for level in EDU_LEVELS:
    col = f"{level}_improvement"
    df  = summary[[col, "gdp_1960"]].dropna()
    corr = df[col].corr(df["gdp_1960"])
    corr_log = df[col].corr(np.log1p(df["gdp_1960"]))
    print(f"  {level:<28}  r={corr:+.3f}  r(log GDP)={corr_log:+.3f}")

print(f"\n{'='*62}")
print(f"  CORRELATION: GDP growth vs education improvement")
print(f"{'='*62}")
for level in EDU_LEVELS:
    col = f"{level}_improvement"
    df  = summary[[col, "gdp_growth"]].dropna()
    corr = df[col].corr(df["gdp_growth"])
    corr_log = df[col].corr(np.log1p(df["gdp_growth"]))
    print(f"  {level:<28}  r={corr:+.3f}  r(log GDP growth)={corr_log:+.3f}")
