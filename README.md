# Module Project 2: Statistical Analysis

## Research Question

Does model performance differ when trained on color images versus grayscale images?

## Hypotheses

H0: There is no difference in mean classification accuracy between the color and grayscale conditions.

H1: There is a difference in mean classification accuracy between the color and grayscale conditions.

## Data

I use the CIFAR 10 dataset.

I keep only two classes:

Cats

Dogs

The CIFAR 10 training data provides:

5,000 cat images

5,000 dog images

The official CIFAR 10 test set provides:

1,000 cat images

1,000 dog images

The raw CIFAR 10 files are not included in this repository because they are large public files.

Download the CIFAR 10 Python version from:

https://www.cs.toronto.edu/~kriz/cifar.html

Place the extracted folder here:

data/raw/cifar-10-batches-py/

The raw data folder is excluded from Git using .gitignore.

## Experimental Conditions

Condition 1:

Color images

Condition 2:

Grayscale versions of the same images

## Model

I use Logistic Regression.

I use the same model and settings for both experimental conditions.

## Experimental Design

I use the official CIFAR 10 training and test sets.

For each experimental run, I randomly sample 4,000 images from the training data.

Each training sample contains:

2,000 cats

2,000 dogs

I use the exact same sampled images for the color and grayscale conditions.

Both models are evaluated on the same fixed official CIFAR 10 test set containing 2,000 images.

The test set contains:

1,000 cats

1,000 dogs

This design creates paired accuracy measurements because the color and grayscale models use matching training samples and the same test set.

## Pilot Study

I first ran 10 paired pilot experiments using random seeds 0 through 9.

The pilot experiment used the same design as the final experiment.

The pilot produced an estimated paired Cohen's d of:

2.35

I used this effect size for the power analysis.

## Power Analysis

I used:

Alpha = 0.05

Power = 0.80

Pilot Cohen's d = 2.35

The estimated minimum sample size was:

3.70 paired runs

I rounded this up to 4 paired runs.

The final experiment used 10 paired runs, which exceeds the estimated minimum sample size.

## Final Experiment

The final experiment used new random seeds 10 through 19.

This kept the final experiment separate from the pilot data used for the power analysis.

For each run:

I randomly selected 2,000 cat images and 2,000 dog images from the training set.

I trained one Logistic Regression model on the color images.

I trained another Logistic Regression model on grayscale versions of the same images.

I evaluated both models on the same official CIFAR 10 test set.

## Statistical Analysis

I use the following statistical procedures:

Shapiro Wilk test

Paired t test

95% confidence interval

Cohen's d

Power analysis

The Shapiro Wilk test is used to check whether the paired accuracy differences are approximately normally distributed.

The paired t test is used because each color accuracy score is directly matched with a grayscale accuracy score from the same experimental run.

Post hoc testing is not required because the experiment compares only two conditions.

## Final Results

Average color accuracy:

57.13%

Average grayscale accuracy:

55.88%

Mean difference:

1.25 percentage points

Shapiro Wilk p value:

0.0744

Paired t test statistic:

4.35

Paired t test p value:

0.00184

95% confidence interval for the mean difference:

0.60 to 1.90 percentage points

Final Cohen's d:

1.38

## Interpretation

The color condition produced higher accuracy than the grayscale condition in all 10 final paired runs.

The Shapiro Wilk p value was 0.0744.

Because this value is greater than 0.05, the normality check did not provide evidence that the paired differences were non normal.

The paired t test p value was 0.00184.

Because this value is below 0.05, I reject the null hypothesis of no mean difference between the color and grayscale conditions.

The 95% confidence interval ranged from approximately 0.60 to 1.90 percentage points.

The interval does not include zero.

The results provide evidence that removing color information reduced classification accuracy in this experiment.

## Project Structure

project2/

data/

raw/

cifar-10-batches-py/

processed/

final_results.csv

figures/

final_accuracy_comparison.png

load_data.py

run_experiment.py

analyze_results.py

power_analysis.py

save_results.py

plot_results.py

run_all.py

README.md

.gitignore

## Project Files

### load_data.py

Loads the CIFAR 10 training data.

Loads the official CIFAR 10 test data.

Keeps only cat and dog images.

Creates grayscale versions of both the training and test images.

### run_experiment.py

Runs the 10 final paired experiments.

Randomly samples 2,000 cats and 2,000 dogs for each run.

Uses the same sampled images for both color and grayscale conditions.

Evaluates both models on the same official test set.

Saves the final accuracy scores.

### analyze_results.py

Loads the experiment scores.

Runs the Shapiro Wilk test.

Runs the paired t test.

Calculates the mean difference.

Calculates the 95% confidence interval.

Calculates Cohen's d.

### power_analysis.py

Uses the pilot effect size to calculate the required number of paired experimental runs.

### save_results.py

Creates:

data/processed/final_results.csv

### plot_results.py

Creates:

figures/final_accuracy_comparison.png

### run_all.py

Runs the experiment and analysis scripts in order.

## Processed Data

The repository includes:

data/processed/final_results.csv

This file contains:

Run number

Color accuracy

Grayscale accuracy

Difference between the paired accuracy scores

## Visualization

The repository includes:

figures/final_accuracy_comparison.png

The figure compares color and grayscale accuracy across the 10 final paired runs.

## Install Dependencies

pip install numpy pandas scipy scikit-learn statsmodels matplotlib

## Run the Project

Run the full workflow with:

python run_all.py

You can also run each script separately:

python run_experiment.py

python analyze_results.py

python power_analysis.py

python save_results.py

python plot_results.py

## Reproducibility

To reproduce the project:

Download the CIFAR 10 Python dataset.

Place the extracted folder here:

data/raw/cifar-10-batches-py/

Install the required Python packages.

Run:

python run_all.py

The scripts will recreate the final experiment results, statistical analysis, processed results file, and visualization.

This project is designed to be fully reproducible using the provided scripts and the publicly available CIFAR 10 dataset.