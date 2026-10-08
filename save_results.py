import pandas as pd
import numpy as np

# Load the final experiment accuracy scores
color_scores = np.load("color_scores.npy")
gray_scores = np.load("gray_scores.npy")

# Put the final results into a table
results = pd.DataFrame({
    "run": range(1, len(color_scores) + 1),
    "color_accuracy": color_scores,
    "grayscale_accuracy": gray_scores,
    "difference": color_scores - gray_scores
})

# Save the final experiment results
results.to_csv(
    "data/processed/final_results.csv",
    index=False
)

print(results)