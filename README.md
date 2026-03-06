# 🏦 UniversalBank Loan Analytics Dashboard

An AI-powered Streamlit dashboard for analyzing customer loan acceptance patterns at UniversalBank.

## 🚀 Live Demo
Deploy instantly on [Streamlit Cloud](https://streamlit.io/cloud)

## 📊 Features
- **Descriptive Analysis**: Interactive drill-down donut charts, demographic profiling
- **Diagnostic Analysis**: Correlation heatmaps, feature importance, decision tree insights
- **Predictive Analysis**: 4 ML models (Logistic Regression, Decision Tree, Random Forest, Gradient Boosting) with ROC curves, confusion matrices, and a **live loan predictor**
- **Prescriptive Analysis**: Budget optimizer, targeting rule builder, tiered campaign segments
- **Segmentation**: K-Means clustering, association rule mining, uplift modeling with cumulative gain charts

## 🛠️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/universalbank-dashboard.git
cd universalbank-dashboard
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Data
Place `UniversalBank_updated.xlsx` in the root directory.  
The app falls back to synthetic data if the file is not found (for demo purposes).

## 🌐 Deploy on Streamlit Cloud
1. Fork this repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub and select this repo
4. Set main file path: `app.py`
5. Click **Deploy!**

> **Note**: For the live deployment, either include the Excel file in the repo or the app will use synthetic data.

## 📦 Tech Stack
- `streamlit` — Dashboard framework
- `plotly` — Interactive visualizations
- `scikit-learn` — ML models
- `pandas` / `numpy` — Data processing
- `scipy` — Statistical tests

## 🎯 Key Insights
- Only **9.6%** of customers accept personal loans
- **CD Account holders** have 5x higher acceptance rates
- **Income > $80K** + **Graduate education** = highest conversion tier
- Top 20% of customers (by uplift score) capture ~50% of potential loans
