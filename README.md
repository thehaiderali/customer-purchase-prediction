
---

# Customer Purchase Prediction App

## Overview

This project predicts whether a customer will make a purchase based on their profile and behavior data. It uses **Logistic Regression** and **K-Nearest Neighbors (KNN)** models to analyze features such as age, income, website activity, loyalty program status, and discounts availed.

The app provides a **user-friendly interface** built with **Streamlit** for making predictions on new customer data.

---

## Features

* Predict purchase likelihood for new customers.
* Input validation to ensure realistic and safe values.
* Supports multiple models:

  * Logistic Regression
  * KNN (tested with multiple K values, best K chosen)
* Displays **probability of purchase** (if available).
* Confusion matrix and evaluation metrics used for model comparison.

---

## Dataset

The model was trained on a dataset with the following features:

| Feature            | Type  | Description                              |
| ------------------ | ----- | ---------------------------------------- |
| Age                | int   | Customer age                             |
| Gender             | int   | 0 = Male, 1 = Female                     |
| AnnualIncome       | float | Annual income in USD                     |
| NumberOfPurchases  | int   | Total purchases made                     |
| ProductCategory    | int   | ID of most purchased category            |
| TimeSpentOnWebsite | float | Average time spent per session (minutes) |
| LoyaltyProgram     | int   | 0 = Not enrolled, 1 = Enrolled           |
| DiscountsAvailed   | int   | Number of discounts availed              |
| PurchaseStatus     | int   | Target: 0 = No purchase, 1 = Purchase    |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/thehaiderali/customer-purchase-prediction.git
cd customer-purchase-prediction
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Enter customer details in the sidebar.
* Click **Predict Purchase Status**.
* The app will display the prediction and the probability of purchase.

---

## Model Details

* **Logistic Regression:** Used as baseline for binary classification.
* **KNN:** Tested multiple K values (3,5,7,9,11) and best model selected based on accuracy.
* **Evaluation Metrics:** Accuracy, Precision, Recall, and Confusion Matrix.

---

## Files in Repository

* `app.py` – Streamlit app for predicting purchase status.
* `best_model.pkl` – Trained model (either Logistic Regression or best KNN).
* `scaler.pkl` – MinMaxScaler used for feature scaling.
* `requirements.txt` – Python libraries required.
* `README.md` – Project documentation.

---

