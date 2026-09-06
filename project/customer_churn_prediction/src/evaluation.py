from pathlib import Path

import joblib

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

import streamlit as st
import plotly.express as px


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

PREPROCESSOR_PATH = (
    BASE_DIR
    / "models"
    / "preprocessor.pkl"
)

FEATURE_SELECTOR_PATH = (
    BASE_DIR
    / "models"
    / "feature_selector.pkl"
)


# ---------------------------------------------------------
# Load preprocessing objects
# ---------------------------------------------------------

def load_preprocessor():

    return joblib.load(
        PREPROCESSOR_PATH
    )


def load_feature_selector():

    return joblib.load(
        FEATURE_SELECTOR_PATH
    )


# ---------------------------------------------------------
# Evaluate model
# ---------------------------------------------------------

def evaluate_model(
    model,
    df,
    preprocessor,
    feature_indices
):

    X = df.drop(
        columns=["churn_flag"]
    )

    y = df["churn_flag"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # --------------------------------------------------------
    # PREPROCESS
    # --------------------------------------------------------

    X_test_processed = preprocessor.transform(
        X_test
    )

    # --------------------------------------------------------
    # APPLY BEST FEATURE SELECTION
    # --------------------------------------------------------

    X_test_selected = X_test_processed[
        :,
        feature_indices
    ]

    # --------------------------------------------------------
    # PREDICT
    # --------------------------------------------------------

    y_pred = model.predict(
        X_test_selected
    )

    y_probability = model.predict_proba(
        X_test_selected
    )[:, 1]

    metrics = {
        "precision": precision_score(
            y_test,
            y_pred
        ),

        "recall": recall_score(
            y_test,
            y_pred
        ),

        "f1": f1_score(
            y_test,
            y_pred
        ),

        "roc_auc": roc_auc_score(
            y_test,
            y_probability
        )
    }

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    return metrics, cm

# ---------------------------------------------------------
# Streamlit evaluation page
# ---------------------------------------------------------

def show_evaluation(
    model,
    df,
    preprocessor,
    feature_indices
):

    st.header("🤖 Model Performance")

    st.write(
        "Performance of the XGBoost model "
        "on the test dataset."
    )

    metrics, cm = evaluate_model(
        model,
        df,
        preprocessor,
        feature_indices
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Precision",
        f"{metrics['precision']:.2%}"
    )

    col2.metric(
        "Recall",
        f"{metrics['recall']:.2%}"
    )

    col3.metric(
        "F1 Score",
        f"{metrics['f1']:.2%}"
    )

    col4.metric(
        "ROC-AUC",
        f"{metrics['roc_auc']:.2%}"
    )

    st.divider()

    st.subheader("Confusion Matrix")

    fig_cm = px.imshow(
        cm,
        text_auto=True,
        color_continuous_scale="Blues",
        labels={
            "x": "Predicted",
            "y": "Actual",
            "color": "Customers"
        },
        x=["No Churn", "Churn"],
        y=["No Churn", "Churn"]
    )

    st.plotly_chart(
        fig_cm,
        use_container_width=True
    )
