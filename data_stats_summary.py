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
print("The lowest value in each column is: \n{}".format(df.min()))
print('\n')

# Identifies the highest value in each column
print("The highest value in each column is: \n{}".format(df.max()))
print('\n')

# Provides mean/average value of each column
print("The mean value in each column is: \n{}".format(df.mean()))
print('\n')

# Provides median/midpoint value for each column
print("The median value in each column is: \n{}".format(df.median()))
print('\n')

# Provides the standard deviation (std) for each column
print("The standard deviation of the values in each column is: \n{}".format(df.std()))
print('\n')

# Provides summary statistics for numerical columns
# Includes count, min, max, mean, std and percentiles for data in each column
print("Statistical summary of data \n{}".format(df.describe()))
