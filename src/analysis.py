import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def plot_top_commodities(df):
    data = df.groupby('commodity')['avg_usdprice'].mean().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=data.values, y=data.index)
    plt.title("Top 10 Most Expensive Commodities")
    plt.xlabel("USD Price")

    plt.savefig("outputs/top_commodities.png", dpi=300)
    plt.close()


def plot_top_countries(df):
    data = df.groupby('countryiso3')['avg_usdprice'].mean().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=data.values, y=data.index)
    plt.title("Top 10 Countries by Food Price")

    plt.savefig("outputs/top_countries.png", dpi=300)
    plt.close()


def plot_monthly_trend(df):
    rice = df[df['commodity'].str.contains("Rice", case=False, na=False)]
    trend = rice.groupby('month')['avg_usdprice'].mean()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=trend.index, y=trend.values, marker="o")
    plt.title("Rice Price Trend (2016)")

    plt.savefig("outputs/rice_trend.png", dpi=300)
    plt.close()


def run_analysis():
    df = load_data("data/processed/wfp_2016_clean.csv")

    plot_top_commodities(df)
    plot_top_countries(df)
    plot_monthly_trend(df)


if __name__ == "__main__":
    run_analysis()
