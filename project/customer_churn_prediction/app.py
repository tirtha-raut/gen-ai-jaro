import streamlit as st

from src.data import load_data
from src.model import (
    load_model,
    load_feature_indices,
    load_preprocessor
)
from src.dashboard import show_dashboard
from src.prediction import show_prediction
from src.evaluation import show_evaluation


# -------------------------
# Page configuration
# -------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# -------------------------
# Load resources
# -------------------------

df = load_data()

model = load_model()
feature_indices = load_feature_indices()
preprocessor = load_preprocessor()


# -------------------------
# Header
# -------------------------

st.title("📊 Customer Churn Prediction")

st.write(
    "Analyze customer churn patterns and "
    "predict customer churn risk."
)

st.divider()

# -------------------------
# Tabs
# -------------------------

tab1, tab2, tab3 = st.tabs([
    "📊 Dashboard",
    "🔮 Predict Churn",
    "🤖 Model Performance"
])

with tab1:
    show_dashboard(df)

with tab2:
    show_prediction(
        model,
        preprocessor,
        feature_indices
    )

with tab3:
    show_evaluation(
        model,
        df,
        preprocessor,
        feature_indices
    )