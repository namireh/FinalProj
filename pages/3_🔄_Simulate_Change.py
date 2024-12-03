import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="What-If Analysis", page_icon="🔍")

if "form_data" not in st.session_state or not st.session_state.form_data:
    st.warning("No form data found. Please fill out the form on the first page.")
    st.stop()


form_data = st.session_state.form_data.copy()  
model_value = form_data.get("Model")  

if not model_value:
    st.warning("No ML model selected. Please go back to the first page and complete the form.")
    st.stop()

# Function to align input features with training features
def align_features(input_data, trained_features):
    encoded_input = pd.get_dummies(input_data)
    aligned_input = encoded_input.reindex(columns=trained_features, fill_value=0)
    return aligned_input

# Function to make predictions
def make_prediction(form_data, model_value):
    x = form_data.copy() 
    x.pop("Model", None)  

    x = pd.DataFrame([x])

    df_main = pd.read_csv("loan_data.csv")
    df_main = df_main.drop(columns="credit.policy", errors="coerce")
    trained_encoded = pd.get_dummies(df_main)
    X_encoded = pd.get_dummies(x).reindex(columns=trained_encoded.columns, fill_value=0)

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

    return prediction, confidence_score

# Sidebar for displaying predictions
with st.sidebar:
    st.header("📊 Prediction Results")

    # Generate predictions based on the current form data
    prediction, confidence_score = make_prediction(form_data, model_value)

    if prediction == 1 or prediction == "1":
        st.success("✅ Borrower is likely to repay the loan!")
    else:
        st.error("❌ Borrower is likely to default on the loan!")
    st.write(f"**Confidence Score**: {confidence_score:.2%}")

    st.write("### Current Borrower Details")
    st.json(form_data)

# Main section for modifying inputs
st.title("Modify Borrower Details")
updated_form_data = {}


updated_form_data["purpose"] = st.selectbox(
    "Purpose of Loan",
    options=["credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", "all_other"],
    index=["credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", "all_other"].index(
        form_data["purpose"]
    ),
)

updated_form_data["int.rate"] = st.number_input(
    "Interest Rate (as proportion)", value=form_data["int.rate"], min_value=0.0, max_value=1.0, step=0.01
)

updated_form_data["installment"] = st.number_input(
    "Monthly Installment ($)", value=form_data["installment"], min_value=0.0, step=0.01
)

updated_form_data["log.annual.inc"] = st.number_input(
    "Log of Annual Income", value=form_data["log.annual.inc"], min_value=0.0, step=0.01
)

updated_form_data["dti"] = st.number_input(
    "Debt-to-Income Ratio", value=form_data["dti"], min_value=0.0, step=0.01
)

updated_form_data["fico"] = st.slider(
    "FICO Score", value=form_data["fico"], min_value=300, max_value=850, step=1
)

updated_form_data["days.with.cr.line"] = st.number_input(
    "Credit Line Age (in days)", value=form_data["days.with.cr.line"], min_value=0.0, step=1.0
)

updated_form_data["revol.bal"] = st.number_input(
    "Revolving Balance ($)", value=form_data["revol.bal"], min_value=0.0, step=1.0
)

updated_form_data["revol.util"] = st.number_input(
    "Revolving Line Utilization Rate (%)", value=form_data["revol.util"], min_value=0.0, max_value=100.0, step=0.1
)

updated_form_data["inq.last.6mths"] = st.number_input(
    "Inquiries in Last 6 Months", value=form_data["inq.last.6mths"], min_value=0, step=1
)

updated_form_data["delinq.2yrs"] = st.number_input(
    "Delinquencies in Last 2 Years", value=form_data["delinq.2yrs"], min_value=0, step=1
)

updated_form_data["pub.rec"] = st.number_input(
    "Public Derogatory Records", value=form_data["pub.rec"], min_value=0, step=1
)

# Add back the model value for predictions
updated_form_data["Model"] = model_value

# Submit button to apply changes
if st.button("Submit Changes"):
    st.session_state.form_data = updated_form_data  # Update the session state directly