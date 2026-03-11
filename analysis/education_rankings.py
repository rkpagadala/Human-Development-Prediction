"""
Global Education Achievement Rankings — 1960 to 2015
202 countries, 4 ladder levels, multiple ranking dimensions.

Outputs:
  education_rankings.md  — readable report with sorted tables
  education_rankings.csv — full metrics table for spreadsheet use

Metrics per country:
  Completion at primary / lower-sec / upper-sec / college (1960, 1975, 1990, 2005, 2015)
  Edu Score = unweighted mean of the 4 levels (0–100)
  Ladder Score = weighted: college counts most (reflects how far up the ladder)
  Gain = 2015 score minus 1960 score
  Speed = years taken to cross the 60% primary threshold (earlier = faster)
  Gender gap = female primary completion minus overall primary, 2015
  Sequential gap = primary minus lower-secondary completion, 2015
  Archetype = human-readable cluster

Rankings produced:
  1. World rank by 2015 Edu Score
  2. Most improved 1960→2015 (largest gain)
  3. By archetype
  4. Decade-by-decade snapshot for key countries
  5. Gender gap ranking
  6. Sequential vs simultaneous compressors
"""

import pandas as pd
import numpy as np
from io import StringIO

ROOT = "datasets/"
OBS_YEARS = ["1960","1965","1970","1975","1980","1985","1990","1995","2000","2005","2010","2015"]
SNAP_YEARS = ["1960","1975","1990","2005","2015"]

# ── Load ──────────────────────────────────────────────────────────────────────
def load_comp(path, is_ol=True):
    """Load dataset and convert to completion % (100 - OL if is_ol)."""
    df = pd.read_csv(path)
    df["Country"] = df["Country"].str.lower()
    df = df.set_index("Country")
    if is_ol:
        for c in df.columns:
            df[c] = 100 - pd.to_numeric(df[c], errors="coerce")
    else:
        for c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

print("Loading data...")
pri   = load_comp(ROOT + "Primary_OL.csv",                is_ol=True)
low   = load_comp(ROOT + "Lower_Secondary_OL.csv",        is_ol=True)
upp   = load_comp(ROOT + "Upper_Secondary_OL.csv",        is_ol=True)
col   = load_comp(ROOT + "College_comp.csv",              is_ol=False)
f_pri = load_comp(ROOT + "female_Primary_OL.csv",         is_ol=True)
f_low = load_comp(ROOT + "female_Lower_Secondary_OL.csv", is_ol=True)

all_countries = sorted(set(pri.index) & set(low.index) & set(upp.index) & set(col.index))
print(f"  Countries with all 4 levels: {len(all_countries)}")

def v(df, country, year):
    try:
        val = float(df.loc[country, str(year)])
        return val if not np.isnan(val) else np.nan
    except:
        return np.nan

def safe_mean(*vals):
    vals = [x for x in vals if not np.isnan(x)]
    return np.mean(vals) if vals else np.nan

