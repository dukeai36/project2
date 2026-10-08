import numpy as np
from scipy.stats import shapiro, ttest_rel, t

# Load the accuracy scores from the 10 experiment runs
color_scores = np.load("color_scores.npy")
gray_scores = np.load("gray_scores.npy")

# Calculate the difference between color and grayscale accuracy for each run
differences = color_scores - gray_scores

# Check whether the paired differences are approximately normally distributed
shapiro_stat, shapiro_p = shapiro(differences)

# Run a paired t-test because each color run is matched with a grayscale run
t_stat, p_value = ttest_rel(color_scores, gray_scores)

# Calculate the average difference between the two conditions
mean_diff = np.mean(differences)

# Calculate the standard deviation of the paired differences
std_diff = np.std(differences, ddof=1)

# Number of paired runs
n = len(differences)

# Calculate the standard error of the mean difference
standard_error = std_diff / np.sqrt(n)

# Find the critical t value for a 95% confidence interval
t_critical = t.ppf(0.975, df=n - 1)

# Calculate the lower and upper bounds of the 95% confidence interval
ci_lower = mean_diff - t_critical * standard_error
ci_upper = mean_diff + t_critical * standard_error

# Calculate Cohen's d for the paired differences
cohens_d = mean_diff / std_diff

# Print the main statistical results
print("Average color accuracy:", np.mean(color_scores))
print("Average grayscale accuracy:", np.mean(gray_scores))
print("Shapiro-Wilk p-value:", shapiro_p)
print("Paired t-test statistic:", t_stat)
print("Paired t-test p-value:", p_value)
print("Mean difference:", mean_diff)
print("95% CI:", ci_lower, ci_upper)
print("Cohen's d:", cohens_d)