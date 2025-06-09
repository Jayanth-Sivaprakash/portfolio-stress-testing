import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Helvetica', 'sans-serif']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10

segments = ['Short-to-Medium', 'Medium-Term', 'Long-Term']
weights = [0.70, 0.15, 0.15]
baseline_returns = [7.11, 7.76, 11.83]
total_value = 2000
segment_amounts = [1400, 300, 300]

all_instruments = ['T-Bills', 'CDs', 'Comm. Paper', 'MM Funds', 'Savings', 'Green Bonds', 'Corp. Bonds', 'Infl. Bonds', 'Mun. Bonds', 'Equity Funds', 'REITs', 'Gold']
all_allocations = [0.15*0.70, 0.20*0.70, 0.30*0.70, 0.15*0.70, 0.05*0.70, 0.15*0.70, 0.65*0.15, 0.15*0.15, 0.20*0.15, 0.65*0.15, 0.30*0.15, 0.05*0.15]
all_returns = [6.9, 6.1, 8.3, 6.4, 4.4, 7.9, 8.3, 6.6, 6.9, 13.5, 9.6, 7.5]
all_volatilities = [0.5, 0.8, 1.2, 0.7, 0.3, 1.5, 2.0, 1.8, 1.9, 15.0, 10.0, 8.0]
all_betas = [0.0, 0.0, 0.05, 0.0, 0.0, 0.1, 0.15, 0.05, 0.1, 1.3, 0.8, -0.2]

corr_matrix = np.array([
    [1.0, 0.8, 0.7, 0.9, 0.5, 0.6, 0.4, 0.3, 0.4, -0.3, -0.2, 0.1],
    [0.8, 1.0, 0.8, 0.8, 0.4, 0.5, 0.3, 0.2, 0.3, -0.3, -0.2, 0.1],
    [0.7, 0.8, 1.0, 0.7, 0.3, 0.6, 0.4, 0.2, 0.4, -0.3, -0.2, 0.1],
    [0.9, 0.8, 0.7, 1.0, 0.5, 0.6, 0.4, 0.3, 0.4, -0.3, -0.2, 0.1],
    [0.5, 0.4, 0.3, 0.5, 1.0, 0.3, 0.2, 0.1, 0.2, -0.1, -0.1, 0.0],
    [0.6, 0.5, 0.6, 0.6, 0.3, 1.0, 0.7, 0.5, 0.7, -0.3, -0.2, 0.2],
    [0.4, 0.3, 0.4, 0.4, 0.2, 0.7, 1.0, 0.6, 0.8, -0.3, -0.2, 0.2],
    [0.3, 0.2, 0.2, 0.3, 0.1, 0.5, 0.6, 1.0, 0.5, -0.2, -0.1, 0.3],
    [0.4, 0.3, 0.4, 0.4, 0.2, 0.7, 0.8, 0.5, 1.0, -0.3, -0.2, 0.2],
    [-0.3, -0.3, -0.3, -0.3, -0.1, -0.3, -0.3, -0.2, -0.3, 1.0, 0.8, -0.5],
    [-0.2, -0.2, -0.2, -0.2, -0.1, -0.2, -0.2, -0.1, -0.2, 0.8, 1.0, -0.4],
    [0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.2, 0.3, 0.2, -0.5, -0.4, 1.0]
])

scenarios = {
    '2008 Global Financial Crisis': {
        'returns': [7.7, 6.9, 9.1, 7.2, 5.2, 8.7, 9.1, 7.4, 7.7, -35.0, -20.0, 17.5],
        'stress_months': 3,
        'recovery_months': 24,
        'recovery_max': 0.94,
        'recovery_type': 'logistic',
        'noise': 0.02,
        'annotation': 'Oct 2008: NIFTY 500 dropped 30% due to global financial crisis.'
    },
    '2013 RBI Rate Hike': {
        'returns': [7.9, 7.1, 9.3, 7.4, 5.4, 0.9, 1.3, 10.6, -0.1, -1.5, -5.4, 7.5],
        'stress_months': 2,
        'recovery_months': 15,
        'recovery_max': 0.91,
        'recovery_type': 'exponential',
        'noise': 0.015,
        'annotation': 'Jul 2013: RBI raised repo rate by 200 bps to 9.25%.'
    },
    '2022 Inflation Spike': {
        'returns': [3.9, 3.1, 5.3, 4.4, 2.4, 2.9, 3.3, 12.6, 1.9, 6.5, 12.6, 22.5],
        'stress_months': 4,
        'recovery_months': 12,
        'recovery_max': 0.93,
        'recovery_type': 'logistic',
        'noise': 0.018,
        'annotation': 'Sep 2022: Inflation hit 7.41% due to supply shocks.'
    }
}

