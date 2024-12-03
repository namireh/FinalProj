import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="Interactive Loan Data Visualizations", page_icon="📊")

@st.cache_data
def load_data():
    return pd.read_csv("loan_data.csv")

df = load_data()

# Set up the page
st.title("Interactive Loan Data Visualizations")
st.write("Filter and explore trends from the LendingClub loan dataset.")

# Filters Section
st.sidebar.header("Filters")

# Filter 1: Loan Purpose

# Chat GPT helped in the creation of this filter
selected_purpose = st.sidebar.multiselect(
    "Select Loan Purpose(s):",
    options=df["purpose"].unique(),
    default=df["purpose"].unique()
)

# Filter 2: Credit Policy
credit_policy_filter = st.sidebar.selectbox(
    "Filter by Credit Policy:",
    options=["All", "Meets Policy", "Does Not Meet Policy"]
)

# Filter 3: FICO Range
fico_range = st.sidebar.slider(
    "Select FICO Range:",
    min_value=int(df["fico"].min()),
    max_value=int(df["fico"].max()),
    value=(int(df["fico"].min()), int(df["fico"].max()))
)

# Apply Filters to the Data
filtered_df = df[
    (df["purpose"].isin(selected_purpose)) &
    ((df["credit.policy"] == 1) if credit_policy_filter == "Meets Policy" else True) &
    ((df["credit.policy"] == 0) if credit_policy_filter == "Does Not Meet Policy" else True) &
    (df["fico"] >= fico_range[0]) &
    (df["fico"] <= fico_range[1])
]

# Display Filtered Dataframe
st.subheader("Filtered Data")
st.write(filtered_df)

# Visualization Section
st.subheader("Visualizations Based on Filters")

# Plot 1: Average Interest Rate by Loan Purpose
st.subheader("1. Average Interest Rate by Loan Purpose")
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.barplot(data=filtered_df, x="purpose", y="int.rate", ci=None, ax=ax1)
ax1.set_title("Average Interest Rate by Loan Purpose")
ax1.set_xlabel("Loan Purpose")
ax1.set_ylabel("Interest Rate")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Plot 2: FICO Score vs. Interest Rate
st.subheader("2. FICO Score vs. Interest Rate")
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=filtered_df, x="fico", y="int.rate", hue="purpose", ax=ax2, palette="viridis")
ax2.set_title("FICO Score vs. Interest Rate")
ax2.set_xlabel("FICO Score")
ax2.set_ylabel("Interest Rate")
plt.legend(title="Purpose", bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig2)

# Plot 3: Debt-to-Income Ratio vs. Annual Income
st.subheader("3. Debt-to-Income Ratio vs. Annual Income")
fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=filtered_df, x="log.annual.inc", y="dti", hue="credit.policy", ax=ax3, palette="coolwarm")
ax3.set_title("Debt-to-Income Ratio vs. Annual Income")
ax3.set_xlabel("Log Annual Income")
ax3.set_ylabel("Debt-to-Income Ratio")
plt.legend(title="Credit Policy", loc="upper right")
st.pyplot(fig3)

# Plot 4: Loan Purpose Distribution
st.subheader("4. Loan Purpose Distribution")
fig4, ax4 = plt.subplots(figsize=(8, 6))
filtered_df["purpose"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set3"), ax=ax4)
ax4.set_title("Loan Purpose Distribution")
ax4.set_ylabel("")  # Remove y-label for pie chart
st.pyplot(fig4)

# Plot 5: Revolving Balance vs. Revolving Utilization Rate
st.subheader("5. Revolving Balance vs. Revolving Utilization Rate")
fig5, ax5 = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=filtered_df, x="revol.bal", y="revol.util", hue="credit.policy", ax=ax5, palette="viridis")
ax5.set_title("Revolving Balance vs. Revolving Utilization Rate")
ax5.set_xlabel("Revolving Balance ($)")
ax5.set_ylabel("Revolving Utilization Rate (%)")
plt.legend(title="Credit Policy", loc="upper right")
st.pyplot(fig5)
