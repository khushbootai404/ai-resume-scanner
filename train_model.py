import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("dataset.csv")

# Combine resume + job
data["text"] = data["resume"] + " " + data["job"]

X = data["text"]
y = data["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create vectorizer
vectorizer = TfidfVectorizer(max_features=5000)

# Convert text to numbers
X_train_vec = vectorizer.fit_transform(X_train)

# Create model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train_vec, y_train)

# Test model
X_test_vec = vectorizer.transform(X_test)
accuracy = model.score(X_test_vec, y_test)

print("Train-Test Accuracy:", round(accuracy * 100, 2), "%")

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully!")

print("Actual:", list(y_test))
print("Predicted:", list(model.predict(X_test_vec)))