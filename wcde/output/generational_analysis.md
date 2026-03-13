# Generational Transmission of Education — WCDE v3

*Does parental education or GDP growth better explain a country's education progress?*
*Testing the leapfrog hypothesis: intergenerational transmission as primary mechanism.*

## Data

- **Countries:** 189 (WCDE v3, 228 entities minus regional aggregates)
- **Target:** lower secondary completion rate (% of 20–24 cohort)
- **Parental proxy:** same country's lower secondary completion 25 years earlier (T−25)
  - Child year 1975 → parent year 1950; child year 2015 → parent year 1990; etc.
- **Panel obs (1975–2015):** 1701 country-years

### Methodological note on pre-1960 parent data

WCDE v3 provides data from 1950. The 1950 and 1955 parent-year observations are included
but have a different interpretation depending on country history:

- **Japan, Europe, North America, Latin America**: pre-1960 data reflects genuine domestic
  education investment decisions, extending the panel usefully.
- **Colonised countries (Africa, South/Southeast Asia)**: pre-1960 schooling reflects
  colonial policy, not the independent state's choices. The T−25 parental signal is valid
  as a mechanistic predictor (a parent educated under colonialism still transmits literacy)
  but the *policy* interpretation does not apply.
- **Sri Lanka (anomaly)**: British colonial policy in Ceylon actively invested in education,
  unlike most colonies. Sri Lanka consistently appears as an over-performer in 1975–1985
  child cohorts because its 1950 colonial-era parental education was already high relative
  to income. This is a genuine structural advantage, not a data artefact.

## Regression Results

| Model | Specification | Parental β | GDP β | R² |
|---|---|---|---|---|
| 1 | OLS: child ~ parent (pooled) | 0.847 | — | 0.800 |
| 2 | OLS: child ~ parent + log GDP (pooled) | 0.704 | 4.788 | 0.845 |
| 3 | FE: child ~ parent (within-country) | 0.485 | — | 0.464 |
| 4 | FE: child ~ parent + log GDP (within-country) | 0.490 | 5.142 | 0.531 |
| 5 | FE: child ~ log GDP only | — | 15.808 | 0.266 |

### Interpretation

- **Model 1**: Every 1 pp increase in parental lower-secondary completion predicts **0.85 pp** gain in child completion (pooled). R²=0.80 — parental education alone explains 80% of cross-country variance.

- **Model 3 (FE)**: Within the same country over time, a 1 pp rise in parental completion predicts **0.48 pp** gain in child completion. This controls for all fixed country characteristics (culture, institutions, colonial history).

- **Model 4 vs 3**: Adding log GDP raises R² from 0.464 to 0.531. Parental education remains the dominant predictor; GDP adds marginal explanatory power.

- **Model 5**: Log GDP alone (FE) explains only R²=0.266 of within-country education variation — far less than parental education (R²=0.464). **Income growth cannot substitute for the generational transmission pathway.**

---

## Table 1 — Countries Where Generational Transmission is Strongest

Per-country OLS β of child lower-sec on parent lower-sec. High β = strong transmission.

