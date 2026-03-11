"""
College completion and full-ladder generational transmission analysis.

Questions:
1. Was the tiger saturation a whole-ladder phenomenon (not just primary)?
   Show within-country variance at each level for tigers vs non-tigers.

2. Does generational transmission hold for college completion?
   College(T) ~ UpperSec(T-25) or College(T-25)?

3. Since tigers' college is NOT saturated (Korea: 23→67%), does the
   FE mechanism re-emerge at the college level?

4. Ladder propagation: does each level transmit to the level above?
   Primary(T-25) → LowerSec(T)
   LowerSec(T-25) → UpperSec(T)
   UpperSec(T-25) → College(T)
   College(T-25) → College(T)  [within-generation reproduction]
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

ROOT = "datasets/"
PARENTAL_LAG = 25
SCHOOLING_LAG = 12
TIGERS = ["south korea", "singapore", "malaysia", "thailand"]

def load(path):
    df = pd.read_csv(path)
    df["Country"] = df["Country"].str.lower()
    return df.set_index("Country")

print("Loading data...")
dfs = {
    "Primary_OL":         load(ROOT + "Primary_OL.csv"),
    "Lower_Secondary_OL": load(ROOT + "Lower_Secondary_OL.csv"),
    "Upper_Secondary_OL": load(ROOT + "Upper_Secondary_OL.csv"),
    "College":            load(ROOT + "College_comp.csv"),
    "female_Primary_OL":  load(ROOT + "female_Primary_OL.csv"),
    "gdp":                load(ROOT + "gdppercapita_us_inflation_adjusted.csv"),
}

all_countries = sorted(
    set(dfs["gdp"].index) &
    set(dfs["Primary_OL"].index) &
    set(dfs["Lower_Secondary_OL"].index)
)

def get(name, country, year):
    try:
        return float(dfs[name].loc[country, str(year)])
    except (KeyError, ValueError):
        return np.nan

def comp(ol): return 100 - ol  # out-of-level → completion

def ols(X, y):
    reg = LinearRegression().fit(X, y)
    return reg, reg.score(X, y)

def demean(df, col):
    return df[col] - df.groupby("country")[col].transform("mean")

def twoway_demean(df, col):
    cmeans = df.groupby("country")[col].transform("mean")
    ymeans = df.groupby("year")[col].transform("mean")
    return df[col] - cmeans - ymeans + df[col].mean()


# ─────────────────────────────────────────────────────────────────────────────
# BUILD FULL LADDER PANEL
# ─────────────────────────────────────────────────────────────────────────────
print("Building full-ladder panel (1985–2015)...")
rows = []
for country in all_countries:
    for yr in range(1985, 2016):
        pri   = comp(get("Primary_OL",         country, yr))
        low   = comp(get("Lower_Secondary_OL", country, yr))
        upper = comp(get("Upper_Secondary_OL", country, yr))
        col   = get("College", country, yr)          # already a completion %
        gdp   = get("gdp",     country, yr - SCHOOLING_LAG)

        par_pri   = comp(get("Primary_OL",         country, yr - PARENTAL_LAG))
        par_low   = comp(get("Lower_Secondary_OL", country, yr - PARENTAL_LAG))
        par_upper = comp(get("Upper_Secondary_OL", country, yr - PARENTAL_LAG))
        par_col   = get("College", country, yr - PARENTAL_LAG)
        par_f_pri = comp(get("female_Primary_OL",  country, yr - PARENTAL_LAG))

        if any(np.isnan(v) for v in [pri, par_pri, gdp]):
            continue

        rows.append({
            "country": country, "year": yr,
            "pri": pri, "low": low, "upper": upper, "col": col,
            "par_pri": par_pri, "par_low": par_low,
            "par_upper": par_upper, "par_col": par_col,
            "par_f_pri": par_f_pri,
            "log_gdp": np.log(gdp) if gdp > 0 else np.nan,
            "is_tiger": 1 if country in TIGERS else 0,
        })

panel = pd.DataFrame(rows)
print(f"  Full panel: {len(panel)} obs, {panel['country'].nunique()} countries")
college_panel = panel.dropna(subset=["col", "par_upper", "log_gdp"])
print(f"  College sub-panel: {len(college_panel)} obs, {college_panel['country'].nunique()} countries\n")


# ═══════════════════════════════════════════════════════════════════════════
print("=" * 68)
print("  SECTION 1: WITHIN-COUNTRY VARIANCE AT EACH LADDER LEVEL")
print("  Tigers vs Non-tigers — how much within-country variation")
print("  remains at each level? Saturation = low within-variance.")
print("=" * 68)

print(f"\n  {'Level':<15}  {'Group':<12}  {'Mean':>6}  {'Within-SD':>9}  {'Between-SD':>10}  {'Within%':>8}")
print(f"  {'-'*15}  {'-'*12}  {'-'*6}  {'-'*9}  {'-'*10}  {'-'*8}")

for level, col in [("Primary", "pri"), ("Lower Sec", "low"),
                   ("Upper Sec", "upper"), ("College", "col")]:
    for group_name, mask in [("Tigers", panel["is_tiger"] == 1),
                              ("Non-tigers", panel["is_tiger"] == 0)]:
        sub = panel[mask].dropna(subset=[col])
        if len(sub) < 10:
            continue
        country_means = sub.groupby("country")[col].transform("mean")
        within_sd  = (sub[col] - country_means).std()
        between_sd = country_means.groupby(sub["country"]).first().std()
        total_var  = sub[col].var()
        within_pct = (sub[col] - country_means).var() / total_var * 100 if total_var > 0 else 0
        print(f"  {level:<15}  {group_name:<12}  {sub[col].mean():>6.1f}  {within_sd:>9.2f}  {between_sd:>10.2f}  {within_pct:>7.1f}%")


# ═══════════════════════════════════════════════════════════════════════════
print(f"\n{'='*68}")
print(f"  SECTION 2: FULL LADDER — GENERATIONAL TRANSMISSION")
print(f"  Each rung tests: does parental level predict child level,")
print(f"  controlling for GDP, within countries?")
print(f"  Primary(T-25)→Pri(T),  LowSec(T-25)→LowSec(T), etc.")
print(f"{'='*68}")

ladder_tests = [
    ("Primary → Primary",           "pri",   "par_pri",   "log_gdp"),
    ("LowerSec → LowerSec",         "low",   "par_low",   "log_gdp"),
    ("UpperSec → UpperSec",         "upper", "par_upper", "log_gdp"),
    ("College → College",           "col",   "par_col",   "log_gdp"),
    # Cross-level: does prev level transmit to the next?
    ("Primary(T-25) → LowSec(T)",   "low",   "par_pri",   "log_gdp"),
    ("LowSec(T-25) → UpperSec(T)",  "upper", "par_low",   "log_gdp"),
    ("UpperSec(T-25) → College(T)", "col",   "par_upper", "log_gdp"),
]

print(f"\n  {'Transmission path':<30}  {'n':>5}  {'Pool-par':>8}  {'FE-par':>6}  {'FE-gdp':>6}  {'FE-both':>7}  {'Incr-par':>8}")
print(f"  {'-'*30}  {'-'*5}  {'-'*8}  {'-'*6}  {'-'*6}  {'-'*7}  {'-'*8}")

for label, child_col, par_col, gdp_col in ladder_tests:
    sub = panel.dropna(subset=[child_col, par_col, gdp_col])
    if len(sub) < 50:
        print(f"  {label:<30}  insufficient data")
        continue
    _, r2_pool = ols(sub[[par_col]].values, sub[child_col].values)

    s2 = sub.copy()
    for c in [child_col, par_col, gdp_col]:
        s2[c+"_dm"] = demean(s2, c)
    _, r2_fe_par  = ols(s2[[par_col+"_dm"]].values,              s2[child_col+"_dm"].values)
    _, r2_fe_gdp  = ols(s2[[gdp_col+"_dm"]].values,              s2[child_col+"_dm"].values)
    _, r2_fe_both = ols(s2[[par_col+"_dm", gdp_col+"_dm"]].values, s2[child_col+"_dm"].values)
    print(f"  {label:<30}  {len(sub):>5}  {r2_pool:>8.3f}  {r2_fe_par:>6.3f}  {r2_fe_gdp:>6.3f}  {r2_fe_both:>7.3f}  {r2_fe_both-r2_fe_gdp:>8.3f}")


# ═══════════════════════════════════════════════════════════════════════════
print(f"\n{'='*68}")
print(f"  SECTION 3: COLLEGE TRANSMISSION — TIGERS vs NON-TIGERS")
print(f"  Korea's college went 23%→67% (1985→2015) — not saturated.")
print(f"  Does the FE mechanism re-emerge at college level for tigers?")
print(f"{'='*68}")

for group_name, mask in [
    ("All countries",   panel["col"].notna()),
    ("Tigers",          (panel["is_tiger"] == 1) & panel["col"].notna()),
    ("Non-tigers",      (panel["is_tiger"] == 0) & panel["col"].notna()),
]:
    sub = panel[mask].dropna(subset=["col", "par_upper", "par_col", "log_gdp"])
    if len(sub) < 20:
        print(f"\n  {group_name}: insufficient data (n={len(sub)})")
        continue

    s2 = sub.copy()
    for c in ["col", "par_upper", "par_col", "log_gdp"]:
        s2[c+"_dm"] = demean(s2, c)

    _, r2_pu  = ols(s2[["par_upper_dm"]].values, s2["col_dm"].values)
    _, r2_pc  = ols(s2[["par_col_dm"]].values,   s2["col_dm"].values)
    _, r2_g   = ols(s2[["log_gdp_dm"]].values,   s2["col_dm"].values)
    _, r2_pub = ols(s2[["par_upper_dm","log_gdp_dm"]].values, s2["col_dm"].values)
    _, r2_pcb = ols(s2[["par_col_dm","log_gdp_dm"]].values,   s2["col_dm"].values)

    reg_pu, _ = ols(s2[["par_upper_dm","log_gdp_dm"]].values, s2["col_dm"].values)
    reg_pc, _ = ols(s2[["par_col_dm","log_gdp_dm"]].values,   s2["col_dm"].values)

    print(f"\n  {group_name}  (n={len(sub)}, {sub['country'].nunique()} countries):")
    print(f"    FE — UpperSec parental(T-25) only:    R² = {r2_pu:.3f}")
    print(f"    FE — College parental(T-25) only:     R² = {r2_pc:.3f}")
    print(f"    FE — GDP only:                        R² = {r2_g:.3f}")
    print(f"    FE — UpperSec parental + GDP:         R² = {r2_pub:.3f}  (incr.parental +{r2_pub-r2_g:.3f})")
    print(f"    FE — College parental + GDP:          R² = {r2_pcb:.3f}  (incr.parental +{r2_pcb-r2_g:.3f})")
    print(f"    Coef: 1pp UpperSec(T-25) → {reg_pu.coef_[0]:.3f}pp College  |  1% GDP → {reg_pu.coef_[1]:.3f}pp College")
    print(f"    Coef: 1pp College(T-25)  → {reg_pc.coef_[0]:.3f}pp College  |  1% GDP → {reg_pc.coef_[1]:.3f}pp College")


# ═══════════════════════════════════════════════════════════════════════════
print(f"\n{'='*68}")
print(f"  SECTION 4: SIMULTANEOUS LADDER COMPRESSION — TIGER SIGNATURE")
print(f"  For each year, show the gap between primary and lower secondary")
print(f"  completion. Non-tigers show large Pri→LowSec gap (sequential).")
print(f"  Tigers show small gap (simultaneous). Does this hold?")
print(f"{'='*68}")

print(f"\n  {'Country':<15}  {'Year':>5}  {'Pri%':>6}  {'LowSec%':>8}  {'UpSec%':>7}  {'College%':>9}  {'Pri-LowSec gap':>14}")
for c in TIGERS + ["china", "india", "ghana", "brazil"]:
    for yr in [1980, 1990, 2000, 2010, 2015]:
        pri   = comp(get("Primary_OL",         c, yr))
        low   = comp(get("Lower_Secondary_OL", c, yr))
        upper = comp(get("Upper_Secondary_OL", c, yr))
        col   = get("College", c, yr)
        if np.isnan(pri) or np.isnan(low):
            continue
        gap = pri - low
        col_str = f"{col:.1f}%" if not np.isnan(col) else "  n/a"
        upper_str = f"{upper:.1f}%" if not np.isnan(upper) else "  n/a"
        print(f"  {c:<15}  {yr:>5}  {pri:>5.1f}%  {low:>7.1f}%  {upper_str:>7}  {col_str:>9}  {gap:>+13.1f}pp")
    print()


# ═══════════════════════════════════════════════════════════════════════════
print(f"\n{'='*68}")
print(f"  SECTION 5: WITHIN-TIGER VARIANCE AT COLLEGE LEVEL")
print(f"  College completion has substantial room to grow in tigers.")
print(f"  Does the primary-level FE anomaly (coef≈0) reverse at college?")
print(f"  Compare FE college coefficients: tigers vs non-tigers")
print(f"{'='*68}")

# Show within-tiger variance in college vs primary
tiger_panel = panel[panel["is_tiger"] == 1].dropna(subset=["col","par_upper","log_gdp"])
for c in TIGERS:
    sub = panel[(panel["country"] == c)].dropna(subset=["col","pri"])
    if len(sub) == 0:
        continue
    pri_range  = sub["pri"].max()  - sub["pri"].min()
    col_range  = sub["col"].max()  - sub["col"].min() if sub["col"].notna().any() else np.nan
    low_range  = sub["low"].max()  - sub["low"].min() if sub["low"].notna().any() else np.nan
    print(f"\n  {c}:")
    print(f"    Primary   range 1985–2015: {pri_range:.1f}pp  (little within-country variation to exploit)")
    if not np.isnan(low_range):
        print(f"    LowerSec  range 1985–2015: {low_range:.1f}pp")
    if not np.isnan(col_range):
        print(f"    College   range 1985–2015: {col_range:.1f}pp  (this is where the action is)")


# ═══════════════════════════════════════════════════════════════════════════
print(f"\n{'='*68}")
print(f"  SUMMARY")
print(f"{'='*68}")

# Quick comparison table across all levels and groups
print(f"\n  Country FE R² — generational transmission by level and group:")
print(f"\n  {'Level (same→same)':<25}  {'All':>5}  {'Tigers':>7}  {'Non-tigers':>10}")
print(f"  {'-'*25}  {'-'*5}  {'-'*7}  {'-'*10}")

for label, child_col, par_col in [
    ("Primary → Primary",      "pri",   "par_pri"),
    ("LowerSec → LowerSec",    "low",   "par_low"),
    ("UpperSec → UpperSec",    "upper", "par_upper"),
    ("College → College",      "col",   "par_col"),
    ("UpperSec(T-25)→College", "col",   "par_upper"),
]:
    row_vals = []
    for mask in [panel["col"].notna() | True,   # all
                 panel["is_tiger"] == 1,
                 panel["is_tiger"] == 0]:
        sub = panel[mask].dropna(subset=[child_col, par_col, "log_gdp"])
        if len(sub) < 20:
            row_vals.append("  n/a")
            continue
        s2 = sub.copy()
        for c in [child_col, par_col, "log_gdp"]:
            s2[c+"_dm"] = demean(s2, c)
        _, r2 = ols(s2[[par_col+"_dm"]].values, s2[child_col+"_dm"].values)
        row_vals.append(f"{r2:.3f}")
    print(f"  {label:<25}  {row_vals[0]:>5}  {row_vals[1]:>7}  {row_vals[2]:>10}")
