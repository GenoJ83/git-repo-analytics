from src.engine.churn import compute_file_churn
def test_churn():
    assert compute_file_churn(100, 40) == 140
