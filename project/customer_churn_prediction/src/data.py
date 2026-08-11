import pandas as pd


DATA_PATH = "data/processed/customer_churn_cleaned.csv"


def load_data():
    return pd.read_csv(DATA_PATH)