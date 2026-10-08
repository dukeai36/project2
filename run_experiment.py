import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from load_data import (
    train_images,
    train_grayscale,
    train_labels,
    test_images,
    test_grayscale,
    test_labels
)

color_scores = []
gray_scores = []

# Run the final experiment 10 times using new seeds
for seed in range(10, 20):

    # Create a random number generator for this run
    rng = np.random.default_rng(seed)

    # Find all cat and dog training images
    cat_indices = np.where(train_labels == 3)[0]
    dog_indices = np.where(train_labels == 5)[0]

    # Randomly sample 2,000 cats and 2,000 dogs
    sampled_cats = rng.choice(cat_indices, 2000, replace=False)
    sampled_dogs = rng.choice(dog_indices, 2000, replace=False)

    sample_indices = np.concatenate([sampled_cats, sampled_dogs])

    # Use the same training images for both conditions
    X_color_train = train_images[sample_indices]
    X_gray_train = train_grayscale[sample_indices]
    y_train = train_labels[sample_indices]

    # Flatten and scale the training images
    X_color_train = X_color_train.reshape(4000, -1) / 255.0
    X_gray_train = X_gray_train.reshape(4000, -1) / 255.0

    # Flatten and scale the fixed official test set
    X_color_test = test_images.reshape(2000, -1) / 255.0
    X_gray_test = test_grayscale.reshape(2000, -1) / 255.0

    # Create the same model for both conditions
    color_model = LogisticRegression(max_iter=1000)
    gray_model = LogisticRegression(max_iter=1000)

    # Train both models
    color_model.fit(X_color_train, y_train)
    gray_model.fit(X_gray_train, y_train)

    # Measure color accuracy
    color_accuracy = accuracy_score(
        test_labels,
        color_model.predict(X_color_test)
    )

    # Measure grayscale accuracy
    gray_accuracy = accuracy_score(
        test_labels,
        gray_model.predict(X_gray_test)
    )

    # Save the results
    color_scores.append(color_accuracy)
    gray_scores.append(gray_accuracy)

    print(seed, color_accuracy, gray_accuracy)

# Save the final experiment scores
np.save("color_scores.npy", color_scores)
np.save("gray_scores.npy", gray_scores)