def stress_curve(t, duration, max_loss):
    t = np.clip(t, 0, duration)
    return 1 - max_loss * (t / duration)**2

def logistic_recovery(t, duration, max_recovery, noise):
    k = 5 / duration
    base = max_recovery / (1 + np.exp(-k * (t - duration / 2)))
    return base * (1 + np.random.normal(0, noise))

def exponential_recovery(t, duration, max_recovery, noise):
    base = max_recovery * (1 - np.exp(-t / (duration / 5)))
    return base * (1 + np.random.normal(0, noise))

baseline_return = sum(w * r for w, r in zip(all_allocations, all_returns))
variance_terms = np.array([(w * v) ** 2 for w, v in zip(all_allocations, all_volatilities)])
covariance_terms = sum(
    w_i * w_j * v_i * v_j * corr_matrix[i, j]
    for i, (w_i, v_i) in enumerate(zip(all_allocations, all_volatilities))
    for j, (w_j, v_j) in enumerate(zip(all_allocations, all_volatilities)) if i != j
)
baseline_std = np.sqrt(sum(variance_terms) + covariance_terms)
risk_free_rate = 5.5
baseline_sharpe = (baseline_return - risk_free_rate) / baseline_std
z_score_95 = 1.65
baseline_var = z_score_95 * baseline_std

scenario_losses = {}
scenario_metrics = {'Baseline': [baseline_return, baseline_std, baseline_sharpe, baseline_var]}

mono_colors = sns.color_palette("Blues", n_colors=12)
bar_colors = sns.color_palette("Blues", n_colors=4)

pie_colors = sns.color_palette("tab20", n_colors=12)

for scenario_name, params in scenarios.items():
    stressed_returns = params['returns']
    portfolio_return = sum(w * r for w, r in zip(all_allocations, stressed_returns))
    
    losses = [(r_base - r_stress) * w * total_value / 100 for r_base, r_stress, w in zip(all_returns, stressed_returns, all_allocations)]
    total_loss = sum(loss for loss in losses if loss > 0)
    loss_contributions = [max(0, loss) / total_loss * 100 if total_loss > 0 else 0 for loss in losses]
    
    stressed_std = np.sqrt(sum((w * v) ** 2 for w, v in zip(all_allocations, all_volatilities)) + covariance_terms * 1.2)
    stressed_sharpe = (portfolio_return - risk_free_rate) / stressed_std if stressed_std > 0 else 0
    stressed_var = z_score_95 * stressed_std
    
    scenario_metrics[scenario_name] = [portfolio_return, stressed_std, stressed_sharpe, stressed_var]
    
    stress_months = params['stress_months']
    recovery_months = params['recovery_months']
    total_months = stress_months + recovery_months
    time = np.linspace(0, total_months, 100)
    value = np.zeros_like(time)
    max_loss = 1 - (1 + portfolio_return / 100) / (1 + baseline_return / 100)
    scenario_losses[scenario_name] = max_loss * total_value
    
    for i, t in enumerate(time):
        if t <= stress_months:
            value[i] = total_value * stress_curve(t, stress_months, max_loss)
        else:
            if params['recovery_type'] == 'logistic':
                value[i] = total_value * (1 - max_loss) + total_value * max_loss * logistic_recovery(t - stress_months, recovery_months, params['recovery_max'], params['noise'])
            else:
                value[i] = total_value * (1 - max_loss) + total_value * max_loss * exponential_recovery(t - stress_months, recovery_months, params['recovery_max'], params['noise'])
    
    plt.figure(figsize=(12, 7), dpi=300)
    plt.plot(time, value, label='Portfolio Value', color=mono_colors[8], linewidth=3, alpha=0.9)
    plt.axvline(x=stress_months, color=mono_colors[3], linestyle='--', label='Stress End', linewidth=2)
    plt.text(0.95, 0.15, params['annotation'], transform=plt.gca().transAxes, fontsize=9, 
             ha='right', va='bottom', bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray', boxstyle='round,pad=0.5'))
    plt.xlabel('Months')
    plt.ylabel('Portfolio Value (INR Crore)')
    plt.title(f'{scenario_name}: Stress Test and Recovery\n(Return: {portfolio_return:.2f}%)', pad=20)
    plt.legend(loc='upper left', frameon=True, edgecolor='gray', bbox_to_anchor=(0.01, 0.99))
    plt.grid(True, linestyle='--', alpha=0.5, color='gray')
    plt.minorticks_on()
    plt.gca().set_facecolor('#f5f5f5')
    plt.tight_layout()
    plt.savefig(f'{scenario_name.lower().replace(" ", "_")}_stress_recovery.png', dpi=300)
    plt.close()

    recovery_time = np.linspace(0, recovery_months, 50)
    recovery_value = np.zeros_like(recovery_time)
    for i, t in enumerate(recovery_time):
        if params['recovery_type'] == 'logistic':
            recovery_value[i] = total_value * (1 - max_loss) + total_value * max_loss * logistic_recovery(t, recovery_months, params['recovery_max'], params['noise'])
        else:
            recovery_value[i] = total_value * (1 - max_loss) + total_value * max_loss * exponential_recovery(t, recovery_months, params['recovery_max'], params['noise'])
    
    plt.figure(figsize=(10, 6), dpi=300)
    plt.plot(recovery_time, recovery_value, label='Recovery Value', color=mono_colors[8], linewidth=3, alpha=0.9)
    plt.xlabel('Months Post-Stress')
    plt.ylabel('Portfolio Value (INR Crore)')
    plt.title(f'{scenario_name}: Recovery Phase\nPost-Stress Value Trajectory', pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1), frameon=True, edgecolor='gray')
    plt.grid(True, linestyle='--', alpha=0.5, color='gray')
    plt.minorticks_on()
    plt.gca().set_facecolor('#f5f5f5')
    plt.tight_layout()
    plt.savefig(f'{scenario_name.lower().replace(" ", "_")}_recovery.png', dpi=300)
    plt.close()

    plt.figure(figsize=(12, 12), dpi=300)
    explode = [0.1 if contrib > 10 else 0 for contrib in loss_contributions]
    non_zero_contrib = [c for c in loss_contributions if c > 0]
    non_zero_labels = [f"{inst} ({contrib:.1f}%)" for inst, contrib in zip(all_instruments, loss_contributions) if contrib > 0]
    non_zero_colors = [pie_colors[i] for i, contrib in enumerate(loss_contributions) if contrib > 0]
    wedges, _ = plt.pie(
        non_zero_contrib,
        startangle=140,
        colors=non_zero_colors,
        explode=[0.1 if c > 10 else 0 for c in non_zero_contrib], 
        shadow=True, 
        wedgeprops={'edgecolor': 'white', 'linewidth': 1}
    )
    plt.legend(wedges, non_zero_labels, title="Instruments", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), 
               frameon=True, edgecolor='gray', fontsize=9)
    plt.title(f'{scenario_name}: Loss Contribution by Security', pad=30)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f'{scenario_name.lower().replace(" ", "_")}_loss_contribution.png', dpi=300)
    plt.close()

