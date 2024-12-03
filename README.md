# Credit Risk Assessment and What-If Analysis

Welcome to the **Credit Risk Assessment and What-If Analysis** project! This application uses machine learning to predict loan repayment probabilities and provides users with interactive tools to analyze and simulate changes in borrower details. The project is designed to offer a seamless experience for both data exploration and prediction tasks.

---

## Features

### **1. Loan Repayment Prediction**
- **What It Does**:
  - Predicts the likelihood of loan repayment using multiple machine learning models.
  - Includes models such as Decision Tree, Random Forest, ADA Boost, XGBoost, and a Soft Voting Ensemble for improved accuracy.
- **How It Works**:
  - Users fill out a form with borrower and loan details.
  - The model generates a prediction (repayment or default) along with a confidence score.

### **2. What-If Analysis**
- **What It Does**:
  - Allows users to modify borrower and loan details and see real-time changes in the model's predictions.
- **How It Works**:
  - A simple interface with sliders and input fields pre-filled with the user's data.
  - Predictive results update dynamically based on the changes, enabling interactive simulations.

### **3. Machine Learning Charts and Statistics**
- **What It Does**:
  - Visualizes performance metrics and feature importances for all included ML models.
  - Helps users and developers understand model behavior and decision-making.
- **Includes**:
  - Confusion Matrices
  - Feature Importances
  - Classification Reports
  - Tree Structure Visualization (for Decision Tree model)

---

## Project Structure

The application is divided into the following pages:

1. **Form Input Page**:
   - Users provide borrower and loan information through an intuitive form.
   - Selected model details and configurations are also specified here.

2. **Prediction Page**:
   - Displays the prediction results (repayment or default) with confidence scores.
   - Simple and focused output for quick insights.

3. **What-If Analysis Page**:
   - Enables interactive modification of input features to explore how changes affect the prediction.
   - Real-time feedback on predictions for actionable insights.

4. **ML Charts and Statistics Page**:
   - Provides in-depth model performance metrics and visualizations.
   - Includes charts for Confusion Matrix, Feature Importances, and Classification Reports.

---

## How to Use

### **1. Clone the Repository**
```bash
git clone https://github.com/namireh/FinalProj.git
cd FinalProj