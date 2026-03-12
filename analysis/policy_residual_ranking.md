# Policy-Adjusted Education Ranking

*Which countries delivered more lower-secondary education than their income and parental education predict?*

## Method

**Target:** lower secondary completion rate (% of 20–24 cohort) at year T
**Predictors:** parental lower secondary completion at T−25, log GDP per capita at T
**Model:** country fixed effects (within-country variation only)

Fixed effects coefficients:
- Parental lower secondary: **0.615** pp per 1 pp of parental completion
- Log GDP: **6.864** pp per 1% GDP

**Residual = actual − predicted.** Positive residual = country delivered more education than its
income and parental history predict. This is the policy signal.

Two residuals are shown:
- **FE residual**: within-country deviation — how much did the country outperform its own predicted trajectory?
- **OLS residual**: cross-country deviation — how much did the country outperform the global prediction?
The FE residual is more demanding: it asks whether the country accelerated beyond its own trend.

---

## Table 1 — Biggest Over-Performers in 2015 (FE Residual)

Countries whose lower secondary completion in 2015 most exceeded what their own
historical trajectory and income level predict.

| Rank | Country | Low Sec 2015 | FE Residual | OLS Residual | GDP/capita 2015 |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Yemen | 33.6% | +25.4 pp | +15.8 pp | $1,600 |
| 2 | Tunisia | 52.2% | +19.6 pp | +21.1 pp | $3,860 |
| 3 | Kiribati | 63.6% | +16.3 pp | +26.9 pp | $1,540 |
| 4 | Haiti | 33.3% | +16.1 pp | +12.7 pp | $1,390 |
| 5 | Algeria | 64.4% | +15.9 pp | +24.6 pp | $4,180 |
| 6 | Morocco | 36.6% | +15.9 pp | +11.4 pp | $3,220 |
| 7 | Nepal | 45.8% | +14.9 pp | +23.4 pp | $902 |
| 8 | Gambia | 25.8% | +14.8 pp | +10.0 pp | $661 |
| 9 | Cuba | 66.8% | +14.4 pp | +17.7 pp | $7,690 |
| 10 | Comoros | 28.3% | +14.0 pp | +7.1 pp | $1,240 |
| 11 | Nigeria | 43.9% | +12.8 pp | +15.3 pp | $2,690 |
| 12 | El Salvador | 38.9% | +12.8 pp | +8.4 pp | $3,710 |
| 13 | Aruba | 49.9% | +12.4 pp | +2.2 pp | $28,400 |
| 14 | Botswana | 53.8% | +12.3 pp | +15.5 pp | $6,800 |
| 15 | Bolivia | 52.4% | +11.9 pp | +15.5 pp | $3,040 |
| 16 | Eswatini | 45.4% | +11.9 pp | +10.6 pp | $3,680 |
| 17 | Indonesia | 58.1% | +11.5 pp | +21.4 pp | $3,330 |
| 18 | Fiji | 61.3% | +11.3 pp | +13.1 pp | $5,390 |
| 19 | Curaçao | 49.9% | +11.0 pp | -0.8 pp | $20,000 |
| 20 | Zimbabwe | 52.6% | +10.8 pp | +14.8 pp | $1,450 |
| 21 | Paraguay | 43.9% | +10.5 pp | +7.8 pp | $5,410 |
| 22 | Denmark | 66.2% | +10.0 pp | -3.3 pp | $53,300 |
| 23 | Iran | 54.6% | +9.9 pp | +13.5 pp | $4,900 |
| 24 | South Africa | 53.6% | +9.9 pp | +9.8 pp | $5,730 |
| 25 | India | 48.6% | +9.8 pp | +18.3 pp | $1,610 |
| 26 | Oman | 57.6% | +9.7 pp | +12.0 pp | $16,000 |
| 27 | Timor-Leste | 56.4% | +9.5 pp | +32.4 pp | $1,330 |
| 28 | Saudi Arabia | 69.5% | +9.5 pp | +16.0 pp | $20,600 |
| 29 | Thailand | 65.7% | +9.5 pp | +22.2 pp | $5,840 |
| 30 | Guyana | 60.6% | +9.3 pp | +12.3 pp | $5,580 |

## Table 2 — Biggest Under-Performers in 2015 (FE Residual)

Countries whose lower secondary completion in 2015 most fell short of what their
income and parental trajectory predict — structural failure or policy neglect.

