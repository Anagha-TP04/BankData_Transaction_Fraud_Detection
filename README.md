🔍 Fraud Detection in Financial Transactions using Machine Learning

📌 Overview
This project aims to detect fraudulent financial transactions using a supervised Machine Learning approach. By analyzing transaction patterns and user behavior, the model predicts whether a future transaction is fraudulent or legitimate, helping financial institutions reduce risk and protect customers.

📂 Dataset from kaggle: https://www.kaggle.com/datasets/qusaybtoush1990/transactions-data-bank-fraud-detection
Dataset Overview
The dataset includes detailed information on financial transactions, with the following features:

Date – Date of the transaction

nameOrig – User ID or account number

amount – Transaction amount

oldbalanceOrg – Account balance before transaction

newbalanceOrig – Account balance after transaction

City – Location of transaction

type – Transaction type (TRANSFER, CASH_OUT, etc.)

Card Type – Type of card used (Platinum, Gold, etc.)

Exp Type – Purpose of transaction (Food, Bills, Travel, etc.)

Gender – User’s gender

isFraud – Target label: 0 = Not Fraud, 1 = Fraud

🧠 Model Approach
The model is built using popular ML algorithms such as:

Logistic Regression

Random Forest Classifier

XGBoost

Gradient Boosting

(Optional) Neural Networks for more complex patterns

🔧 Steps:

Data Preprocessing – Handle missing values, encode categorical data, and scale numeric features.

Exploratory Data Analysis (EDA) – Understand class imbalance, transaction types, card usage, etc.

Feature Engineering – Create meaningful features like transaction time difference, balance delta, etc.

Model Training – Train and validate on historical transaction data.

Evaluation – Metrics like accuracy, precision, recall, F1-score, and ROC-AUC are used.

Prediction – Use the trained model to predict whether a new transaction is fraudulent.

📈 Goal
To build a robust and accurate system for real-time fraud detection, reducing false positives while catching true fraud cases effectively.
