Portfolio Stress Testing in Python
==================================

Project Summary
---------------

This project presents a custom **Portfolio Stress Testing** framework built entirely in Python. It simulates how a multi-asset investment portfolio behaves under various adverse market scenarios, helping stakeholders assess risk and recovery dynamics effectively.

Business Problem
----------------

Investment portfolios face varying risks during market crises due to changes in asset correlations and volatilities. This framework was developed to:

*   Estimate potential portfolio losses during crises
    
*   Identify which securities contribute most to losses
    
*   Model recovery timelines after stress events
    
*   Evaluate if the current asset mix sufficiently hedges risk
    
*   Support informed portfolio risk management decisions
    

Tools & Techniques
------------------

*   **Python** — Core programming language for development
    
*   **NumPy** — Numerical computations and data handling
    
*   **Matplotlib & Seaborn** — Data visualization and storytelling
    
*   **Custom stress return models** — Based on historical crisis data
    
*   **Correlation matrix modeling** — To capture asset relationships and simulate realistic portfolio behavior
    

Key Features
------------

*   Simulation of **portfolio value** under multiple historical crisis scenarios
    
*   **Stress and recovery path modeling** (logistic and exponential)
    
*   **Security-wise risk contribution** analysis
    
*   Calculation of key risk metrics:
    
    *   **Sharpe Ratio**
        
    *   **Value at Risk (VaR)**
        
    *   **Portfolio Return and Volatility**
        
*   Visualizations:
    
    *   **Portfolio value timelines**
        
    *   **Loss contribution pie charts**
        
    *   **Scenario loss comparisons**
        
    *   **Performance metrics comparison**

  Portfolio
  ---------
  
  | Instrument                  | Portfolio Weight (%) | Baseline Return (%) | Volatility (%) | Beta |
|-----------------------------|---------------------|--------------------|----------------|------|
| T-Bills                     | 10.5                | 6.9                | 0.5            | 0.0  |
| Certificates of Deposit (CDs) | 14.0                | 6.1                | 0.8            | 0.0  |
| Commercial Paper            | 21.0                | 8.3                | 1.2            | 0.05 |
| Money Market Funds          | 10.5                | 6.4                | 0.7            | 0.0  |
| Savings Accounts            | 3.5                 | 4.4                | 0.3            | 0.0  |
| Green Bonds                 | 10.5                | 7.9                | 1.5            | 0.1  |
| Corporate Bonds             | 9.75                | 8.3                | 2.0            | 0.15 |
| Inflation Bonds             | 2.25                | 6.6                | 1.8            | 0.05 |
| Municipal Bonds             | 3.0                 | 6.9                | 1.9            | 0.1  |
| Equity Funds                | 9.75                | 13.5               | 15.0           | 1.3  |
| REITs                       | 4.5                 | 9.6                | 10.0           | 0.8  |
| Gold                        | 0.75                | 7.5                | 8.0            | -0.2 |


Correlation Matrix & Assumptions
--------------------------------

### Correlation Matrix

A **correlation matrix** was used to model interdependencies between different asset classes. Correlations were estimated based on **historical co-movement patterns** and aligned with typical behaviors observed during past stress periods.

Key assumptions and observations:

Asset ClassExample Correlation BehaviorT-Bills, CDs, Money Market**Highly correlated** (~0.8–0.9), behave similarly in risk-off environmentsGovernment Bonds (Green Bonds, Inflation Bonds, Municipal Bonds)**Moderate correlation** (~0.4–0.7) with fixed income and partly with equitiesCorporate BondsCorrelates with both government bonds and equities (~0.4–0.7), depending on credit risk premiumEquities (Equity Funds, REITs)**Negatively correlated** with risk-free assets; equity returns typically crash during crisesGold**Hedge asset**, weak correlation with most traditional assets, sometimes negative with equitiesSavings Accounts**Minimal volatility**, largely uncorrelated, low correlation used (0.3–0.5)

### Sample Matrix Excerpt:

