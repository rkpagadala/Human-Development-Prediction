# Human Development Prediction

A research project studying which factors drive human development — life expectancy, fertility, GDP, and education — using machine learning and longitudinal global data.

## Collaborators

- **Krishna Pagadala** — research direction, analysis, and ongoing development
- **Jaya Shankar** — original co-collaborator; built the initial ML models and data pipeline as an undergraduate CS project

## What This Project Does

Uses Random Forest and Gradient Boosting models to identify which indicators most strongly predict human development outcomes across countries. Subsequent analysis extends this into causal investigation, generational education effects, and policy implications.

## Key Findings

Female education — particularly lower secondary completion — is the strongest predictor of improvements in life expectancy and fertility rate. GDP and population are weak predictors once education is accounted for.

Full findings: [`analysis/findings.md`](analysis/findings.md)

## Repository Structure

- `analysis/` — research outputs, rankings, policy briefs, and analysis scripts
- `wcde/` — WCDE v3 data pipeline and long-run generational analysis
- `datasets/` — cleaned CSVs (World Bank, WCDE) used by analysis scripts
- `vision/` — policy and philanthropist vision documents

## Original ML Results (2021)

**All countries**
| Indicator | Random Forest NRMSE | Gradient Tree NRMSE |
|:---|:---:|---:|
| Life Expectancy | 0.032 | 0.027 |
| Total Fertility Rate | 0.089 | 0.107 |
| GDP per capita | 0.123 | — |
| Primary Education Completion | 0.047 | 0.042 |
| Lower Secondary Completion | 0.051 | 0.058 |

**Developing countries only**
| Indicator | Random Forest NRMSE | Gradient Tree NRMSE |
|:---|:---:|---:|
| Life Expectancy | 0.034 | 0.024 |
| Total Fertility Rate | 0.054 | 0.048 |
| GDP per capita | 0.188 | — |
| Primary Education Completion | 0.077 | 0.070 |
| Lower Secondary Completion | 0.094 | 0.079 |

NRMSE < 0.10 indicates a reliable model.
