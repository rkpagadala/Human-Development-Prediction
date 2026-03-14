---
layout: page
---

# Policy-Adjusted Education Ranking — WCDE v3

*Supersedes prior analysis/policy_residual_ranking.md (old model included GDP as predictor — bad control: education causes income, so controlling for income blocks the education signal). This version uses country fixed effects on parental education only. Source: wcde/output/policy_residual.md.*


*Which countries delivered more lower-secondary education than their parental education history predicts?*

## Method

**Target:** lower secondary completion rate (% of 20–24 cohort) at year T
**Predictor:** parental lower secondary completion at T−25
**Model:** country fixed effects (within-country variation only)

GDP is intentionally excluded as a predictor. Because education causes GDP
(see education_outcomes.md), controlling for current income would block part of the
education signal via the income channel — a bad control / mediation problem. Countries
like Korea and Singapore that invested early in education, grew rich as a result, and
continued investing would otherwise show as under-performers because the model assigns
credit for their education gains to their income. The residual here measures policy
contribution above the intergenerational inheritance baseline only. GDP is shown in
the tables for context.

Fixed effects coefficient:
- Parental lower secondary: **0.458** pp per 1 pp of parental completion
- Panel: 1323 obs, 189 countries

**Residual = actual − predicted.** Positive residual = policy over-performance.

---

## Table 1 — Biggest Over-Performers in 2015 (FE Residual)

| Rank | Country | Low Sec 2015 | FE Residual | OLS Residual | GDP/capita 2015 |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Maldives | 87.2% | +34.9 pp | +47.5 pp | $9,030 |
| 2 | Cape Verde | 64.9% | +26.3 pp | +25.1 pp | $3,040 |
| 3 | Bhutan | 66.0% | +26.1 pp | +24.1 pp | $2,750 |
| 4 | Tunisia | 93.7% | +25.5 pp | +35.7 pp | $3,860 |
| 5 | Yemen | 49.1% | +24.6 pp | +16.3 pp | $1,600 |
| 6 | Sierra Leone | 48.3% | +20.2 pp | +7.8 pp | $588 |
| 7 | Bahrain | 87.3% | +19.6 pp | +17.9 pp | $22,600 |
| 8 | Kuwait | 87.7% | +17.9 pp | +13.4 pp | $29,900 |
| 9 | Nepal | 65.0% | +17.8 pp | +16.1 pp | $902 |
| 10 | Botswana | 86.1% | +16.5 pp | +25.0 pp | $6,800 |
| 11 | Benin | 37.3% | +16.5 pp | +0.8 pp | $1,080 |
| 12 | Viet Nam | 80.8% | +16.0 pp | +12.1 pp | $2,090 |
| 13 | Bangladesh | 52.6% | +15.8 pp | +7.1 pp | $1,250 |
| 14 | Thailand | 89.5% | +15.8 pp | +25.8 pp | $5,840 |
| 15 | India | 67.1% | +14.1 pp | +10.2 pp | $1,610 |
| 16 | Mauritius | 80.5% | +13.7 pp | +14.3 pp | $9,260 |
| 17 | Kiribati | 82.5% | +13.6 pp | +17.6 pp | $1,540 |
| 18 | Bolivia (Plurinational State of) | 84.4% | +13.4 pp | +16.6 pp | $3,040 |
| 19 | Sao Tome and Principe | 39.1% | +13.4 pp | -1.1 pp | $1,580 |
| 20 | Angola | 33.8% | +13.3 pp | -2.9 pp | $4,170 |
| 21 | Gambia | 50.5% | +13.0 pp | +6.2 pp | $661 |
| 22 | Guinea | 29.6% | +12.6 pp | -4.3 pp | $769 |
| 23 | Morocco | 51.9% | +12.6 pp | +3.6 pp | $3,220 |
| 24 | Guatemala | 49.5% | +12.5 pp | +3.1 pp | $3,990 |
| 25 | Timor-Leste | 68.8% | +12.4 pp | +15.2 pp | $1,330 |
| 26 | Colombia | 78.4% | +12.4 pp | +14.0 pp | $6,180 |
| 27 | Saint Vincent and the Grenadines | 73.1% | +12.3 pp | +12.6 pp | n/a |
| 28 | Malawi | 54.3% | +12.2 pp | +3.9 pp | $381 |
| 29 | United Republic of Tanzania | 29.6% | +12.1 pp | -4.8 pp | $872 |
| 30 | Myanmar | 43.5% | +11.7 pp | -1.5 pp | $1,140 |

