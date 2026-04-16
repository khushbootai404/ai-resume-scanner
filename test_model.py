import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Load test data
data = pd.read_csv("test_dataset.csv")

# Prepare input
data["text"] = data["resume"] + " " + data["job"]

X_test = vectorizer.transform(data["text"])
y_true = data["label"]

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_true, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")