# ── Build country metrics ─────────────────────────────────────────────────────
print("Computing metrics...")
rows = []
for c in all_countries:
    # Snapshots at each level
    def snap(df, yr): return v(df, c, yr)

    p60, p75, p90, p05, p15 = snap(pri,"1960"), snap(pri,"1975"), snap(pri,"1990"), snap(pri,"2005"), snap(pri,"2015")
    l60, l75, l90, l05, l15 = snap(low,"1960"), snap(low,"1975"), snap(low,"1990"), snap(low,"2005"), snap(low,"2015")
    u60, u75, u90, u05, u15 = snap(upp,"1960"), snap(upp,"1975"), snap(upp,"1990"), snap(upp,"2005"), snap(upp,"2015")
    c60, c75, c90, c05, c15 = snap(col,"1960"), snap(col,"1975"), snap(col,"1990"), snap(col,"2005"), snap(col,"2015")

    # Composite edu score = mean of all 4 levels
    edu60  = safe_mean(p60, l60, u60, c60)
    edu15  = safe_mean(p15, l15, u15, c15)
    gain   = edu15 - edu60 if not np.isnan(edu60) else np.nan

    # Ladder score 2015 (weighted: higher rungs weighted more)
    # 1×primary + 1.5×lowsec + 2×uppsec + 2.5×college / 7 × 100
    def wscore(p,l,u,cl):
        vals = [(p,1),(l,1.5),(u,2),(cl,2.5)]
        num = sum(val*w for val,w in vals if not np.isnan(val))
        den = sum(w for val,w in vals if not np.isnan(val))
        return num/den if den>0 else np.nan
    ladder15 = wscore(p15,l15,u15,c15)
    ladder60 = wscore(p60,l60,u60,c60)

    # Speed: year first crossed 60% primary completion
    speed_year = np.nan
    for yr in OBS_YEARS:
        pv = v(pri, c, yr)
        if not np.isnan(pv) and pv >= 60:
            speed_year = int(yr)
            break

    # Gender gap 2015 (female primary - overall primary); negative = girls behind
    fp15 = snap(f_pri,"2015")
    gender_gap = fp15 - p15 if not np.isnan(fp15) and not np.isnan(p15) else np.nan

    # Female lower sec gap 2015
    fl15 = snap(f_low,"2015")
    gender_gap_low = fl15 - l15 if not np.isnan(fl15) and not np.isnan(l15) else np.nan

    # Sequential gap 2015: primary - lower secondary (large = sequential, small = simultaneous)
    seq_gap15 = p15 - l15 if not np.isnan(p15) and not np.isnan(l15) else np.nan

    # Peak decade: which 10-yr period had largest composite gain
    decade_gains = {}
    for i in range(0, len(OBS_YEARS)-2, 2):  # every 10 years
        y0, y1 = OBS_YEARS[i], OBS_YEARS[i+2]
        s0 = safe_mean(v(pri,c,y0),v(low,c,y0),v(upp,c,y0),v(col,c,y0))
        s1 = safe_mean(v(pri,c,y1),v(low,c,y1),v(upp,c,y1),v(col,c,y1))
        if not np.isnan(s0) and not np.isnan(s1):
            decade_gains[f"{y0}–{y1}"] = s1 - s0
    peak_decade = max(decade_gains, key=decade_gains.get) if decade_gains else "n/a"
    peak_gain   = max(decade_gains.values()) if decade_gains else np.nan

    # Archetype 2015
    if not np.isnan(p15) and not np.isnan(l15):
        if   p15 >= 92 and l15 >= 85 and (np.isnan(u15) or u15 >= 70):
            archetype = "Universal"
        elif p15 >= 85 and l15 >= 65:
            archetype = "Near-Universal"
        elif p15 >= 80 and l15 >= 40:
            archetype = "Secondary Transition"
        elif p15 >= 70 and l15 < 40:
            archetype = "Primary Complete"
        elif p15 >= 45:
            archetype = "Primary Building"
        else:
            archetype = "Low Access"
    else:
        archetype = "No Data"

    # Trajectory (gain-based)
    if not np.isnan(gain):
        if edu60 >= 65:
            trajectory = "Early Achiever"      # already high, less room to gain
        elif gain >= 40:
            trajectory = "Breakthrough"
        elif gain >= 22:
            trajectory = "Strong Progress"
        elif gain >= 10:
            trajectory = "Moderate Progress"
        else:
            trajectory = "Minimal Progress"
    else:
        trajectory = "Insufficient Data"

    rows.append({
        "country": c,
        # 2015 levels
        "pri_2015": p15, "low_2015": l15, "upp_2015": u15, "col_2015": c15,
        # 1960 levels
        "pri_1960": p60, "low_1960": l60, "upp_1960": u60, "col_1960": c60,
        # snapshots
        "pri_1975": p75, "low_1975": l75,
        "pri_1990": p90, "low_1990": l90,
        "pri_2005": p05, "low_2005": l05,
        # composite
        "edu_score_2015": edu15, "edu_score_1960": edu60,
        "ladder_score_2015": ladder15, "ladder_score_1960": ladder60,
        "gain_1960_2015": gain,
        # speed
        "year_crossed_60pct_primary": speed_year,
        # gaps
        "gender_gap_primary_2015": gender_gap,
        "gender_gap_lowsec_2015": gender_gap_low,
        "sequential_gap_2015": seq_gap15,
        # trajectory
        "peak_decade": peak_decade, "peak_decade_gain": peak_gain,
        "archetype": archetype, "trajectory": trajectory,
    })

