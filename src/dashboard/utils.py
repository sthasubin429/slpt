import pandas as pd
import joblib
import os

current_path = os.path.abspath(os.getcwd())

# Set base path to project folder (where 'slpt' is assumed to be)
if "slpt" in current_path:
    base_path = current_path[: current_path.index("slpt") + len("slpt")]
else:
    base_path = current_path

def get_path(*args):
    """Returns the absolute path to a file or directory relative to the base path."""
    return os.path.join(base_path, *args)


def load_processed_data():
    """Loads the processed telecom churn dataset."""
    return pd.read_csv(get_path("data/raw/cell2celltrain.csv"))


def load_model():
    """Loads the trained churn prediction model."""
    return joblib.load(get_path("models/logistic_regression_model.joblib"))


def predict_churn(model, input_df):
    """Predicts churn for input data."""
    return model.predict(input_df)