| Instrument →  | T-Bills | CDs   | Comm. Paper | MM Funds | Savings | Green Bonds | Corp. Bonds | Infl. Bonds | Mun. Bonds | Equity Funds | REITs | Gold  |
|---------------|---------|-------|-------------|----------|---------|-------------|-------------|-------------|------------|--------------|-------|-------|
| T-Bills       | 1.00    | 0.80  | 0.70        | 0.90     | 0.50    | 0.60        | 0.40        | 0.30        | 0.40       | -0.30        | -0.20 | 0.10  |
| CDs           | 0.80    | 1.00  | 0.80        | 0.80     | 0.40    | 0.50        | 0.30        | 0.20        | 0.30       | -0.30        | -0.20 | 0.10  |
| Comm. Paper   | 0.70    | 0.80  | 1.00        | 0.70     | 0.30    | 0.60        | 0.40        | 0.20        | 0.40       | -0.30        | -0.20 | 0.10  |
| MM Funds      | 0.90    | 0.80  | 0.70        | 1.00     | 0.50    | 0.60        | 0.40        | 0.30        | 0.40       | -0.30        | -0.20 | 0.10  |
| Savings       | 0.50    | 0.40  | 0.30        | 0.50     | 1.00    | 0.30        | 0.20        | 0.10        | 0.20       | -0.10        | -0.10 | 0.00  |
| Green Bonds   | 0.60    | 0.50  | 0.60        | 0.60     | 0.30    | 1.00        | 0.70        | 0.50        | 0.70       | -0.30        | -0.20 | 0.20  |
| Corp. Bonds   | 0.40    | 0.30  | 0.40        | 0.40     | 0.20    | 0.70        | 1.00        | 0.60        | 0.80       | -0.30        |       |       |


### Justification of Assumptions

*   **Flight to safety**: In stress scenarios, correlation between risk-free and risky assets diverges:
    
    *   Fixed income products (T-Bills, CDs) become highly correlated as investors flock to safe assets.
        
    *   Equities and REITs tend to crash, and gold sometimes acts as a hedge with inverse correlation.
        
*   **Historical alignment**: The matrix aligns well with behavior observed during events such as:
    
    *   **2008 Global Financial Crisis**
        
    *   **2013 RBI Rate Hike**
        
    *   **2022 Inflation Spike**
        
*   **Recovery modeling**: Recovery phases assume that post-crisis correlations slowly revert to normal, but initial co-movement remains elevated.
    

### Assumption Rates

*   **Baseline returns** and **volatility** levels were set based on realistic values for each instrument (e.g., 6.9%–13.5% returns, volatility 0.5%–15%).
    
*   **Sharpe Ratio** and **VaR** calculations used an assumed risk-free rate of **5.5%**, reflecting an Indian market context.
    
*   **Scenario return shocks** were chosen based on **real historical data** (e.g., 2008 crisis saw ~35% equity decline, bonds showed resilience).
    
*   **Covariance terms** were scaled by **+20%** under stress scenarios to reflect rising correlations in crises — a common real-world phenomenon.
    

Project Outcomes
----------------

*   Enhanced **understanding of portfolio behavior** under extreme market conditions
    
*   Clear **identification of loss drivers** within the portfolio
    
*   Actionable **risk metrics** to guide portfolio allocation and hedging strategies
    
*   Visual insights into **recovery dynamics** and scenario comparisons
    
*   A **scalable and customizable Python framework** for future stress testing needs
    

How to Use
----------

1.  Clone or download the project repository.
    
2.  Ensure Python environment has dependencies installed:
    
    *   numpy
        
    *   matplotlib
        
    *   seaborn
        
3.  Configure **portfolio allocation** and **scenario parameters** as needed in the code.
    
4.  Run the simulation script:
    
    *   Generates **stress test results** and visualizations as .png files.
        
5.  Analyze output:
    
    *   Portfolio value evolution
        
    *   Loss contribution per instrument
        
    *   Scenario loss comparisons
        
    *   Risk metrics comparison
        

Contact
-------

📧 jayanthsivaprakash12@gmail.com

Thank you for reviewing this project!**Open to feedback and collaboration opportunities.** 🚀