df = pd.DataFrame(rows)

# World rank by 2015 edu score
df["world_rank_2015"]     = df["edu_score_2015"].rank(ascending=False, na_option="bottom").astype(int)
df["world_rank_gain"]     = df["gain_1960_2015"].rank(ascending=False, na_option="bottom").astype(int)
df["world_rank_ladder"]   = df["ladder_score_2015"].rank(ascending=False, na_option="bottom").astype(int)
df["world_rank_speed"]    = df["year_crossed_60pct_primary"].rank(ascending=True, na_option="bottom").astype(int)
df["world_rank_gender"]   = df["gender_gap_primary_2015"].rank(ascending=False, na_option="bottom").astype(int)

df.sort_values("world_rank_2015", inplace=True)
df.reset_index(drop=True, inplace=True)

# Save CSV
csv_path = "education_rankings.csv"
df.to_csv(csv_path, index=False, float_format="%.1f")
print(f"  CSV saved: {csv_path}")

# ── Format helpers ────────────────────────────────────────────────────────────
def pct(v, width=5):
    if np.isnan(v): return " " * width + "n/a"
    return f"{v:>{width}.1f}%"

def fmt_gap(v):
    if np.isnan(v): return "  n/a"
    sign = "+" if v >= 0 else ""
    return f"{sign}{v:.1f}pp"

# ── Build report ──────────────────────────────────────────────────────────────
lines = []
def h(txt): lines.append(txt)
def hr(char="─", n=100): lines.append(char * n)
def blank(): lines.append("")

h("# Global Education Achievement Rankings  |  1960–2015")
h("*202 countries · Primary / Lower Secondary / Upper Secondary / College*")
blank()
h("**Edu Score** = simple mean of 4 completion levels (0–100).")
h("**Ladder Score** = weighted mean (college weight 2.5×, primary 1×) — rewards climbing higher.")
h("**Gain** = Edu Score 2015 minus Edu Score 1960.")
h("**Speed** = year country first crossed 60% primary completion.")
h("**Sequential Gap** = primary minus lower-secondary completion 2015 (small = simultaneous expansion).")
blank()
h("---")

# ────────────────────────────────────────────────────────────────────────────
h("## TABLE 1 — World Ranking by 2015 Edu Score (all 202 countries)")
blank()
h("Full 4-level composite. Ranked highest to lowest.")
blank()
header = (f"{'Rank':>4}  {'Country':<28}  {'Pri':>6}  {'LowSec':>7}  {'UppSec':>7}  {'College':>8}"
          f"  {'EduScore':>8}  {'Gain60→15':>9}  {'Archetype':<22}  {'PeakDec'}")
h(header)
hr("─", len(header))

for _, r in df.iterrows():
    gain_str = f"{r.gain_1960_2015:>+8.1f}" if not np.isnan(r.gain_1960_2015) else "     n/a"
    line = (f"{r.world_rank_2015:>4}  {r.country:<28}  "
            f"{pct(r.pri_2015):>6}  {pct(r.low_2015):>7}  {pct(r.upp_2015):>7}  {pct(r.col_2015):>8}"
            f"  {r.edu_score_2015:>7.1f}   {gain_str}  {r.archetype:<22}  {r.peak_decade}")
    h(line)

blank()

# ────────────────────────────────────────────────────────────────────────────
h("---")
h("## TABLE 2 — Most Improved 1960→2015 (top 60 by composite gain)")
blank()
h("Countries that made the largest absolute jump across the whole education ladder.")
blank()
top_gain = df.sort_values("gain_1960_2015", ascending=False).head(60)
header2 = (f"{'Rank':>4}  {'Country':<28}  {'EduScore1960':>12}  {'EduScore2015':>12}"
           f"  {'Gain':>6}  {'PeakDecade':>12}  {'PeakGain':>9}  {'Archetype'}")
