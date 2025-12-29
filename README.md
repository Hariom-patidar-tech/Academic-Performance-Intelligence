# 🎓 Student Performance Prediction System
### Academic Performance Intelligence using Machine Learning

---

## 📌 Project Overview
The **Student Performance Prediction System** is an AI/ML-based application designed to predict a student’s academic performance using key educational parameters such as study hours, attendance, previous exam scores, and assignment performance.

This project demonstrates a **real-world machine learning workflow**, combined with an **interactive dashboard built using Streamlit**, making it suitable for academic analysis and decision support in educational institutions.

---

## 🎯 Project Objectives
- Predict student academic performance using Machine Learning
- Categorize performance levels (Poor, Average, Good, Excellent)
- Provide data-driven insights and recommendations
- Build a clean, professional, real-world dashboard
- Apply end-to-end ML pipeline (data → model → deployment)

---

## 🛠️ Technologies & Tools Used
- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **VS Code**

---

## 📊 Dataset Information
The dataset used in this project is a **custom educational dataset** created for academic and demonstration purposes.

### Dataset Features:
- `Student_Name` – Name/Identifier of the student  
- `Study_Hours` – Weekly study hours  
- `Attendance` – Attendance percentage  
- `Previous_Score` – Previous exam marks  
- `Assignment_Score` – Assignment performance score  
- `Final_Score` – Target variable (final academic score)

> **Note:** Student names are included only for readability and UI presentation.  
They are not used as input features for model training.

---

## 🤖 Machine Learning Model
- **Algorithm Used:** Random Forest Regressor
- **Reason for Selection:**
  - Handles non-linear relationships
  - Robust and accurate for tabular data
  - Widely used in real-world analytics applications

### Model Evaluation Metrics:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 🖥️ Application Features
- Professional and clean dashboard layout
- Student profile overview panel
- Interactive input controls (sliders & inputs)
- Performance prediction with progress bar
- Color-based performance status indicators
- AI-based academic recommendations
- Real-world style UI built using Streamlit

---

## 📂 Project Structure
Student_performance/
├── app.py # Streamlit application (UI + prediction)
├── model.py # Machine Learning model training & evaluation
├── data.csv # Dataset
└── README.md # Project documentation

yaml
Copy code

---

## ▶️ How to Run the Project Locally

### Step 1: Clone the Repository

git clone https://github.com/YOUR_USERNAME/Student-Performance-Prediction.git
Step 2: Navigate to Project Directory

cd Student_performance
Step 3: Install Required Libraries

pip install pandas numpy scikit-learn streamlit
Step 4: Run the Streamlit Application

python -m streamlit run app.py
Step 5: Open in Browser

http://localhost:8501


📚 Learning Outcomes
Practical understanding of data preprocessing techniques

Hands-on experience with machine learning models

Experience in deploying ML models using Streamlit

Designing real-world style dashboards

End-to-end AI/ML project development

🚀 Future Enhancements
User authentication (Admin / Student view)

Interactive data visualizations (charts & graphs)

PDF report generation

Database integration for large-scale data

Model optimization and comparison

👨‍💻 Author
Hariom Patidar
AI / ML & Data Science Learner

I am still learning and continuously improving my skills.


