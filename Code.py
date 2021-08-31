# import required libraries
import pandas as pd
import numpy as np
import matplotlib as plt
import os

# Check the working directory
os.getcwd()

# import the dataset
Houses = pd.read_csv("New_House.csv")

# view & understand the structure of the dataset
print(Houses.head())
print(Houses.shape)
print(Houses.columns)

# Identify any missing values
missing_values_count = Houses.isnull().sum()
print(missing_values_count)

# Replace missing values with zero
cleaned_data = Houses.fillna(0)
print(cleaned_data.isnull().sum())

# Sorted the values by County, then year
Houses_Sorted = Houses.sort_values(by=["County", "Year"])
print(Houses_Sorted.head(50))

# Assigned a new index using County & Year columns, then sorted that index.
Houses_Index = Houses.set_index(["Year", "County"])
Houses_Index.sort_index()
print(Houses_Index.head(50))