import argparse
import re
import sys
import joblib

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


def load_model_artifacts():
    try:
        model = joblib.load("phishing_model.pkl")
        vectorizer = joblib.load("vectorizer.pkl")
    except FileNotFoundError as exc:
        raise SystemExit(
            "Model artifacts not found. Run train_model.py first and ensure phishing_model.pkl and vectorizer.pkl are present."
        ) from exc

    return model, vectorizer


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


def analyze_email(email_text, model, vectorizer):
    urls = count_urls(email_text)
    keyword_count, keywords = count_keywords(email_text)
    processed_text = clean_text(email_text)
    features = vectorizer.transform([processed_text])

    prediction = model.predict(features)[0]
    confidence = max(model.predict_proba(features)[0])

    print("\nEMAIL ANALYSIS")
    print("-" * 50)
    print(f"URLs Found      : {urls}")
    print(f"Keyword Count   : {keyword_count}")
    print(f"Prediction      : {'PHISHING' if prediction == 1 else 'SAFE'}")
    print(f"Confidence      : {confidence*100:.2f}%")

    print("\nIndicators")
    if urls:
        print("✓ URL detected")
    if keyword_count:
        print(f"✓ Suspicious keywords: {', '.join(keywords)}")
    if keyword_count >= 3:
        print("✓ Multiple phishing indicators found")
    print("-" * 50)


def read_email_from_stdin():
    print(
        "Paste email content below, then press Ctrl+Z and Enter on Windows or Ctrl+D on macOS/Linux to finish.\n"
    )
    return sys.stdin.read().strip()


def main():
    parser = argparse.ArgumentParser(
        description="Detect phishing emails from text input or a file."
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Path to a text file containing the email content."
    )
    args = parser.parse_args()

    model, vectorizer = load_model_artifacts()

    if args.file:
        with open(args.file, encoding="utf-8") as fp:
            email = fp.read().strip()
    else:
        email = read_email_from_stdin()

    if not email:
        raise SystemExit("No email text provided. Exiting.")

    analyze_email(email, model, vectorizer)


if __name__ == "__main__":
    main()