| Rank | Country | Parental β | R² | Low Sec 2015 | Obs |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Maldives | 5.742 | 0.922 | 87.2% | 9 |
| 2 | Yemen | 5.662 | 0.830 | 49.1% | 9 |
| 3 | Rwanda | 3.953 | 0.971 | 22.5% | 9 |
| 4 | Bhutan | 3.217 | 0.983 | 66.0% | 9 |
| 5 | Cape Verde | 3.061 | 0.777 | 64.9% | 9 |
| 6 | Burundi | 2.694 | 0.966 | 14.2% | 9 |
| 7 | Chad | 2.485 | 0.992 | 21.4% | 9 |
| 8 | Bangladesh | 2.364 | 0.959 | 52.6% | 9 |
| 9 | Ethiopia | 2.165 | 0.975 | 15.2% | 9 |
| 10 | Nepal | 2.092 | 0.983 | 65.0% | 9 |
| 11 | Mozambique | 2.071 | 0.975 | 26.0% | 9 |
| 12 | Mali | 1.920 | 0.638 | 24.0% | 9 |
| 13 | Uganda | 1.920 | 0.952 | 32.6% | 9 |
| 14 | Tunisia | 1.898 | 0.915 | 93.7% | 9 |
| 15 | United Republic of Tanzania | 1.896 | 0.715 | 29.6% | 9 |
| 16 | Gambia | 1.890 | 0.975 | 50.5% | 9 |
| 17 | Angola | 1.856 | 0.881 | 33.8% | 9 |
| 18 | Benin | 1.770 | 0.699 | 37.3% | 9 |
| 19 | Guatemala | 1.767 | 0.989 | 49.5% | 9 |
| 20 | Sierra Leone | 1.761 | 0.773 | 48.3% | 9 |
| 21 | Botswana | 1.746 | 0.939 | 86.1% | 9 |
| 22 | Timor-Leste | 1.701 | 0.709 | 68.8% | 9 |
| 23 | Thailand | 1.633 | 0.953 | 89.5% | 9 |
| 24 | Kiribati | 1.534 | 0.987 | 82.5% | 9 |
| 25 | Paraguay | 1.513 | 0.991 | 64.1% | 9 |
| 26 | Lesotho | 1.503 | 0.975 | 42.8% | 9 |
| 27 | Cambodia | 1.462 | 0.538 | 38.6% | 9 |
| 28 | India | 1.445 | 0.984 | 67.1% | 9 |
| 29 | Solomon Islands | 1.445 | 0.897 | 49.7% | 9 |
| 30 | Bolivia (Plurinational State of) | 1.416 | 0.992 | 84.4% | 9 |

## Table 2 — Countries Where Parental Transmission Broke Down

Low β means child education is not well predicted by parental education — either disruption or leapfrog policy.

| Rank | Country | Parental β | R² | Low Sec 2015 | Obs |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 170 | Hungary | 0.041 | 0.580 | 99.4% | 9 |
| 171 | Romania | 0.029 | 0.134 | 97.7% | 9 |
| 172 | Kazakhstan | 0.023 | 0.606 | 99.0% | 9 |
| 173 | Tajikistan | 0.017 | 0.188 | 95.8% | 9 |
| 174 | Republic of Moldova | 0.016 | 0.364 | 97.9% | 9 |
| 175 | Georgia | 0.015 | 0.396 | 98.6% | 9 |
| 176 | Armenia | 0.009 | 0.785 | 99.1% | 9 |
| 177 | Kyrgyzstan | 0.009 | 0.196 | 98.4% | 9 |
| 178 | Belarus | 0.009 | 0.578 | 99.9% | 9 |
| 179 | Ukraine | 0.007 | 0.554 | 99.9% | 9 |
| 180 | Russian Federation | 0.003 | 0.023 | 98.5% | 9 |
| 181 | Democratic People's Republic of Ko | 0.001 | 0.798 | 100.0% | 9 |
| 182 | Estonia | -0.010 | 0.056 | 98.3% | 9 |
| 183 | Japan | -0.011 | 0.057 | 99.9% | 9 |
| 184 | Lithuania | -0.013 | 0.263 | 98.0% | 9 |
| 185 | Poland | -0.035 | 0.079 | 99.1% | 9 |
| 186 | Bulgaria | -0.068 | 0.280 | 93.2% | 9 |
| 187 | Latvia | -0.082 | 0.419 | 97.7% | 9 |
| 188 | Norway | -0.938 | 0.088 | 99.9% | 9 |
| 189 | Denmark | -0.997 | 0.771 | 100.0% | 9 |

## Table 3 — Countries Outperforming Their Parental + Income Prediction (2015)

OLS residual from Model 2 (child ~ parental education + log GDP) in 2015.
Positive = country delivered more lower-secondary completion than income and parental history predict.

