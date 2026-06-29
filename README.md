Comprehensive mutual fund performance analysis of 40 Indian funds using CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, Maximum Drawdown, Tracking Error, and benchmark comparison against NIFTY indices.

## Project Overview

This project analyzes the performance of 40 Indian mutual funds using historical NAV data from January 2022 to May 2026. The objective is to evaluate fund performance using multiple financial metrics and compare them with benchmark indices (NIFTY 50 and NIFTY 100).

The project computes risk-adjusted returns, benchmark comparison, drawdown analysis, fund rankings, and generates a composite fund scorecard.

---

## Objectives

- Calculate Daily Returns
- Calculate CAGR (1 Year, 3 Year, 5 Year)
- Compute Sharpe Ratio
- Compute Sortino Ratio
- Estimate Alpha and Beta using NIFTY100
- Calculate Maximum Drawdown
- Generate Fund Scorecard (0–100)
- Compare Top 5 Funds against NIFTY50 and NIFTY100
- Calculate Tracking Error

---

## Dataset

The project uses:

- Historical Mutual Fund NAV data
- NIFTY50 Benchmark Data
- NIFTY100 Benchmark Data
- Fund Master Dataset

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SciPy
- Jupyter Notebook

---

## Performance Metrics

### Daily Return

Daily Return = NAV(t) / NAV(t−1) − 1

---

### CAGR

CAGR = (Ending NAV / Starting NAV)^(1/n) − 1

Calculated for:

- 1 Year
- 3 Years
- 5 Years

---

### Sharpe Ratio

Sharpe = (Rp − Rf) / σ × √252

Risk-free Rate = 6.5%

---

### Sortino Ratio

Uses downside deviation instead of total standard deviation.

---

### Alpha & Beta

Estimated using Ordinary Least Squares (OLS) regression against NIFTY100 returns.

---

### Maximum Drawdown

Maximum Drawdown = Minimum(NAV / Running Maximum − 1)

---

### Tracking Error

Tracking Error = Std(Fund Return − Benchmark Return) × √252

---

### Fund Scorecard

Composite Score:

- 30% CAGR Rank
- 25% Sharpe Rank
- 20% Alpha Rank
- 15% Expense Ratio Rank
- 10% Maximum Drawdown Rank

Final score is scaled to 100.

---

## Project Structure
