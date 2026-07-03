import re
import joblib

model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

PHISHING_KEYWORDS = [
    "urgent",
    "verify",
    "account",
    "password",
    "bank",
    "login",
    "security",
    "click",
    "winner",
    "reward",
    "suspended",
    "confirm",
    "limited",
    "payment",
    "invoice",
    "update"
]


def count_urls(text):
    pattern = r'https?://\S+|www\.\S+'
    return len(re.findall(pattern, text))


def count_keywords(text):

    text = text.lower()

    count = 0

    found = []

    for keyword in PHISHING_KEYWORDS:

        if re.search(rf"\b{re.escape(keyword)}\b", text):
            count += 1
            found.append(keyword)

    return count, found


def clean_text(text):

    text = text.lower()

    text = re.sub(r"http\S+", " URL ", text)
    text = re.sub(r"www\S+", " URL ", text)

    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    return text


def analyze_email(email_text):

    urls = count_urls(email_text)

    keyword_count, keywords = count_keywords(email_text)

    processed_text = clean_text(email_text)

    features = vectorizer.transform([processed_text])

    prediction = model.predict(features)[0]

    confidence = max(
        model.predict_proba(features)[0]
    )

    print("\nEMAIL ANALYSIS")
    print("-" * 50)

    print(f"URLs Found      : {urls}")
    print(f"Keyword Count   : {keyword_count}")

    print(
        f"Prediction      : "
        f"{'PHISHING' if prediction == 1 else 'SAFE'}"
    )

    print(
        f"Confidence      : "
        f"{confidence*100:.2f}%"
    )

    print("\nIndicators")

    if urls:
        print("✓ URL detected")

    if keyword_count:
        print(
            f"✓ Suspicious keywords: "
            f"{', '.join(keywords)}"
        )

    if keyword_count >= 3:
        print(
            "✓ Multiple phishing indicators found"
        )

    print("-" * 50)


if __name__ == "__main__":

    email = input(
        "Paste email content:\n\n"
    )

    analyze_email(email)