h(header2)
hr("─", len(header2))
for i, (_, r) in enumerate(top_gain.iterrows(), 1):
    e60 = f"{r.edu_score_1960:.1f}" if not np.isnan(r.edu_score_1960) else " n/a"
    e15 = f"{r.edu_score_2015:.1f}" if not np.isnan(r.edu_score_2015) else " n/a"
    gain = f"{r.gain_1960_2015:+.1f}" if not np.isnan(r.gain_1960_2015) else " n/a"
    pk = f"{r.peak_decade_gain:.1f}" if not np.isnan(r.peak_decade_gain) else " n/a"
    h(f"{i:>4}  {r.country:<28}  {e60:>12}  {e15:>12}  {gain:>6}  {r.peak_decade:>12}  {pk:>9}  {r.archetype}")
blank()

# ────────────────────────────────────────────────────────────────────────────
h("---")
h("## TABLE 3 — Archetype Groups")
blank()
h("Six archetypes based on 2015 primary and lower-secondary completion.")
blank()
archetype_order = ["Universal","Near-Universal","Secondary Transition",
                   "Primary Complete","Primary Building","Low Access"]
archetype_desc = {
    "Universal":            "Primary ≥92% AND Lower Secondary ≥85% AND Upper Secondary ≥70%",
    "Near-Universal":       "Primary ≥85% AND Lower Secondary ≥65%",
    "Secondary Transition": "Primary ≥80% AND Lower Secondary 40–65%",
    "Primary Complete":     "Primary ≥70% AND Lower Secondary <40%",
    "Primary Building":     "Primary 45–70%",
    "Low Access":           "Primary <45%",
}

for arch in archetype_order:
    sub = df[df["archetype"] == arch].sort_values("edu_score_2015", ascending=False)
    if len(sub) == 0:
        continue
    h(f"### {arch}  ({len(sub)} countries)")
    h(f"*{archetype_desc[arch]}*")
    blank()
    header3 = (f"  {'Country':<28}  {'Pri':>6}  {'LowSec':>7}  {'UppSec':>7}  {'College':>8}"
               f"  {'EduScore':>8}  {'Gain':>6}  {'Trajectory'}")
    h(header3)
    hr("─", 100)
    for _, r in sub.iterrows():
        gain = f"{r.gain_1960_2015:+.1f}" if not np.isnan(r.gain_1960_2015) else " n/a"
        h(f"  {r.country:<28}  {pct(r.pri_2015):>6}  {pct(r.low_2015):>7}  "
          f"{pct(r.upp_2015):>7}  {pct(r.col_2015):>8}  {r.edu_score_2015:>7.1f}  {gain:>6}  {r.trajectory}")
    blank()

# ────────────────────────────────────────────────────────────────────────────
h("---")
h("## TABLE 4 — Speed Rankings: Who Crossed 60% Primary First?")
blank()
h("Year each country first reached 60% primary completion.")
h("Countries that never crossed 60% by 2015 are listed separately.")
blank()

crossed = df.dropna(subset=["year_crossed_60pct_primary"]).sort_values("year_crossed_60pct_primary")
never   = df[df["year_crossed_60pct_primary"].isna()].sort_values("pri_2015", ascending=False)

h(f"{'Rank':>4}  {'Country':<28}  {'Crossed 60%':>11}  {'Pri 2015':>9}  {'EduScore 2015':>14}")
hr("─", 75)
for i, (_, r) in enumerate(crossed.iterrows(), 1):
    yr = int(r.year_crossed_60pct_primary)
    h(f"{i:>4}  {r.country:<28}  {yr:>11}  {pct(r.pri_2015):>9}  {r.edu_score_2015:>13.1f}")

blank()
h(f"  Countries that had NOT crossed 60% primary by 2015 ({len(never)} countries):")
hr("─", 75)
for _, r in never.iterrows():
    h(f"       {r.country:<28}  {'never':>11}  {pct(r.pri_2015):>9}  {r.edu_score_2015:>13.1f}")
blank()

# ────────────────────────────────────────────────────────────────────────────
h("---")
h("## TABLE 5 — Gender Gap Rankings (2015)")
blank()
h("Female primary completion minus overall primary completion (2015).")
h("Positive = girls ahead. Negative = girls behind. Large negative = gender equity gap.")
blank()

