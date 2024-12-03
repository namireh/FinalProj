import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(page_title="Loan Repayment Prediction", page_icon="💵")


if "form_data" not in st.session_state:
    st.session_state.form_data = {}

if "mode" not in st.session_state:
    st.session_state.mode = None

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
form_data = st.session_state.form_data
# Ensure Session State has the required data
if "form_data" not in st.session_state or not st.session_state.form_data:
    st.warning("No form data found. Please fill out the form on the previous page.")
    st.stop()   


form_data = st.session_state.form_data
x = form_data
model_value = x.pop('Model')

x = pd.DataFrame([form_data])

df_main = pd.read_csv('loan_data.csv')
df_main = df_main.drop(columns = "credit.policy", errors = 'coerce')
combined = pd.concat([df_main,x])
encoded = pd.get_dummies(df_main)
X_encoded = encoded.tail(1)



if model_value == "Decision Tree":

    with open('DT.pickle', 'rb') as dt_file:
        clf = pickle.load(dt_file)

elif model_value == "Random Forest":

    with open('RF.pickle', 'rb') as rf_file:
        clf = pickle.load(rf_file)

elif model_value == "Ada Boost":

    with open('ADA.pickle', 'rb') as ada_file:
        clf = pickle.load(ada_file)
    
elif model_value == "XGBoost":

    with open('XGB.pickle', 'rb') as xgb_file:
        clf = pickle.load(xgb_file)

elif model_value == "Soft Voting (Recomended)":

    with open('SV.pickle', 'rb') as SV_file:
        clf = pickle.load(SV_file)


prediction = clf.predict(X_encoded)
confidence_score = clf.predict_proba(X_encoded).max()


# Display the submitted form data (Optional)
st.write("### Submitted Borrower Details:")
st.json(form_data)

# Display Prediction Results
st.success("🎉 Prediction Generated!")
st.write(f"**Prediction**: The borrower is likely to **{prediction}** the loan.")
st.write(f"**Confidence Score**: {confidence_score:.2%}")

# Optional: Add visual representation
if prediction == "1" or prediction == 1:
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