| Rank | Country | Low Sec 2015 | FE Residual | OLS Residual | GDP/capita 2015 |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Mauritania | 15.9% | -72.6 pp | -79.9 pp | $1,520 |
| 2 | Papua New Guinea | 30.6% | -61.5 pp | -67.8 pp | $2,680 |
| 3 | Brunei | 58.1% | -35.2 pp | -51.6 pp | $31,200 |
| 4 | Libya | 54.9% | -30.9 pp | -45.7 pp | $4,340 |
| 5 | Seychelles | 70.2% | -28.1 pp | -36.1 pp | $14,700 |
| 6 | Grenada | 72.2% | -26.2 pp | -31.9 pp | $9,100 |
| 7 | Guam | 61.3% | -26.0 pp | -49.0 pp | $35,800 |
| 8 | Antigua And Barbuda | 72.7% | -24.2 pp | -33.4 pp | $14,300 |
| 9 | Barbados | 72.5% | -24.0 pp | -34.3 pp | $16,500 |
| 10 | South Korea | 96.3% | -21.8 pp | -5.1 pp | $28,700 |
| 11 | Virgin Islands (U.S.) | 72.2% | -17.2 pp | -38.0 pp | $34,800 |
| 12 | Singapore | 96.2% | -14.8 pp | +1.2 pp | $55,600 |
| 13 | Ireland | 88.7% | -11.5 pp | -3.5 pp | $62,000 |
| 14 | Uzbekistan | 90.8% | -11.2 pp | -7.5 pp | $2,620 |
| 15 | Austria | 80.0% | -8.4 pp | -13.2 pp | $44,200 |
| 16 | Turkmenistan | 97.0% | -8.1 pp | +3.1 pp | $6,430 |
| 17 | Georgia | 91.1% | -7.9 pp | -0.6 pp | $4,010 |
| 18 | Bahamas | 96.5% | -7.1 pp | +0.0 pp | $31,300 |
| 19 | Azerbaijan | 91.6% | -7.0 pp | +2.7 pp | $5,500 |
| 20 | Mongolia | 82.5% | -6.1 pp | +6.3 pp | $3,920 |
| 21 | New Zealand | 87.9% | -5.1 pp | -3.7 pp | $38,600 |
| 22 | Australia | 95.5% | -5.1 pp | -8.7 pp | $56,800 |
| 23 | Cyprus | 85.3% | -5.1 pp | +0.7 pp | $27,900 |
| 24 | Belarus | 95.1% | -4.9 pp | +1.8 pp | $5,950 |
| 25 | Lithuania | 79.3% | -4.9 pp | -7.9 pp | $14,300 |
| 26 | Germany | 76.8% | -4.8 pp | -13.5 pp | $41,100 |
| 27 | Kazakhstan | 94.1% | -4.6 pp | +1.9 pp | $10,500 |
| 28 | Sweden | 82.3% | -4.6 pp | -10.8 pp | $51,500 |
| 29 | Bosnia And Herzegovina | 90.5% | -4.2 pp | +14.9 pp | $4,730 |
| 30 | Russia | 92.5% | -4.1 pp | -0.8 pp | $11,400 |

## Table 3 — Chronic Over-Performers (Mean OLS Residual Across All Years)

Countries that consistently outperformed the global cross-country prediction across all years.
OLS residual = actual minus predicted by pooled model (income + parental education).
This measures how much more education a country delivered than a country with the same income
and parental history would deliver on average globally.

