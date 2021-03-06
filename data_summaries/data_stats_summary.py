# Sharon Gibbons, 21-04-2018
# Summary review of Iris data set
# http://www.datasciencemadesimple.com/python-pandas-tutorial/

# Load NumPy package
import numpy as np 

# Load pandas package
import pandas as pd

# Load csv data file in Python using with statement to ensure files closes after functions complete
with open('fishers_iris_data_set/iris.csv') as datafile:

    # Assign headers to columns
    headers = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

    # Read csv data file with pandas read_csv function
    df = pd.read_csv(datafile, header=None, names=headers)

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
    print("Statistical summary of data: \n{}".format(df.describe()))
