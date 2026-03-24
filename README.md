# 🌍 WFP Food Price ETL Pipeline

This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** using real-world humanitarian data from the World Food Programme (WFP) from 2016. The pipeline processes global food price data, cleans and standardizes it, and produces analysis-ready outputs along with visualizations.

---

## 📊 Data Source

Data was obtained from the **Humanitarian Data Exchange (HDX)**:

- Dataset: Global WFP Food Prices  
- Source: https://data.humdata.org/dataset/global-wfp-food-prices  

The dataset contains market-level food prices across multiple countries, commodities, and time periods.

---

## ⚙️ Project Overview

This project implements a modular ETL pipeline:

### 🔹 Extract
- Reads raw CSV data from WFP dataset
- Validates file existence and loads into a pandas DataFrame

### 🔹 Transform
- Cleans and standardizes column names
- Converts and extracts date features (year, month)
- Filters for food-related categories (e.g., cereals and tubers)
- Standardizes units (KG only for consistency)
- Removes missing or invalid entries
- Aggregates average monthly prices by country and commodity

### 🔹 Load
- Saves cleaned dataset to CSV
- Stores results in a SQLite database

### 📈 Analysis & Visualization
- Identifies top commodities by price
- Compares average prices across countries
- Analyzes monthly trends for key commodities
- Generates publication-ready plots

---

## 📁 Project Structure

```bash
etl-wfp-food-prices/
│
├── data/
│   ├── raw/
│   │   └── wfp_food_prices_global_2016.csv   # Original dataset
│   └── processed/
│       └── wfp_2016_clean.csv               # Cleaned output (generated)
│
├── outputs/
│   ├── top_commodities.png                  # Visualization
│   ├── top_countries.png                    # Visualization
│   └── rice_trend.png                       # Visualization
│
├── src/
│   ├── extract.py                           # Data extraction logic
│   ├── transform.py                         # Data cleaning & transformation
│   ├── load.py                              # Save to CSV & SQLite
│   ├── pipeline.py                          # ETL pipeline runner
│   └── analysis.py                          # Data analysis & visualization
│
├── requirements.txt                         # Dependencies
├── README.md                                # Project documentation
└── .gitignore                               # Ignore unnecessary files
```

## 🚀 How to Run This Project

### 1. Clone the repository.

```bash
git clone https://github.com/nkodgi/ETL_WFP_Food_Prices_2016.git
cd ETL_WFP_Food_Prices_2016
```

### 2. Create conda environment and install packages.
```bash
conda create -n etl-wfp python=3.10 -y
conda activate etl-wfp
pip install -r requirements.txt
```

### 3. Run pipeline and visualization scripts.
```bash
python src/pipeline.py
python src/analysis.py
```

## 📊 Key Insights

- Rice is consistently one of the most expensive commodities, with certain varieties significantly exceeding others in price  
- Food prices vary widely across countries, with Bhutan and Somalia showing the highest average prices  
- Monthly price trends indicate fluctuations in staple food costs, suggesting seasonal or supply-driven effects
- Cassava-based products remain among the lowest-priced food items, suggesting their role as staple, affordable food sources in many regions.
- Certain commodities such as buckwheat and bread maintain consistently higher price levels, indicating stronger demand or limited supply stability.
