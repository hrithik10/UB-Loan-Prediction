import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    import os
    paths = ["UniversalBank_updated.xlsx", "data/UniversalBank_updated.xlsx"]
    for p in paths:
        if os.path.exists(p):
            df = pd.read_excel(p)
            break
    else:
        # fallback synthetic data for deployment without file
        np.random.seed(42)
        n = 5000
        df = pd.DataFrame({
            'ID': range(1, n+1),
            'Age': np.random.randint(23, 67, n),
            'Experience': np.random.randint(0, 43, n),
            'Income': np.random.randint(8, 224, n),
            'ZIP Code': np.random.randint(90000, 99999, n),
            'Family': np.random.randint(1, 5, n),
            'CCAvg': np.round(np.random.exponential(1.5, n), 1),
            'Education': np.random.randint(1, 4, n),
            'Mortgage': np.random.randint(0, 635, n),
            'Personal Loan': np.random.binomial(1, 0.096, n),
            'Securities Account': np.random.binomial(1, 0.1, n),
            'CD Account': np.random.binomial(1, 0.06, n),
            'Online': np.random.binomial(1, 0.6, n),
            'CreditCard': np.random.binomial(1, 0.29, n),
        })

    df = df.drop(columns=['ZIP Code'], errors='ignore')
    df['Education_Label'] = df['Education'].map({1: 'Undergrad', 2: 'Graduate', 3: 'Advanced/Prof'})
    df['Loan_Label'] = df['Personal Loan'].map({0: 'No Loan', 1: 'Accepted Loan'})
    df['Family_Label'] = df['Family'].map({1: 'Single (1)', 2: 'Couple (2)', 3: 'Family (3)', 4: 'Large (4)'})
    df['Income_Bin'] = pd.cut(df['Income'], bins=[0,30,60,100,150,300], labels=['<30k','30-60k','60-100k','100-150k','150k+'])
    df['CCAvg_Bin'] = pd.cut(df['CCAvg'], bins=[-0.1,1,3,6,20], labels=['Low(<1k)','Mid(1-3k)','High(3-6k)','VHigh(6k+)'])
    df['Age_Group'] = pd.cut(df['Age'], bins=[20,30,40,50,60,70], labels=['20s','30s','40s','50s','60s'])
    return df

FEATURE_COLS = ['Age', 'Experience', 'Income', 'Family', 'CCAvg', 'Education',
                'Mortgage', 'Securities Account', 'CD Account', 'Online', 'CreditCard']
TARGET_COL = 'Personal Loan'

COLORS = {
    'primary': '#2563eb',
    'success': '#16a34a',
    'warning': '#d97706',
    'danger': '#dc2626',
    'purple': '#7c3aed',
    'loan_yes': '#2563eb',
    'loan_no': '#e2e8f0',
    'palette': ['#2563eb','#16a34a','#d97706','#dc2626','#7c3aed','#0891b2','#be185d']
}
