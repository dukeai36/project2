import subprocess

# List the scripts in the order they should run
scripts = [
    "run_experiment.py",
    "analyze_results.py",
    "power_analysis.py",
    "save_results.py",
    "plot_results.py"
]

# Run each script one at a time
for script in scripts:

    # Show which script is currently running
    print(f"Running {script}...")

    # Run the script and stop if an error occurs
    subprocess.run(["python", script], check=True)