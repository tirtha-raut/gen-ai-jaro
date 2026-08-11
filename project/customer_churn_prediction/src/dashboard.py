import streamlit as st
import plotly.express as px


def show_dashboard(df):

    st.header("📈 Customer Overview")

    # -------------------------
    # KPIs
    # -------------------------

    total_customers = len(df)

    churned_customers = df["churn_flag"].sum()

    churn_rate = (
        churned_customers / total_customers
    )

    average_revenue = df["monthly_revenue"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Customers",
        f"{total_customers:,}"
    )

    col2.metric(
        "Churned Customers",
        f"{churned_customers:,}"
    )

    col3.metric(
        "Churn Rate",
        f"{churn_rate:.1%}"
    )

    col4.metric(
        "Avg Monthly Revenue",
        f"{average_revenue:.2f}"
    )

    st.divider()

    # -------------------------
    # Churn Distribution
    # -------------------------

    st.subheader("🍩 Customer Churn Distribution")

    fig = px.pie(
        df,
        names="churn_flag",
        title="Customer Churn Distribution",
        hole=0.4
    )

    fig.update_traces(
        textinfo="percent+label"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -------------------------
    # Contract
    # -------------------------

    st.subheader("📄 Churn Rate by Contract Type")

    contract_churn = (
        df.groupby("contract_type")["churn_flag"]
        .mean()
        .reset_index()
    )

    contract_churn["churn_flag"] *= 100

    fig_contract = px.bar(
        contract_churn,
        x="contract_type",
        y="churn_flag",
        color="contract_type",
        labels={
            "contract_type": "Contract Type",
            "churn_flag": "Churn Rate (%)"
        }
    )

    st.plotly_chart(
        fig_contract,
        use_container_width=True
    )

    # -------------------------
    # Segment + Plan
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("👥 Churn by Customer Segment")

        segment_churn = (
            df.groupby("customer_segment")["churn_flag"]
            .mean()
            .reset_index()
        )

        segment_churn["churn_flag"] *= 100

        fig_segment = px.bar(
            segment_churn,
            x="customer_segment",
            y="churn_flag",
            color="customer_segment",
            labels={
                "customer_segment": "Customer Segment",
                "churn_flag": "Churn Rate (%)"
            }
        )

        st.plotly_chart(
            fig_segment,
            use_container_width=True
        )

    with col2:

        st.subheader("📱 Churn by Plan Type")

        plan_churn = (
            df.groupby("plan_type")["churn_flag"]
            .mean()
            .reset_index()
        )

        plan_churn["churn_flag"] *= 100

        fig_plan = px.bar(
            plan_churn,
            x="plan_type",
            y="churn_flag",
            color="plan_type",
            labels={
                "plan_type": "Plan Type",
                "churn_flag": "Churn Rate (%)"
            }
        )

        st.plotly_chart(
            fig_plan,
            use_container_width=True
        )

    # -------------------------
    # City
    # -------------------------

    st.subheader("🏙️ Churn Rate by City")

    city_churn = (
        df.groupby("city")["churn_flag"]
        .mean()
        .reset_index()
    )

    city_churn["churn_flag"] *= 100

    fig_city = px.bar(
        city_churn,
        x="city",
        y="churn_flag",
        color="city",
        labels={
            "city": "City",
            "churn_flag": "Churn Rate (%)"
        }
    )

    st.plotly_chart(
        fig_city,
        use_container_width=True
    )

    # -------------------------
    # Tenure
    # -------------------------

    st.subheader("📅 Churn by Customer Tenure")

    tenure_churn = (
        df.groupby("customer_tenure_months")["churn_flag"]
        .mean()
        .reset_index()
    )

    tenure_churn["churn_flag"] *= 100

    fig_tenure = px.line(
        tenure_churn,
        x="customer_tenure_months",
        y="churn_flag",
        markers=True,
        labels={
            "customer_tenure_months": "Tenure (Months)",
            "churn_flag": "Churn Rate (%)"
        }
    )

    st.plotly_chart(
        fig_tenure,
        use_container_width=True
    )