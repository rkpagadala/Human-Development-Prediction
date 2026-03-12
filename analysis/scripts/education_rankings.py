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

import os
import pandas as pd
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(SCRIPT_DIR, "../../datasets/")
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
            archetype = "Secondary Building"   # primary achieved; ~35% still not completing lower sec
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
        if gain <= -10:
            trajectory = "Regression"          # education declined over the period
        elif edu60 >= 65:
            trajectory = "Early Achiever"      # already high in 1960, maintained
        elif gain >= 40:
            trajectory = "Large Gain"          # 40pp+ gain; endpoint quality varies
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

OUT_MD  = os.path.join(SCRIPT_DIR, "../education_rankings.md")
OUT_CSV = os.path.join(SCRIPT_DIR, "../education_rankings.csv")

df.to_csv(OUT_CSV, index=False, float_format="%.1f")
print(f"  CSV saved: {OUT_CSV}")

# ── Format helpers ────────────────────────────────────────────────────────────
def pct(val):
    return f"{val:.1f}%" if not np.isnan(val) else "n/a"

def signed(val):
    if np.isnan(val): return "n/a"
    return f"+{val:.1f}" if val >= 0 else f"{val:.1f}"

def cn(name, maxlen=32):
    return name.title()[:maxlen]

# ── Build report ──────────────────────────────────────────────────────────────
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

archetype_order = ["Universal","Secondary Building","Secondary Transition",
                   "Primary Complete","Primary Building","Low Access"]
archetype_desc  = {
    "Universal":            "Primary ≥92%, Lower Sec ≥85%, Upper Sec ≥70%",
    "Secondary Building":   "Primary ≥85%, Lower Sec 65–85% — primary mostly done, secondary still incomplete",
    "Secondary Transition": "Primary ≥80%, Lower Sec 40–65%",
    "Primary Complete":     "Primary ≥70%, Lower Sec <40%",
    "Primary Building":     "Primary 45–70%",
    "Low Access":           "Primary <45%",
}
traj_order = ["Regression","Early Achiever","Large Gain","Strong Progress",
              "Moderate Progress","Minimal Progress","Insufficient Data"]
traj_desc  = {
    "Regression":        "Edu Score declined ≥10 pp — education contracted over the period",
    "Early Achiever":    "Edu Score ≥65 already in 1960, maintained",
    "Large Gain":        "Gained ≥40 pp — endpoint quality varies widely",
    "Strong Progress":   "Gained 22–40 pp",
    "Moderate Progress": "Gained 10–22 pp",
    "Minimal Progress":  "Gained <10 pp",
    "Insufficient Data": "Missing 1960 data",
}

h("# Global Education Achievement Rankings — 1960–2015")
h()
h("**175 countries** with complete data across all four levels.")
h("Data source: WCDE (5-year cohorts, linearly interpolated between observations).")
h()
h("| Metric | Definition |")
h("|---|---|")
h("| **Edu Score** | Simple mean of 4 completion levels (0–100) |")
h("| **Ladder Score** | Weighted mean — college 2.5×, upper-sec 2×, lower-sec 1.5×, primary 1× |")
h("| **Gain** | Edu Score 2015 minus Edu Score 1960 |")
h("| **Speed** | First year country crossed 60% primary completion |")
h("| **Sequential Gap** | Primary minus lower-secondary 2015. Small gap at high primary = simultaneous expansion. Small gap at low primary = both levels underdeveloped. |")
h()
h("---")
h()
h("## Summary Statistics")
h()
h("| | |")
h("|---|---|")
h(f"| Global Edu Score 1960 | {df['edu_score_1960'].mean():.1f} |")
h(f"| Global Edu Score 2015 | {df['edu_score_2015'].mean():.1f} |")
h(f"| Global Gain 1960→2015 | +{df['gain_1960_2015'].mean():.1f} pp |")
h(f"| Countries never reaching 60% primary by 2015 | {df['year_crossed_60pct_primary'].isna().sum()} |")
h(f"| Countries with gender gap >5 pp (girls behind) | {(df['gender_gap_primary_2015'] < -5).sum()} |")
h()
pipe_table(["Archetype","Countries","Definition"],
           [[a, len(df[df["archetype"]==a]), archetype_desc.get(a,"")] for a in archetype_order])
pipe_table(["Trajectory","Countries","Definition"],
           [[t, len(df[df["trajectory"]==t]), traj_desc.get(t,"")] for t in traj_order])
h("---")
h()

h("## Table 1 — World Ranking by 2015 Edu Score")
h()
h("All 175 countries with complete data, ranked highest to lowest.")
h()
pipe_table(
    ["Rank","Country","Primary","Lower Sec","Upper Sec","College","Edu Score","Gain 60→15","Archetype","Peak Decade"],
    [[r.world_rank_2015, cn(r.country),
      pct(r.pri_2015), pct(r.low_2015), pct(r.upp_2015), pct(r.col_2015),
      f"{r.edu_score_2015:.1f}", signed(r.gain_1960_2015), r.archetype, r.peak_decade]
     for _, r in df.iterrows()],
    ["right","left","right","right","right","right","right","right","left","left"]
)

