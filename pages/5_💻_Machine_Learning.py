import streamlit as st
import pandas as pd

# Set up the Streamlit app layout
st.title("Machine Learning Model Performance Visuals")

# Create tabs for each model
ada_tab, dt_tab, rf_tab, xgb_tab, sv_tab = st.tabs([
    "ADA Boost",
    "Decision Tree",
    "Random Forest",
    "XG Boost",
    "Soft Voting"
])

# ADA Boost visuals
with ada_tab:
    st.subheader("ADA Boost Performance")
    tab1, tab2, tab3 = st.tabs([
        "Confusion Matrix",
        "Feature Importance",
        "Classification Report"
    ])

    with tab1:
        st.image("ADA_CM.svg", use_column_width=True)
        st.caption("Confusion Matrix for ADA Boost model.")
    with tab2:
        st.image("ADA_imp.svg", use_column_width=True)
        st.caption("Feature Importance for ADA Boost model.")
    with tab3:
        st.write("### Classification Report")
        ada_cr = pd.read_csv("ADA_CR.csv")
        st.dataframe(ada_cr)
        st.caption("Classification report for ADA Boost model.")

# Decision Tree visuals
with dt_tab:
    st.subheader("Decision Tree Performance")
    tab1, tab2, tab3, tab4 = st.tabs([
        "Confusion Matrix",
        "Feature Importance",
        "Tree Visualization",
        "Classification Report"
    ])

    with tab1:
        st.image("DT_CM.svg", use_column_width=True)
        st.caption("Confusion Matrix for Decision Tree model.")
    with tab2:
        st.image("DT_imp.svg", use_column_width=True)
        st.caption("Feature Importance for Decision Tree model.")
    with tab3:
        st.image("DT_vis.svg", use_column_width=True)
        st.caption("Visualization of the Decision Tree structure.")
    with tab4:
        st.write("### Classification Report")
        dt_cr = pd.read_csv("DT_CR.csv")
        st.dataframe(dt_cr)
        st.caption("Classification report for Decision Tree model.")

# Random Forest visuals
with rf_tab:
    st.subheader("Random Forest Performance")
    tab1, tab2, tab3 = st.tabs([
        "Confusion Matrix",
        "Feature Importance",
        "Classification Report"
    ])

    with tab1:
        st.image("RF_CM.svg", use_column_width=True)
        st.caption("Confusion Matrix for Random Forest model.")
    with tab2:
        st.image("RF_imp.svg", use_column_width=True)
        st.caption("Feature Importance for Random Forest model.")
    with tab3:
        st.write("### Classification Report")
        rf_cr = pd.read_csv("RF_CR.csv")
        st.dataframe(rf_cr)
        st.caption("Classification report for Random Forest model.")

# XG Boost visuals
with xgb_tab:
    st.subheader("XG Boost Performance")
    tab1, tab2, tab3 = st.tabs([
        "Confusion Matrix",
        "Feature Importance",
        "Classification Report"
    ])

    with tab1:
        st.image("XGB_CM.svg", use_column_width=True)
        st.caption("Confusion Matrix for XG Boost model.")
    with tab2:
        st.image("XGB_imp.svg", use_column_width=True)
        st.caption("Feature Importance for XG Boost model.")
    with tab3:
        st.write("### Classification Report")
        xgb_cr = pd.read_csv("XGB_CR.csv")
        st.dataframe(xgb_cr)
        st.caption("Classification report for XG Boost model.")

# Soft Voting visuals
with sv_tab:
    st.subheader("Soft Voting Performance")
    tab1, tab2, tab3 = st.tabs([
        "Confusion Matrix",
        "Feature Importance",
        "Classification Report"
    ])

    with tab1:
        st.image("SV_CM.svg", use_column_width=True)
        st.caption("Confusion Matrix for Soft Voting model.")
    with tab2:
        st.image("SV_imp.svg", use_column_width=True)
        st.caption("Feature Importance for Soft Voting model.")
    with tab3:
        st.write("### Classification Report")
        sv_cr = pd.read_csv("SV.csv")
        st.dataframe(sv_cr)
        st.caption("Classification report for Soft Voting model.")

# Add a footer
st.write("---")
st.markdown(
    "Explore detailed performance metrics and insights for each model above."
)