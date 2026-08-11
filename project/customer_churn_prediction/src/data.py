from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "customer_churn_cleaned.csv"
)


def load_data():
    return pd.read_csv(DATA_PATH)