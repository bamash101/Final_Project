# import required libraries
import pandas as pd
import numpy as np
import matplotlib as plt
import os

# Check the working directory
os.getcwd()

# import the datasets
Houses = pd.read_csv("New_House.csv")
Province = pd.read_csv("Province.csv")

# view & understand the structure of the dataset
print(Houses.head())
print(Houses.shape)
print(Houses.columns)
print()

# Identify any missing values
missing_values_count = Houses.isnull().sum()
print(missing_values_count)
print()

# Replace missing values with zero
cleaned_data = Houses.fillna(0)
print(cleaned_data.isnull().sum())
print()

# Sorted the values by County, then year
Houses_Sorted = Houses.sort_values(by=["County", "Year"])
print("Houses Sorted by County, then Year:")
print(Houses_Sorted.head(10))
print()

# Assigned a new index using County & Year columns, then sorted that index.
Houses_Index = Houses.set_index(["Year", "County"])
Houses_Index.sort_index()
print("Houses Indexed by Year & County:")
print(Houses_Index.head(10))
print()

# Group the data by totals in each County
Houses_Grouped = Houses.groupby("County")["VALUE"].sum()
print("The number of houses built from 1978 - 2019:")
print(Houses_Grouped.head(20))
print()

#Merge
Houses_Merged = pd.merge(Houses,Province,on="County", how = "left")
print(Houses_Merged.head(20))