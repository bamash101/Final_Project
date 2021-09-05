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
print(Houses_Grouped.head(27))
print()

# Looping through a list until Dublin is found, then printing it
County_List = Province["County"].to_list()
for i in County_List :
    if i == "Dublin" :
        print (i)
        break
else:
    print("Not found")

# Using iterrows to print out which province each county is in
for index, row in Province.iterrows():
    print(row['County'], 'is in', row['Province'])
    print()

# Merge Houses dataframe with Provinces dataframe
Houses_Merged = pd.merge(Houses,Province,on="County", how = "left")
print(Houses_Merged.head(20))
print()

# Creating a function
def drop_total():
    County_Only = Houses[Houses.County != "All Counties"]
    print("'All Counties' rows removed from the Houses dataframe")
    print(County_Only.head(30))
    return County_Only

# Calling the function
drop_total()

# Creating a list from a dataframe and converting it to a Numpy Array
County_Only = Houses[Houses.County != "All Counties"]
List = County_Only.values.tolist()
Array = np.array(List)
print(List)

