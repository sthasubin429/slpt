import pandas as pd
import joblib
import os

current_path = os.path.abspath(os.getcwd())

# Find the index of 'slpt' in the path and keep everything up to and including 'slpt'
if "slpt" in current_path:
    base_path = current_path[: current_path.index("slpt") + len("slpt")]
else:
    base_path = current_path

# print(base_path) # ensure slpt is the last part of the path


def get_path(*args):
    """
    Returns the absolute path to a file or directory relative to the base path.
    """
    return os.path.join(base_path, *args)


def load_processed_data():
    # Adjust the path as needed
    return pd.read_csv(get_path("data/raw/cell2cellholdout.csv"))


def load_model():
    # Adjust the path as needed
    return joblib.load(get_path("models/logistic_regression_model.joblib"))


def predict_churn(model, input_df):
    return model.predict(input_df)
