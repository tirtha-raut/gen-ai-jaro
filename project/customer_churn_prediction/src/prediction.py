import streamlit as st
import pandas as pd


# ============================================================
# GET ORIGINAL FEATURES USED BY SELECTED MODEL
# ============================================================

def get_selected_original_features(
    preprocessor,
    feature_indices
):

    processed_features = (
        preprocessor.get_feature_names_out()
    )

    selected_processed_features = (
        processed_features[feature_indices]
    )

    original_features = []

    numeric_features = list(
        preprocessor.transformers_[0][2]
    )

    categorical_features = list(
        preprocessor.transformers_[1][2]
    )

    for feature in selected_processed_features:

        # Remove transformer prefix
        #
        # num__customer_age
        #       ↓
        # customer_age
        #
        # cat__plan_type_Postpaid
        #       ↓
        # plan_type_Postpaid

        feature_without_prefix = feature.split(
            "__",
            1
        )[-1]

        # ----------------------------------------------------
        # Numeric feature
        # ----------------------------------------------------

        if feature_without_prefix in numeric_features:

            if feature_without_prefix not in original_features:

                original_features.append(
                    feature_without_prefix
                )

        # ----------------------------------------------------
        # Categorical feature
        # ----------------------------------------------------

        else:

            for column in categorical_features:

                if feature_without_prefix.startswith(
                    column + "_"
                ):

                    if column not in original_features:

                        original_features.append(
                            column
                        )

                    break

    return original_features


# ============================================================
# PREDICTION PAGE
# ============================================================

def show_prediction(
    model,
    preprocessor,
    feature_indices
):

    st.header(
        "🔮 Customer Churn Prediction"
    )

    st.write(
        "Enter customer information to estimate "
        "the probability of churn."
    )

    st.divider()

    # ========================================================
    # DETERMINE SELECTED FEATURES DYNAMICALLY
    # ========================================================

    selected_features = (
        get_selected_original_features(
            preprocessor,
            feature_indices
        )
    )

    processed_features = (
        preprocessor.get_feature_names_out()
    )

    selected_processed_features = (
        processed_features[feature_indices]
    )

    # ========================================================
    # DISPLAY SELECTED FEATURES
    # ========================================================

    st.subheader(
        "🎯 Features Used by the Model"
    )

    st.write(
        f"The selected model uses "
        f"**{len(feature_indices)} processed features** "
        f"from **{len(selected_features)} original input features**."
    )

    with st.expander(
        "View selected model features"
    ):

        for feature in selected_processed_features:

            st.write(
                f"• {feature}"
            )

    st.divider()

    # ========================================================
    # INPUT VALUES
    # ========================================================

    input_values = {}

    col1, col2 = st.columns(2)

    # ========================================================
    # CATEGORY OPTIONS
    # ========================================================

    category_options = {

        "gender": [
            "Male",
            "Female"
        ],

        "city": [
            "Pune",
            "Hyderabad",
            "Delhi",
            "Chennai",
            "Kolkata",
            "Mumbai",
            "Bangalore"
        ],

        "customer_segment": [
            "Family",
            "Consumer",
            "Premium",
            "Business"
        ],

        "plan_type": [
            "Enterprise",
            "Prepaid",
            "Postpaid",
            "Unlimited",
            "postpaid",
            "POSTPAID"
        ],

        "contract_type": [
            "Month-to-Month",
            "2 Year",
            "1 Year"
        ]
    }

    # ========================================================
    # CREATE INPUTS DYNAMICALLY
    # ========================================================

    for i, feature in enumerate(
        selected_features
    ):

        column = (
            col1
            if i % 2 == 0
            else col2
        )

        with column:

            label = (
                feature
                .replace(
                    "_",
                    " "
                )
                .title()
            )

            # ------------------------------------------------
            # Binary features
            # ------------------------------------------------

            if feature in [
                "international_usage_flag",
                "autopay_enabled"
            ]:

                input_values[feature] = (
                    st.selectbox(
                        label,
                        [0, 1],
                        key=f"input_{feature}"
                    )
                )

            # ------------------------------------------------
            # Categorical features
            # ------------------------------------------------

            elif feature in category_options:

                input_values[feature] = (
                    st.selectbox(
                        label,
                        category_options[feature],
                        key=f"input_{feature}"
                    )
                )

            # ------------------------------------------------
            # Numeric features
            # ------------------------------------------------

            else:

                input_values[feature] = (
                    st.number_input(
                        label,
                        min_value=0.0,
                        value=0.0,
                        key=f"input_{feature}"
                    )
                )

    st.divider()

    # ========================================================
    # PREDICT BUTTON
    # ========================================================

    if st.button(
        "🔮 Predict Churn",
        type="primary",
        use_container_width=True
    ):

        # ====================================================
        # GET ALL ORIGINAL FEATURES REQUIRED BY PREPROCESSOR
        # ====================================================

        numeric_features = list(
            preprocessor.transformers_[0][2]
        )

        categorical_features = list(
            preprocessor.transformers_[1][2]
        )

        all_features = (
            numeric_features
            +
            categorical_features
        )

        # ====================================================
        # BUILD COMPLETE INPUT
        # ====================================================

        complete_input = {}

        for feature in all_features:

            if feature in input_values:

                complete_input[feature] = [
                    input_values[feature]
                ]

            else:

                # Feature is not required by the
                # selected model, but the preprocessor
                # still expects it.

                complete_input[feature] = [0]

        input_data = pd.DataFrame(
            complete_input
        )

        # ====================================================
        # PREPROCESS
        # ====================================================

        input_processed = (
            preprocessor.transform(
                input_data
            )
        )

        # ====================================================
        # APPLY SELECTED FEATURES
        # ====================================================

        input_selected = (
            input_processed[
                :,
                feature_indices
            ]
        )

        # ====================================================
        # DEBUG INFORMATION
        # ====================================================

        print(
            "Processed input shape:",
            input_processed.shape
        )

        print(
            "Selected input shape:",
            input_selected.shape
        )

        # ====================================================
        # PREDICTION
        # ====================================================

        prediction = model.predict(
            input_selected
        )[0]

        probability = (
            model.predict_proba(
                input_selected
            )[0][1]
        )

        # ====================================================
        # DISPLAY RESULT
        # ====================================================

        st.subheader(
            "Prediction Result"
        )

        result_col1, result_col2 = (
            st.columns(2)
        )

        with result_col1:

            if prediction == 1:

                st.error(
                    "🔴 Customer is likely to churn"
                )

            else:

                st.success(
                    "🟢 Customer is unlikely to churn"
                )

        with result_col2:

            st.metric(
                "Churn Probability",
                f"{probability:.1%}"
            )

        st.progress(
            float(probability)
        )