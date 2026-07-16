# StudentDrop AI

## Explainable AI-Powered Early Warning System for Student Dropout Prediction

---

# 1. Project Overview

**StudentDrop AI** is an Explainable AI-powered Early Warning System designed to identify students who are at high risk of dropping out before withdrawal occurs.

The system uses historical student data, including academic performance, demographic information, and socioeconomic factors, to predict dropout risk and provide explainable insights that support early intervention.

Instead of reacting after students leave, universities can proactively identify struggling students and provide targeted support such as:

* Academic counselling
* Financial assistance
* Mentoring programs
* Psychological support
* Attendance monitoring

---

# 2. Business Problem

Many universities discover struggling students only after they have already withdrawn from their studies.

At this stage:

* Tuition revenue has been lost
* Intervention opportunities are limited
* Graduation rates decrease
* Student satisfaction declines
* Institutional performance may be affected

## Business Objective

Increase student retention by enabling universities to identify high-risk students early and provide timely intervention.

---

# 3. Data Science Objective

Develop a supervised machine learning model that predicts whether a student is at risk of dropout based on:

* Academic performance
* Attendance behavior
* Demographic characteristics
* Socioeconomic conditions
* Previous academic history

The model focuses not only on prediction accuracy but also on:

* Identifying high-risk students
* Understanding dropout drivers
* Providing explainable predictions

---

# 4. Project Architecture

```
Student Data
      |
      |
Data Processing & Feature Engineering
      |
      |
Machine Learning Model
      |
      |
Risk Prediction Engine
      |
      |
Explainable AI Output
      |
      |
Student Intervention Recommendation
```

---

# 5. Repository Structure

```
StudentDrop-AI/
│
├── core/
│   │
│   ├── explain.py/
│   ├── predictor.py/
│   ├── preprocessing.py/
│   └── recomendation.py/
│
├── models/
│   │
│   └── tuned_binary_ensemble.pkl
│
├── reports/
│   │
│   ├── Data_Dictionary.pdf
│   ├── Pillar_5_Capstone_Project.pdf
│   ├── StudentDrop_Business Deck.pdf
│   └── StudentDrop_Technical Deck.pdf
│
├── Student dropout.xlsx
│
├── student-drop-out.ipynb
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
└── LICENSE
```

---

# 6. Machine Learning Workflow

## Step 1 — Data Understanding

Objective:

Understand student characteristics and identify factors associated with dropout.

Activities:

* Dataset exploration
* Data quality checking
* Feature analysis
* Target variable analysis

---

## Step 2 — Exploratory Data Analysis (EDA)

Analyze relationships between:

* Academic performance
* Attendance
* Financial conditions
* Demographics
* Dropout status

Key outputs:

* Distribution analysis
* Correlation analysis
* Dropout pattern identification

---

## Step 3 — Data Preparation

Performed:

* Missing value handling
* Feature encoding
* Feature scaling
* Dataset splitting

Dataset split:

```
Training Set
Validation Set
Testing Set
```

---

## Step 4 — Model Development

Problem Type:

**Binary Classification**

Target:

```
Dropout Risk

0 = Continue Study
1 = Dropout
```

Candidate models:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost

Model evaluation focuses on:

* Recall
* Precision
* F1-score
* ROC-AUC

---

# 7. Model Evaluation Strategy

For dropout prediction, identifying at-risk students is more important than overall accuracy.

The priority is:

> Missing a high-risk student is more costly than incorrectly identifying a low-risk student.

Therefore, evaluation emphasizes:

## Technical Metrics

* Recall
* Precision
* F1 Score
* ROC-AUC

## Business Metrics

* Early intervention coverage
* Reduction in dropout rate
* Students successfully retained
* Estimated tuition revenue preserved

---

# 8. Prediction Engine

The prediction engine provides:

Input:

Student information

↓

Processing:

Feature transformation

↓

Prediction:

Dropout probability

↓

Output:

Example:

```
Student ID:
12345

Risk Level:
HIGH RISK

Probability:
82%

Main Risk Factors:
- Low GPA
- High absence rate
- Financial difficulty

Recommended Action:
Academic counselling
Financial support review
```

---

# 9. Application Development Status

## Completed

✅ Data analysis pipeline
✅ Machine learning model development
✅ Model evaluation
✅ Prediction engine
✅ Business presentation
✅ Technical presentation
✅ Project documentation

---

## In Development

🚧 Interactive prediction application

🚧 Student risk dashboard

🚧 Automated intervention recommendation system

Future application capabilities:

* Individual student prediction
* Bulk student prediction
* Risk ranking
* Explainable prediction report
* Advisor dashboard

---

# 10. Reports and Deliverables

The `reports/` folder contains project documentation:

## Data Dictionary

Description of:

* Dataset variables
* Feature definitions
* Data types
* Target variable explanation

---

## Pillar 5 Capstone Project Report

Contains:

* Problem understanding
* Data science methodology
* Model development
* Evaluation
* Business impact

---

## Business Presentation

**StudentDrop_Business_Deck**

Focus:

* Business problem
* ROI impact
* Stakeholder benefits
* Implementation strategy

Audience:

University executives and decision makers

---

## Technical Presentation

**StudentDrop_Technical_Deck**

Focus:

* Dataset
* Machine learning methodology
* Feature engineering
* Model evaluation
* Technical findings

Audience:

Data science and technical reviewers

---

# 11. Installation

Clone repository:

```bash
git clone https://github.com/jojhony/StudentDropAI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 12. Running Prediction Engine

```python
from app.predictor_engine import predict_student_risk

result = predict_student_risk(student_data)

print(result)
```

---

# 13. Future Improvements

Future development plans:

### Model Improvement

* Hyperparameter optimization
* Ensemble modeling
* Model monitoring

### Application Improvement

* Web-based dashboard
* Automated PDF risk reports
* University database integration
* Real-time monitoring

### AI Explainability

* SHAP-based explanation
* Individual student risk analysis
* Intervention recommendation engine

---

# 14. Conclusion

StudentDrop AI demonstrates how Artificial Intelligence can transform student retention management from a reactive process into a proactive intervention system.

By identifying students at risk earlier, universities can:

* Improve student success
* Increase retention rates
* Protect institutional revenue
* Support better academic outcomes

---

## Author

**Jo Jhony**

AI / Data Science Capstone Project

2026
