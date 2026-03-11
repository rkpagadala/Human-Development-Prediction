"""
Deep analysis of East Asian education outliers: Singapore, South Korea,
Malaysia, Thailand, China — vs comparable countries that did NOT achieve
the same education trajectory.

Questions:
  1. Sequencing: did education lead GDP or follow it?
  2. Which education level moved first at each decade?
  3. How does TFR/life expectancy track alongside?
  4. Female vs total education — was female education the leading edge?
  5. Comparator countries: same starting GDP, different outcome
  6. Dropout gap: how much does each country lose at each transition?
"""

import pandas as pd
import numpy as np

ROOT = "datasets/"

DATASETS = {
    "In_Primary_OL":          ROOT + "In_Primary_OL.csv",
    "Primary_OL":             ROOT + "Primary_OL.csv",
    "Lower_Secondary_OL":     ROOT + "Lower_Secondary_OL.csv",
    "Higher_Secondary":       ROOT + "Higher_Secondary_fin_complete.csv",
    "female_Primary_OL":      ROOT + "female_Primary_OL.csv",
    "female_Lower_Sec_OL":    ROOT + "female_Lower_Secondary_OL.csv",
    "gdp":                    ROOT + "gdppercapita_us_inflation_adjusted.csv",
    "tfr":                    ROOT + "children_per_woman_total_fertility.csv",
    "life_expectancy":        ROOT + "life_expectancy_years.csv",
    "infant_mortality":       ROOT + "Infant_Mortality_Rate.csv",
    "gini":                   ROOT + "gini.csv",
}

FOCUS   = ["singapore", "south korea", "malaysia", "thailand", "china"]
# Comparators: similar 1960 GDP to each focus country but slower education growth
COMPARATORS = {
    "singapore":   ["jamaica", "venezuela", "argentina"],   # similar 1960 GDP ~3000-4000
    "south korea": ["ghana", "bolivia", "guatemala"],       # similar 1960 GDP ~500-1200
    "malaysia":    ["nigeria", "cameroon", "ecuador"],      # similar 1960 GDP ~1000-1500
    "thailand":    ["kenya", "senegal", "haiti"],           # similar 1960 GDP ~500-700
    "china":       ["india", "bangladesh", "pakistan"],     # similar 1960 GDP ~200-400
}
ALL_COUNTRIES = FOCUS + [c for lst in COMPARATORS.values() for c in lst]

YEARS_5 = list(range(1960, 2016, 5))

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

def completion_from_OL(ol_val):
    """Convert 'or less' % to 'reached at least this level' %"""
    return 100 - ol_val

# ── 1. Decade-by-decade timeline for each focus country ──────────────────────
print(f"\n{'='*90}")
print(f"  SECTION 1: Decade-by-decade education + GDP + TFR + life expectancy")
print(f"  Education shown as '% who reached AT LEAST this level'")
print(f"{'='*90}")

for country in FOCUS:
    print(f"\n  ── {country.upper()} ──")
    print(f"  {'Year':>5}  {'≥Primary':>9} {'≥LowerSec':>10} {'≥HigherSec':>11}  "
          f"{'fml≥Pri':>8} {'fml≥Low':>8}  {'GDP':>7}  {'TFR':>5}  {'LifeExp':>8}  {'InfMort':>8}")
    print(f"  {'-'*5}  {'-'*9} {'-'*10} {'-'*11}  {'-'*8} {'-'*8}  {'-'*7}  {'-'*5}  {'-'*8}  {'-'*8}")
    for yr in YEARS_5:
        pri    = completion_from_OL(get("Primary_OL",         country, yr))
        low    = completion_from_OL(get("Lower_Secondary_OL", country, yr))
        high   = get("Higher_Secondary",   country, yr)
        fpri   = completion_from_OL(get("female_Primary_OL",  country, yr))
        flow   = completion_from_OL(get("female_Lower_Sec_OL",country, yr))
        gdp    = get("gdp",                country, yr)
        tfr    = get("tfr",                country, yr)
        le     = get("life_expectancy",    country, yr)
        im     = get("infant_mortality",   country, yr)
        print(f"  {yr:>5}  {pri:>8.1f}% {low:>9.1f}% {high:>10.1f}%  "
              f"{fpri:>7.1f}% {flow:>7.1f}%  {gdp:>7.0f}  {tfr:>5.2f}  {le:>8.1f}  {im:>8.1f}")

# ── 2. Education LEADS GDP: correlation with lag ──────────────────────────────
print(f"\n{'='*80}")
print(f"  SECTION 2: Does education lead GDP? (5-year lag correlations)")
print(f"  Corr(edu at t, GDP at t+lag) vs Corr(GDP at t, edu at t+lag)")
print(f"{'='*80}")

for country in FOCUS:
    edu_vals, gdp_vals = [], []
    for yr in range(1960, 2011):
        e = completion_from_OL(get("Lower_Secondary_OL", country, yr))
        g = get("gdp", country, yr)
        if not (np.isnan(e) or np.isnan(g)):
            edu_vals.append((yr, e))
            gdp_vals.append((yr, g))

    edu_s = pd.Series({y: v for y, v in edu_vals})
    gdp_s = pd.Series({y: v for y, v in gdp_vals})

    lags = [0, 5, 10, 15, 20]
    print(f"\n  {country.upper()}")
    print(f"  {'Lag':>5}  {'Corr(edu→GDP)':>14}  {'Corr(GDP→edu)':>14}")
    for lag in lags:
        # edu at t vs GDP at t+lag
        common_yrs = [y for y in edu_s.index if y + lag in gdp_s.index]
        if len(common_yrs) > 5:
            e_lead = pd.Series([edu_s[y] for y in common_yrs])
            g_lag  = pd.Series([gdp_s[y + lag] for y in common_yrs])
            c1 = e_lead.corr(g_lag)
        else:
            c1 = np.nan
        # GDP at t vs edu at t+lag
        common_yrs2 = [y for y in gdp_s.index if y + lag in edu_s.index]
        if len(common_yrs2) > 5:
            g_lead = pd.Series([gdp_s[y] for y in common_yrs2])
            e_lag  = pd.Series([edu_s[y + lag] for y in common_yrs2])
            c2 = g_lead.corr(e_lag)
        else:
            c2 = np.nan
        print(f"  {lag:>5}  {c1:>14.3f}  {c2:>14.3f}")

