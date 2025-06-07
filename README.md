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
        

Correlation Matrix & Assumptions
--------------------------------

### Correlation Matrix

A **correlation matrix** was used to model interdependencies between different asset classes. Correlations were estimated based on **historical co-movement patterns** and aligned with typical behaviors observed during past stress periods.

Key assumptions and observations:

Asset ClassExample Correlation BehaviorT-Bills, CDs, Money Market**Highly correlated** (~0.8–0.9), behave similarly in risk-off environmentsGovernment Bonds (Green Bonds, Inflation Bonds, Municipal Bonds)**Moderate correlation** (~0.4–0.7) with fixed income and partly with equitiesCorporate BondsCorrelates with both government bonds and equities (~0.4–0.7), depending on credit risk premiumEquities (Equity Funds, REITs)**Negatively correlated** with risk-free assets; equity returns typically crash during crisesGold**Hedge asset**, weak correlation with most traditional assets, sometimes negative with equitiesSavings Accounts**Minimal volatility**, largely uncorrelated, low correlation used (0.3–0.5)

### Sample Matrix Excerpt:

InstrumentPortfolio Weight (%)Baseline Return (%)Volatility (%)BetaT-Bills10.56.90.50.0Certificates of Deposit (CDs)14.06.10.80.0Commercial Paper21.08.31.20.05Money Market Funds10.56.40.70.0Savings Accounts3.54.40.30.0Green Bonds10.57.91.50.1Corporate Bonds9.758.32.00.15Inflation Bonds2.256.61.80.05Municipal Bonds3.06.91.90.1Equity Funds9.7513.515.01.3REITs4.59.610.00.8Gold0.757.58.0-0.2

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
