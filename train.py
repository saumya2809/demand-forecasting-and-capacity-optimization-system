import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("azure_ml_demand_dataset_5years-1.csv")
#df = pd.read_csv(r"C:\Users\saumy\OneDrive\Desktop\azure_ml_demand_dataset_5years-1.csv")


 # print(df) -> displays the dataset
print(df.shape) #rows and columns
print(df.columns) #column names
print(df.info()) #data types and nulls
print(df.describe()) #statistics
print(df.head()) #output first 5 rows
print(df.isnull().sum()) #check for missing values
print(df.duplicated().sum()) #check for duplicates
df=df.drop_duplicates() #remove duplicates
print(df.shape) #new shape after removing duplicates
df.fillna(df.mode().iloc[0], inplace=True) #impute missing values with mode
print(df.isnull().sum()) #check again for missing values and this should show 0 for all columns
df['timestamp'] = pd.to_datetime(df['timestamp']) #convert Date to datetime
print(df.dtypes) #check data types
df=df.sort_values('timestamp') #sort by Date
print(df.head()) #check sorted data
df['usage_units']=df['usage_units'].fillna(df['usage_units'].median())
df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['week_of_year'] = df['timestamp'].dt.isocalendar().week
