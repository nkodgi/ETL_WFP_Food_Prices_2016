import pandas as pd
import logging
from pathlib import Path
import sqlite3

logging.basicConfig(level=logging.INFO)


def save_to_csv(df: pd.DataFrame, output_path: str):
    logging.info(f"Saving CSV to {output_path}...")

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)


def save_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str):
    logging.info(f"Saving to SQLite: {db_path}...")

    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


def load_data(
    df: pd.DataFrame,
    csv_path: str = "data/processed/wfp_2016_clean.csv",
    db_path: str = "data/database.db",
    table_name: str = "food_prices_2016"
):
    logging.info("Starting load step...")

    save_to_csv(df, csv_path)
    save_to_sqlite(df, db_path, table_name)

    logging.info("Load complete!")
