import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Customer Purchase Prediction")
st.write("Enter customer details to predict Purchase Status")

# Input fields with validation
age = st.number_input("Age", min_value=10, max_value=100, value=25, step=1)
gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x==0 else "Female")
annual_income = st.number_input("Annual Income ($)", min_value=0, max_value=1_000_000, value=50000, step=1000)
num_purchases = st.number_input("Number of Purchases", min_value=0, max_value=1000, value=5, step=1)
product_category = st.number_input("Product Category (ID)", min_value=0, max_value=50, value=1, step=1)
time_spent = st.number_input("Time Spent on Website (minutes)", min_value=0.0, max_value=1440.0, value=10.0, step=0.5)
loyalty_program = st.selectbox("Loyalty Program", [0, 1], format_func=lambda x: "No" if x==0 else "Yes")
discounts_availed = st.number_input("Discounts Availed", min_value=0, max_value=100, value=0, step=1)

# Button click for prediction
if st.button("Predict Purchase Status"):
    # Additional runtime validations
    errors = []
    if age < 10 or age > 100:
        errors.append("Age must be between 10 and 100.")
    if annual_income < 0:
        errors.append("Annual Income cannot be negative.")
    if num_purchases < 0:
        errors.append("Number of Purchases cannot be negative.")
    if time_spent < 0:
        errors.append("Time Spent cannot be negative.")
    if discounts_availed < 0:
        errors.append("Discounts Availed cannot be negative.")

    if errors:
        st.error(" | ".join(errors))
    else:
        # Create dataframe for model
        input_df = pd.DataFrame([[age, gender, annual_income, num_purchases, product_category,
                                  time_spent, loyalty_program, discounts_availed]],
                                columns=['Age', 'Gender', 'AnnualIncome', 'NumberOfPurchases',
                                         'ProductCategory', 'TimeSpentOnWebsite', 'LoyaltyProgram', 'DiscountsAvailed'])

        # Scale input
        input_scaled = scaler.transform(input_df)

        # Prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1] if hasattr(model, "predict_proba") else None

        st.subheader("Prediction:")
        st.write("✅ Will Purchase" if prediction == 1 else "❌ Will Not Purchase")
        if probability is not None:
            st.write(f"Probability of Purchase: {probability:.2f}")