## Table 2 — Biggest Under-Performers in 2015 (FE Residual)

| Rank | Country | Low Sec 2015 | FE Residual | OLS Residual | GDP/capita 2015 |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Malta | 99.9% | -15.5 pp | -9.2 pp | $24,900 |
| 2 | Taiwan Province of China | 99.7% | -13.4 pp | -7.3 pp | n/a |
| 3 | Zimbabwe | 71.2% | -11.5 pp | -12.3 pp | $1,450 |
| 4 | Republic of Korea | 99.9% | -10.0 pp | -8.0 pp | $28,700 |
| 5 | Finland | 99.5% | -9.8 pp | -9.7 pp | $42,800 |
| 6 | Spain | 89.2% | -8.7 pp | -9.7 pp | $25,700 |
| 7 | Bosnia and Herzegovina | 98.8% | -8.2 pp | -7.9 pp | $4,730 |
| 8 | Micronesia (Federated States of) | 81.2% | -7.8 pp | -12.7 pp | n/a |
| 9 | Cyprus | 97.4% | -7.7 pp | -5.2 pp | $27,900 |
| 10 | Mongolia | 90.6% | -7.6 pp | -13.0 pp | $3,920 |
| 11 | Swaziland | 46.0% | -7.6 pp | -17.2 pp | n/a |
| 12 | Italy | 99.5% | -7.3 pp | -4.9 pp | $30,200 |
| 13 | Greece | 93.2% | -7.3 pp | -3.3 pp | $18,100 |
| 14 | Albania | 96.3% | -7.0 pp | -10.1 pp | $3,950 |
| 15 | Singapore | 99.2% | -6.9 pp | -1.1 pp | $55,600 |
| 16 | Montenegro | 96.3% | -6.5 pp | -11.2 pp | $6,520 |
| 17 | Ireland | 98.8% | -6.5 pp | -5.2 pp | $62,000 |
| 18 | Jamaica | 95.3% | -6.4 pp | -1.5 pp | $4,910 |
| 19 | Serbia | 97.8% | -6.2 pp | -9.5 pp | $5,590 |
| 20 | The former Yugoslav Republic of  | 96.0% | -6.0 pp | -4.6 pp | n/a |
| 21 | Hong Kong Special Administrative | 97.7% | -5.9 pp | +0.9 pp | n/a |
| 22 | Macao Special Administrative Reg | 93.4% | -5.4 pp | +3.2 pp | n/a |
| 23 | Bahamas | 99.0% | -5.3 pp | -6.5 pp | $31,300 |
| 24 | Chile | 96.6% | -5.1 pp | +0.1 pp | $13,600 |
| 25 | Kenya | 62.4% | -4.8 pp | -6.2 pp | $1,340 |
| 26 | Qatar | 53.8% | -4.8 pp | -16.8 pp | $63,000 |
| 27 | Malaysia | 96.3% | -4.6 pp | +3.2 pp | $9,960 |
| 28 | New Caledonia | 98.4% | -4.5 pp | +1.6 pp | n/a |
| 29 | Republic of Moldova | 97.9% | -4.5 pp | -9.6 pp | $2,730 |
| 30 | Curaçao | 89.5% | -4.3 pp | -9.3 pp | $20,000 |

## Table 3 — Chronic Over-Performers (Mean OLS Residual Across All Years)

