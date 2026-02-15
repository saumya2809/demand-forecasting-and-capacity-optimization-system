# demand-forecasting-and-capacity-optimization-system
# Azure Demand Forecasting & Capacity Optimization System

## 📌 Milestone 1: Data Collection & Preparation

### 🎯 Objective
Compile, clean, and prepare historical Azure usage data along with relevant external variables for demand forecasting model development.

---

## 📂 Dataset Description

The dataset includes historical Azure Compute and Storage usage data with the following features:

| Column Name | Description |
|-------------|-------------|
| timestamp | Date of usage (daily granularity) |
| region | Azure region |
| service_type | Compute / Storage |
| usage_units | Demand units (cores / GB) |
| provisioned_capacity | Allocated capacity |
| cost_usd | Cost incurred |
| availability_pct | Service availability percentage |
| is_holiday | External variable (holiday indicator) |

---

## 🛠 Tasks Completed

### 1️⃣ Data Collection
- Collected historical Azure Compute and Storage usage data
- Included regional and seasonal dimensions
- Integrated external variables such as holiday indicators

### 2️⃣ Data Cleaning
- Checked for missing values
- Removed duplicate records
- Standardized column formats
- Ensured data consistency

### 3️⃣ Data Validation
- Verified data types
- Validated date formats
- Ensured no null values in critical columns

---

## 🧹 Data Preprocessing Steps (Python)

`python
import pandas as pd

# Load dataset
df = pd.read_csv("azure_ml_demand_dataset_5years-1.csv")

# Check basic info
print(df.info())

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

print("Data cleaned successfully")
