from statsmodels.stats.power import TTestPower

# Effect size estimated from the pilot experiment
effect_size = 2.35

# Significance level
alpha = 0.05

# Desired statistical power
power = 0.80

# Create the power analysis object
analysis = TTestPower()

# Calculate the required number of paired runs
required_n = analysis.solve_power(
    effect_size=effect_size,
    alpha=alpha,
    power=power,
    alternative="two-sided"
)

print("Required paired runs:", required_n)