Countries that consistently outperformed the global cross-country prediction across all years.

| Rank | Country | Low Sec 2015 | Mean OLS Residual | 2015 OLS Residual | 2015 FE Residual |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Macao Special Administrative Reg | 93.4% | +20.0 pp | +3.2 pp | -5.4 pp |
| 2 | Malaysia | 96.3% | +19.6 pp | +3.2 pp | -4.6 pp |
| 3 | Malta | 99.9% | +19.2 pp | -9.2 pp | -15.5 pp |
| 4 | Portugal | 90.8% | +18.7 pp | +18.5 pp | +8.1 pp |
| 5 | Taiwan Province of China | 99.7% | +18.6 pp | -7.3 pp | -13.4 pp |
| 6 | Turkey | 92.8% | +18.1 pp | +17.3 pp | +9.2 pp |
| 7 | Hong Kong Special Administrative | 97.7% | +17.9 pp | +0.9 pp | -5.9 pp |
| 8 | Algeria | 82.0% | +17.9 pp | +10.2 pp | +2.3 pp |
| 9 | Thailand | 89.5% | +17.1 pp | +25.8 pp | +15.8 pp |
| 10 | Trinidad and Tobago | 97.5% | +16.8 pp | +8.1 pp | +1.0 pp |
| 11 | China | 94.6% | +16.7 pp | +5.9 pp | -1.4 pp |
| 12 | Botswana | 86.1% | +16.7 pp | +25.0 pp | +16.5 pp |
| 13 | Tunisia | 93.7% | +16.5 pp | +35.7 pp | +25.5 pp |
| 14 | Maldives | 87.2% | +16.2 pp | +47.5 pp | +34.9 pp |
| 15 | Oman | 82.5% | +15.9 pp | +18.8 pp | +10.8 pp |
| 16 | New Caledonia | 98.4% | +15.6 pp | +1.6 pp | -4.5 pp |
| 17 | Fiji | 88.2% | +15.6 pp | +3.8 pp | -1.9 pp |
| 18 | Samoa | 95.3% | +15.6 pp | +15.7 pp | +8.7 pp |
| 19 | Singapore | 99.2% | +15.6 pp | -1.1 pp | -6.9 pp |
| 20 | Jamaica | 95.3% | +14.9 pp | -1.5 pp | -6.4 pp |
| 21 | Chile | 96.6% | +14.6 pp | +0.1 pp | -5.1 pp |
| 22 | Mexico | 86.1% | +14.6 pp | +6.7 pp | +1.8 pp |
| 23 | Reunion | 88.9% | +14.5 pp | +9.1 pp | +2.7 pp |
| 24 | Polynesia | 95.7% | +14.2 pp | +7.9 pp | +2.3 pp |
| 25 | Greece | 93.2% | +14.2 pp | -3.3 pp | -7.3 pp |
| 26 | South Africa | 86.5% | +13.4 pp | +6.6 pp | +1.3 pp |
| 27 | Tonga | 95.3% | +13.1 pp | -0.6 pp | -3.9 pp |
| 28 | Saint Lucia | 83.1% | +13.1 pp | +17.4 pp | +10.6 pp |
| 29 | Iran (Islamic Republic of) | 82.5% | +12.8 pp | +15.7 pp | +10.0 pp |
| 30 | French Polynesia | 96.2% | +12.6 pp | +5.9 pp | +0.8 pp |

## Table 4 — Chronic Under-Performers (Mean OLS Residual)