| Rank | Country | Low Sec 2015 | Mean OLS Residual | 2015 OLS Residual | 2015 FE Residual |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Timor-Leste | 56.4% | +23.3 pp | +32.4 pp | +9.5 pp |
| 2 | South Korea | 96.3% | +21.2 pp | -5.1 pp | -21.8 pp |
| 3 | Malaysia | 80.3% | +20.7 pp | +15.7 pp | -1.7 pp |
| 4 | Singapore | 96.2% | +20.6 pp | +1.2 pp | -14.8 pp |
| 5 | Tajikistan | 94.1% | +20.6 pp | +16.0 pp | -2.5 pp |
| 6 | Philippines | 79.1% | +20.4 pp | +20.3 pp | +2.5 pp |
| 7 | Bosnia And Herzegovina | 90.5% | +20.0 pp | +14.9 pp | -4.2 pp |
| 8 | Egypt | 75.9% | +18.8 pp | +23.8 pp | +7.6 pp |
| 9 | Mongolia | 82.5% | +14.3 pp | +6.3 pp | -6.1 pp |
| 10 | Thailand | 65.7% | +14.1 pp | +22.2 pp | +9.5 pp |
| 11 | St. Lucia | 72.2% | +13.7 pp | +19.6 pp | +8.8 pp |
| 12 | North Macedonia | 78.6% | +13.7 pp | +9.4 pp | -1.8 pp |
| 13 | Sri Lanka | 65.8% | +13.5 pp | +14.9 pp | +2.5 pp |
| 14 | Kyrgyz Republic | 84.1% | +12.7 pp | +8.3 pp | -3.3 pp |
| 15 | Kiribati | 63.6% | +12.7 pp | +26.9 pp | +16.3 pp |
| 16 | Colombia | 63.9% | +12.4 pp | +16.7 pp | +6.2 pp |
| 17 | Peru | 71.7% | +12.2 pp | +12.3 pp | +2.2 pp |
| 18 | Hong Kong, China | 83.0% | +11.9 pp | +6.5 pp | -2.3 pp |
| 19 | Turkmenistan | 97.0% | +11.5 pp | +3.1 pp | -8.1 pp |
| 20 | Moldova | 76.8% | +11.3 pp | +18.0 pp | +7.0 pp |
| 21 | Bahamas | 96.5% | +11.3 pp | +0.0 pp | -7.1 pp |
| 22 | Ireland | 88.7% | +11.3 pp | -3.5 pp | -11.5 pp |
| 23 | Indonesia | 58.1% | +10.8 pp | +21.4 pp | +11.5 pp |
| 24 | Trinidad And Tobago | 70.8% | +10.7 pp | +8.7 pp | +0.5 pp |
| 25 | Algeria | 64.4% | +10.7 pp | +24.6 pp | +15.9 pp |
| 26 | Greece | 79.3% | +10.2 pp | +3.6 pp | -2.5 pp |
| 27 | Azerbaijan | 91.6% | +9.7 pp | +2.7 pp | -7.0 pp |
| 28 | Cyprus | 85.3% | +9.5 pp | +0.7 pp | -5.1 pp |
| 29 | Saudi Arabia | 69.5% | +9.3 pp | +16.0 pp | +9.5 pp |
| 30 | Nepal | 45.8% | +8.5 pp | +23.4 pp | +14.9 pp |

## Table 4 — Chronic Under-Performers (Mean OLS Residual Across All Years)

Countries that consistently delivered less education than their income and parental history predict.

| Rank | Country | Low Sec 2015 | Mean OLS Residual | 2015 OLS Residual | 2015 FE Residual |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 1 | Djibouti | 20.5% | -77.9 pp | -77.9 pp | +0.0 pp |
| 2 | Guam | 61.3% | -23.1 pp | -49.0 pp | -26.0 pp |
| 3 | Virgin Islands (U.S.) | 72.2% | -20.4 pp | -38.0 pp | -17.2 pp |
| 4 | Gabon | 20.6% | -19.0 pp | -11.5 pp | +8.3 pp |
| 5 | Qatar | 43.5% | -18.9 pp | -17.4 pp | +2.2 pp |
| 6 | Angola | 6.1% | -18.8 pp | -16.7 pp | +1.5 pp |
| 7 | Kuwait | 36.9% | -18.7 pp | -15.9 pp | +4.0 pp |
| 8 | Brunei | 58.1% | -16.2 pp | -51.6 pp | -35.2 pp |
| 9 | Maldives | 18.7% | -14.9 pp | -8.0 pp | +6.5 pp |
| 10 | Libya | 54.9% | -13.9 pp | -45.7 pp | -30.9 pp |
| 11 | Iceland | 60.3% | -13.1 pp | -7.2 pp | +6.5 pp |
| 12 | Cote D'Ivoire | 15.1% | -12.7 pp | -6.4 pp | +6.6 pp |
| 13 | Equatorial Guinea | 20.7% | -12.7 pp | -9.9 pp | +0.1 pp |
| 14 | Denmark | 66.2% | -12.2 pp | -3.3 pp | +10.0 pp |
| 15 | Norway | 69.8% | -11.4 pp | -15.9 pp | -3.1 pp |
| 16 | Curaçao | 49.9% | -11.0 pp | -0.8 pp | +11.0 pp |
| 17 | Niger | 2.9% | -10.9 pp | -9.8 pp | +1.0 pp |
| 18 | Barbados | 72.5% | -10.4 pp | -34.3 pp | -24.0 pp |
| 19 | Finland | 68.0% | -10.4 pp | -8.1 pp | +3.8 pp |
| 20 | Tanzania | 8.7% | -10.2 pp | -8.1 pp | +1.4 pp |
| 21 | Chad | 7.9% | -10.0 pp | -6.9 pp | +2.2 pp |
| 22 | Senegal | 15.9% | -9.9 pp | -4.3 pp | +5.7 pp |
| 23 | Benin | 13.6% | -9.8 pp | -4.5 pp | +5.2 pp |
| 24 | Uruguay | 38.1% | -9.8 pp | -9.2 pp | +1.2 pp |
| 25 | Congo, Rep. | 20.3% | -9.6 pp | -12.7 pp | -1.6 pp |
| 26 | Antigua And Barbuda | 72.7% | -9.5 pp | -33.4 pp | -24.2 pp |
| 27 | Mali | 9.5% | -9.4 pp | -6.1 pp | +3.0 pp |
| 28 | Cape Verde | 18.7% | -9.3 pp | -5.1 pp | +3.3 pp |
| 29 | Burkina Faso | 8.3% | -9.3 pp | -6.0 pp | +2.5 pp |
| 30 | Yemen | 33.6% | -8.9 pp | +15.8 pp | +25.4 pp |