# ── 3. Dropout gap at each level per country ─────────────────────────────────
print(f"\n{'='*80}")
print(f"  SECTION 3: Dropout gap — % lost at each education transition")
print(f"  (gap = % who completed lower level but NOT the next)")
print(f"{'='*80}")

print(f"\n  {'Country':<20}  {'Year':>5}  "
      f"{'≥Primary':>9}  {'≥LowerSec':>10}  {'≥HigherSec':>11}  "
      f"{'Drop@Pri':>9}  {'Drop@Low':>9}")
print(f"  {'-'*20}  {'-'*5}  {'-'*9}  {'-'*10}  {'-'*11}  {'-'*9}  {'-'*9}")

for country in FOCUS:
    for yr in [1960, 1980, 2000, 2015]:
        pri  = completion_from_OL(get("Primary_OL",         country, yr))
        low  = completion_from_OL(get("Lower_Secondary_OL", country, yr))
        high = get("Higher_Secondary", country, yr)
        if np.isnan(high): high = 0
        drop_pri = pri - low    # lost between primary and lower sec
        drop_low = low - high   # lost between lower sec and higher sec
        print(f"  {country:<20}  {yr:>5}  "
              f"{pri:>8.1f}%  {low:>9.1f}%  {high:>10.1f}%  "
              f"{drop_pri:>8.1f}%  {drop_low:>8.1f}%")
    print()

# ── 4. Focus vs comparators: same starting GDP, different trajectory ──────────
print(f"\n{'='*80}")
print(f"  SECTION 4: Focus countries vs GDP-comparable countries")
print(f"  (same ~1960 GDP, very different education outcomes)")
print(f"{'='*80}")

for focus, comps in COMPARATORS.items():
    group = [focus] + comps
    print(f"\n  {focus.upper()} vs comparators:")
    print(f"  {'Country':<28}  {'GDP 60':>7} {'GDP 15':>7} {'GDP×':>5}  "
          f"{'Pri 60':>7} {'Pri 15':>7}  {'Hi 60':>6} {'Hi 15':>6}  "
          f"{'TFR 60':>7} {'TFR 15':>7}  {'LE 60':>6} {'LE 15':>6}")
    print(f"  {'-'*28}  {'-'*7} {'-'*7} {'-'*5}  "
          f"{'-'*7} {'-'*7}  {'-'*6} {'-'*6}  "
          f"{'-'*7} {'-'*7}  {'-'*6} {'-'*6}")
    for c in group:
        g60  = get("gdp",             c, 1960)
        g15  = get("gdp",             c, 2015)
        gmul = g15/g60 if g60 > 0 else np.nan
        p60  = completion_from_OL(get("Primary_OL", c, 1960))
        p15  = completion_from_OL(get("Primary_OL", c, 2015))
        h60  = get("Higher_Secondary", c, 1960)
        h15  = get("Higher_Secondary", c, 2015)
        t60  = get("tfr",             c, 1960)
        t15  = get("tfr",             c, 2015)
        l60  = get("life_expectancy", c, 1960)
        l15  = get("life_expectancy", c, 2015)
        marker = " ◄" if c == focus else ""
        print(f"  {c:<28}  {g60:>7.0f} {g15:>7.0f} {gmul:>5.1f}x  "
              f"{p60:>6.1f}% {p15:>6.1f}%  "
              f"{h60:>5.1f}% {h15:>5.1f}%  "
              f"{t60:>7.2f} {t15:>7.2f}  "
              f"{l60:>6.1f} {l15:>6.1f}{marker}")

# ── 5. Female education lead: was female education ahead of male? ─────────────
print(f"\n{'='*80}")
print(f"  SECTION 5: Female vs total education — did female education lead?")
print(f"  (negative gap = female BEHIND total; positive = female AHEAD)")
print(f"{'='*80}")

for country in FOCUS:
    print(f"\n  {country.upper()} — female completion gap vs total (female minus total):")
    print(f"  {'Year':>5}  {'Total≥Pri':>10}  {'Female≥Pri':>11}  {'Gap':>6}  "
          f"{'Total≥Low':>10}  {'Female≥Low':>11}  {'Gap':>6}")
    for yr in YEARS_5:
        t_pri  = completion_from_OL(get("Primary_OL",         country, yr))
        f_pri  = completion_from_OL(get("female_Primary_OL",  country, yr))
        t_low  = completion_from_OL(get("Lower_Secondary_OL", country, yr))
        f_low  = completion_from_OL(get("female_Lower_Sec_OL",country, yr))
        g_pri  = f_pri - t_pri
        g_low  = f_low - t_low
        print(f"  {yr:>5}  {t_pri:>9.1f}%  {f_pri:>10.1f}%  {g_pri:>+6.1f}  "
              f"{t_low:>9.1f}%  {f_low:>10.1f}%  {g_low:>+6.1f}")