# ────────────────────────────────────────────────────────────────────────────
h("---")
h()
h("## Table 2 — Most Improved 1960→2015")
h()
h("Top 60 countries by composite gain across all four levels.")
h()
top_gain = df.sort_values("gain_1960_2015", ascending=False).head(60)
pipe_table(
    ["Rank","Country","Edu Score 1960","Edu Score 2015","Gain","Peak Decade","Peak Gain","Archetype"],
    [[i+1, cn(r.country),
      f"{r.edu_score_1960:.1f}" if not np.isnan(r.edu_score_1960) else "n/a",
      f"{r.edu_score_2015:.1f}" if not np.isnan(r.edu_score_2015) else "n/a",
      signed(r.gain_1960_2015), r.peak_decade,
      f"{r.peak_decade_gain:.1f}" if not np.isnan(r.peak_decade_gain) else "n/a",
      r.archetype]
     for i, (_, r) in enumerate(top_gain.iterrows())],
    ["right","left","right","right","right","left","right","left"]
)

# ────────────────────────────────────────────────────────────────────────────
h("---")
h()
h("## Table 3 — Archetype Groups")
h()
h("Countries grouped by 2015 primary and lower-secondary completion levels.")
h()
for arch in archetype_order:
    sub = df[df["archetype"] == arch].sort_values("edu_score_2015", ascending=False)
    if len(sub) == 0: continue
    h(f"### {arch} ({len(sub)} countries)")
    h(f"*{archetype_desc[arch]}*")
    h()
    pipe_table(
        ["Country","Primary","Lower Sec","Upper Sec","College","Edu Score","Gain","Trajectory"],
        [[cn(r.country), pct(r.pri_2015), pct(r.low_2015), pct(r.upp_2015), pct(r.col_2015),
          f"{r.edu_score_2015:.1f}", signed(r.gain_1960_2015), r.trajectory]
         for _, r in sub.iterrows()],
        ["left","right","right","right","right","right","right","left"]
    )

# ────────────────────────────────────────────────────────────────────────────
h("---")
h()
h("## Table 4 — Speed Rankings: First to Cross 60% Primary Completion")
h()
crossed = df.dropna(subset=["year_crossed_60pct_primary"]).sort_values("year_crossed_60pct_primary")
never   = df[df["year_crossed_60pct_primary"].isna()].sort_values("pri_2015", ascending=False)
h(f"{len(crossed)} countries crossed the threshold. {len(never)} had not crossed 60% primary by 2015.")
h()
h("**Countries that crossed 60% primary (ranked by speed):**")
h()
pipe_table(
    ["Rank","Country","Crossed 60%","Primary 2015","Edu Score 2015"],
    [[i+1, cn(r.country), int(r.year_crossed_60pct_primary), pct(r.pri_2015), f"{r.edu_score_2015:.1f}"]
     for i, (_, r) in enumerate(crossed.iterrows())],
    ["right","left","right","right","right"]
)
h("**Countries that never crossed 60% primary by 2015:**")
h()
pipe_table(
    ["Country","Primary 2015","Edu Score 2015"],
    [[cn(r.country), pct(r.pri_2015), f"{r.edu_score_2015:.1f}"] for _, r in never.iterrows()],
    ["left","right","right"]
)

# ────────────────────────────────────────────────────────────────────────────
h("---")
h()
h("## Table 5 — Gender Gap Rankings (2015 Primary)")
h()
h("Female primary completion minus overall primary completion. **Negative** = girls behind.")
h()
gdf = df.dropna(subset=["gender_gap_primary_2015"]).sort_values("gender_gap_primary_2015")
h("**Worst 30 gender gaps (girls furthest behind):**")
h()
pipe_table(
    ["Country","Female Primary","Overall Primary","Gap (pp)"],
    [[cn(r.country), pct(v(f_pri,r.country,"2015")), pct(r.pri_2015), signed(r.gender_gap_primary_2015)]
     for _, r in gdf.head(30).iterrows()],
    ["left","right","right","right"]
)
h("**Best 20: gender parity or girls leading:**")
h()
pipe_table(
    ["Country","Female Primary","Overall Primary","Gap (pp)"],
    [[cn(r.country), pct(v(f_pri,r.country,"2015")), pct(r.pri_2015), signed(r.gender_gap_primary_2015)]
     for _, r in gdf.tail(20).iterrows()],
    ["left","right","right","right"]
)

# ────────────────────────────────────────────────────────────────────────────
h("---")
h()
h("## Table 6 — Sequential vs Simultaneous Expansion (2015)")
h()
h("Primary minus lower-secondary completion gap.")
h("A **small gap at high primary (≥80%)** means both levels were expanded together — genuine simultaneous strategy.")
h("A **small gap at low primary (<60%)** means both levels are equally underdeveloped — not a success.")
h("A **large gap (>30 pp)** means primary was expanded first and secondary lagged — sequential path.")
h()
sdf = df.dropna(subset=["sequential_gap_2015"]).sort_values("sequential_gap_2015")

