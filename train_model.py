import pandas as pd
import re
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

DATASETS = [
    "CEAS_08.csv",
    "Enron.csv",
    "Ling.csv",
    "Nazario.csv",
    "SpamAssasin.csv",
    "Nigerian_Fraud.csv"
]


def clean_text(text):
    text = str(text).lower()

    text = re.sub(r"http\S+", " URL ", text)
    text = re.sub(r"www\S+", " URL ", text)

    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    return text


all_data = []

print("Loading datasets...")

for file in DATASETS:

    df = pd.read_csv(file)

    if "subject" in df.columns:
        subject = df["subject"].fillna("")
    else:
        subject = ""

    if "body" in df.columns:
        body = df["body"].fillna("")
    else:
        body = ""

    text = subject.astype(str) + " " + body.astype(str)

    temp = pd.DataFrame({
        "text": text,
        "label": df["label"]
    })

    all_data.append(temp)

dataset = pd.concat(all_data, ignore_index=True)

print(f"\nTotal Emails: {len(dataset)}")

dataset["text"] = dataset["text"].apply(clean_text)

X = dataset["text"]
y = dataset["label"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=15000,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining model...")

model = LogisticRegression(
    max_iter=3000,
    class_weight="balanced"
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel saved successfully.")