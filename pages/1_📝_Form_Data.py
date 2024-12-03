import streamlit as st
import pandas as pd

st.set_page_config(page_title="Credit Risk Assessment", page_icon="💳")


if "form_data" not in st.session_state:
    st.session_state.form_data = {}

if "mode" not in st.session_state:
    st.session_state.mode = None

# Centered Title using HTML and Markdown
st.markdown(
    """
    <h2 style="text-align: center; color: #0000FF;">Credit Risk Assessment Form</h2>
    """,
    unsafe_allow_html=True,
)

# Subtitle with styling
st.markdown(
    """
    <h3 style="text-align: center; color: #808080; font-family: Arial, sans-serif;">
    Fill out the form below and push the submit button to assess credit risk.
    </h3>
    """,
    unsafe_allow_html=True,
)

# Sidebar information
with st.sidebar:
    st.header("📋 Form Page Instructions")
    st.write("""
    On this page, you can:
    1. **Fill out the form** to input borrower details and loan characteristics.
    2. **Information requested in the form** includes:
    """)
    st.markdown("""
    - **'credit.policy'**: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.
    - **'purpose'**: The purpose of the loan (e.g., "credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", "all_other").
    - **'int.rate'**: The interest rate of the loan as a proportion (e.g., 11% is stored as 0.11). Higher rates indicate higher risk.
    - **'installment'**: The monthly installments owed by the borrower if the loan is funded.
    - **'log.annual.inc'**: The natural log of the self-reported annual income of the borrower.
    - **'dti'**: The debt-to-income ratio (total debt divided by annual income).
    - **'fico'**: The FICO credit score of the borrower (ranges from 300 to 850).
    - **'days.with.cr.line'**: The number of days the borrower has had a credit line.
    - **'revol.bal'**: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).
    - **'revol.util'**: The borrower's revolving line utilization rate (credit used relative to total credit available).
    - **'inq.last.6mths'**: The number of inquiries by creditors in the last 6 months.
    - **'delinq.2yrs'**: The number of times the borrower was 30+ days past due on a payment in the last 2 years.
    - **'pub.rec'**: The number of derogatory public records (e.g., bankruptcy filings, tax liens, or judgments).
    """)
    st.write("""
    3. **Submit the form** to view a success message and move on to the next page.
    """)

# Manual entry option
st.title("Borrower Details Manual Entry")

# Start form
with st.form("credit_data_form"):
    st.write("Please fill out the form below:")
    
    # Form fields
    credit_policy = st.selectbox("Credit Policy", options=["Yes", "No"], help="If the customer meets the underwriting credit criteria of LendingClub.com")
    purpose = st.selectbox(
        "Purpose of Loan", 
        options=["credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", "all_other"]
    )
    int_rate = st.number_input("Interest Rate (as proportion)", min_value=0.0, max_value=1.0, step=0.01)
    installment = st.number_input("Monthly Installment ($)", min_value=0.0, step=0.01)
    log_annual_inc = st.number_input("Log of Annual Income", min_value=0.0, step=0.01)
    dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, step=0.01)
    fico = st.slider("FICO Score", min_value=300, max_value=850, step=1)
    days_with_cr_line = st.number_input("Credit Line Age (in days)", min_value=0.0, step=1.0)
    revol_bal = st.number_input("Revolving Balance ($)", min_value=0.0, step=1.0)
    revol_util = st.number_input("Revolving Line Utilization Rate (%)", min_value=0.0, max_value=100.0, step=0.1)
    inq_last_6mths = st.number_input("Inquiries in Last 6 Months", min_value=0, step=1)
    delinq_2yrs = st.number_input("Delinquencies in Last 2 Years", min_value=0, step=1)
    pub_rec = st.number_input("Public Derogatory Records", min_value=0, step=1)
    ML_model = st.selectbox("Choose an ML model to run the data through", options = ["Decision Tree", "Random Forest", "ADA Boost", "XGBoost","Soft Voting (Recomended)"])
    
    # Submit button
    submit_button = st.form_submit_button("Submit")

    
# Process the form data on submission
if submit_button:
    st.balloons()  # Fun animation for feedback!
    st.success("🎉 Form Submitted Successfully!")
    
    # Encouragement message
    st.markdown("""
    <h5 style='text-align: center; color: #013220;'>
    Thank you! Your data has been submitted. Navigate to other pages for further analysis.
    </h5>
    """, unsafe_allow_html=True)


    st.session_state.form_data = {
        "credit.policy": 1 if credit_policy == "Yes" else 0,
        "purpose": purpose,
        "int.rate": int_rate,
        "installment": installment,
        "log.annual.inc": log_annual_inc,
        "dti": dti,
        "fico": fico,
        "days.with.cr.line": days_with_cr_line,
        "revol.bal": revol_bal,
        "revol.util": revol_util,
        "inq.last.6mths": inq_last_6mths,
        "delinq.2yrs": delinq_2yrs,
        "pub.rec": pub_rec,
        "Model": ML_model
    }