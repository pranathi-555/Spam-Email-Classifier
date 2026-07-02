import streamlit as st
import joblib

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="AI Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📌 Project Information")

st.sidebar.success("Artificial Intelligence Internship Project")

st.sidebar.markdown("""
### 👩‍💻 Developer
**Pranathi Kurapati**

---

### 🤖 Model
- TF-IDF Vectorizer
- Multinomial Naive Bayes

---

### 📚 Technologies
- Python
- Pandas
- Scikit-learn
- Streamlit

---

### 📊 Dataset
SMS Spam Collection Dataset

---

### 🎯 Accuracy
**98%**
""")

# ---------------------------
# Main Title
# ---------------------------
st.title("📧 AI Spam Email Classifier")

st.markdown("""
Detect whether an SMS or Email message is **Spam** or **Not Spam**
using **Machine Learning**.
""")

st.info("Model: TF-IDF + Multinomial Naive Bayes")

# ---------------------------
# Input
# ---------------------------
message = st.text_area(
    "Enter your Message",
    height=180,
    placeholder="Example: Congratulations! You have won ₹50,000..."
)

col1, col2 = st.columns(2)

predict = col1.button("🔍 Predict")
clear = col2.button("🗑 Clear")

# ---------------------------
# Prediction
# ---------------------------
if predict:

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:

        vector = vectorizer.transform([message])

        prediction = model.predict(vector)

        st.divider()

        if prediction[0] == 1:

            st.error("🚨 This message is SPAM")

            st.markdown("""
### Tips

- Do not click suspicious links.
- Verify the sender.
- Never share OTPs or passwords.
""")

        else:

            st.success("✅ This message is NOT SPAM")

            st.markdown("""
This message appears to be safe based on the trained model.
""")

# ---------------------------
# Footer
# ---------------------------
st.divider()

st.caption(
    "Developed by Pranathi Kurapati | AI Internship Project | Machine Learning using TF-IDF & Naive Bayes"
)