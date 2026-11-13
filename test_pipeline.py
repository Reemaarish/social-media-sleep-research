"""Synthetic-data test; does not use or reveal the real survey responses."""
import pandas as pd
from analysis import clean_primary_data, run_spearman

def test_cleaning_and_spearman_pipeline():
    synthetic = pd.DataFrame({
        "night_social_media_hours": [1, 2, 3, 4, None, "not recorded"],
        "sleep_hours": [8, 7.5, 7, 6.5, 8, 7],
    })
    cleaned = clean_primary_data(
        synthetic, "night_social_media_hours", "sleep_hours"
    )
    assert len(cleaned) == 4
    result = run_spearman(
        synthetic, "night_social_media_hours", "sleep_hours"
    )
    assert result["n"] == 4
    assert result["spearman_rho"] < 0
    assert 0 <= result["p_value"] <= 1