## Table 5 — Full Country Ranking by 2015 FE Residual

| Rank | Country | Low Sec 2015 | FE Residual | OLS Residual |
| ---: | :--- | ---: | ---: | ---: |
| 1 | Yemen | 33.6% | +25.4 pp | +15.8 pp |
| 2 | Tunisia | 52.2% | +19.6 pp | +21.1 pp |
| 3 | Kiribati | 63.6% | +16.3 pp | +26.9 pp |
| 4 | Haiti | 33.3% | +16.1 pp | +12.7 pp |
| 5 | Algeria | 64.4% | +15.9 pp | +24.6 pp |
| 6 | Morocco | 36.6% | +15.9 pp | +11.4 pp |
| 7 | Nepal | 45.8% | +14.9 pp | +23.4 pp |
| 8 | Gambia | 25.8% | +14.8 pp | +10.0 pp |
| 9 | Cuba | 66.8% | +14.4 pp | +17.7 pp |
| 10 | Comoros | 28.3% | +14.0 pp | +7.1 pp |
| 11 | Nigeria | 43.9% | +12.8 pp | +15.3 pp |
| 12 | El Salvador | 38.9% | +12.8 pp | +8.4 pp |
| 13 | Aruba | 49.9% | +12.4 pp | +2.2 pp |
| 14 | Botswana | 53.8% | +12.3 pp | +15.5 pp |
| 15 | Bolivia | 52.4% | +11.9 pp | +15.5 pp |
| 16 | Eswatini | 45.4% | +11.9 pp | +10.6 pp |
| 17 | Indonesia | 58.1% | +11.5 pp | +21.4 pp |
| 18 | Fiji | 61.3% | +11.3 pp | +13.1 pp |
| 19 | Curaçao | 49.9% | +11.0 pp | -0.8 pp |
| 20 | Zimbabwe | 52.6% | +10.8 pp | +14.8 pp |
| 21 | Paraguay | 43.9% | +10.5 pp | +7.8 pp |
| 22 | Denmark | 66.2% | +10.0 pp | -3.3 pp |
| 23 | Iran | 54.6% | +9.9 pp | +13.5 pp |
| 24 | South Africa | 53.6% | +9.9 pp | +9.8 pp |
| 25 | India | 48.6% | +9.8 pp | +18.3 pp |
| 26 | Oman | 57.6% | +9.7 pp | +12.0 pp |
| 27 | Timor-Leste | 56.4% | +9.5 pp | +32.4 pp |
| 28 | Saudi Arabia | 69.5% | +9.5 pp | +16.0 pp |
| 29 | Thailand | 65.7% | +9.5 pp | +22.2 pp |
| 30 | Guyana | 60.6% | +9.3 pp | +12.3 pp |
| 31 | Sudan | 36.4% | +9.3 pp | +10.5 pp |
| 32 | Pakistan | 36.7% | +9.2 pp | +10.9 pp |
| 33 | Bangladesh | 29.3% | +9.1 pp | +8.0 pp |
| 34 | Portugal | 61.4% | +9.1 pp | +8.9 pp |
| 35 | Brazil | 56.2% | +8.9 pp | +10.9 pp |
| 36 | Guatemala | 28.4% | +8.9 pp | +0.0 pp |
| 37 | St. Lucia | 72.2% | +8.8 pp | +19.6 pp |
| 38 | Central African Republic | 12.9% | +8.8 pp | +0.7 pp |
| 39 | Cameroon | 29.8% | +8.4 pp | +5.8 pp |
| 40 | Gabon | 20.6% | +8.3 pp | -11.5 pp |
| 41 | Belize | 49.9% | +8.3 pp | +9.5 pp |
| 42 | Solomon Islands | 30.6% | +8.2 pp | +3.4 pp |
| 43 | Jamaica | 46.5% | +7.8 pp | +4.0 pp |
| 44 | Spain | 66.7% | +7.6 pp | +4.4 pp |
| 45 | Egypt | 75.9% | +7.6 pp | +23.8 pp |
| 46 | Samoa | 43.8% | +7.5 pp | +4.0 pp |
| 47 | Guinea | 19.0% | +7.1 pp | +1.9 pp |
| 48 | Kenya | 34.4% | +7.0 pp | +7.8 pp |
| 49 | Moldova | 76.8% | +7.0 pp | +18.0 pp |
| 50 | Malawi | 19.7% | +6.9 pp | +5.2 pp |
| 51 | China | 53.6% | +6.8 pp | +13.1 pp |
| 52 | Vanuatu | 26.1% | +6.8 pp | -2.2 pp |
| 53 | Argentina | 60.3% | +6.7 pp | +7.2 pp |
| 54 | Tonga | 45.5% | +6.7 pp | +5.4 pp |
| 55 | Lebanon | 57.0% | +6.6 pp | +9.7 pp |
| 56 | Cote D'Ivoire | 15.1% | +6.6 pp | -6.4 pp |
| 57 | Maldives | 18.7% | +6.5 pp | -8.0 pp |
| 58 | St. Vincent And The Grenadines | 54.9% | +6.5 pp | +9.0 pp |
| 59 | Iceland | 60.3% | +6.5 pp | -7.2 pp |
| 60 | Lao | 37.0% | +6.5 pp | +8.1 pp |
| 61 | Colombia | 63.9% | +6.2 pp | +16.7 pp |
| 62 | Mauritius | 57.6% | +5.9 pp | +10.7 pp |
| 63 | Togo | 19.6% | +5.9 pp | +1.6 pp |
| 64 | Dominican Republic | 54.6% | +5.8 pp | +11.3 pp |
| 65 | Ukraine | 90.5% | +5.7 pp | +12.4 pp |
| 66 | Honduras | 23.2% | +5.7 pp | -1.9 pp |
| 67 | Senegal | 15.9% | +5.7 pp | -4.3 pp |
| 68 | Belgium | 74.8% | +5.4 pp | +1.3 pp |
| 69 | Costa Rica | 49.0% | +5.4 pp | +1.1 pp |
| 70 | Burundi | 7.0% | +5.4 pp | -3.2 pp |
| 71 | Congo, Dem. Rep. | 24.8% | +5.3 pp | +4.6 pp |
| 72 | United Arab Emirates | 63.7% | +5.2 pp | -4.4 pp |
| 73 | Benin | 13.6% | +5.2 pp | -4.5 pp |
| 74 | South Sudan | 22.3% | +5.2 pp | +4.3 pp |
| 75 | Nicaragua | 37.6% | +5.1 pp | +5.8 pp |
| 76 | Czech Republic | 80.6% | +5.0 pp | -0.4 pp |
| 77 | Bahrain | 58.9% | +5.0 pp | +2.9 pp |
| 78 | Mexico | 46.5% | +4.7 pp | +3.0 pp |
| 79 | Ecuador | 54.7% | +4.7 pp | +9.1 pp |
| 80 | Bhutan | 21.6% | +4.4 pp | -0.6 pp |
| 81 | Guinea-Bissau | 13.9% | +4.2 pp | -2.0 pp |
| 82 | Sierra Leone | 17.7% | +4.2 pp | -0.6 pp |
| 83 | Chile | 71.4% | +4.2 pp | +8.6 pp |
| 84 | Rwanda | 12.7% | +4.1 pp | -2.1 pp |
| 85 | Namibia | 32.2% | +4.1 pp | +0.6 pp |
| 86 | Kuwait | 36.9% | +4.0 pp | -15.9 pp |
| 87 | Finland | 68.0% | +3.8 pp | -8.1 pp |
| 88 | Israel | 75.1% | +3.7 pp | +5.7 pp |
| 89 | Afghanistan | 18.4% | +3.6 pp | +3.1 pp |
| 90 | Myanmar | 31.0% | +3.5 pp | +7.4 pp |
| 91 | Cape Verde | 18.7% | +3.3 pp | -5.1 pp |
| 92 | Ghana | 30.2% | +3.3 pp | +1.6 pp |
| 93 | Vietnam | 36.4% | +3.2 pp | +4.6 pp |
| 94 | Cambodia | 19.3% | +3.1 pp | +1.1 pp |
| 95 | Uganda | 13.5% | +3.0 pp | -3.8 pp |
| 96 | Mali | 9.5% | +3.0 pp | -6.1 pp |
| 97 | Ethiopia | 12.4% | +2.7 pp | -2.1 pp |
| 98 | Canada | 83.7% | +2.6 pp | -4.7 pp |
| 99 | Lesotho | 24.1% | +2.5 pp | -0.1 pp |
| 100 | Sri Lanka | 65.8% | +2.5 pp | +14.9 pp |
| 101 | Turkey | 58.8% | +2.5 pp | +7.3 pp |
| 102 | Burkina Faso | 8.3% | +2.5 pp | -6.0 pp |
| 103 | Suriname | 39.9% | +2.5 pp | -4.0 pp |
| 104 | Philippines | 79.1% | +2.5 pp | +20.3 pp |
| 105 | Malta | 71.2% | +2.2 pp | +7.6 pp |
| 106 | Chad | 7.9% | +2.2 pp | -6.9 pp |
| 107 | Qatar | 43.5% | +2.2 pp | -17.4 pp |
| 108 | Peru | 71.7% | +2.2 pp | +12.3 pp |
| 109 | Liberia | 20.6% | +1.7 pp | -2.0 pp |
| 110 | Estonia | 65.8% | +1.7 pp | -6.3 pp |
| 111 | Serbia | 81.3% | +1.7 pp | +5.4 pp |
| 112 | Zambia | 28.7% | +1.5 pp | -3.1 pp |
| 113 | Angola | 6.1% | +1.5 pp | -16.7 pp |
| 114 | Mozambique | 11.3% | +1.5 pp | -3.0 pp |
| 115 | Tanzania | 8.7% | +1.4 pp | -8.1 pp |
| 116 | Madagascar | 8.5% | +1.4 pp | -7.8 pp |
| 117 | Hungary | 78.2% | +1.3 pp | +2.2 pp |
| 118 | Uruguay | 38.1% | +1.2 pp | -9.2 pp |
| 119 | Sao Tome And Principe | 11.9% | +1.2 pp | -7.4 pp |
| 120 | Niger | 2.9% | +1.0 pp | -9.8 pp |
| 121 | Panama | 61.4% | +0.8 pp | +4.6 pp |
| 122 | Romania | 71.0% | +0.8 pp | +3.7 pp |
| 123 | Albania | 58.8% | +0.6 pp | +4.2 pp |
| 124 | Trinidad And Tobago | 70.8% | +0.5 pp | +8.7 pp |
| 125 | United Kingdom | 81.0% | +0.5 pp | -3.2 pp |
| 126 | Poland | 81.0% | +0.3 pp | +0.4 pp |
| 127 | Montenegro | 81.2% | +0.2 pp | +2.0 pp |
| 128 | Equatorial Guinea | 20.7% | +0.1 pp | -9.9 pp |
| 129 | Luxembourg | 77.5% | +0.0 pp | -6.0 pp |
| 130 | Djibouti | 20.5% | +0.0 pp | -77.9 pp |
| 131 | Somalia | 12.7% | +0.0 pp | -2.0 pp |
| 132 | Italy | 72.7% | -0.5 pp | -2.1 pp |
| 133 | Slovak Republic | 83.4% | -0.8 pp | -3.9 pp |
| 134 | Croatia | 84.5% | -0.8 pp | -0.1 pp |
| 135 | France | 80.7% | -1.1 pp | -0.8 pp |
| 136 | Micronesia, Fed. Sts. | 55.6% | -1.1 pp | +2.7 pp |
| 137 | Japan | 93.6% | -1.1 pp | -4.7 pp |
| 138 | Jordan | 58.8% | -1.2 pp | +3.2 pp |
| 139 | Bulgaria | 74.9% | -1.2 pp | +0.5 pp |
| 140 | Congo, Rep. | 20.3% | -1.6 pp | -12.7 pp |
| 141 | Netherlands | 76.9% | -1.7 pp | -4.9 pp |
| 142 | Malaysia | 80.3% | -1.7 pp | +15.7 pp |
| 143 | North Macedonia | 78.6% | -1.8 pp | +9.4 pp |
| 144 | Puerto Rico | 87.7% | -1.9 pp | +2.1 pp |
| 145 | Hong Kong, China | 83.0% | -2.3 pp | +6.5 pp |
| 146 | Greece | 79.3% | -2.5 pp | +3.6 pp |
| 147 | Tajikistan | 94.1% | -2.5 pp | +16.0 pp |
| 148 | Slovenia | 86.5% | -2.8 pp | -4.6 pp |
| 149 | Norway | 69.8% | -3.1 pp | -15.9 pp |
| 150 | Switzerland | 82.9% | -3.2 pp | -11.3 pp |
| 151 | Kyrgyz Republic | 84.1% | -3.3 pp | +8.3 pp |
| 152 | United States | 89.1% | -3.3 pp | -11.5 pp |
| 153 | Armenia | 89.7% | -3.8 pp | +2.4 pp |
| 154 | Latvia | 74.7% | -3.8 pp | -8.2 pp |
| 155 | Iraq | 28.1% | -3.9 pp | -12.5 pp |
| 156 | Russia | 92.5% | -4.1 pp | -0.8 pp |
| 157 | Bosnia And Herzegovina | 90.5% | -4.2 pp | +14.9 pp |
| 158 | Sweden | 82.3% | -4.6 pp | -10.8 pp |
| 159 | Kazakhstan | 94.1% | -4.6 pp | +1.9 pp |
| 160 | Germany | 76.8% | -4.8 pp | -13.5 pp |
| 161 | Lithuania | 79.3% | -4.9 pp | -7.9 pp |
| 162 | Belarus | 95.1% | -4.9 pp | +1.8 pp |
| 163 | Cyprus | 85.3% | -5.1 pp | +0.7 pp |
| 164 | Australia | 95.5% | -5.1 pp | -8.7 pp |
| 165 | New Zealand | 87.9% | -5.1 pp | -3.7 pp |
| 166 | Mongolia | 82.5% | -6.1 pp | +6.3 pp |
| 167 | Azerbaijan | 91.6% | -7.0 pp | +2.7 pp |
| 168 | Bahamas | 96.5% | -7.1 pp | +0.0 pp |
| 169 | Georgia | 91.1% | -7.9 pp | -0.6 pp |
| 170 | Turkmenistan | 97.0% | -8.1 pp | +3.1 pp |
| 171 | Austria | 80.0% | -8.4 pp | -13.2 pp |
| 172 | Uzbekistan | 90.8% | -11.2 pp | -7.5 pp |
| 173 | Ireland | 88.7% | -11.5 pp | -3.5 pp |
| 174 | Singapore | 96.2% | -14.8 pp | +1.2 pp |
| 175 | Virgin Islands (U.S.) | 72.2% | -17.2 pp | -38.0 pp |
| 176 | South Korea | 96.3% | -21.8 pp | -5.1 pp |
| 177 | Barbados | 72.5% | -24.0 pp | -34.3 pp |
| 178 | Antigua And Barbuda | 72.7% | -24.2 pp | -33.4 pp |
| 179 | Guam | 61.3% | -26.0 pp | -49.0 pp |
| 180 | Grenada | 72.2% | -26.2 pp | -31.9 pp |
| 181 | Seychelles | 70.2% | -28.1 pp | -36.1 pp |
| 182 | Libya | 54.9% | -30.9 pp | -45.7 pp |
| 183 | Brunei | 58.1% | -35.2 pp | -51.6 pp |
| 184 | Papua New Guinea | 30.6% | -61.5 pp | -67.8 pp |
| 185 | Mauritania | 15.9% | -72.6 pp | -79.9 pp |

---

*Method: country fixed effects regression of lower secondary completion on parental lower secondary (T−25) and log GDP.*
*Residual represents within-country deviation from predicted trajectory.*