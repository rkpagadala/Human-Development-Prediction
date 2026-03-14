"""
11_education_gap_combined.py

Education gap table for all countries, using the correct cohort year
for each education level to reflect who is dropping out TODAY:

  Primary not completing     → 2035 cohort (currently in primary, age ~6-12)
  Lower secondary not comp.  → 2030 cohort (currently in lower sec, age ~12-17)
  Upper secondary not comp.  → 2025 cohort (currently in upper sec, age ~16-19)

Output: analysis/education_gap_all_countries.md
"""

import pandas as pd
import os

pop = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/raw/pop_both.csv"))

edu_order = ["Under 15","No Education","Incomplete Primary","Primary",
             "Lower Secondary","Upper Secondary","Post Secondary"]

region_keywords = [
    "Africa","Asia","Europe","America","Caribbean","Oceania",
    "World","Eastern","Western","Northern","Southern","Central",
    "Sub-Saharan","Latin","Middle East","North Africa",
    "Developed","Developing","Less developed","Least developed",
    "Low income","Lower middle","Upper middle","High income",
    "OECD","EU","G20",
]
def is_region(name):
    return any(kw.lower() in name.lower() for kw in region_keywords)

def get_cohort(year):
    df = pop[
        (pop["scenario"]==2) &
        (pop["age"]=="20--24") &
        (pop["year"]==year)
    ].groupby(["name","education"],as_index=False)["pop"].sum()
    piv = df.pivot_table(index="name",columns="education",values="pop",aggfunc="sum").fillna(0)
    for col in edu_order:
        if col not in piv.columns: piv[col]=0.0
    piv["total"]      = piv[edu_order].sum(axis=1)
    piv["miss_prim"]  = piv["No Education"]+piv["Under 15"]+piv["Incomplete Primary"]
    piv["miss_lower"] = piv["miss_prim"]+piv["Primary"]
    piv["miss_upper"] = piv["miss_lower"]+piv["Lower Secondary"]
    return piv[piv.total > 10]  # drop micro-states

c2025 = get_cohort(2025)
c2030 = get_cohort(2030)
c2035 = get_cohort(2035)

countries = set(c2025.index) & set(c2030.index) & set(c2035.index)
countries = {c for c in countries if not is_region(c)}

rows = []
for country in countries:
    rows.append({
        "name":       country,
        "prim_miss":  c2035.loc[country,"miss_prim"],
        "prim_total": c2035.loc[country,"total"],
        "prim_pct":   c2035.loc[country,"miss_prim"]/c2035.loc[country,"total"]*100,
        "lower_miss": c2030.loc[country,"miss_lower"],
        "lower_total":c2030.loc[country,"total"],
        "lower_pct":  c2030.loc[country,"miss_lower"]/c2030.loc[country,"total"]*100,
        "upper_miss": c2025.loc[country,"miss_upper"],
        "upper_total":c2025.loc[country,"total"],
        "upper_pct":  c2025.loc[country,"miss_upper"]/c2025.loc[country,"total"]*100,
    })

df = pd.DataFrame(rows).sort_values("lower_miss", ascending=False).reset_index(drop=True)

def fM(x):
    m = x/1000
    return f"{m:.1f}M" if m >= 0.05 else "<0.1M"
def fp(x):
    return f"{x:.0f}%"

lines = []
lines.append("---")
lines.append("layout: page")
lines.append("title: Education Gap — All Countries")
lines.append("---")
lines.append("")
lines.append("# Education Gap — All Countries")
lines.append("")
lines.append("*Each education level uses the cohort year that reflects who is dropping out **today**, not historical completions.*")
lines.append("")
lines.append("| Level | Cohort year used | Who it represents |")
lines.append("|---|---|---|")
lines.append("| Not completing primary | **2035** | Children currently in primary school (age ~6–12) |")
lines.append("| Not completing lower secondary | **2030** | Children currently in or approaching lower secondary (age ~12–17) |")
lines.append("| Not completing upper secondary | **2025** | Young people currently in upper secondary (age ~16–19) |")
lines.append("")
lines.append("Sorted by lower secondary intervention target, largest first. Click column headers to sort.")
lines.append("")

# Global totals
g = df
gpt = g["prim_total"].sum(); gpm = g["prim_miss"].sum()
glt = g["lower_total"].sum(); glm = g["lower_miss"].sum()
gut = g["upper_total"].sum(); gum = g["upper_miss"].sum()

lines.append("## Global Totals")
lines.append("")
lines.append("| Level | Not completing | % of cohort |")
lines.append("|---|---:|---:|")
lines.append(f"| Not completing primary (2035 cohort, {fM(gpt)} total) | {fM(gpm)} | {fp(gpm/gpt*100)} |")
lines.append(f"| Not completing lower secondary (2030 cohort, {fM(glt)} total) | {fM(glm)} | {fp(glm/glt*100)} |")
lines.append(f"| Not completing upper secondary (2025 cohort, {fM(gut)} total) | {fM(gum)} | {fp(gum/gut*100)} |")
lines.append("")

lines.append("## All Countries")
lines.append("")
lines.append("| Country | Not completing primary (2035) | | Not completing lower sec (2030) | | Not completing upper sec (2025) | |")
lines.append("|---|---:|---:|---:|---:|---:|---:|")

for _, row in df.iterrows():
    lines.append(
        f"| {row['name']} "
        f"| {fM(row['prim_miss'])} | {fp(row['prim_pct'])} "
        f"| {fM(row['lower_miss'])} | {fp(row['lower_pct'])} "
        f"| {fM(row['upper_miss'])} | {fp(row['upper_pct'])} |"
    )
lines.append("")

out = os.path.join(os.path.dirname(__file__), "../../analysis/education_gap_all_countries.md")
with open(out, "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Written: {out}  ({len(df)} countries)")
print(f"Global primary not completing (2035):   {gpm/1000:.0f}M ({gpm/gpt*100:.0f}%)")
print(f"Global lower sec not completing (2030):  {glm/1000:.0f}M ({glm/glt*100:.0f}%)")
print(f"Global upper sec not completing (2025):  {gum/1000:.0f}M ({gum/gut*100:.0f}%)")
