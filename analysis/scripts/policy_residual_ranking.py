"""
Policy-adjusted education ranking.

Question: which countries delivered MORE education than their income level
and parental education history predict?

This is the ranking that separates structural luck (rich parents, strong
colonial school infrastructure) from deliberate policy investment.

Method:
  For each country-year, regress lower secondary completion on:
    - parental lower secondary (T-25)
    - log GDP per capita
  The residual = actual - predicted = policy over/under-performance.

  Countries are ranked by their average residual across the panel,
  and by their 2015 residual specifically.

We use lower secondary as the target because:
  - It is the policy-critical level (leapfrog thesis)
  - Primary is near-saturated in many countries, compressing variance
  - College is too thin in most developing countries pre-2000

Outputs: analysis/policy_residual_ranking.md
"""

import os
import warnings
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

warnings.filterwarnings("ignore")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(SCRIPT_DIR, "../../datasets/")
OUT_MD = os.path.join(SCRIPT_DIR, "../policy_residual_ranking.md")

OBS_YEARS = ["1960","1965","1970","1975","1980","1985","1990","1995","2000","2005","2010","2015"]

def load_comp(path, is_ol=True):
    df = pd.read_csv(path)
    df["Country"] = df["Country"].str.lower()
    df = df.set_index("Country")
    for c in df.columns:
        df[c] = 100 - pd.to_numeric(df[c], errors="coerce") if is_ol else pd.to_numeric(df[c], errors="coerce")
    return df

def load_raw(path):
    df = pd.read_csv(path)
    df["Country"] = df["Country"].str.lower()
    df = df.set_index("Country")
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

print("Loading data...")
low  = load_comp(ROOT + "Lower_Secondary_OL.csv", is_ol=True)
pri  = load_comp(ROOT + "Primary_OL.csv",         is_ol=True)
gdp  = load_raw(ROOT + "gdppercapita_us_inflation_adjusted.csv")

def v(df, c, yr):
    try:
        val = float(df.loc[c, str(yr)])
        return val if not np.isnan(val) else np.nan
    except:
        return np.nan

# Build panel: target = lower sec at T, predictors = lower sec at T-25 + log GDP at T
panel_rows = []
countries = sorted(set(low.index) & set(gdp.index) & set(pri.index))

for c in countries:
    for yr in OBS_YEARS:
        yr_int = int(yr)
        parent_yr = str(yr_int - 25)
        child_low  = v(low, c, yr)
        parent_low = v(low, c, parent_yr)
        gdp_val    = v(gdp, c, yr)
        pri_val    = v(pri, c, yr)

        if any(np.isnan(x) for x in [child_low, parent_low, gdp_val]):
            continue
        if gdp_val <= 0:
            continue

        panel_rows.append({
            "country": c,
            "year": yr_int,
            "child_low": child_low,
            "parent_low": parent_low,
            "log_gdp": np.log(gdp_val),
            "pri": pri_val,
        })

panel = pd.DataFrame(panel_rows)
print(f"  Panel: {len(panel)} obs, {panel['country'].nunique()} countries")

# ── Country fixed effects regression ─────────────────────────────────────────
# Demean within country (FE)
panel["child_low_dm"]  = panel["child_low"]  - panel.groupby("country")["child_low"].transform("mean")
panel["parent_low_dm"] = panel["parent_low"] - panel.groupby("country")["parent_low"].transform("mean")
panel["log_gdp_dm"]    = panel["log_gdp"]    - panel.groupby("country")["log_gdp"].transform("mean")

X_fe = panel[["parent_low_dm","log_gdp_dm"]].values
y_fe = panel["child_low_dm"].values
ok   = ~np.isnan(X_fe).any(axis=1) & ~np.isnan(y_fe)
reg_fe = LinearRegression(fit_intercept=False).fit(X_fe[ok], y_fe[ok])
panel.loc[ok, "fitted_dm"] = reg_fe.predict(X_fe[ok])

# Reconstruct level-fitted values: add back country mean of child + fitted demeaned
panel["child_mean"] = panel.groupby("country")["child_low"].transform("mean")
panel["fitted"]     = panel["child_mean"] + panel["fitted_dm"].fillna(0)
panel["residual"]   = panel["child_low"] - panel["fitted"]

