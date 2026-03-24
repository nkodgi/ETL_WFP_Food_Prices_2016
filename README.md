# 🌍 WFP Food Price ETL Pipeline

This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** using real-world humanitarian data from the World Food Programme (WFP). The pipeline processes global food price data, cleans and standardizes it, and produces analysis-ready outputs along with visualizations.

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