# Simultaneous at scale: primary ≥80% AND gap ≤15pp
simul_high = sdf[(sdf["sequential_gap_2015"] <= 15) & (sdf["pri_2015"] >= 80)]
# Low-base tie: both levels underdeveloped, primary <60%
simul_low  = sdf[(sdf["sequential_gap_2015"] <= 15) & (sdf["pri_2015"] < 60)]

h("**Simultaneous at scale — primary ≥80%, gap ≤15 pp (expansion ran in parallel):**")
h()
pipe_table(
    ["Country","Primary","Lower Sec","Gap (pp)","Edu Score"],
    [[cn(r.country), pct(r.pri_2015), pct(r.low_2015), signed(r.sequential_gap_2015), f"{r.edu_score_2015:.1f}"]
     for _, r in simul_high.iterrows()],
    ["left","right","right","right","right"]
)
h("**Low-base tied — primary <60%, gap ≤15 pp (both levels underdeveloped equally):**")
h()
pipe_table(
    ["Country","Primary","Lower Sec","Gap (pp)","Edu Score"],
    [[cn(r.country), pct(r.pri_2015), pct(r.low_2015), signed(r.sequential_gap_2015), f"{r.edu_score_2015:.1f}"]
     for _, r in simul_low.sort_values("pri_2015", ascending=False).iterrows()],
    ["left","right","right","right","right"]
)
h("**Most sequential — gap >30 pp (primary expanded first, secondary lagged):**")
h()
pipe_table(
    ["Country","Primary","Lower Sec","Gap (pp)","Edu Score"],
    [[cn(r.country), pct(r.pri_2015), pct(r.low_2015), signed(r.sequential_gap_2015), f"{r.edu_score_2015:.1f}"]
     for _, r in sdf[sdf["sequential_gap_2015"] > 30].sort_values("sequential_gap_2015", ascending=False).iterrows()],
    ["left","right","right","right","right"]
)

# ────────────────────────────────────────────────────────────────────────────
h("---")
h()
h("## Table 7 — Decade-by-Decade Trajectories (40 Key Countries)")
h()
h("Primary and Lower Secondary completion at each 5-year WCDE observation point.")
h()
key_countries = [
    "south korea","singapore","japan","china","malaysia","thailand",
    "indonesia","vietnam","philippines","myanmar",
    "india","bangladesh","pakistan","nepal","sri lanka",
    "kenya","ghana","nigeria","ethiopia","tanzania","senegal",
    "mozambique","mali","niger","burkina faso","south africa","rwanda",
    "egypt","morocco","algeria","iran","turkey","saudi arabia",
    "brazil","mexico","colombia","peru","bolivia","guatemala",
    "united states","germany","finland","france",
]
key_countries = [c for c in key_countries if c in df["country"].values]
kdf = df[df["country"].isin(key_countries)].set_index("country").loc[key_countries].reset_index()
pipe_table(
    ["Country",
     "Pri 1960","Pri 1975","Pri 1990","Pri 2005","Pri 2015",
     "Low 1960","Low 1975","Low 1990","Low 2005","Low 2015",
     "Edu Score","Archetype"],
    [[cn(r.country),
      pct(r.pri_1960),pct(r.pri_1975),pct(r.pri_1990),pct(r.pri_2005),pct(r.pri_2015),
      pct(r.low_1960),pct(r.low_1975),pct(r.low_1990),pct(r.low_2005),pct(r.low_2015),
      f"{r.edu_score_2015:.1f}", r.archetype]
     for _, r in kdf.iterrows()],
    ["left"] + ["right"]*10 + ["right","left"]
)

# ────────────────────────────────────────────────────────────────────────────
h("---")
h()
h("## Table 8 — Trajectory Classification")
h()
for traj in traj_order:
    sub = df[df["trajectory"] == traj].sort_values("edu_score_2015", ascending=False)
    if len(sub) == 0: continue
    h(f"**{traj} ({len(sub)})** — *{traj_desc[traj]}*")
    h()
    h(", ".join(cn(c) for c in sub["country"]))
    h()

h("---")
h()
h("## Table 9 — Ladder Score Ranking (Top 60)")
h()
h("Weighted: College 2.5× | Upper Sec 2× | Lower Sec 1.5× | Primary 1×. Rewards climbing beyond primary.")
h()
ldf = df.dropna(subset=["ladder_score_2015"]).sort_values("ladder_score_2015", ascending=False).head(60)
pipe_table(
    ["Rank","Country","Primary","Lower Sec","Upper Sec","College","Ladder Score","Edu Score"],
    [[i+1, cn(r.country),
      pct(r.pri_2015), pct(r.low_2015), pct(r.upp_2015), pct(r.col_2015),
      f"{r.ladder_score_2015:.1f}", f"{r.edu_score_2015:.1f}"]
     for i, (_, r) in enumerate(ldf.iterrows())],
    ["right","left","right","right","right","right","right","right"]
)

# ── Write report ──────────────────────────────────────────────────────────────
with open(OUT_MD, "w") as f:
    f.write("\n".join(lines))
print(f"  Markdown saved: {OUT_MD}")
print(f"  Lines: {len(lines)}")
print("\nDone.")
