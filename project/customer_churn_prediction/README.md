# 📊 ConnectTel Customer Churn Prediction

## Project Overview

Customer churn is one of the major challenges faced by telecommunications companies. Losing existing customers can affect revenue and long-term business growth.

This project analyzes historical customer data from **ConnectTel Communications** to understand customer churn patterns and build a machine learning model that can identify customers who are likely to churn.

The project covers:

- Data cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Feature selection
- Machine learning model building
- Model evaluation
- Interactive churn prediction
- Business insights and recommendations

The final application provides an interactive dashboard where users can explore customer churn patterns and enter customer information to estimate churn probability.

---

## 🚀 Live Demo

### Streamlit Dashboard

[Open the ConnectTel Customer Churn Prediction App](https://connecttel-customer-churn-prediction.streamlit.app/)

The application allows users to:

- Explore customer churn patterns
- Analyze churn across customer segments
- Compare churn across cities, plans and contract types
- Enter customer information
- Predict the probability of customer churn
- View model performance
- View the confusion matrix

---

## 🎯 Business Problem

ConnectTel Communications wants to move from a reactive customer-retention strategy to a proactive one.

Instead of waiting until customers leave, the company wants to identify customers who are more likely to churn and take action beforehand.

The project aims to help answer questions such as:

- Which types of customers are more likely to churn?
- Which customer characteristics are associated with churn?
- Can we predict whether a customer is likely to churn?
- How accurately can we identify high-risk customers?
- How can the business use these predictions to improve retention?

---

## 🎯 Project Objectives

The main objectives of this project are:

- Understand customer churn behavior
- Perform exploratory data analysis
- Identify potential churn drivers
- Clean and prepare customer data
- Handle missing values and data-quality issues
- Engineer useful features
- Reduce unnecessary features
- Build a customer churn prediction model
- Compare different feature-selection approaches
- Evaluate model performance
- Provide an interactive prediction application
- Support proactive customer-retention decisions

---

## 📊 Dataset

The dataset contains historical customer information collected from different operational areas of the business.

The features cover areas such as:

- Customer demographics
- Subscription information
- Billing information
- Payment behavior
- Service usage
- Contract details
- Customer support interactions
- Network performance
- Customer engagement
- Customer value and revenue

### Target Variable

The target variable is:

`churn_flag`

Where:

- `0` = Customer did not churn
- `1` = Customer churned

---

## 🔄 Project Workflow

```text
Business Understanding
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Selection
        │
        ├───────────────┐
        │               │
        ▼               ▼
     RFECV          Tree-Based
        │            Selection
        │               │
        └───────┬───────┘
                ▼
           Consensus
                │
                ▼
         Model Building
                │
                ▼
       SMOTE + XGBoost
                │
                ▼
       Experiment Comparison
                │
                ▼
        Select Best Model
                │
                ▼
       Streamlit Application

```
---

## 🧹 Data Cleaning

The data-cleaning stage prepares the raw customer data for analysis and modelling.

The process includes:

- Checking the dataset structure
- Identifying missing values
- Checking duplicate records
- Checking data types
- Handling invalid or inconsistent values
- Examining numerical distributions
- Identifying potential outliers
- Preparing the target variable

The cleaned dataset is then used for EDA and subsequent modelling stages.
---

## 🔎 Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the data before building the prediction model.

The analysis includes:

- Dataset overview
- Missing-value analysis
- Duplicate detection
- Statistical summaries
- Churn distribution
- Numerical feature distributions
- Categorical feature analysis
- Correlation analysis
- Outlier analysis
- Customer segmentation
- Relationships between customer characteristics and churn

### Visualizations

The EDA includes:

- Histograms
- Count plots
- Box plots
- Bar charts
- Heatmaps
- Correlation matrices
- Other exploratory visualizations

The purpose of EDA is to understand the data and identify patterns that may be useful for predicting churn.
---

## ⚙️ Feature Engineering and Preprocessing

Before machine learning, the customer data needs to be converted into a format that the model can understand.

The preprocessing pipeline includes:

- Missing-value imputation
- Numerical feature processing
- Categorical feature processing
- One-hot encoding of categorical variables
- Scaling of numerical features
- Data transformation

After preprocessing, the dataset contains **46 processed features**.

For example, a categorical feature such as:

`plan_type`

can be converted into multiple numerical features through one-hot encoding.

The preprocessing pipeline is saved so that the exact same transformations can be applied when making predictions in the application.
---

## 🎯 Feature Selection

Using all 46 processed features is not necessarily optimal.

Some features may provide little useful information to the model. Using unnecessary features can also make the model more difficult to interpret.

Therefore, three feature-selection experiments were performed.

Each experiment selects **15 features from the 46 processed features**.

### Experiment 1 — RFECV + Logistic Regression

RFECV stands for **Recursive Feature Elimination with Cross-Validation**.

In simple terms, it repeatedly removes less useful features and evaluates the remaining features using Logistic Regression.

The process helps identify a smaller group of features that work well for classification.

**Result:** 15 features selected.

### Experiment 2 — Tree-Based Feature Selection

Tree-based feature importance was used to identify features that contribute strongly to predictions.

Tree models can measure how useful each feature is when making decisions.

The highest-ranked features were selected.

**Result:** 15 features selected.

### Experiment 3 — Consensus Feature Selection

The results from the first two feature-selection approaches were combined.

Features selected by both approaches receive higher priority because two different methods agree that they are useful.

The highest-ranked features based on this consensus were selected.

**Result:** 15 features selected.
---

## 🤖 Model Building

All three feature-selection experiments were evaluated using the **same XGBoost model setup**.

This is important because it makes the comparison fair.

Each experiment uses:

- The same train/test split
- The same random state
- The same SMOTE approach
- The same XGBoost algorithm
- The same XGBoost hyperparameters
- The same evaluation metrics
- 15 selected features
---

## ⚖️ SMOTE

The churn dataset contains fewer churned customers than non-churned customers.

This creates an imbalance between the two classes.

**SMOTE (Synthetic Minority Over-sampling Technique)** is used to create additional synthetic examples of the minority class in the training data.

This helps the model learn the churn class better.

SMOTE is applied **only to the training data**, not the test data.
---

## 🌳 XGBoost

XGBoost is the machine learning algorithm used for the final churn prediction models.

It is a tree-based machine learning algorithm that builds multiple decision trees and combines their predictions.

The XGBoost configuration used for the experiments includes:

```text
n_estimators = 200
learning_rate = 0.05
max_depth = 6
eval_metric = logloss
random_state = 42
n_jobs = -1

```
---

## 📈 Model Comparison

The three experiments were evaluated using Precision, Recall, F1 Score and ROC-AUC.

| Experiment | Features | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| **Experiment 1 – RFECV** | 15 | 60.55% | **78.08%** | **68.20%** | 86.75% |
| Experiment 2 – Tree | 15 | **61.19%** | 76.74% | 68.08% | 86.59% |
| Experiment 3 – Consensus | 15 | 60.87% | 75.62% | 67.45% | **86.88%** |
---

## 🏆 Best Model

**Experiment 1 – RFECV + Logistic Regression feature selection** was selected as the current winning experiment because it achieved the highest **F1 Score of 68.20%**.

The winning model uses:

```text
46 processed features
        ↓
15 selected features
        ↓
SMOTE
        ↓
XGBoost
        ↓
Churn prediction

## 16. Model Evaluation Metrics

```
---

## 📏 Model Evaluation Metrics

The application reports the following metrics.

### Precision

Of the customers predicted to churn, how many actually churned?

### Recall

Of all customers who actually churned, how many did the model successfully identify?

### F1 Score

F1 combines Precision and Recall into a single score.

It is particularly useful when the dataset contains an imbalance between churned and non-churned customers.

### ROC-AUC

ROC-AUC measures how well the model distinguishes between customers who churn and customers who do not churn.

### Confusion Matrix

The confusion matrix shows:

- True Negatives
- False Positives
- False Negatives
- True Positives

This provides a more detailed view of the model's predictions.
---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application.

The application contains three main sections.

### 📊 Dashboard

The dashboard provides an overview of customer churn patterns.

Users can explore:

- Customer distributions
- Churn patterns
- Customer segments
- Cities
- Plans
- Contract types
- Other customer characteristics

### 🔮 Predict Churn

Users can enter customer information and receive:

- Churn prediction
- Churn probability
- Visual indication of churn risk

The prediction interface is **dynamic**.

It automatically uses the features selected by the current winning experiment.

If a different experiment becomes the best model in the future, the saved feature indices can be updated and the prediction interface adapts accordingly.

### 🤖 Model Performance

The application displays:

- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix

This allows users to understand how well the selected model performs.
---

## 📁 Project Structure

```text
customer_churn_prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_building.ipynb
│
├── src/
│   ├── data.py
│   ├── model.py
│   ├── dashboard.py
│   ├── prediction.py
│   └── evaluation.py
│
├── models/
│   ├── preprocessor.pkl
│   ├── feature_selector.pkl
│   ├── best_churn_model.pkl
│   ├── best_feature_indices.pkl
│   └── best_experiment.pkl
│
├── app.py
├── requirements.txt
└── README.md
```
---

## 🚀 Running the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
streamlit run app.py

```
---

## 📌 Key Takeaways

The project demonstrates a complete machine-learning workflow for customer churn prediction.

The main findings from the current experiments are:

- The processed dataset contains **46 features**.
- Feature selection reduced this to **15 features**.
- Three feature-selection approaches were compared.
- All three approaches were evaluated using the same **SMOTE + XGBoost** setup.
- **Experiment 1** currently performs best.
- The best F1 Score is **68.20%**.
- The best Recall is **78.08%**.
- The best Precision is **60.55%**.
- The best ROC-AUC among the three experiments is **86.88%**, achieved by Experiment 3.
- The final application uses the current best-performing experiment.

The model can help the business identify customers who may be at higher risk of leaving, allowing customer-retention teams to take action earlier.
---

## 🔮 Future Improvements

Potential future improvements include:

- Hyperparameter tuning
- Threshold optimization
- Additional feature-selection techniques
- Testing additional machine learning algorithms
- Model explainability using SHAP
- Improved churn-risk segmentation
- Automated model retraining
- Monitoring model performance over time
- More targeted retention recommendations
---

## 🏁 Conclusion

This project demonstrates how customer data can be transformed into actionable churn predictions.

Starting with raw customer information, the project goes through data cleaning, EDA, feature engineering, preprocessing, feature selection, model training and evaluation.

Three different feature-selection strategies were compared fairly using the same SMOTE and XGBoost configuration. The current best-performing approach is **RFECV-based feature selection followed by XGBoost**, achieving an F1 Score of **68.20%**.

The resulting model is integrated into a Streamlit application that allows users to explore churn patterns, make individual customer predictions and evaluate model performance.

Overall, the project provides a foundation for moving from **reactive customer retention to proactive, data-driven churn management**.
---

## 👤 Author

**Tirtha Raut**

Data Analytics | Machine Learning | Customer Analytics
---

## 📄 License

This project is intended for educational and analytical purposes.