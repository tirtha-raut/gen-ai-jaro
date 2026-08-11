import streamlit as st
import pandas as pd


def show_prediction(model):

    st.header("🔮 Customer Churn Prediction")

    st.write(
        "Enter customer information to estimate "
        "the probability of churn."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📊 Customer Details")

        customer_age = st.number_input(
            "Customer Age",
            min_value=18,
            max_value=100,
            value=35
        )

        customer_tenure_months = st.number_input(
            "Customer Tenure (months)",
            min_value=0,
            max_value=120,
            value=24
        )

        monthly_bill_amount = st.number_input(
            "Monthly Bill Amount",
            min_value=0.0,
            value=50.0
        )

        monthly_revenue = st.number_input(
            "Monthly Revenue",
            min_value=0.0,
            value=50.0
        )

        customer_lifetime_value = st.number_input(
            "Customer Lifetime Value",
            min_value=0.0,
            value=1200.0
        )

        billing_disputes_last_12m = st.number_input(
            "Billing Disputes (Last 12 Months)",
            min_value=0,
            value=0
        )

        number_of_services = st.number_input(
            "Number of Services",
            min_value=1,
            value=2
        )

        retention_offer_count = st.number_input(
            "Retention Offers Received",
            min_value=0,
            value=0
        )

    with col2:

        st.subheader("🏷️ Customer Information")

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        city = st.selectbox(
            "City",
            [
                "Pune",
                "Hyderabad",
                "Delhi",
                "Chennai",
                "Kolkata",
                "Mumbai",
                "Bangalore"
            ]
        )

        customer_segment = st.selectbox(
            "Customer Segment",
            [
                "Family",
                "Consumer",
                "Premium",
                "Business"
            ]
        )

        plan_type = st.selectbox(
            "Plan Type",
            [
                "Enterprise",
                "Prepaid",
                "Postpaid",
                "Unlimited",
                "postpaid",
                "POSTPAID"
            ]
        )

        contract_type = st.selectbox(
            "Contract Type",
            [
                "Month-to-Month",
                "2 Year",
                "1 Year"
            ]
        )

        service_region_cluster = st.selectbox(
            "Service Region Cluster",
            list(range(1, 50))
        )

    st.divider()

    if st.button(
        "🔮 Predict Churn",
        type="primary",
        use_container_width=True
    ):

        input_data = pd.DataFrame({
            "customer_age": [customer_age],
            "customer_tenure_months": [
                customer_tenure_months
            ],
            "monthly_bill_amount": [
                monthly_bill_amount
            ],
            "monthly_revenue": [
                monthly_revenue
            ],
            "customer_lifetime_value": [
                customer_lifetime_value
            ],
            "billing_disputes_last_12m": [
                billing_disputes_last_12m
            ],
            "number_of_services": [
                number_of_services
            ],
            "retention_offer_count": [
                retention_offer_count
            ],
            "gender": [gender],
            "city": [city],
            "customer_segment": [
                customer_segment
            ],
            "plan_type": [plan_type],
            "contract_type": [
                contract_type
            ],
            "service_region_cluster": [
                service_region_cluster
            ]
        })

        prediction = model.predict(
            input_data
        )[0]

        probability = model.predict_proba(
            input_data
        )[0][1]

        st.subheader("Prediction Result")

        result_col1, result_col2 = st.columns(2)

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