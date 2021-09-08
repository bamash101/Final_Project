# import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
County_List = Houses["County"].to_list()
for i in County_List :
    if i == "Dublin" :
        print ("Your search returned:", i)
        print()
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

# A function to count the number of unique entries in a user defined dataframe column
def unique(Dataframe,Column):
    print("The number of unique entries in this column is:", Dataframe[Column].nunique())
    print()

# Calling the function unique
unique(Dataframe=Houses, Column='County')

# Creating a list from a dataframe and converting it to a Numpy Array
County_Only = Houses[Houses.County != "All Counties"]
List = County_Only.values.tolist()
Array = np.array(List)
print("Example of a Numpy Array")
print(Array)

# Matplotlib visualisation
Plot_Data = Houses.loc[(Houses["County"] == "All Counties")]
Plot_Data.plot(x="Year", y=["VALUE"], kind="bar")
plt.title("Fig.1 - No. of houses built per year in Ireland", color = 'black')
plt.xlabel('Year', color = 'grey', fontsize='12', horizontalalignment='center')
plt.ylabel('No. of Houses', color = 'grey', fontsize='12', horizontalalignment='center')
plt.xticks(color='black', rotation=90, fontsize='8', horizontalalignment='center')
plt.yticks(color='black', rotation=0, fontsize='8', horizontalalignment='right')
plt.grid(color='grey', linewidth=.5, linestyle='--', axis='y')
plt.legend('')
plt.show()

# Seaborn visualisation
Counties = ['Dublin','Cork','Galway','Limerick','Waterford']
Seaborn_Data = Houses[Houses['County'].isin(Counties)]
sns.lineplot(data = Seaborn_Data , x = 'Year', y = 'VALUE' , hue = 'County').set(title='Fig.2 - Number of houses built annually in counties with cities')
plt.show()



