from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


# File and folder locations
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "SMSSpamCollection"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# Load the dataset
data = pd.read_csv(
    DATA_FILE,
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Remove missing values and duplicate messages
data = data.dropna()
data = data.drop_duplicates()

# Convert labels into numbers:
# ham = 0 (normal message), spam = 1
data["label"] = data["label"].map({"ham": 0, "spam": 1})


# Separate the messages and labels
messages = data["message"]
labels = data["label"]


# Use 80% of the data for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)


# Create the machine-learning pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])


# Train and test the model
model.fit(X_train, y_train)
predictions = model.predict(X_test)


# Calculate performance metrics
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, zero_division=0)
recall = recall_score(y_test, predictions, zero_division=0)


# Display the results
print("Spam Classification Results")
print("---------------------------")
print(f"Dataset size: {len(data)} messages")
print(f"Training messages: {len(X_train)}")
print(f"Testing messages: {len(X_test)}")
print(f"Accuracy: {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")


# Save the metrics as a CSV file
metrics = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall"],
    "Score": [accuracy, precision, recall]
})

metrics.to_csv(
    OUTPUT_DIR / "performance-metrics.csv",
    index=False
)


# Create and save a confusion matrix
ConfusionMatrixDisplay.from_predictions(
    y_test,
    predictions,
    display_labels=["Normal", "Spam"],
    cmap="Blues"
)

plt.title("SMS Spam Classifier Confusion Matrix")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "confusion-matrix.png",
    dpi=300
)
plt.close()


# Test the model with two new example messages
example_messages = [
    "Congratulations! You have won a free cash prize. Call now.",
    "Hello, are we still meeting tomorrow morning?"
]

example_predictions = model.predict(example_messages)

print("\nExample predictions:")

for message, prediction in zip(example_messages, example_predictions):
    result = "Spam" if prediction == 1 else "Normal"
    print(f"{result}: {message}")


print("\nFiles saved in the outputs folder.")