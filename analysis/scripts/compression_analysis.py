"""
The Asian tiger anomaly: they compressed two generational steps (primary → secondary)
into a single ~30-year policy window, rather than the natural 50-year path
(25yr for primary to spread, then another 25yr for secondary to follow).

Normal path:
  Gen 1 (1960): gets primary education via policy
  Gen 2 (1985): children of Gen1, now gets secondary (natural transmission)
  Gen 3 (2010): gets higher secondary

Tiger path (compressed):
  1960-1990 (30 years): primary AND secondary expand simultaneously
  Children of parents with primary education go straight to secondary —
  not because their parents had secondary, but because the state pushed them.

Measurements:
  1. Compression ratio: how fast did secondary grow relative to primary?
     If natural: secondary lags primary by ~25 years
     If compressed: secondary tracks primary with small or zero lag
  2. Secondary "above parental prediction":
     How far above what parental-primary-only would predict is secondary completion?
  3. Speed: years to go from 10% to 60% at each level
  4. Primary-secondary co-movement: did they grow together or in sequence?
"""

import pandas as pd
import numpy as np

ROOT = "datasets/"

DATASETS = {
    "Primary_OL":         ROOT + "Primary_OL.csv",
    "Lower_Secondary_OL": ROOT + "Lower_Secondary_OL.csv",
    "Higher_Secondary":   ROOT + "Higher_Secondary_fin_complete.csv",
    "gdp":                ROOT + "gdppercapita_us_inflation_adjusted.csv",
}

def load(path):
    df = pd.read_csv(path)
    df["Country"] = df["Country"].str.lower()
    return df.set_index("Country")

dfs = {name: load(path) for name, path in DATASETS.items()}

def get(name, country, year):
    try:
        return float(dfs[name].loc[country, str(year)])
    except (KeyError, ValueError):
        return np.nan

def comp(ol): return 100 - ol

TIGERS  = ["south korea", "singapore", "malaysia", "thailand"]
COMPARE = ["india", "china", "ghana", "kenya", "nigeria", "brazil", "colombia", "egypt", "algeria"]
ALL     = TIGERS + COMPARE

# ── Section 1: Speed — years to cross thresholds at each level ───────────────
print(f"{'='*80}")
print(f"  SECTION 1: Speed — years to go from 10% → 60% at each education level")
print(f"  Natural path: primary crosses first, secondary follows ~25 years later")
print(f"  Compressed:   both cross within the same 30-year window")
print(f"{'='*80}")

def year_crossing(country, level, threshold):
    """Year when country first crossed threshold at education level."""
    func = comp if level != "Higher_Secondary" else (lambda x: x)
    get_name = level
    for yr in range(1960, 2016):
        v = func(get(get_name, country, yr))
        if not np.isnan(v) and v >= threshold:
            return yr
    return None

print(f"\n  {'Country':<22}  {'Pri→10%':>7} {'Pri→60%':>7} {'Low→10%':>7} {'Low→60%':>7} "
      f"{'Hi→10%':>7} {'Hi→60%':>7}  {'Compress':>9}  {'Pri-Low lag':>11}")
print(f"  {'-'*22}  {'-'*7} {'-'*7} {'-'*7} {'-'*7} "
      f"{'-'*7} {'-'*7}  {'-'*9}  {'-'*11}")

for country in ALL:
    p10  = year_crossing(country, "Primary_OL",         10)
    p60  = year_crossing(country, "Primary_OL",         60)
    l10  = year_crossing(country, "Lower_Secondary_OL", 10)
    l60  = year_crossing(country, "Lower_Secondary_OL", 60)
    h10  = year_crossing(country, "Higher_Secondary",   10)
    h60  = year_crossing(country, "Higher_Secondary",   60)

    # Compression: years between primary 10% and secondary 60%
    if p10 and l60:
        total_span = l60 - p10
    else:
        total_span = None

    # Lag between primary 60% and lower secondary 60%
    if p60 and l60:
        pri_low_lag = l60 - p60
    else:
        pri_low_lag = None

    marker = " ◄" if country in TIGERS else ""
    print(f"  {country:<22}  "
          f"{str(p10) if p10 else 'never':>7} "
          f"{str(p60) if p60 else 'never':>7} "
          f"{str(l10) if l10 else 'never':>7} "
          f"{str(l60) if l60 else 'never':>7} "
          f"{str(h10) if h10 else 'never':>7} "
          f"{str(h60) if h60 else 'never':>7}  "
          f"{str(total_span)+'yr' if total_span else 'n/a':>9}  "
          f"{str(pri_low_lag)+'yr' if pri_low_lag else 'n/a':>11}"
          f"{marker}")

# ── Section 2: Co-movement — did primary and secondary grow together? ─────────
print(f"\n{'='*80}")
print(f"  SECTION 2: Co-movement — correlation between annual primary and")
print(f"  secondary growth rates within each country")
print(f"  High correlation = grew together (compression)")
print(f"  Low/zero correlation = grew sequentially (natural path)")
print(f"{'='*80}")

