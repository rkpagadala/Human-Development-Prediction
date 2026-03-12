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
| 1 | OLS: child ~ parent (pooled) | 0.864 | — | 0.773 |
| 2 | OLS: child ~ parent + log GDP (pooled) | 0.701 | 5.791 | 0.829 |
| 3 | FE: child ~ parent (within-country) | 0.493 | — | 0.423 |
| 4 | FE: child ~ parent + log GDP (within-country) | 0.468 | 7.306 | 0.478 |
| 5 | FE: child ~ log GDP only | — | 17.784 | 0.264 |

### Interpretation

- **Model 1**: Every 1 pp increase in parental lower-secondary completion predicts **0.86 pp** gain in child completion (pooled). R²=0.77 — parental education alone explains 77% of cross-country variance.

- **Model 3 (FE)**: Within the same country over time, a 1 pp rise in parental completion predicts **0.49 pp** gain in child completion. This controls for all fixed country characteristics (culture, institutions, colonial history).

- **Model 4 vs 3**: Adding log GDP raises R² from 0.423 to 0.478. Parental education remains the dominant predictor; GDP adds marginal explanatory power.

- **Model 5**: Log GDP alone (FE) explains only R²=0.264 of within-country education variation — far less than parental education (R²=0.423). **Income growth cannot substitute for the generational transmission pathway.**

---

## Table 1 — Countries Where Generational Transmission is Strongest

Per-country OLS β of child lower-sec on parent lower-sec. High β = strong transmission.

| Rank | Country | Parental β | R² | Low Sec 2015 | Obs |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Yemen | 29.227 | 0.929 | 27.6% | 9 |
| 2 | Maldives | 8.065 | 0.836 | 91.7% | 9 |
| 3 | Bhutan | 7.046 | 0.959 | 65.1% | 9 |
| 4 | Rwanda | 6.078 | 0.948 | 21.5% | 9 |
| 5 | Chad | 5.653 | 0.857 | 12.9% | 9 |
| 6 | Nepal | 4.761 | 0.955 | 61.4% | 9 |
| 7 | Cape Verde | 4.626 | 0.933 | 66.8% | 9 |
| 8 | Burundi | 4.136 | 0.977 | 12.9% | 9 |
| 9 | Gambia | 3.921 | 0.889 | 48.1% | 9 |
| 10 | Ethiopia | 3.739 | 0.972 | 14.6% | 9 |
| 11 | Angola | 3.496 | 0.934 | 26.1% | 9 |
| 12 | Uganda | 3.464 | 0.970 | 29.4% | 9 |
| 13 | Mozambique | 3.408 | 0.959 | 21.1% | 9 |
| 14 | Bangladesh | 3.353 | 0.999 | 54.5% | 9 |
| 15 | Mali | 3.297 | 0.790 | 18.2% | 9 |
| 16 | Niger | 3.234 | 0.880 | 6.1% | 9 |
| 17 | Sierra Leone | 3.141 | 0.793 | 36.4% | 9 |
| 18 | Tunisia | 3.096 | 0.957 | 93.3% | 9 |
| 19 | United Republic of Tanzania | 2.948 | 0.922 | 26.5% | 9 |
| 20 | Sao Tome and Principe | 2.866 | 0.920 | 40.0% | 9 |
| 21 | Timor-Leste | 2.733 | 0.695 | 68.0% | 9 |
| 22 | Comoros | 2.564 | 0.921 | 52.5% | 9 |
| 23 | Guinea-Bissau | 2.477 | 0.843 | 21.2% | 9 |
| 24 | Benin | 2.418 | 0.587 | 28.6% | 9 |
| 25 | Togo | 2.416 | 0.755 | 27.4% | 9 |
| 26 | Solomon Islands | 2.377 | 0.904 | 49.9% | 9 |
| 27 | South Sudan | 2.340 | 0.945 | 16.7% | 9 |
| 28 | Cote d'Ivoire | 2.193 | 0.964 | 23.5% | 9 |
| 29 | Cambodia | 2.138 | 0.809 | 34.6% | 9 |
| 30 | Guatemala | 2.094 | 0.988 | 46.5% | 9 |

## Table 2 — Countries Where Parental Transmission Broke Down

Low β means child education is not well predicted by parental education — either disruption or leapfrog policy.

