import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Cleaning column names...")
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    return df


def process_dates(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Processing date column...")
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    return df


def filter_food_items(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Filtering food items...")
    return df[df['category'] == 'cereals and tubers']


def filter_units(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Filtering unit == KG...")
    return df[df['unit'] == 'KG']


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Dropping missing values...")
    return df.dropna(subset=['price', 'usdprice', 'commodity', 'countryiso3'])


def select_columns(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Selecting relevant columns...")
    return df[
        [
            'countryiso3',
            'admin1',
            'market',
            'commodity',
            'date',
            'month',
            'price',
            'usdprice'
        ]
    ]


def aggregate_prices(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Aggregating monthly prices...")

    return (
        df.groupby(['countryiso3', 'commodity', 'month'])
        .agg(avg_usdprice=('usdprice', 'mean'))
        .reset_index()
    )


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Starting transformation pipeline...")

    df = clean_columns(df)
    df = process_dates(df)
    df = filter_food_items(df)
    df = filter_units(df)
    df = handle_missing_values(df)
    df = select_columns(df)
    df = aggregate_prices(df)

    logging.info("Transformation complete!")

    return df