print(f"\n  {'Country':<22}  {'Corr(Pri,Low) growth':>20}  {'Corr(Low,High) growth':>22}  {'Interpretation'}")
print(f"  {'-'*22}  {'-'*20}  {'-'*22}  {'-'*20}")

for country in ALL:
    pri_series  = [comp(get("Primary_OL",         country, yr)) for yr in range(1960, 2016)]
    low_series  = [comp(get("Lower_Secondary_OL", country, yr)) for yr in range(1960, 2016)]
    high_series = [get("Higher_Secondary",         country, yr) for yr in range(1960, 2016)]

    # Year-on-year changes
    d_pri  = [pri_series[i+1]  - pri_series[i]  for i in range(len(pri_series)-1)
              if not (np.isnan(pri_series[i]) or np.isnan(pri_series[i+1]))]
    d_low  = [low_series[i+1]  - low_series[i]  for i in range(len(low_series)-1)
              if not (np.isnan(low_series[i]) or np.isnan(low_series[i+1]))]
    d_high = [high_series[i+1] - high_series[i] for i in range(len(high_series)-1)
              if not (np.isnan(high_series[i]) or np.isnan(high_series[i+1]))]

    n = min(len(d_pri), len(d_low))
    if n > 5:
        corr_pl = pd.Series(d_pri[:n]).corr(pd.Series(d_low[:n]))
    else:
        corr_pl = np.nan

    n2 = min(len(d_low), len(d_high))
    if n2 > 5:
        corr_lh = pd.Series(d_low[:n2]).corr(pd.Series(d_high[:n2]))
    else:
        corr_lh = np.nan

    if not np.isnan(corr_pl):
        interp = "compressed" if corr_pl > 0.7 else ("moderate" if corr_pl > 0.4 else "sequential")
    else:
        interp = "n/a"

    marker = " ◄" if country in TIGERS else ""
    print(f"  {country:<22}  {corr_pl:>20.3f}  {corr_lh:>22.3f}  {interp}{marker}")

# ── Section 3: Decade-by-decade primary vs secondary ratio ───────────────────
print(f"\n{'='*80}")
print(f"  SECTION 3: Secondary/Primary ratio by decade")
print(f"  (how much secondary completion per unit of primary)")
print(f"  Tigers should show ratio rising fast = secondary catching primary")
print(f"  Others should show ratio flat or slow = secondary lagging")
print(f"{'='*80}")

print(f"\n  {'Country':<22}", end="")
for yr in [1960, 1970, 1980, 1990, 2000, 2010, 2015]:
    print(f"  {yr:>6}", end="")
print()
print(f"  {'-'*22}", end="")
for yr in [1960, 1970, 1980, 1990, 2000, 2010, 2015]:
    print(f"  {'-'*6}", end="")
print()

for country in ALL:
    marker = " ◄" if country in TIGERS else ""
    print(f"  {country:<22}", end="")
    for yr in [1960, 1970, 1980, 1990, 2000, 2010, 2015]:
        pri  = comp(get("Primary_OL",         country, yr))
        low  = comp(get("Lower_Secondary_OL", country, yr))
        ratio = (low / pri) if (not np.isnan(pri) and not np.isnan(low) and pri > 0) else np.nan
        print(f"  {ratio:>5.2f}" if not np.isnan(ratio) else f"  {'n/a':>5}", end="")
    print(marker)

# ── Section 4: GDP at the time of the education push ─────────────────────────
print(f"\n{'='*80}")
print(f"  SECTION 4: What was GDP when each country made its education push?")
print(f"  (GDP at the year each country crossed 30% lower secondary completion)")
print(f"  If education requires wealth: tigers should have been rich at that point.")
print(f"  If education is a policy choice: tigers should have been poor.")
print(f"{'='*80}")

print(f"\n  {'Country':<22}  {'Year hit 30% LowSec':>19}  {'GDP at that year':>17}  {'World avg GDP ~1980':>20}")
world_avg_1980 = np.nanmean([get("gdp", c, 1980)
                              for c in dfs["gdp"].index])
print(f"  (World average GDP ~1980: ${world_avg_1980:,.0f})\n")

for country in ALL:
    yr30 = year_crossing(country, "Lower_Secondary_OL", 30)
    if yr30:
        gdp_then = get("gdp", country, yr30)
        world_avg_then = np.nanmean([get("gdp", c, yr30) for c in dfs["gdp"].index])
        pct_world = (gdp_then / world_avg_then * 100) if not np.isnan(gdp_then) else np.nan
        marker = " ◄" if country in TIGERS else ""
        print(f"  {country:<22}  {yr30:>19}  "
              f"${gdp_then:>13,.0f}  "
              f"{pct_world:>17.0f}% of world avg{marker}")
    else:
        print(f"  {country:<22}  {'never reached 30%':>19}")
