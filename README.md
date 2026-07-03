# Phishing Email Detection Model

## Overview

This project is a Machine Learning-based Phishing Email Detection System developed using Python and Scikit-learn. The system analyzes email content and classifies emails as either **Phishing** or **Safe**.

The model is trained using multiple publicly available phishing and legitimate email datasets and uses Natural Language Processing (NLP) techniques for email classification.

---

## Features

- Train a machine learning model using phishing and legitimate email datasets
- Extract text features using TF-IDF Vectorization
- Detect URLs present in emails
- Identify suspicious phishing-related keywords
- Classify emails as **Phishing** or **Safe**
- Display prediction confidence
- Generate accuracy score, confusion matrix, and classification report

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Regular Expressions (Regex)

---

## Dataset Used

The model is trained using the following datasets:

- CEAS_08 Dataset
- Enron Email Dataset
- Ling Dataset
- Nazario Dataset
- SpamAssassin Dataset
- Nigerian Fraud Dataset

These datasets contain both phishing and legitimate emails that help train the model to recognize malicious patterns.

---

## Project Structure

```text
phishing-email-detector/
│
├── CEAS_08.csv
├── Enron.csv
├── Ling.csv
├── Nazario.csv
├── Nigerian_Fraud.csv
├── SpamAssasin.csv
│
├── train_model.py
├── phishing_detector.py
├── requirements.txt
├── README.md
└── .gitignore

```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/nithinkumarkb-06/phishing-email-detector.git
cd phishing-email-detector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

Run the training script:

```bash
python train_model.py
```

The script will:

- Load and merge all datasets
- Clean and preprocess email content
- Extract features using TF-IDF
- Train a Logistic Regression model
- Evaluate model performance
- Save the trained model and vectorizer

### Example Output

```text
Accuracy:
98.21%

Confusion Matrix:
[[2100   45]
 [  37 1985]]
```

---

## Running Email Detection

After training the model, run:

```bash
python phishing_detector.py
```

Paste an email when prompted, then finish with Ctrl+Z and Enter on Windows or Ctrl+D on macOS/Linux.

Alternatively, analyze an email from a file:

```bash
python phishing_detector.py --file email.txt
```

```text
URGENT!

Your account has been suspended.

Verify immediately:
http://fake-bank-login.com

Click here to restore access.
```

### Example Output

```text
EMAIL ANALYSIS
--------------------------------------------------
URLs Found      : 1
Keyword Count   : 5

Prediction      : PHISHING
Confidence      : 97.62%

Indicators

✓ URL detected
✓ Suspicious keywords found
✓ Multiple phishing indicators found
--------------------------------------------------
```

---

## Git Large File Warning

This repository includes large dataset files such as `CEAS_08.csv` that exceed GitHub's recommended file size limit (50 MB). Consider using Git LFS for large datasets or storing them externally to keep the repo manageable.

---

## How It Works

### Data Preparation

- Combines multiple email datasets
- Merges email subject and body
- Removes unnecessary characters and noise
- Normalizes text for processing

### Feature Extraction

Uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert email text into numerical features.

### Model Training

The project uses **Logistic Regression** for binary classification:

- `0` → Safe Email
- `1` → Phishing Email

### Prediction

The trained model analyzes:

- Email text
- Suspicious keywords
- URLs

and predicts whether the email is **Phishing** or **Safe**.

---

## Evaluation Metrics

The model is evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

These metrics help measure the effectiveness of the phishing detection system.

---

## Learning Outcomes

Through this project, I learned:

- Machine Learning fundamentals
- Natural Language Processing (NLP)
- Text preprocessing techniques
- TF-IDF feature extraction
- Logistic Regression classification
- Email phishing detection concepts
- Cybersecurity threat analysis
- Model evaluation and performance measurement

---

## Future Enhancements

- Build a web interface using Flask
- Add real-time email scanning
- Improve feature engineering
- Use Deep Learning models such as LSTM or BERT
- Integrate URL reputation analysis
- Deploy the model as a web service

---

## Conclusion

This project demonstrates how Machine Learning can be used to identify phishing emails by analyzing email content and suspicious indicators. The system helps users recognize potentially malicious emails and provides practical experience with NLP, cybersecurity, and machine learning techniques.