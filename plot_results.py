import pandas as pd
import matplotlib.pyplot as plt

# Load the final experiment results
results = pd.read_csv("data/processed/final_results.csv")

# Plot color accuracy for each run
plt.plot(
    results["run"],
    results["color_accuracy"],
    marker="o",
    label="Color"
)

# Plot grayscale accuracy for each run
plt.plot(
    results["run"],
    results["grayscale_accuracy"],
    marker="o",
    label="Grayscale"
)

# Add labels and title
plt.xlabel("Run")
plt.ylabel("Accuracy")
plt.title("Final Color vs Grayscale Accuracy")

# Show which line is which
plt.legend()

# Save the final figure
plt.savefig(
    "figures/final_accuracy_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the plot
plt.show()