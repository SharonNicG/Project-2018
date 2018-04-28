# Sharon Gibbons, 21-04-2018
# Summary review of Iris data set using pandas library
# https://www.datacamp.com/community/blog/python-pandas-cheat-sheet

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

# View instances i.e the number of rows and columns
print(df.shape)

# Summary of basic data about Dataframe and it's data
print(df.info())

# Check for missing attribute values
print(df.count())