| Rank | Country | Parental β | R² | Low Sec 2015 | Obs |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 170 | Romania | 0.043 | 0.265 | 97.9% | 9 |
| 171 | Georgia | 0.031 | 0.711 | 98.6% | 9 |
| 172 | Kazakhstan | 0.024 | 0.607 | 99.2% | 9 |
| 173 | Tajikistan | 0.023 | 0.315 | 96.2% | 9 |
| 174 | Republic of Moldova | 0.018 | 0.390 | 98.1% | 9 |
| 175 | Kyrgyzstan | 0.015 | 0.378 | 98.5% | 9 |
| 176 | Armenia | 0.014 | 0.860 | 99.3% | 9 |
| 177 | Belarus | 0.007 | 0.585 | 99.9% | 9 |
| 178 | Russian Federation | 0.004 | 0.060 | 98.9% | 9 |
| 179 | Ukraine | 0.003 | 0.376 | 100.0% | 9 |
| 180 | Democratic People's Republic of Ko | 0.001 | 0.763 | 100.0% | 9 |
| 181 | Estonia | -0.003 | 0.015 | 98.7% | 9 |
| 182 | Lithuania | -0.008 | 0.153 | 98.0% | 9 |
| 183 | Japan | -0.013 | 0.064 | 99.9% | 9 |
| 184 | Poland | -0.019 | 0.074 | 99.2% | 9 |
| 185 | Bulgaria | -0.047 | 0.183 | 92.6% | 9 |
| 186 | Latvia | -0.050 | 0.324 | 97.8% | 9 |
| 187 | Iceland | -0.160 | 0.023 | 99.9% | 9 |
| 188 | Denmark | -1.020 | 0.718 | 100.0% | 9 |
| 189 | Norway | -1.390 | 0.321 | 99.9% | 9 |

## Table 3 — Countries Outperforming Their Parental + Income Prediction (2015)

OLS residual from Model 2 (child ~ parental education + log GDP) in 2015.
Positive = country delivered more lower-secondary completion than income and parental history predict.

| Rank | Country | Low Sec 2015 | Parental Low Sec | Residual |
| ---: | :--- | ---: | ---: | ---: |
| 1 | Maldives | 91.7% | 12.2% | +46.2 pp |
| 2 | Tunisia | 93.3% | 28.1% | +41.6 pp |
| 3 | Kiribati | 87.0% | 44.1% | +29.4 pp |
| 4 | Nepal | 61.4% | 13.0% | +28.6 pp |
| 5 | Bhutan | 65.1% | 9.7% | +28.3 pp |
| 6 | Thailand | 92.1% | 42.6% | +27.8 pp |
| 7 | Cape Verde | 66.8% | 13.4% | +26.7 pp |
| 8 | Timor-Leste | 68.0% | 22.6% | +26.3 pp |
| 9 | Botswana | 88.2% | 39.1% | +25.5 pp |
| 10 | Bolivia (Plurinational State of) | 83.6% | 43.7% | +22.3 pp |
| 11 | Oman | 88.8% | 38.8% | +21.4 pp |
| 12 | Iran (Islamic Republic of) | 82.4% | 40.7% | +20.5 pp |
| 13 | Turkey | 90.1% | 45.8% | +19.9 pp |
| 14 | India | 63.8% | 25.8% | +18.8 pp |
| 15 | Bangladesh | 54.5% | 15.5% | +18.2 pp |
| 16 | Gambia | 48.1% | 11.9% | +18.0 pp |
| 17 | Indonesia | 77.0% | 41.1% | +17.1 pp |
| 18 | Egypt | 74.5% | 38.7% | +15.8 pp |
| 19 | Samoa | 96.4% | 69.4% | +15.5 pp |
| 20 | Comoros | 52.5% | 16.7% | +15.4 pp |

## Table 4 — Countries Underperforming Their Parental + Income Prediction (2015)

| Rank | Country | Low Sec 2015 | Parental Low Sec | Residual |
| ---: | :--- | ---: | ---: | ---: |
| 1 | Equatorial Guinea | 27.0% | 13.3% | -20.6 pp |
| 2 | Norway | 99.9% | 99.0% | -18.6 pp |
| 3 | Iceland | 99.9% | 99.9% | -17.2 pp |
| 4 | Switzerland | 97.8% | 92.7% | -17.1 pp |
| 5 | Australia | 99.3% | 97.7% | -16.7 pp |
| 6 | Denmark | 100.0% | 98.8% | -16.5 pp |
| 7 | United States of America | 98.4% | 95.6% | -16.1 pp |
| 8 | Burkina Faso | 9.0% | 4.8% | -16.1 pp |
| 9 | Finland | 100.0% | 99.8% | -15.9 pp |
| 10 | Sweden | 99.4% | 97.2% | -15.7 pp |
| 11 | Austria | 99.4% | 98.3% | -15.7 pp |
| 12 | Niger | 6.1% | 1.7% | -15.1 pp |
| 13 | Netherlands | 96.1% | 92.4% | -14.9 pp |
| 14 | Japan | 99.9% | 99.9% | -14.9 pp |
| 15 | Ireland | 98.9% | 93.8% | -14.9 pp |
| 16 | Spain | 90.1% | 88.3% | -14.7 pp |
| 17 | Germany | 99.1% | 96.5% | -14.3 pp |
| 18 | Canada | 99.4% | 96.4% | -14.2 pp |
| 19 | Belgium | 96.0% | 91.8% | -14.0 pp |
| 20 | New Zealand | 97.1% | 93.8% | -14.0 pp |

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