| Rank | Country | Low Sec 2015 | Mean OLS Residual | 2015 OLS Residual | 2015 FE Residual |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Niger | 8.9% | -22.6 pp | -21.0 pp | +2.4 pp |
| 2 | Burkina Faso | 10.3% | -20.9 pp | -23.0 pp | -0.5 pp |
| 3 | Central African Republic | 15.5% | -20.6 pp | -19.5 pp | +1.8 pp |
| 4 | Madagascar | 23.1% | -20.1 pp | -18.3 pp | +3.6 pp |
| 5 | Burundi | 14.2% | -19.6 pp | -16.4 pp | +4.2 pp |
| 6 | Ethiopia | 15.2% | -19.4 pp | -16.2 pp | +4.3 pp |
| 7 | Afghanistan | 22.4% | -19.0 pp | -11.6 pp | +8.5 pp |
| 8 | Mali | 24.0% | -18.1 pp | -8.0 pp | +10.7 pp |
| 9 | Somalia | 20.0% | -18.0 pp | -21.8 pp | -0.8 pp |
| 10 | Senegal | 27.1% | -17.6 pp | -10.7 pp | +8.3 pp |
| 11 | Rwanda | 22.5% | -17.4 pp | -8.8 pp | +9.7 pp |
| 12 | Chad | 21.4% | -17.1 pp | -11.0 pp | +7.2 pp |
| 13 | South Sudan | 21.2% | -16.9 pp | -15.2 pp | +3.7 pp |
| 14 | Guinea | 29.6% | -16.1 pp | -4.3 pp | +12.6 pp |
| 15 | United Republic of Tanzania | 29.6% | -15.8 pp | -4.8 pp | +12.1 pp |
| 16 | Mozambique | 26.0% | -15.3 pp | -8.7 pp | +8.2 pp |
| 17 | Liberia | 30.3% | -14.5 pp | -21.9 pp | -4.0 pp |
| 18 | Benin | 37.3% | -14.2 pp | +0.8 pp | +16.5 pp |
| 19 | Angola | 33.8% | -14.1 pp | -2.9 pp | +13.3 pp |
| 20 | Cote d'Ivoire | 31.6% | -13.6 pp | -7.4 pp | +8.4 pp |
| 21 | Equatorial Guinea | 36.5% | -13.5 pp | -12.6 pp | +3.9 pp |
| 22 | Togo | 35.5% | -13.4 pp | -3.7 pp | +11.2 pp |
| 23 | Uganda | 32.6% | -12.5 pp | -5.8 pp | +8.7 pp |
| 24 | Sao Tome and Principe | 39.1% | -11.9 pp | -1.1 pp | +13.4 pp |
| 25 | Zambia | 45.8% | -11.6 pp | -11.4 pp | +2.2 pp |
| 26 | Guinea-Bissau | 28.0% | -11.1 pp | -11.1 pp | +2.8 pp |
| 27 | Myanmar | 43.5% | -11.0 pp | -1.5 pp | +11.7 pp |
| 28 | Iraq | 43.5% | -9.9 pp | -14.5 pp | -0.0 pp |
| 29 | Sierra Leone | 48.3% | -9.8 pp | +7.8 pp | +20.2 pp |
| 30 | Germany | 98.9% | -9.5 pp | -7.8 pp | +1.7 pp |

## Table 5 — Full Country Ranking by 2015 FE Residual

