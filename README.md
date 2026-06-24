# Amazon Review Sentiment Analysis

-- Work In Progress

A Machine Learning and Natural Language Processing project that classifies Amazon product reviews as Positive or Negative sentiments using text preprocessing, feature engineering, and machine learning algorithms.

---

## Project Objective

Build an end-to-end sentiment analysis system capable of automatically predicting customer sentiment from Amazon product reviews and deploy it as an interactive web application.

## Project Structure

```text
AMAZON-REVIEW-SENTIMENT-ANALYSIS/

├── notebook2.ipynb         # Complete ML workflow
├── README.md               # Project documentation
├── requirements.txt        # Project dependencies
├── .gitignore              # Git ignore rules
├── model.pkl               # Trained LinearSVC model
├── vectorizer.pkl          # TF-IDF vectorizer
├── Cell_Phones_and_Accessories_5.json (ignored from Git)
└── future_streamlit_app/
```

## Current Progress

* [x] Phase 1: Dataset Preparation
* [x] Phase 2: Exploratory Data Analysis (EDA)
* [x] Phase 3: Text Preprocessing 
* [x] Phase 4: TF-IDF Feature Engineering
* [x] Phase 5: Model Training & Evaluation
* [ ] Phase 6: Streamlit Web Application
* [ ] Phase 7: Deployment

---

## Dataset Information

### Original Dataset

* Total Reviews: 173,000
* Positive Reviews: 148,657
* Negative Reviews: 24,343

### Class Distribution

The dataset is imbalanced:

* Positive Reviews ≈ 86%
* Negative Reviews ≈ 14%

### Development Dataset

To improve experimentation speed while preserving class balance, a stratified sample of 50,000 reviews was created.

* Positive Reviews: 42,964
* Negative Reviews: 7,036

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
* Correlation between sentiment and review-length features is close to zero.
* Actual review text content is expected to contribute more to sentiment prediction than review length.
* Dataset imbalance must be considered during model evaluation.
* Text-based feature extraction is likely to be the most influential component of the model.

---

## NLP Preprocessing Pipeline

The following preprocessing steps were applied to review text:

* Lowercasing
* Text Cleaning
* Stopword Removal
* Porter Stemming (NLTK)

### Preprocessing Design Decision

PorterStemmer (NLTK) was chosen over SpaCy Lemmatization because:

- Significantly faster preprocessing on large datasets
- Lower computational cost
- Simpler implementation
- Comparable performance for TF-IDF based sentiment classification

During experimentation, SpaCy lemmatization was found to be considerably slower on the full dataset of 173,000 reviews, while PorterStemmer provided an efficient trade-off between speed and model performance.

### Example

Original Review:

This phone is absolutely amazing and works perfectly!

Processed Review:

phone absolut amaz work perfect

---

## Feature Engineering

TF-IDF (Term Frequency–Inverse Document Frequency) Vectorization was used to convert processed review text into numerical feature vectors suitable for machine learning models.

### Why TF-IDF?

- Captures the importance of words within reviews
- Reduces the influence of extremely common words
- Works exceptionally well with traditional text classification algorithms
- Efficient for large-scale sentiment analysis tasks

### Configuration

- Maximum Features: 5000
- Input: Preprocessed Reviews
- Output: Sparse Numerical Feature Matrix

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* NLTK
* Scikit-Learn
* Streamlit
* Git
* GitHub

---

## Planned Machine Learning Workflow

Raw Review

→ Text Preprocessing

→ TF-IDF Vectorization

→ Train-Test Split

→ Model Training

→ Model Evaluation

→ Streamlit Deployment

---

## Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|---------|---------|---------|---------|---------|
| Multinomial Naive Bayes | 88.27% | 88.06% | 99.90% | 93.60% |
| Logistic Regression | 89.68% | 97.84% | 89.98% | 93.74% |
| LinearSVC | **89.96%** | **97.32%** | **90.82%** | **93.96%** |

---

## Evaluation Metrics

The following metrics will be used to compare model performance:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Final Model Selection

LinearSVC was selected as the production model because it achieved the highest overall performance across Accuracy, Recall, and F1 Score while maintaining strong generalization on unseen reviews.

### Final Test Performance

- Accuracy: 89.96%
- Precision: 97.32%
- Recall: 90.82%
- F1 Score: 93.96%

### Error Analysis

- Test Samples: 10,000
- Correct Predictions: 8,996
- Misclassifications: 1,004

The model demonstrated strong performance while maintaining balanced sentiment detection across both positive and negative reviews.

## Model Interpretability

To understand the model's decision-making process, LinearSVC feature weights were analyzed.

Words with highly positive weights strongly influenced Positive predictions, while words with highly negative weights influenced Negative predictions.

This helped verify that the model learned meaningful sentiment patterns rather than relying on superficial dataset characteristics such as review length.

## Future Improvements

* Hyperparameter tuning
* N-gram feature engineering
* Model comparison and optimization
* Confidence score prediction
* Deep Learning based sentiment analysis
* Support for real-time sentiment prediction

---

## Author

**Omkar Srivastava**