| Rank | Country | Low Sec 2015 | Parental Low Sec | Residual |
| ---: | :--- | ---: | ---: | ---: |
| 1 | Maldives | 87.2% | 16.0% | +40.3 pp |
| 2 | Tunisia | 93.7% | 38.1% | +35.4 pp |
| 3 | Thailand | 89.5% | 44.9% | +24.4 pp |
| 4 | Cape Verde | 64.9% | 16.2% | +23.2 pp |
| 5 | Bhutan | 66.0% | 18.7% | +22.9 pp |
| 6 | Kiribati | 82.5% | 46.3% | +22.7 pp |
| 7 | Botswana | 86.1% | 41.9% | +22.4 pp |
| 8 | Nepal | 65.0% | 27.2% | +21.4 pp |
| 9 | Timor-Leste | 68.8% | 32.8% | +19.3 pp |
| 10 | Bolivia (Plurinational State of) | 84.4% | 49.8% | +18.9 pp |
| 11 | Samoa | 95.3% | 64.1% | +18.4 pp |
| 12 | Yemen | 49.1% | 7.7% | +16.4 pp |
| 13 | Iran (Islamic Republic of) | 82.5% | 48.8% | +15.6 pp |
| 14 | Turkey | 92.8% | 59.1% | +14.6 pp |
| 15 | India | 67.1% | 36.7% | +13.9 pp |
| 16 | Sierra Leone | 48.3% | 17.1% | +13.8 pp |
| 17 | Malawi | 54.3% | 29.0% | +13.5 pp |
| 18 | Portugal | 90.8% | 55.3% | +12.6 pp |
| 19 | Oman | 82.5% | 45.0% | +12.5 pp |
| 20 | Colombia | 78.4% | 45.8% | +12.4 pp |

## Table 4 — Countries Underperforming Their Parental + Income Prediction (2015)

| Rank | Country | Low Sec 2015 | Parental Low Sec | Residual |
| ---: | :--- | ---: | ---: | ---: |
| 1 | Qatar | 53.8% | 53.3% | -28.6 pp |
| 2 | Equatorial Guinea | 36.5% | 27.4% | -19.4 pp |
| 3 | Burkina Faso | 10.3% | 8.3% | -18.5 pp |
| 4 | Iraq | 43.5% | 38.1% | -15.7 pp |
| 5 | Norway | 99.9% | 99.2% | -15.7 pp |
| 6 | Niger | 8.9% | 4.2% | -15.6 pp |
| 7 | Liberia | 30.3% | 31.1% | -15.0 pp |
| 8 | Iceland | 100.0% | 99.9% | -14.5 pp |
| 9 | Austria | 98.2% | 98.7% | -14.4 pp |
| 10 | Switzerland | 97.8% | 93.5% | -14.4 pp |
| 11 | Australia | 99.1% | 97.6% | -14.0 pp |
| 12 | Gabon | 47.1% | 37.6% | -13.9 pp |
| 13 | Denmark | 100.0% | 99.1% | -13.9 pp |
| 14 | Finland | 99.5% | 99.7% | -13.8 pp |
| 15 | Netherlands | 95.1% | 92.7% | -13.4 pp |
| 16 | United States of America | 98.0% | 95.1% | -13.4 pp |
| 17 | Sweden | 99.3% | 97.6% | -13.4 pp |
| 18 | Spain | 89.2% | 87.3% | -12.9 pp |
| 19 | South Sudan | 21.2% | 12.0% | -12.9 pp |
| 20 | Japan | 99.9% | 99.9% | -12.6 pp |

---

## Key Finding

Across all model specifications, **parental education is the dominant predictor of education progress**,
both in cross-country comparisons and within the same country over time.
Income growth explains a fraction of the within-country variation that parental education does.

This is consistent with the leapfrog thesis:
countries that invested in education early created a self-reinforcing generational multiplier
that income-poor countries without that base cannot replicate through economic growth alone.

---

*WCDE v3 data. Lower secondary completion (% of 20–24 cohort). T−25 lag. Historical data 1985–2015.*
*GDP data: World Bank inflation-adjusted USD per capita (1285 obs).*