gdf = df.dropna(subset=["gender_gap_primary_2015"]).sort_values("gender_gap_primary_2015")
h(f"  {'Country':<28}  {'Female Pri':>10}  {'Overall Pri':>11}  {'Gap':>6}  {'Pri 2015':>9}")
hr("─", 80)

# Bottom 30 (girls most behind)
h("  WORST gender gaps (girls furthest behind):")
for _, r in gdf.head(30).iterrows():
    fp = v(f_pri, r.country, "2015")
    h(f"  {r.country:<28}  {pct(fp):>10}  {pct(r.pri_2015):>11}  {fmt_gap(r.gender_gap_primary_2015):>6}  {pct(r.pri_2015):>9}")

blank()
h("  BEST gender parity / girls leading:")
for _, r in gdf.tail(20).iterrows():
    fp = v(f_pri, r.country, "2015")
    h(f"  {r.country:<28}  {pct(fp):>10}  {pct(r.pri_2015):>11}  {fmt_gap(r.gender_gap_primary_2015):>6}  {pct(r.pri_2015):>9}")
blank()

# ────────────────────────────────────────────────────────────────────────────
h("---")
h("## TABLE 6 — Sequential vs Simultaneous Expansion (2015)")
blank()
h("Sequential Gap = Primary completion minus Lower Secondary completion (2015).")
h("Small gap (≤15pp) = countries that expanded primary and secondary together.")
h("Large gap (>30pp) = sequential expanders: primary done, secondary lagging.")
blank()

sdf = df.dropna(subset=["sequential_gap_2015"]).sort_values("sequential_gap_2015")

h("  MOST SIMULTANEOUS (gap ≤15pp, sorted smallest gap first):")
h(f"  {'Country':<28}  {'Pri 2015':>9}  {'LowSec 2015':>12}  {'Gap':>6}  {'EduScore':>9}")
hr("─", 72)
for _, r in sdf[sdf["sequential_gap_2015"] <= 15].iterrows():
    h(f"  {r.country:<28}  {pct(r.pri_2015):>9}  {pct(r.low_2015):>12}  {fmt_gap(r.sequential_gap_2015):>6}  {r.edu_score_2015:>8.1f}")

blank()
h("  MOST SEQUENTIAL (gap >30pp, sorted largest gap first):")
h(f"  {'Country':<28}  {'Pri 2015':>9}  {'LowSec 2015':>12}  {'Gap':>6}  {'EduScore':>9}")
hr("─", 72)
for _, r in sdf[sdf["sequential_gap_2015"] > 30].sort_values("sequential_gap_2015", ascending=False).iterrows():
    h(f"  {r.country:<28}  {pct(r.pri_2015):>9}  {pct(r.low_2015):>12}  {fmt_gap(r.sequential_gap_2015):>6}  {r.edu_score_2015:>8.1f}")
blank()

# ────────────────────────────────────────────────────────────────────────────
h("---")
h("## TABLE 7 — Decade-by-Decade Trajectories for 40 Key Countries")
blank()
h("Primary / Lower Secondary completion at each 5-year WCDE observation.")
blank()

key_countries = [
    # East/SE Asia
    "south korea","singapore","japan","china","malaysia","thailand",
    "indonesia","vietnam","philippines","myanmar",
    # South Asia
    "india","bangladesh","pakistan","nepal","sri lanka",
    # Sub-Saharan Africa
    "kenya","ghana","nigeria","ethiopia","tanzania","senegal",
    "mozambique","mali","niger","burkina faso","south africa","rwanda",
    # Middle East / N Africa
    "egypt","morocco","algeria","iran","turkey","saudi arabia",
    # Latin America
    "brazil","mexico","colombia","peru","bolivia","guatemala",
    # Developed (benchmarks)
    "united states","germany","finland","france",
]
key_countries = [c for c in key_countries if c in df["country"].values]

h(f"  {'Country':<22}  "
  f"{'─────── Primary ──────────────────'}  "
  f"{'─── Lower Secondary ──────────────'}")
h(f"  {'':22}  "
  f"{'1960':>6}{'1975':>7}{'1990':>7}{'2005':>7}{'2015':>7}  "
  f"{'1960':>6}{'1975':>7}{'1990':>7}{'2005':>7}{'2015':>7}  "
  f"{'EduScore':>9}  {'Arch'}")
