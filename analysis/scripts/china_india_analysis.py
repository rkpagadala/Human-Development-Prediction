"""
China vs India: does the "education as policy outcome, unrelated to GDP
when kids were growing up" theory hold?

The 20-24 cohort in year T was aged 5-15 roughly at year T-12 (midpoint).
If education is a policy outcome, education(T) should NOT be explained by
GDP(T-12) — the economy when those children were in school.

Tests:
  1. Across all countries: how well does GDP(T-12) predict education(T)?
     If education were purely economic, this should be strong.
  2. China and India residuals: after removing the global GDP(T-12) → edu
     relationship, how far above/below expectation are each country?
  3. Decade-by-decade: China vs India education vs GDP vs TFR vs life exp
  4. Policy discontinuities: do education jumps in China align with
     known policy events rather than GDP growth?
  5. Gender gap: does the one-child policy show up in female education
     differently in China vs India?
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

ROOT = "datasets/"

DATASETS = {
    "Primary_OL":           ROOT + "Primary_OL.csv",
    "Lower_Secondary_OL":   ROOT + "Lower_Secondary_OL.csv",
    "Higher_Secondary":     ROOT + "Higher_Secondary_fin_complete.csv",
    "female_Primary_OL":    ROOT + "female_Primary_OL.csv",
    "female_Lower_Sec_OL":  ROOT + "female_Lower_Secondary_OL.csv",
    "gdp":                  ROOT + "gdppercapita_us_inflation_adjusted.csv",
    "tfr":                  ROOT + "children_per_woman_total_fertility.csv",
    "life_expectancy":      ROOT + "life_expectancy_years.csv",
    "infant_mortality":     ROOT + "Infant_Mortality_Rate.csv",
}

def load(path):
    df = pd.read_csv(path)
    df["Country"] = df["Country"].str.lower()
    return df.set_index("Country")

print("Loading data...")
dfs = {name: load(path) for name, path in DATASETS.items()}

def get(name, country, year):
    try:
        return float(dfs[name].loc[country, str(year)])
    except (KeyError, ValueError):
        return np.nan

def comp(ol): return 100 - ol  # convert "or less" to "reached at least"

YEARS_5 = list(range(1960, 2016, 5))
LAG = 12  # years between schooling age and 20-24 cohort measurement

# ── 1. Build global panel: education(T) vs GDP(T-LAG) ────────────────────────
print("Building global panel...")
all_countries = list(dfs["gdp"].index)
rows = []
for country in all_countries:
    for yr in range(1972, 2016):  # need LAG years back
        edu = comp(get("Lower_Secondary_OL", country, yr))
        gdp_lag = get("gdp", country, yr - LAG)
        if not (np.isnan(edu) or np.isnan(gdp_lag)):
            rows.append({"country": country, "year": yr,
                         "edu": edu, "gdp_lag": gdp_lag,
                         "log_gdp_lag": np.log(gdp_lag) if gdp_lag > 0 else np.nan})

panel = pd.DataFrame(rows).dropna()

# Fit global model: log(GDP at schooling age) → lower secondary completion
X = panel[["log_gdp_lag"]].values
y = panel["edu"].values
reg = LinearRegression().fit(X, y)
panel["edu_predicted"] = reg.predict(X)
panel["residual"] = panel["edu"] - panel["edu_predicted"]

r2 = reg.score(X, y)

print(f"\n{'='*64}")
print(f"  SECTION 1: Global model — does GDP(T-{LAG}) predict education(T)?")
print(f"{'='*64}")
print(f"  Target: lower secondary completion (20-24 cohort)")
print(f"  Predictor: log(GDP per capita {LAG} years earlier)")
print(f"  Countries: {panel['country'].nunique()}  |  Observations: {len(panel)}")
print(f"  R² = {r2:.3f}  (1.0 = perfectly predicted by lagged GDP)")
print(f"  Coefficient: +{reg.coef_[0]:.2f}pp per doubling of lagged GDP")
print(f"\n  Interpretation:")
if r2 < 0.3:
    print(f"  WEAK — lagged GDP explains only {r2*100:.0f}% of education variation.")
    print(f"  Education is largely NOT determined by GDP at schooling age.")
elif r2 < 0.6:
    print(f"  MODERATE — lagged GDP explains {r2*100:.0f}% of education variation.")
else:
    print(f"  STRONG — lagged GDP explains {r2*100:.0f}% of education variation.")

# ── 2. China and India residuals over time ────────────────────────────────────
print(f"\n{'='*64}")
print(f"  SECTION 2: China vs India — education ABOVE/BELOW what GDP predicts")
print(f"  Positive residual = better educated than GDP(T-{LAG}) would expect")
print(f"{'='*64}")

print(f"\n  {'Year':>5}  {'China edu':>10} {'China pred':>11} {'China res':>10}  "
      f"{'India edu':>10} {'India pred':>11} {'India res':>10}")
print(f"  {'-'*5}  {'-'*10} {'-'*11} {'-'*10}  {'-'*10} {'-'*11} {'-'*10}")

china_res, india_res = [], []
for yr in YEARS_5:
    if yr < 1972: continue
    c_edu = comp(get("Lower_Secondary_OL", "china", yr))
    i_edu = comp(get("Lower_Secondary_OL", "india", yr))
    c_gdp = get("gdp", "china", yr - LAG)
    i_gdp = get("gdp", "india", yr - LAG)

    def predict(gdp):
        if np.isnan(gdp) or gdp <= 0: return np.nan
        return reg.predict([[np.log(gdp)]])[0]

    c_pred = predict(c_gdp)
    i_pred = predict(i_gdp)
    c_res  = c_edu - c_pred if not np.isnan(c_pred) else np.nan
    i_res  = i_edu - i_pred if not np.isnan(i_pred) else np.nan

    china_res.append(c_res)
    india_res.append(i_res)

    print(f"  {yr:>5}  {c_edu:>9.1f}% {c_pred:>10.1f}% {c_res:>+9.1f}pp  "
          f"{i_edu:>9.1f}% {i_pred:>10.1f}% {i_res:>+9.1f}pp")

c_avg = np.nanmean(china_res)
i_avg = np.nanmean(india_res)
print(f"\n  Average residual  China: {c_avg:>+6.1f}pp   India: {i_avg:>+6.1f}pp")

# ── 3. Decade comparison: all indicators side by side ────────────────────────
print(f"\n{'='*90}")
print(f"  SECTION 3: China vs India — full indicator comparison")
print(f"{'='*90}")

for country in ["china", "india"]:
    print(f"\n  ── {country.upper()} ──")
    print(f"  {'Year':>5}  {'≥Primary':>9} {'≥LowSec':>8} {'≥HiSec':>7}  "
          f"{'fml≥Pri':>8} {'fml≥Low':>8}  "
          f"{'GDP':>7}  {'GDP lag':>8}  {'TFR':>5}  {'LE':>6}  {'InfMrt':>7}")
    print(f"  {'-'*5}  {'-'*9} {'-'*8} {'-'*7}  "
          f"{'-'*8} {'-'*8}  "
          f"{'-'*7}  {'-'*8}  {'-'*5}  {'-'*6}  {'-'*7}")
    for yr in YEARS_5:
        pri  = comp(get("Primary_OL",         country, yr))
        low  = comp(get("Lower_Secondary_OL", country, yr))
        high = get("Higher_Secondary",         country, yr)
        fpri = comp(get("female_Primary_OL",  country, yr))
        flow = comp(get("female_Lower_Sec_OL",country, yr))
        gdp  = get("gdp",                     country, yr)
        gdpl = get("gdp",                     country, yr - LAG)
        tfr  = get("tfr",                     country, yr)
        le   = get("life_expectancy",          country, yr)
        im   = get("infant_mortality",         country, yr)
        if np.isnan(high): high = 0
        print(f"  {yr:>5}  {pri:>8.1f}% {low:>7.1f}% {high:>6.1f}%  "
              f"{fpri:>7.1f}% {flow:>7.1f}%  "
              f"{gdp:>7.0f}  {gdpl:>8.0f}  {tfr:>5.2f}  {le:>6.1f}  {im:>7.1f}")

# ── 4. Policy discontinuities: year-on-year change in lower secondary ─────────
print(f"\n{'='*64}")
print(f"  SECTION 4: Annual change in lower secondary completion")
print(f"  (policy shifts should show as sudden accelerations)")
print(f"  Key events: China — Great Leap Forward ~1960, Cultural Revolution")
print(f"  1966-76, Deng reforms 1978, One-Child Policy 1980")
print(f"  India  — 5-year plans, RTE Act 2009")
print(f"{'='*64}")

print(f"\n  {'Year':>5}  {'China ≥LowSec':>14}  {'Δ China':>8}  "
      f"{'India ≥LowSec':>14}  {'Δ India':>8}  {'China GDP':>10}  {'India GDP':>10}")
prev_c = prev_i = None
for yr in range(1960, 2016):
    c = comp(get("Lower_Secondary_OL", "china", yr))
    i = comp(get("Lower_Secondary_OL", "india", yr))
    c_gdp = get("gdp", "china", yr)
    i_gdp = get("gdp", "india", yr)
    dc = (c - prev_c) if prev_c is not None and not np.isnan(c) else np.nan
    di = (i - prev_i) if prev_i is not None and not np.isnan(i) else np.nan

    # flag large acceleration years
    flag = ""
    if not np.isnan(dc) and abs(dc) > 0.8: flag += " ◄ CHINA JUMP"
    if not np.isnan(di) and abs(di) > 0.8: flag += " ◄ INDIA JUMP"

    if yr % 5 == 0 or flag:
        print(f"  {yr:>5}  {c:>13.1f}%  {dc:>+7.2f}pp  "
              f"{i:>13.1f}%  {di:>+7.2f}pp  "
              f"{c_gdp:>10.0f}  {i_gdp:>10.0f}{flag}")
    prev_c, prev_i = c, i

# ── 5. Female vs male gap: one-child policy effect ───────────────────────────
print(f"\n{'='*64}")
print(f"  SECTION 5: Female education gap — China vs India")
print(f"  (one-child policy 1980 → did it close or widen the gap?)")
print(f"{'='*64}")

print(f"\n  {'Year':>5}  {'China f-gap Pri':>16}  {'China f-gap Low':>16}  "
      f"{'India f-gap Pri':>16}  {'India f-gap Low':>16}")
for yr in YEARS_5:
    for country, label in [("china","China"), ("india","India")]:
        pass

print(f"  {'Year':>5}  {'CHN gap Pri':>12} {'CHN gap Low':>12}  "
      f"{'IND gap Pri':>12} {'IND gap Low':>12}")
print(f"  {'-'*5}  {'-'*12} {'-'*12}  {'-'*12} {'-'*12}")
for yr in YEARS_5:
    c_pri_gap = comp(get("female_Primary_OL","china",yr))  - comp(get("Primary_OL","china",yr))
    c_low_gap = comp(get("female_Lower_Sec_OL","china",yr))- comp(get("Lower_Secondary_OL","china",yr))
    i_pri_gap = comp(get("female_Primary_OL","india",yr))  - comp(get("Primary_OL","india",yr))
    i_low_gap = comp(get("female_Lower_Sec_OL","india",yr))- comp(get("Lower_Secondary_OL","india",yr))
    print(f"  {yr:>5}  {c_pri_gap:>+11.1f}pp {c_low_gap:>+11.1f}pp  "
          f"{i_pri_gap:>+11.1f}pp {i_low_gap:>+11.1f}pp")

print(f"\n  Note: One-child policy introduced 1980.")
print(f"  If it reduced female education: gap should widen post-1980.")
print(f"  If it increased investment in only child: gap should close post-1980.")
