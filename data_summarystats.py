# Sharon Gibbons, 21-04-2018
# Summary review of Iris data set

# Load NumPy package
import numpy as np 

# Load pandas package
import pandas as pd

# Load csv data file in Python
datafile = 'fishers_iris_data_set/iris.csv'

# Assign headers to columns
headers = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

# Read csv data file with pandas read_csv function
df = pd.read_csv(datafile, names=headers)

# Identify the lowest value in each column
print(df.min())

# Identifies the highest value in each column
print(df.max())

# Provides mean/average value of each column
print(df.mean())

#Provides median/midpoint value for each column
print(df.median())