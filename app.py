import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Spam Email Classifier")

st.markdown("""
This application predicts whether a message is **Spam** or **Not Spam**
using **Machine Learning (TF-IDF + Naive Bayes)**.
""")

message = st.text_area(
    "Enter your Email or SMS Message",
    height=180,
    placeholder="Type your message here..."
)

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        vector = vectorizer.transform([message])
        prediction = model.predict(vector)

        if prediction[0] == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")

st.divider()

st.caption("Developed by Pranathi Kurapati")