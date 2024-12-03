# Import libraries
import streamlit as st
import pandas as pd
import pickle
import warnings
import numpy as np
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title = "Loan Predictor",
    page_icon = "💰",
)   

# Centered Title using HTML and Markdown
st.markdown(
    """
    <h2 style = "text-align: center; color: #023020;"> Loan Predictor based on Lending Club Dataset</h2>
    """,
    unsafe_allow_html = True,
)

# Subtitle with styling
st.markdown(
    """
    <h3 style = "text-align: center; color: #808080; font-family: Arial, sans-serif;">
    Predict whether a borrower will pay back their loan based on key features!
    </h3>
    """,
    unsafe_allow_html = True,
)


st.image('loan1.jpg')

# Sidebar navigation header
with st.sidebar:
    st.header("🔍 Navigate the App")
    st.write("Use the links above to explore:")
    st.markdown("""
    - **Complete the Form**: Input borrower details to predict loan repayment.
    - **Loan Insights**: Analyze patterns and trends in borrower repayment behaviors.
    - **Simulate Changes**: Explore how changing borrower features impacts repayment likelihood.
    - **Trends**: Discover insights into how features like credit score, debt-to-income ratio, and more influence loan repayment.
    
    """)

st.sidebar.info("Select a task above to proceed.")

# Interactive introduction with expander
with st.expander("**What can you do with this app?**"):
    st.write("""
    📝 **Complete the Form**: Input borrower details such as **credit score (FICO)**, **debt-to-income ratio (DTI)**, and loan purpose to get started.

    💵 **Receive Your Loan Repayment Prediction**: Instantly find out if the borrower is likely to repay their loan, with a confidence score provided for the prediction.

    🔄 **Simulate Changes**: Experiment with borrower attributes—like adjusting the **interest rate**, changing the **loan purpose**, or altering the **annual income**—and observe how these changes affect repayment likelihood in real time.

    📊 **Discover Trends**: Explore interactive visualizations to see how factors like **loan amount**, **credit history**, and **inquiries in the last 6 months** correlate with loan repayment.

    ✨ **Interactive Insights**: All graphs and charts are fully interactive, letting you zoom in, filter data, and uncover patterns that matter most to you!
    """)
