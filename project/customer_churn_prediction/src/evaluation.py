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

def evaluate_model(model, df):

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

    y_pred = model.predict(X_test)

    y_probability = model.predict_proba(
        X_test
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

def show_evaluation(model, df):

    st.header("🤖 Model Performance")

    st.write(
        "Performance of the Logistic Regression model "
        "on the test dataset."
    )

    metrics, cm = evaluate_model(
        model,
        df
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