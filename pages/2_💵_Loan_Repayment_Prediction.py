import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Loan Repayment Prediction", page_icon="💵")

# Centered Title for Prediction Page
st.markdown(
    """
    <h2 style="text-align: center; color: #4CAF50;">Loan Repayment Prediction</h2>
    """,
    unsafe_allow_html=True,
)

# Subtitle for the Page
st.markdown(
    """
    <h3 style="text-align: center; color: #808080;">
    Instantly find out if the borrower is likely to repay their loan, along with a confidence score.
    </h3>
    """,
    unsafe_allow_html=True,
)

# Ensure Session State has the required data
if "form_data" not in st.session_state:
    st.warning("No form data found. Please fill out the form on the previous page.")
    st.stop()

# Accessing form data from Session State
form_data = st.session_state.form_data



df_main = pd.read_csv('loan_data.csv')
df_main.drop(columns = "credit.policy")
df_main.concat(form_data)

pd.get_dummies(df_main)

X_encoded = df_main.tail(1)

print(X_encoded)




# Display the submitted form data (Optional)
st.write("### Submitted Borrower Details:")
st.json(form_data)

# Prediction Logic (Placeholder: Replace with your ML model)
mock_prediction = np.random.choice(["Repay", "Default"], p=[0.8, 0.2])  # Mock prediction
confidence_score = np.random.uniform(0.7, 0.99)  # Mock confidence score

# Display Prediction Results
st.success("🎉 Prediction Generated!")
st.write(f"**Prediction**: The borrower is likely to **{mock_prediction}** the loan.")
st.write(f"**Confidence Score**: {confidence_score:.2%}")

# Optional: Add visual representation
if mock_prediction == "Repay":
    st.markdown(
        """
        <h4 style="text-align: center; color: #4CAF50;">✅ Borrower is likely to repay the loan!</h4>
        """, 
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <h4 style="text-align: center; color: #FF5733;">❌ Borrower is likely to default on the loan!</h4>
        """, 
        unsafe_allow_html=True
    )
