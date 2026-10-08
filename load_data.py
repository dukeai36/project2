import pickle
import numpy as np

# ----------------------------
# Load training data
# ----------------------------

train_images = []
train_labels = []

for i in range(1, 6):
    with open(f"data/raw/cifar-10-batches-py/data_batch_{i}", "rb") as f:
        data = pickle.load(f, encoding="bytes")

    X = data[b"data"]
    y = data[b"labels"]

    # Keep only cats and dogs
    for image, label in zip(X, y):
        if label == 3 or label == 5:
            train_images.append(image)
            train_labels.append(label)

train_images = np.array(train_images)
train_labels = np.array(train_labels)

# Reshape training images into red, green, blue channels
train_images = train_images.reshape(-1, 3, 32, 32)

red = train_images[:, 0]
green = train_images[:, 1]
blue = train_images[:, 2]

# Create grayscale training images
train_grayscale = 0.299 * red + 0.587 * green + 0.114 * blue


# ----------------------------
# Load official test data
# ----------------------------

with open("data/raw/cifar-10-batches-py/test_batch", "rb") as f:
    test_data = pickle.load(f, encoding="bytes")

X_test = test_data[b"data"]
y_test = test_data[b"labels"]

test_images = []
test_labels = []

# Keep only cats and dogs
for image, label in zip(X_test, y_test):
    if label == 3 or label == 5:
        test_images.append(image)
        test_labels.append(label)

test_images = np.array(test_images)
test_labels = np.array(test_labels)

# Reshape test images
test_images = test_images.reshape(-1, 3, 32, 32)

red_test = test_images[:, 0]
green_test = test_images[:, 1]
blue_test = test_images[:, 2]

# Create grayscale test images
test_grayscale = (
    0.299 * red_test
    + 0.587 * green_test
    + 0.114 * blue_test
)

print("Training images:", len(train_images))
print("Test images:", len(test_images))