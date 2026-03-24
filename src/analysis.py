import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set(style="whitegrid")


def ensure_output_dir():
    Path("outputs").mkdir(parents=True, exist_ok=True)


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


# summary stats
def save_summary_stats(df):
    summary = {
        "num_rows": len(df),
        "num_countries": df['countryiso3'].nunique(),
        "num_commodities": df['commodity'].nunique(),
    }

    summary_df = pd.DataFrame([summary])

    summary_df.to_csv("outputs/summary_stats.csv", index=False)
    summary_df.to_excel("outputs/summary_stats.xlsx", index=False)

    print("📊 Summary stats saved!")

    return summary_df


def save_commodity_stats(df):
    commodity_stats = (
        df.groupby('commodity')['avg_usdprice']
        .agg(['mean', 'min', 'max', 'std'])
        .reset_index()
    )

    commodity_stats.to_csv("outputs/commodity_stats.csv", index=False)
    commodity_stats.to_excel("outputs/commodity_stats.xlsx", index=False)

    print("📊 Commodity stats saved!")


# visualizations
def plot_top_commodities(df):
    data = (
        df.groupby('commodity')['avg_usdprice']
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(x=data.values, y=data.index)

    plt.title("Top 10 Most Expensive Commodities (USD)")
    plt.xlabel("Average Price (USD)")
    plt.ylabel("Commodity")

    plt.tight_layout()
    plt.savefig("outputs/top_commodities.png", dpi=300)
    plt.show()


def plot_top_countries(df):
    data = (
        df.groupby('countryiso3')['avg_usdprice']
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(x=data.values, y=data.index)

    plt.title("Top 10 Countries by Average Food Price")
    plt.xlabel("Average Price (USD)")
    plt.ylabel("Country")

    plt.tight_layout()
    plt.savefig("outputs/top_countries.png", dpi=300)
    plt.show()


def plot_monthly_trend(df, commodity="Rice"):
    df_commodity = df[df['commodity'].str.contains(commodity, case=False, na=False)]

    trend = df_commodity.groupby('month')['avg_usdprice'].mean()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=trend.index, y=trend.values, marker="o")

    plt.title(f"Monthly Price Trend for {commodity} (2016)")
    plt.xlabel("Month")
    plt.ylabel("Average Price (USD)")
    plt.xticks(range(1, 13))

    plt.tight_layout()
    plt.savefig("outputs/rice_trend.png", dpi=300)
    plt.show()


def plot_heatmap(df):
    pivot = df.pivot_table(
        values='avg_usdprice',
        index='commodity',
        columns='month'
    )

    
    pivot = pivot.head(15)

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, cmap="coolwarm", linewidths=0.5)

    plt.title("Commodity Price Heatmap (USD)")
    plt.xlabel("Month")
    plt.ylabel("Commodity")

    plt.tight_layout()
    plt.savefig("outputs/heatmap.png", dpi=300)
    plt.show()


# main
def run_analysis():
    ensure_output_dir()

    df = load_data("data/processed/wfp_2016_clean.csv")

    # Save stats
    save_summary_stats(df)
    save_commodity_stats(df)

    # Generate plots
    plot_top_commodities(df)
    plot_top_countries(df)
    plot_monthly_trend(df, commodity="Rice")
    plot_heatmap(df)


if __name__ == "__main__":
    run_analysis()
