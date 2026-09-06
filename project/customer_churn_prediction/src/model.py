from pathlib import Path
import joblib


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "best_churn_model.pkl"
)

FEATURE_INDICES_PATH = (
    BASE_DIR
    / "models"
    / "best_feature_indices.pkl"
)

PREPROCESSOR_PATH = (
    BASE_DIR
    / "models"
    / "preprocessor.pkl"
)


def load_model():
    return joblib.load(MODEL_PATH)


def load_feature_indices():
    return joblib.load(FEATURE_INDICES_PATH)


def load_preprocessor():
    return joblib.load(PREPROCESSOR_PATH)