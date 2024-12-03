import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Loan Repayment Prediction", page_icon="💵", layout="centered")

if "form_data" not in st.session_state or not st.session_state.form_data:
    st.warning("No form data found. Please fill out the form on the first page.")
    st.stop()

# Load form data
form_data = st.session_state.form_data.copy()
model_value = form_data.get("Model")  # Retrieve the model value without popping

if not model_value:
    st.warning("No ML model selected. Please go back to the first page.")
    st.stop()

# Function to make predictions
def make_prediction(form_data, model_value):
    x = form_data.copy() 
    x.pop("Model", None)  

    x = pd.DataFrame([x])

    df_main = pd.read_csv("loan_data.csv")
    df_main = df_main.drop(columns="credit.policy", errors="coerce")
    trained_encoded = pd.get_dummies(df_main)
    X_encoded = pd.get_dummies(x).reindex(columns=trained_encoded.columns, fill_value=0)

    # Load the selected ML model Chat GPT helped organize this
    model_files = {
        "Decision Tree": "DT.pickle",
        "Random Forest": "RF.pickle",
        "Ada Boost": "ADA.pickle",
        "XGBoost": "XGB.pickle",
        "Soft Voting (Recommended)": "SV.pickle",
    }
    with open(model_files[model_value], "rb") as model_file:
        clf = pickle.load(model_file)

    prediction = clf.predict(X_encoded)[0]
    confidence_score = clf.predict_proba(X_encoded).max()
    print(prediction)
    return prediction, confidence_score

# Generate prediction
prediction, confidence_score = make_prediction(form_data, model_value)

# Display results
st.markdown(
    """
    <h2 style="text-align: center; color: #4CAF50;">Loan Repayment Prediction</h2>
    """,
    unsafe_allow_html=True,
)

if prediction == 1 or prediction == '1':
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h3 style="color: #4CAF50;">✅ The borrower is likely to repay the loan!</h3>
            <p style="font-size: 18px;">Confidence Score: <strong>{confidence_score:.2%}</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h3 style="color: #FF5733;">❌ The borrower is likely to default on the loan!</h3>
            <p style="font-size: 18px;">Confidence Score: <strong>{confidence_score:.2%}</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

