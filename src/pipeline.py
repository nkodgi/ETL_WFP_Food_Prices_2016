import logging
import argparse

from extract import extract_data
from transform import transform_data
from load import load_data

logging.basicConfig(level=logging.INFO)


def run_pipeline(input_path: str):
    logging.info("Starting ETL pipeline...")

    df_raw = extract_data(input_path)
    df_clean = transform_data(df_raw)
    load_data(df_clean)

    logging.info("Pipeline finished successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        type=str,
        default="data/raw/wfp_food_prices_global_2016.csv",
        help="Path to input CSV"
    )

    args = parser.parse_args()

    run_pipeline(args.input)