| Rank | Country | Low Sec 2015 | FE Residual | OLS Residual |
| ---: | :--- | ---: | ---: | ---: |
| 1 | Maldives | 87.2% | +34.9 pp | +47.5 pp |
| 2 | Cape Verde | 64.9% | +26.3 pp | +25.1 pp |
| 3 | Bhutan | 66.0% | +26.1 pp | +24.1 pp |
| 4 | Tunisia | 93.7% | +25.5 pp | +35.7 pp |
| 5 | Yemen | 49.1% | +24.6 pp | +16.3 pp |
| 6 | Sierra Leone | 48.3% | +20.2 pp | +7.8 pp |
| 7 | Bahrain | 87.3% | +19.6 pp | +17.9 pp |
| 8 | Kuwait | 87.7% | +17.9 pp | +13.4 pp |
| 9 | Nepal | 65.0% | +17.8 pp | +16.1 pp |
| 10 | Botswana | 86.1% | +16.5 pp | +25.0 pp |
| 11 | Benin | 37.3% | +16.5 pp | +0.8 pp |
| 12 | Viet Nam | 80.8% | +16.0 pp | +12.1 pp |
| 13 | Bangladesh | 52.6% | +15.8 pp | +7.1 pp |
| 14 | Thailand | 89.5% | +15.8 pp | +25.8 pp |
| 15 | India | 67.1% | +14.1 pp | +10.2 pp |
| 16 | Mauritius | 80.5% | +13.7 pp | +14.3 pp |
| 17 | Kiribati | 82.5% | +13.6 pp | +17.6 pp |
| 18 | Bolivia (Plurinational State of) | 84.4% | +13.4 pp | +16.6 pp |
| 19 | Sao Tome and Principe | 39.1% | +13.4 pp | -1.1 pp |
| 20 | Angola | 33.8% | +13.3 pp | -2.9 pp |
| 21 | Gambia | 50.5% | +13.0 pp | +6.2 pp |
| 22 | Guinea | 29.6% | +12.6 pp | -4.3 pp |
| 23 | Morocco | 51.9% | +12.6 pp | +3.6 pp |
| 24 | Guatemala | 49.5% | +12.5 pp | +3.1 pp |
| 25 | Timor-Leste | 68.8% | +12.4 pp | +15.2 pp |
| 26 | Colombia | 78.4% | +12.4 pp | +14.0 pp |
| 27 | Saint Vincent and the Grenadines | 73.1% | +12.3 pp | +12.6 pp |
| 28 | Malawi | 54.3% | +12.2 pp | +3.9 pp |
| 29 | United Republic of Tanzania | 29.6% | +12.1 pp | -4.8 pp |
| 30 | Myanmar | 43.5% | +11.7 pp | -1.5 pp |
| 31 | Costa Rica | 67.9% | +11.2 pp | +5.4 pp |
| 32 | Togo | 35.5% | +11.2 pp | -3.7 pp |
| 33 | Oman | 82.5% | +10.8 pp | +18.8 pp |
| 34 | Mali | 24.0% | +10.7 pp | -8.0 pp |
| 35 | United Arab Emirates | 87.8% | +10.7 pp | +8.0 pp |
| 36 | Paraguay | 64.1% | +10.7 pp | +7.3 pp |
| 37 | Saint Lucia | 83.1% | +10.6 pp | +17.4 pp |
| 38 | Cameroon | 52.9% | +10.6 pp | +2.7 pp |
| 39 | Comoros | 51.1% | +10.5 pp | +3.4 pp |
| 40 | Saudi Arabia | 88.0% | +10.1 pp | +13.8 pp |
| 41 | Iran (Islamic Republic of) | 82.5% | +10.0 pp | +15.7 pp |
| 42 | Rwanda | 22.5% | +9.7 pp | -8.8 pp |
| 43 | Lao People's Democratic Republic | 41.7% | +9.6 pp | -2.9 pp |
| 44 | Honduras | 43.6% | +9.5 pp | -2.3 pp |
| 45 | Turkey | 92.8% | +9.2 pp | +17.3 pp |
| 46 | Belize | 59.9% | +8.7 pp | +2.2 pp |
| 47 | Samoa | 95.3% | +8.7 pp | +15.7 pp |
| 48 | Uganda | 32.6% | +8.7 pp | -5.8 pp |
| 49 | Brazil | 79.0% | +8.5 pp | +9.3 pp |
| 50 | Afghanistan | 22.4% | +8.5 pp | -11.6 pp |
| 51 | Cote d'Ivoire | 31.6% | +8.4 pp | -7.4 pp |
| 52 | Senegal | 27.1% | +8.3 pp | -10.7 pp |
| 53 | Mozambique | 26.0% | +8.2 pp | -8.7 pp |
| 54 | Portugal | 90.8% | +8.1 pp | +18.5 pp |
| 55 | Egypt | 76.8% | +7.9 pp | +10.3 pp |
| 56 | Vanuatu | 48.1% | +7.8 pp | -2.0 pp |
| 57 | Pakistan | 47.9% | +7.7 pp | -1.6 pp |
| 58 | Indonesia | 76.6% | +7.3 pp | +10.6 pp |
| 59 | Chad | 21.4% | +7.2 pp | -11.0 pp |
| 60 | Lesotho | 42.8% | +7.1 pp | -3.4 pp |
| 61 | Solomon Islands | 49.7% | +6.8 pp | -0.4 pp |
| 62 | El Salvador | 65.2% | +6.7 pp | +4.2 pp |
| 63 | Nigeria | 59.9% | +6.5 pp | +3.6 pp |
| 64 | Nicaragua | 49.3% | +6.4 pp | -3.6 pp |
| 65 | Sri Lanka | 90.7% | +5.5 pp | +8.0 pp |
| 66 | Syrian Arab Republic | 46.6% | +5.0 pp | -7.3 pp |
| 67 | Dominican Republic | 78.4% | +4.6 pp | +5.4 pp |
| 68 | Ecuador | 72.1% | +4.5 pp | +2.3 pp |
| 69 | Luxembourg | 98.2% | +4.4 pp | +3.1 pp |
| 70 | Ethiopia | 15.2% | +4.3 pp | -16.2 pp |
| 71 | Burundi | 14.2% | +4.2 pp | -16.4 pp |
| 72 | Peru | 87.0% | +4.2 pp | +5.7 pp |
| 73 | Argentina | 73.0% | +4.0 pp | +1.0 pp |
| 74 | Jordan | 76.5% | +4.0 pp | -2.6 pp |
| 75 | Equatorial Guinea | 36.5% | +3.9 pp | -12.6 pp |
| 76 | Occupied Palestinian Territory | 90.8% | +3.8 pp | +8.0 pp |
| 77 | Haiti | 45.5% | +3.8 pp | -3.8 pp |
| 78 | South Sudan | 21.2% | +3.7 pp | -15.2 pp |
| 79 | Madagascar | 23.1% | +3.6 pp | -18.3 pp |
| 80 | Ghana | 60.9% | +3.0 pp | -5.8 pp |
| 81 | Guyana | 91.0% | +2.9 pp | +2.8 pp |
| 82 | Cambodia | 38.6% | +2.8 pp | -7.8 pp |
| 83 | Guinea-Bissau | 28.0% | +2.8 pp | -11.1 pp |
| 84 | Reunion | 88.9% | +2.7 pp | +9.1 pp |
| 85 | Niger | 8.9% | +2.4 pp | -21.0 pp |
| 86 | Polynesia | 95.7% | +2.3 pp | +7.9 pp |
| 87 | Panama | 76.9% | +2.3 pp | -0.4 pp |
| 88 | Algeria | 82.0% | +2.3 pp | +10.2 pp |
| 89 | Zambia | 45.8% | +2.2 pp | -11.4 pp |
| 90 | Democratic Republic of the Congo | 59.6% | +1.9 pp | -5.5 pp |
| 91 | Mexico | 86.1% | +1.8 pp | +6.7 pp |
| 92 | Central African Republic | 15.5% | +1.8 pp | -19.5 pp |
| 93 | Germany | 98.9% | +1.7 pp | -7.8 pp |
| 94 | Micronesia | 81.8% | +1.6 pp | +1.1 pp |
| 95 | Venezuela (Bolivarian Republic o | 87.3% | +1.5 pp | +3.2 pp |
| 96 | Uruguay | 72.5% | +1.4 pp | -3.8 pp |
| 97 | Suriname | 82.2% | +1.4 pp | -0.6 pp |
| 98 | United States of America | 98.0% | +1.3 pp | -7.3 pp |
| 99 | South Africa | 86.5% | +1.3 pp | +6.6 pp |
| 100 | Switzerland | 97.8% | +1.1 pp | -6.2 pp |
| 101 | French Guiana | 64.9% | +1.1 pp | -11.1 pp |
| 102 | Trinidad and Tobago | 97.5% | +1.0 pp | +8.1 pp |
| 103 | French Polynesia | 96.2% | +0.8 pp | +5.9 pp |
| 104 | Denmark | 100.0% | +0.6 pp | -8.7 pp |
| 105 | Norway | 99.9% | +0.6 pp | -8.9 pp |
| 106 | Sudan | 38.6% | +0.5 pp | -10.4 pp |
| 107 | United Kingdom of Great Britain  | 100.0% | +0.1 pp | -9.1 pp |
| 108 | Slovakia | 100.0% | +0.1 pp | -9.3 pp |
| 109 | Czech Republic | 99.5% | +0.1 pp | -9.3 pp |
| 110 | Iceland | 100.0% | +0.0 pp | -9.4 pp |
| 111 | Iraq | 43.5% | -0.0 pp | -14.5 pp |
| 112 | Hungary | 99.4% | -0.2 pp | -8.5 pp |
| 113 | Israel | 90.2% | -0.3 pp | -5.4 pp |
| 114 | Lebanon | 85.0% | -0.3 pp | +3.4 pp |
| 115 | Burkina Faso | 10.3% | -0.5 pp | -23.0 pp |
| 116 | Poland | 99.1% | -0.6 pp | -10.0 pp |
| 117 | Canada | 99.2% | -0.7 pp | -7.0 pp |
| 118 | Aruba | 80.4% | -0.8 pp | -4.3 pp |
| 119 | Somalia | 20.0% | -0.8 pp | -21.8 pp |
| 120 | Philippines | 75.3% | -1.0 pp | -2.9 pp |
| 121 | Georgia | 98.6% | -1.0 pp | -9.8 pp |
| 122 | Japan | 99.9% | -1.1 pp | -9.4 pp |
| 123 | Armenia | 99.1% | -1.2 pp | -9.5 pp |
| 124 | Latvia | 97.7% | -1.4 pp | -11.1 pp |
| 125 | China | 94.6% | -1.4 pp | +5.9 pp |
| 126 | Estonia | 98.3% | -1.5 pp | -10.5 pp |
| 127 | Melanesia | 72.3% | -1.7 pp | -2.6 pp |
| 128 | Turkmenistan | 99.9% | -1.7 pp | -8.8 pp |
| 129 | Fiji | 88.2% | -1.9 pp | +3.8 pp |
| 130 | Slovenia | 99.7% | -2.0 pp | -8.7 pp |
| 131 | Netherlands | 95.1% | -2.1 pp | -8.2 pp |
| 132 | Democratic People's Republic of  | 100.0% | -2.1 pp | -9.4 pp |
| 133 | New Zealand | 96.5% | -2.2 pp | -7.1 pp |
| 134 | Azerbaijan | 99.4% | -2.2 pp | -9.3 pp |
| 135 | Puerto Rico | 96.7% | -2.2 pp | -4.8 pp |
| 136 | Belarus | 99.9% | -2.3 pp | -9.0 pp |
| 137 | Ukraine | 99.9% | -2.5 pp | -9.1 pp |
| 138 | Gabon | 47.1% | -2.5 pp | -10.4 pp |
| 139 | Australia and New Zealand | 98.7% | -2.5 pp | -8.0 pp |
| 140 | Australia | 99.1% | -2.6 pp | -8.2 pp |
| 141 | Bulgaria | 93.2% | -2.8 pp | -13.0 pp |
| 142 | Kazakhstan | 99.0% | -2.9 pp | -9.6 pp |
| 143 | Namibia | 59.4% | -2.9 pp | -6.0 pp |
| 144 | Russian Federation | 98.5% | -3.0 pp | -10.0 pp |
| 145 | Martinique | 91.1% | -3.2 pp | -1.0 pp |
| 146 | Sweden | 99.3% | -3.2 pp | -8.1 pp |
| 147 | Guadeloupe | 88.0% | -3.2 pp | -2.4 pp |
| 148 | Kyrgyzstan | 98.4% | -3.3 pp | -10.2 pp |
| 149 | Tajikistan | 95.8% | -3.4 pp | -10.5 pp |
| 150 | Belgium | 96.3% | -3.4 pp | -6.5 pp |
| 151 | Congo | 42.1% | -3.7 pp | -16.1 pp |
| 152 | Romania | 97.7% | -3.8 pp | -9.2 pp |
| 153 | Austria | 98.2% | -3.8 pp | -10.0 pp |
| 154 | Lithuania | 98.0% | -3.9 pp | -10.9 pp |
| 155 | Tonga | 95.3% | -3.9 pp | -0.6 pp |
| 156 | Liberia | 30.3% | -4.0 pp | -21.9 pp |
| 157 | Croatia | 99.5% | -4.1 pp | -8.8 pp |
| 158 | France | 95.2% | -4.2 pp | -4.6 pp |
| 159 | Cuba | 96.8% | -4.3 pp | -3.9 pp |
| 160 | Curaçao | 89.5% | -4.3 pp | -9.3 pp |
| 161 | Republic of Moldova | 97.9% | -4.5 pp | -9.6 pp |
| 162 | New Caledonia | 98.4% | -4.5 pp | +1.6 pp |
| 163 | Malaysia | 96.3% | -4.6 pp | +3.2 pp |
| 164 | Qatar | 53.8% | -4.8 pp | -16.8 pp |
| 165 | Kenya | 62.4% | -4.8 pp | -6.2 pp |
| 166 | Chile | 96.6% | -5.1 pp | +0.1 pp |
| 167 | Bahamas | 99.0% | -5.3 pp | -6.5 pp |
| 168 | Macao Special Administrative Reg | 93.4% | -5.4 pp | +3.2 pp |
| 169 | Hong Kong Special Administrative | 97.7% | -5.9 pp | +0.9 pp |
| 170 | The former Yugoslav Republic of  | 96.0% | -6.0 pp | -4.6 pp |
| 171 | Serbia | 97.8% | -6.2 pp | -9.5 pp |
| 172 | Jamaica | 95.3% | -6.4 pp | -1.5 pp |
| 173 | Ireland | 98.8% | -6.5 pp | -5.2 pp |
| 174 | Montenegro | 96.3% | -6.5 pp | -11.2 pp |
| 175 | Singapore | 99.2% | -6.9 pp | -1.1 pp |
| 176 | Albania | 96.3% | -7.0 pp | -10.1 pp |
| 177 | Greece | 93.2% | -7.3 pp | -3.3 pp |
| 178 | Italy | 99.5% | -7.3 pp | -4.9 pp |
| 179 | Swaziland | 46.0% | -7.6 pp | -17.2 pp |
| 180 | Mongolia | 90.6% | -7.6 pp | -13.0 pp |
| 181 | Cyprus | 97.4% | -7.7 pp | -5.2 pp |
| 182 | Micronesia (Federated States of) | 81.2% | -7.8 pp | -12.7 pp |
| 183 | Bosnia and Herzegovina | 98.8% | -8.2 pp | -7.9 pp |
| 184 | Spain | 89.2% | -8.7 pp | -9.7 pp |
| 185 | Finland | 99.5% | -9.8 pp | -9.7 pp |
| 186 | Republic of Korea | 99.9% | -10.0 pp | -8.0 pp |
| 187 | Zimbabwe | 71.2% | -11.5 pp | -12.3 pp |
| 188 | Taiwan Province of China | 99.7% | -13.4 pp | -7.3 pp |
| 189 | Malta | 99.9% | -15.5 pp | -9.2 pp |

---

*Method: country fixed effects regression of lower secondary completion on parental lower secondary (T−25) only.*
*GDP excluded to avoid bad-control bias (education → GDP). GDP shown for context only. WCDE v3 education data.*