import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import nltk

try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords')

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Review Sentiment Analyzer",
    page_icon="⭐",
    layout="centered"
)

# -------------------------------
# Load Model
# -------------------------------

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# -------------------------------
# NLP Preprocessing
# -------------------------------

stop_words = set(stopwords.words("english"))
ps = PorterStemmer()

def transform_review(review):

    review = str(review).lower()

    review = re.sub(r'[^a-zA-Z\s]', ' ', review)

    words = review.split()

    words = [
        ps.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# -------------------------------
# Custom Styling
# -------------------------------

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.title {
    text-align:center;
    font-size:42px;
    font-weight:700;
}

.subtitle {
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.result-box {
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:22px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# UI
# -------------------------------



st.markdown(
    '<div class="title">⭐ Review Sentiment Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict whether a customer review is Positive or Negative using Machine Learning</div>',
    unsafe_allow_html=True
)

review = st.text_area(
    "Enter Review",
    height=180,
    placeholder="Example: This product exceeded my expectations..."
)

# -------------------------------
# Prediction
# -------------------------------

if st.button("Analyze Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a review.")
    else:

        processed_review = transform_review(review)

        vector = vectorizer.transform([processed_review])

        prediction = model.predict(vector)[0]

        if prediction == 1:

            st.success("😊 Positive Review")

        else:

            st.error("😞 Negative Review")

st.markdown("---")

st.caption(
    "Built by Omkar Srivastava | "
    "TF-IDF + LinearSVC | "
    "Amazon Review Sentiment Analysis"
)