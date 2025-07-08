# 🍄 Mushroom Project – Edibility Classifier with ML

## 🧾 Project Abstract

This project aims to classify mushrooms as edible or poisonous using machine learning techniques. It combines an intuitive Streamlit interface with robust models trained on the UCI Mushroom Dataset. The web app also includes a secure authentication system and educational sections on mushrooms' ecological, biological, and nutritional roles.

---

## 📌 Table of Contents

- [Demo](#-demo)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Technologies Used](#-technologies-used)
- [Installation Guide](#-installation-guide)
- [Authentication System](#-authentication-system)
- [How It Works](#-how-it-works)
- [Machine Learning Models](#-machine-learning-models)
- [Feature Engineering](#-feature-engineering)
- [Data Preprocessing](#-data-preprocessing)
- [Data Exploration & Visualization](#-data-exploration--visualization)
- [Model Selection Rationale](#-model-selection-rationale)
- [Performance Metrics](#-performance-metrics)
- [Testing & Evaluation](#-testing--evaluation)
- [Real-World Applications](#-real-world-applications)
- [Dashboard Preview](#-dashboard-preview)
- [Deployment](#-deployment)
- [API Support](#-api-support)
- [Future Enhancements](#-future-enhancements)
- [Project Timeline / Milestones](#-project-timeline--milestones)
- [Safety Disclaimer](#-safety-disclaimer)
- [Feedback & Support](#-feedback--support)
- [Team](#-team)
- [Acknowledgments](#-acknowledgments)
- [References](#-references)
- [To-Do List](#-to-do-list)
- [License](#-license)

---

## 🚀 Demo

🖥️ [Live Demo](https://mushroom-trio-classifier.onrender.com/) (https://mushroom-trio-classifier.onrender.com/)  


---

## 📂 Project Structure

```
Mushroom-Project/
├── datasets/
├── models/
├── views/
├── Main.py
├── requirements.txt
├── users.db
└── README.md
```

## ⚙️ Technologies Used

- **Python** 🐍
- **Streamlit** 🌐 – for web interface
- **SQLite** 🗃️ – for authentication
- **Pandas & NumPy** – data handling
- **Scikit-learn** – ML model training
- **Matplotlib & Seaborn** – data visualization

---

## 📥 Installation Guide

1. Clone the repository:
```bash
git clone https://github.com/samarthgarde/Mushroom_Final_Project.git
cd Mushroom_Final_Project
```

2. Create and activate virtual environment:
```bash
python -m venv mushroom-env
source mushroom-env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python Main.py

```

---

## 🔒 Authentication System

- User login/signup
- Password hashing
- SQLite database

---

## 💡 How It Works

1. **User Login/Signup** through a secure interface.
2. **Select Mushroom Features** using dropdowns and forms.
3. **Model predicts** whether the mushroom is edible or poisonous.
4. Display results with **confidence score** and explanations.
5. Includes pages like:
   - 📚 **Mushroom Wisdom**: Biological, nutritional, and ecological info,Fun facts, types, and safety tips.
    - ✅ **Gallery**: project information ,behind the sceen and team.

---

## 📊 Machine Learning Models

Three classification models were trained and evaluated:
- 🔍 Logistic Regression
- 🌲 Random Forest Classifier
- 📈 Support Vector Machine (SVM)
---

## 📦 Feature Engineering

- Categorical encoding using LabelEncoder
- Removal of ambiguous data
- Feature selection based on correlation

---

## 🗃️ Data Preprocessing

- UCI dataset (8124 samples)
- Null/missing handling
- Train-test split (80:20)

---

## 📈 Data Exploration & Visualization

- Class distribution
- Feature correlation heatmaps
- Count plots for each feature

---

## 🧠 Model Selection Rationale

- Logistic Regression: Simple baseline
- Random Forest: Robust and accurate
- SVM: Great for small, high-dimensional data

---

## 📈 Performance Metrics

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 94.6% | 0.95 | 0.94 | 0.94 |
| Random Forest | 99.1% | 0.99 | 0.99 | 0.99 |
| SVM | 98.2% | 0.98 | 0.98 | 0.98 |

---

## 🧪 Testing & Evaluation

- 5-fold cross-validation
- Confusion matrix analysis
- ROC-AUC evaluation

---

## 🌍 Real-World Applications

- 🍽️ Food safety checks in rural foraging
- 🧑‍🌾 Agricultural advisory systems
- 📱 Edibility Checker apps for campers and hikers
- 🎓 Educational tools for botany students

---

## 📊 Dashboard Preview

(Insert real-time dashboard screenshots or preview here)

---

## 🛠️ Deployment

- To be deployed on Streamlit Cloud / Render 

---

## 📦 API Support

Planned future feature: REST API to classify mushrooms via JSON input

---

## 🌱 Future Enhancements

- Image-based classification (CNN)
- Mobile optimization
- Admin dashboard
- Multilingual support

---

## 📆 Project Timeline / Milestones

- 📌 Dataset research – Week 1
- 🤖 Model training & evaluation – Week 2
- 🧱 Streamlit frontend – Week 3
- 🔐 Auth integration – Week 4
- 🌐 Deployment – Week 5 (planned)

---

## 🛡️ Safety Disclaimer

⚠️ **Educational tool only.** Do not use for real-life mushroom identification. Seek expert advice.

---

## 💬 Feedback & Support

- Raise issues via GitHub Issues tab
- Contact developer via [GitHub Profile](https://github.com/samarthgarde)

---

## 🙏 Acknowledgments

- UCI Machine Learning Repository
- Streamlit team
- OpenAI for assistance
- Mentors and Professors 
- Team Members and Contributors

---

## 📚 References

- [UCI Mushroom Dataset](https://archive.ics.uci.edu/ml/datasets/Mushroom)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Scikit-learn Docs](https://scikit-learn.org/stable/user_guide.html)

---

## ✅ To-Do List

- [x] Implement Authentication System
- [x] Design UI in Streamlit
- [x] Build ML Modle 
- [X] Conduct User Testing & Feedback Collection
- [x] Deploy app publicly
- [ ] Implement REST API
- [ ] Admin Dashboard 
- [ ] Multilingual Support 

---

## 📄 License
This project is licensed under the [MIT License](https://mit-license.org/)

---
