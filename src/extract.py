import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)


def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file
    """
    logging.info(f"Starting data extraction from {file_path}...")

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(path)
    logging.info(f"Loaded data with shape: {df.shape}")

    return df