print(f"  FE coefs: parental={reg_fe.coef_[0]:.3f}, log_gdp={reg_fe.coef_[1]:.3f}")

# ── Pooled OLS residual (for comparison) ──────────────────────────────────────
X_ols = panel[["parent_low","log_gdp"]].values
y_ols = panel["child_low"].values
ok2   = ~np.isnan(X_ols).any(axis=1) & ~np.isnan(y_ols)
reg_ols = LinearRegression().fit(X_ols[ok2], y_ols[ok2])
panel.loc[ok2, "fitted_ols"] = reg_ols.predict(X_ols[ok2])
panel["resid_ols"] = panel["child_low"] - panel["fitted_ols"]

# ── Country-level summaries ───────────────────────────────────────────────────
# 1. Mean residual across all years (chronic over/under-performance)
# 2. Most recent (2015) residual
summary_rows = []
for c, grp in panel.groupby("country"):
    grp15 = grp[grp["year"] == 2015]
    resid_2015    = grp15["residual"].values[0]    if len(grp15) > 0 and not grp15["residual"].isna().all()    else np.nan
    resid_ols2015 = grp15["resid_ols"].values[0]   if len(grp15) > 0 and not grp15["resid_ols"].isna().all()  else np.nan

    low2015 = grp15["child_low"].values[0] if len(grp15) > 0 else np.nan
    pri2015 = grp15["pri"].values[0]        if len(grp15) > 0 else np.nan
    gdp2015 = np.exp(grp15["log_gdp"].values[0]) if len(grp15) > 0 and not grp15["log_gdp"].isna().all() else np.nan

    mean_resid     = grp["residual"].mean()
    mean_resid_ols = grp["resid_ols"].mean()

    summary_rows.append({
        "country": c,
        "resid_fe_2015":   resid_2015,
        "resid_ols_2015":  resid_ols2015,
        "mean_resid_fe":   mean_resid,
        "mean_resid_ols":  mean_resid_ols,
        "low_2015": low2015,
        "pri_2015": pri2015,
        "gdp_2015": gdp2015,
    })

sdf = pd.DataFrame(summary_rows)

def cn(name, maxlen=32): return name.title()[:maxlen]
def pct(val): return f"{val:.1f}%" if not np.isnan(val) else "n/a"
def pp(val):
    if np.isnan(val): return "n/a"
    return f"+{val:.1f} pp" if val >= 0 else f"{val:.1f} pp"
def gdp_fmt(val): return f"${val:,.0f}" if not np.isnan(val) else "n/a"

# ── Report ────────────────────────────────────────────────────────────────────
lines = []
def h(t=""): lines.append(t)

def pipe_table(headers, rows_data, aligns=None):
    if aligns is None:
        aligns = ["left"] + ["right"] * (len(headers) - 1)
    def sep(a): return ":---" if a == "left" else "---:"
    h("| " + " | ".join(headers) + " |")
    h("| " + " | ".join(sep(a) for a in aligns) + " |")
    for r in rows_data:
        h("| " + " | ".join(str(x) for x in r) + " |")
    h()

h("# Policy-Adjusted Education Ranking")
h()
h("*Which countries delivered more lower-secondary education than their income and parental education predict?*")
h()
h("## Method")
h()
h("**Target:** lower secondary completion rate (% of 20–24 cohort) at year T")
h("**Predictors:** parental lower secondary completion at T−25, log GDP per capita at T")
h("**Model:** country fixed effects (within-country variation only)")
h()
h(f"Fixed effects coefficients:")
h(f"- Parental lower secondary: **{reg_fe.coef_[0]:.3f}** pp per 1 pp of parental completion")
h(f"- Log GDP: **{reg_fe.coef_[1]:.3f}** pp per 1% GDP")
h()
h("**Residual = actual − predicted.** Positive residual = country delivered more education than its")
h("income and parental history predict. This is the policy signal.")
h()
h("Two residuals are shown:")
h("- **FE residual**: within-country deviation — how much did the country outperform its own predicted trajectory?")
h("- **OLS residual**: cross-country deviation — how much did the country outperform the global prediction?")
h("The FE residual is more demanding: it asks whether the country accelerated beyond its own trend.")
h()
h("---")
h()

