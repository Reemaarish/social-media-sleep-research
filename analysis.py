"""Small, reusable analysis functions for the sleep/social-media project."""
import pandas as pd
from scipy.stats import spearmanr

def clean_primary_data(data, predictor_column, outcome_column):
    """Return rows with numeric, finite values for the two primary variables."""
    frame = data[[predictor_column, outcome_column]].copy()
    frame[predictor_column] = pd.to_numeric(frame[predictor_column], errors="coerce")
    frame[outcome_column] = pd.to_numeric(frame[outcome_column], errors="coerce")
    frame = frame.dropna()
    return frame

def run_spearman(data, predictor_column, outcome_column):
    """Calculate Spearman correlation and return a simple results dictionary."""
    clean = clean_primary_data(data, predictor_column, outcome_column)
    if len(clean) < 3:
        raise ValueError("At least three complete observations are required.")
    rho, p_value = spearmanr(clean[predictor_column], clean[outcome_column])
    return {
        "n": int(len(clean)),
        "spearman_rho": float(rho),
        "p_value": float(p_value),
    }