hr("─", 120)

for c in key_countries:
    row = df[df["country"] == c]
    if len(row) == 0:
        continue
    r = row.iloc[0]
    def fv(val): return f"{val:>6.1f}" if not np.isnan(val) else "   n/a"
    h(f"  {c:<22}  "
      f"{fv(r.pri_1960)}{fv(r.pri_1975)}{fv(r.pri_1990)}{fv(r.pri_2005)}{fv(r.pri_2015)}  "
      f"{fv(r.low_1960)}{fv(r.low_1975)}{fv(r.low_1990)}{fv(r.low_2005)}{fv(r.low_2015)}  "
      f"{r.edu_score_2015:>8.1f}  {r.archetype}")
blank()

# ────────────────────────────────────────────────────────────────────────────
h("---")
h("## TABLE 8 — Trajectory Classification Summary")
blank()
traj_order = ["Early Achiever","Breakthrough","Strong Progress",
              "Moderate Progress","Minimal Progress","Insufficient Data"]
traj_desc = {
    "Early Achiever":    "Edu Score ≥65 already in 1960 — started near the top",
    "Breakthrough":      "Gained ≥40pp composite 1960→2015",
    "Strong Progress":   "Gained 22–40pp",
    "Moderate Progress": "Gained 10–22pp",
    "Minimal Progress":  "Gained <10pp (or started low, remained low)",
    "Insufficient Data": "Missing 1960 data",
}

for traj in traj_order:
    sub = df[df["trajectory"] == traj].sort_values("edu_score_2015", ascending=False)
    if len(sub) == 0: continue
    h(f"### {traj}  ({len(sub)} countries)")
    h(f"*{traj_desc[traj]}*")
    h("  " + ",  ".join(sub["country"].tolist()))
    blank()

# ────────────────────────────────────────────────────────────────────────────
h("---")
h("## TABLE 9 — Ladder Score Ranking (rewards climbing higher, not just primary)")
blank()
h("Weighted: College 2.5× | Upper Sec 2× | Lower Sec 1.5× | Primary 1×")
h("Reveals countries that moved beyond primary universality into secondary/tertiary.")
blank()

ldf = df.dropna(subset=["ladder_score_2015"]).sort_values("ladder_score_2015", ascending=False).head(60)
h(f"{'Rank':>4}  {'Country':<28}  {'Pri':>6}  {'LowSec':>7}  {'UppSec':>7}  {'College':>8}  {'LadderScore':>11}  {'EduScore':>9}")
hr("─", 95)
for i, (_, r) in enumerate(ldf.iterrows(), 1):
    h(f"{i:>4}  {r.country:<28}  {pct(r.pri_2015):>6}  {pct(r.low_2015):>7}  "
      f"{pct(r.upp_2015):>7}  {pct(r.col_2015):>8}  {r.ladder_score_2015:>10.1f}  {r.edu_score_2015:>8.1f}")
blank()

# ────────────────────────────────────────────────────────────────────────────
h("---")
h("## SUMMARY STATISTICS")
blank()

for arch in archetype_order:
    sub = df[df["archetype"]==arch]
    h(f"  {arch:<26} {len(sub):>3} countries")
blank()
for traj in traj_order:
    sub = df[df["trajectory"]==traj]
    h(f"  {traj:<26} {len(sub):>3} countries")
blank()
h(f"  Global Edu Score 1960:  {df['edu_score_1960'].mean():.1f}")
h(f"  Global Edu Score 2015:  {df['edu_score_2015'].mean():.1f}")
h(f"  Global Gain 1960→2015:  {df['gain_1960_2015'].mean():+.1f}pp")
h(f"  Countries never reaching 60% primary:  {df['year_crossed_60pct_primary'].isna().sum()}")
h(f"  Countries with gender gap > 5pp (girls behind, primary):  "
  f"{(df['gender_gap_primary_2015'] < -5).sum()}")

# ── Write report ──────────────────────────────────────────────────────────────
report = "\n".join(lines)
with open("education_rankings.md", "w") as f:
    f.write(report)
print(f"  Report saved: education_rankings.md")
print(f"  Total lines: {len(lines)}")
print("\nDone.")
