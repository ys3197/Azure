## import packages
import numpy as np
import pandas as pd


## First Question

# Read the files first
df1 = pd.read_csv('people_1.txt', delimiter='\t')
df2 = pd.read_csv('people_2.txt', delimiter='\t')
df = pd.concat([df1, df2])

# Lower case all columns and remove space before or after the strings
df = df.apply(lambda x: x.astype(str).str.lower())
df = df.apply(lambda x: x.astype(str).str.strip())

# For phone and address col, replace some signs with empty space
df['Phone'] = df['Phone'].apply(lambda x: x.replace("-", ""))
df['Address'] = df['Address'].apply(lambda x: x.replace("no.", ""))
df['Address'] = df['Address'].apply(lambda x: x.replace("#", ""))

# Finally drop the duplicates and save to a new csv
df = df.drop_duplicates()
df.to_csv("final_df.csv")


## Second Question

# Read the json first
data = pd.read_json("movie.json")

# Split the data
target = np.array_split(data, 8)
n = 1

# Use a for loop to output each pieces of data
for df in target:
  df.to_json("chunk_"+str(n)+'.json')
  n += 1