plt.figure(figsize=(10, 6), dpi=300)
scenarios_names = list(scenario_losses.keys())
losses = [scenario_losses[name] for name in scenarios_names]
bars = plt.bar(scenarios_names, losses, color=bar_colors, edgecolor='black', width=0.6)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 20, f'{height:.1f}', 
             ha='center', fontsize=10, fontweight='bold')
plt.xlabel('Scenario')
plt.ylabel('Maximum Loss (INR Crore)')
plt.title('Portfolio Loss Comparison Across Scenarios', pad=20)
plt.grid(True, axis='y', linestyle='--', alpha=0.5, color='gray')
plt.xticks(rotation=10)
plt.gca().set_facecolor('#f5f5f5')
plt.tight_layout()
plt.savefig('scenario_loss_comparison.png', dpi=300)
plt.close()

metrics = ['Expected Return', 'Std Dev', 'Sharpe Ratio', 'VaR (95%)']
n_metrics = len(metrics)
n_scenarios = len(scenario_metrics)
x = np.arange(n_metrics)
width = 0.2

plt.figure(figsize=(16, 8), dpi=300)
for i, (name, values) in enumerate(scenario_metrics.items()):
    plt.bar(x + i * width, values, width, label=name, color=bar_colors[i], edgecolor='black', alpha=0.9)

plt.xlabel('Metrics')
plt.ylabel('Value (%) or Ratio')
plt.title('Performance Metrics: Baseline vs. Stressed Scenarios\nComparing Risk and Return', pad=20)
plt.xticks(x + width * (n_scenarios - 1) / 2, metrics, ha='center', rotation=0)
plt.tick_params(axis='x', pad=10)
plt.legend(loc='upper right', bbox_to_anchor=(1.20, 1), frameon=True, edgecolor='gray')
plt.grid(True, axis='y', linestyle='--', alpha=0.5, color='gray')
plt.gca().set_facecolor('#f5f5f5')
plt.tight_layout(pad=3.0)
plt.savefig('performance_metrics.png', dpi=300)
plt.close()