# 📧 AI Spam Email Classifier

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Deployed-success)

An end-to-end **Machine Learning** web application that intelligently classifies SMS or Email messages as **Spam** or **Not Spam** using **Natural Language Processing (NLP)** techniques.

The project uses **TF-IDF Vectorization** with a **Multinomial Naive Bayes** classifier and is deployed as an interactive **Streamlit** web application.

---

# 🚀 Live Demo

### 🌐 Web Application

👉 **https://spam-email-classifier-xeoj8ezz7jcoyhgqgtmbhv.streamlit.app/**

---

# 💻 GitHub Repository

👉 **https://github.com/pranathi-555/Spam-Email-Classifier**

---

# 📌 Project Overview

Spam emails and SMS messages are among the most common forms of unwanted digital communication. This project demonstrates how **Machine Learning** and **Natural Language Processing (NLP)** can automatically identify spam messages with high accuracy.

The application converts text into numerical features using **TF-IDF Vectorization**, then predicts whether the message is Spam or Not Spam using a trained **Multinomial Naive Bayes** model.

---

# ✨ Features

- 📧 Detect Spam & Legitimate Messages
- 🤖 Machine Learning-Based Prediction
- 🧠 Natural Language Processing (NLP)
- ⚡ TF-IDF Feature Extraction
- 📊 Multinomial Naive Bayes Classifier
- 🌐 Interactive Streamlit Web Application
- 🚀 Fully Deployed Online
- 💻 Responsive & User-Friendly Interface

---

# 🛠️ Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF Vectorizer |
| ML Algorithm | Multinomial Naive Bayes |
| Model Storage | Joblib |
| Web Framework | Streamlit |
| Version Control | Git & GitHub |

---

# 🧠 Machine Learning Workflow

```
Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Label Encoding
     │
     ▼
Train-Test Split
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Multinomial Naive Bayes
     │
     ▼
Model Evaluation
     │
     ▼
Save Model (.pkl)
     │
     ▼
Streamlit Web App
     │
     ▼
Deployment
```

---

# 📂 Project Structure

```
Spam-Email-Classifier
│
├── images/
│   ├── home.png
│   ├── spam.png
│   └── not_spam.png
│
├── app.py
├── spam_classifier.ipynb
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Application Screenshots

## 🏠 Home Page

![Home](images/home.png)

---

## 🚨 Spam Prediction

![Spam](images/spam.png)

---

## ✅ Not Spam Prediction

![Not Spam](images/not_spam.png)

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/pranathi-555/Spam-Email-Classifier.git
```

Navigate into the project folder

```bash
cd Spam-Email-Classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📖 Usage

1. Launch the application.
2. Enter an Email or SMS message.
3. Click **Predict**.
4. The model classifies the message as:
   - 🚨 Spam
   - ✅ Not Spam

---

# 🧪 Sample Predictions

### Example 1

**Input**

```
Congratulations!

You have won ₹50,000.

Click here to claim your prize immediately.
```

**Prediction**

```
🚨 Spam
```

---

### Example 2

**Input**

```
Hi Pranathi,

Can we meet tomorrow at 10 AM?
```

**Prediction**

```
✅ Not Spam
```

---

# 📈 Model Information

| Attribute | Details |
|-----------|---------|
| Dataset | SMS Spam Collection |
| Vectorization | TF-IDF |
| Algorithm | Multinomial Naive Bayes |
| Train/Test Split | 80/20 |
| Framework | Scikit-learn |
| Deployment | Streamlit |

---

# 🎯 Future Enhancements

- 📈 Display prediction confidence
- 📁 Bulk CSV message classification
- 🌍 Multi-language spam detection
- 📊 Prediction analytics dashboard
- 📝 Save prediction history
- ☁️ Docker & Cloud deployment

---

# 🎓 Learning Outcomes

Through this project, I gained hands-on experience in:

- Data preprocessing
- Natural Language Processing (NLP)
- Feature Engineering using TF-IDF
- Machine Learning Model Training
- Model Serialization
- Streamlit Web Application Development
- Git & GitHub
- Cloud Deployment

---

# 👩‍💻 Developer

**Pranathi Kurapati**

Artificial Intelligence Intern

GitHub:
https://github.com/pranathi-555


---

# 🙏 Acknowledgements

- SMS Spam Collection Dataset
- Scikit-learn
- Streamlit
- Python Community

---

# ⭐ Support

If you found this project useful, please consider giving this repository a ⭐ on GitHub.

---

# 📜 License

This project is developed for educational, learning, and internship purposes.
