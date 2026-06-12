# Amazon Review Sentiment Analysis

🚧 Work In Progress

A Machine Learning and Natural Language Processing project that classifies Amazon product reviews as Positive or Negative sentiments.

## Project Objective

Build an end-to-end sentiment analysis system using NLP preprocessing, feature engineering, machine learning models, and a deployable web application.

---

## Current Progress

* [x] Phase 1: Dataset Preparation
* [x] Phase 2: Exploratory Data Analysis (EDA)
* [ ] Phase 3: Text Preprocessing
* [ ] Phase 4: TF-IDF Feature Engineering
* [ ] Phase 5: Model Training & Evaluation
* [ ] Phase 6: Streamlit Web Application
* [ ] Phase 7: Deployment

---

## Dataset Information

* Total Reviews: 173,000
* Positive Reviews: 148,657
* Negative Reviews: 24,343

### Class Distribution

The dataset is imbalanced:

* Positive Reviews ≈ 86%
* Negative Reviews ≈ 14%

---

## Exploratory Data Analysis Findings

### Average Review Statistics

| Metric          | Overall | Positive | Negative |
| --------------- | ------- | -------- | -------- |
| Character Count | 513     | 518      | 487      |
| Word Count      | 95      | 96       | 91       |
| Sentence Count  | 7.34    | 7.31     | 7.49     |

### Key Insights

* Review length has very little correlation with sentiment.
* Correlation between sentiment and review length features is close to zero.
* Actual review text content is expected to be significantly more important than review length.
* Dataset imbalance must be considered during model evaluation.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* NLTK
* SpaCy
* Scikit-Learn
* Streamlit

---

## Planned NLP Pipeline

Raw Review

→ Lowercasing

→ Tokenization

→ Stopword Removal

→ Lemmatization

→ TF-IDF Vectorization

→ Machine Learning Model

→ Sentiment Prediction

---

## Future Models To Experiment With

* Logistic Regression
* Multinomial Naive Bayes
* LinearSVC
* Random Forest

---

## Author

Omkar Srivastava