# Table 1: Top over-performers by 2015 FE residual
h("## Table 1 — Biggest Over-Performers in 2015 (FE Residual)")
h()
h("Countries whose lower secondary completion in 2015 most exceeded what their own")
h("historical trajectory and income level predict.")
h()
over = sdf.dropna(subset=["resid_fe_2015"]).sort_values("resid_fe_2015", ascending=False)
pipe_table(
    ["Rank","Country","Low Sec 2015","FE Residual","OLS Residual","GDP/capita 2015"],
    [[i+1, cn(r.country), pct(r.low_2015), pp(r.resid_fe_2015), pp(r.resid_ols_2015), gdp_fmt(r.gdp_2015)]
     for i, (_, r) in enumerate(over.head(30).iterrows())],
    ["right","left","right","right","right","right"]
)

# Table 2: Biggest under-performers
h("## Table 2 — Biggest Under-Performers in 2015 (FE Residual)")
h()
h("Countries whose lower secondary completion in 2015 most fell short of what their")
h("income and parental trajectory predict — structural failure or policy neglect.")
h()
under = sdf.dropna(subset=["resid_fe_2015"]).sort_values("resid_fe_2015")
pipe_table(
    ["Rank","Country","Low Sec 2015","FE Residual","OLS Residual","GDP/capita 2015"],
    [[i+1, cn(r.country), pct(r.low_2015), pp(r.resid_fe_2015), pp(r.resid_ols_2015), gdp_fmt(r.gdp_2015)]
     for i, (_, r) in enumerate(under.head(30).iterrows())],
    ["right","left","right","right","right","right"]
)

# Table 3: Chronic over-performers (average OLS residual across all years)
# Note: mean FE residual is zero by construction for every country (FE removes country mean).
# Chronic over-performance uses OLS residuals: how much did country X consistently outperform
# the global prediction based on income and parental education?
h("## Table 3 — Chronic Over-Performers (Mean OLS Residual Across All Years)")
h()
h("Countries that consistently outperformed the global cross-country prediction across all years.")
h("OLS residual = actual minus predicted by pooled model (income + parental education).")
h("This measures how much more education a country delivered than a country with the same income")
h("and parental history would deliver on average globally.")
h()
chronic_over = sdf.dropna(subset=["mean_resid_ols"]).sort_values("mean_resid_ols", ascending=False)
pipe_table(
    ["Rank","Country","Low Sec 2015","Mean OLS Residual","2015 OLS Residual","2015 FE Residual"],
    [[i+1, cn(r.country), pct(r.low_2015), pp(r.mean_resid_ols), pp(r.resid_ols_2015), pp(r.resid_fe_2015)]
     for i, (_, r) in enumerate(chronic_over.head(30).iterrows())],
    ["right","left","right","right","right","right"]
)

# Table 4: Chronic under-performers
h("## Table 4 — Chronic Under-Performers (Mean OLS Residual Across All Years)")
h()
h("Countries that consistently delivered less education than their income and parental history predict.")
h()
chronic_under = sdf.dropna(subset=["mean_resid_ols"]).sort_values("mean_resid_ols")
pipe_table(
    ["Rank","Country","Low Sec 2015","Mean OLS Residual","2015 OLS Residual","2015 FE Residual"],
    [[i+1, cn(r.country), pct(r.low_2015), pp(r.mean_resid_ols), pp(r.resid_ols_2015), pp(r.resid_fe_2015)]
     for i, (_, r) in enumerate(chronic_under.head(30).iterrows())],
    ["right","left","right","right","right","right"]
)

# Table 5: Full country ranking by 2015 FE residual
h("## Table 5 — Full Country Ranking by 2015 FE Residual")
h()
full = sdf.dropna(subset=["resid_fe_2015"]).sort_values("resid_fe_2015", ascending=False).reset_index(drop=True)
pipe_table(
    ["Rank","Country","Low Sec 2015","FE Residual","OLS Residual"],
    [[i+1, cn(r.country), pct(r.low_2015), pp(r.resid_fe_2015), pp(r.resid_ols_2015)]
     for i, r in full.iterrows()],
    ["right","left","right","right","right"]
)

h("---")
h()
h("*Method: country fixed effects regression of lower secondary completion on parental lower secondary (T−25) and log GDP.*")
h("*Residual represents within-country deviation from predicted trajectory.*")

with open(OUT_MD, "w") as f:
    f.write("\n".join(lines))
print(f"  Saved: {OUT_MD}")
print("Done.")
