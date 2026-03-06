import streamlit as st

st.set_page_config(
    page_title="UniversalBank Loan Analytics",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main-header {
    background: linear-gradient(135deg, #1a3a5c 0%, #2563eb 100%);
    padding: 2.5rem 2rem; border-radius: 16px; margin-bottom: 2rem;
    text-align: center; box-shadow: 0 8px 32px rgba(37,99,235,0.3);
}
.main-header h1 { color: white; font-size: 2.8rem; margin: 0; font-weight: 800; }
.main-header p { color: #bfdbfe; font-size: 1.1rem; margin-top: 0.5rem; }
.metric-card {
    background: white; border-radius: 12px; padding: 1.5rem;
    border-left: 5px solid #2563eb; box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🏦 UniversalBank Loan Analytics</h1>
    <p>AI-Powered Customer Intelligence & Loan Acceptance Prediction Dashboard</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Customers", "5,000")
with col2:
    st.metric("Loan Acceptances", "480 (9.6%)")
with col3:
    st.metric("Avg Annual Income", "$74K")
with col4:
    st.metric("AI Models Built", "4 Models")

st.markdown("---")
st.markdown("## 📊 Navigate via the Sidebar")
st.info("👈 Use the sidebar to explore: **Descriptive → Diagnostic → Predictive → Prescriptive → Segmentation**")

st.markdown("""
| Module | Description |
|--------|-------------|
| 📈 **1_Descriptive** | Demographics, income distributions, drill-down donut charts |
| 🔍 **2_Diagnostic** | Correlation heatmaps, feature importance, decision tree viz |
| 🤖 **3_Predictive** | 4 ML models, ROC curves, confusion matrices, live predictor |
| 🎯 **4_Prescriptive** | Campaign targeting strategies & budget ROI optimizer |
| 🧩 **5_Segmentation** | K-Means clustering, association rules, uplift modeling |
""")
