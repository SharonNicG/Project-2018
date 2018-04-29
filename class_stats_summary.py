# Sharon Gibbons, 29-04-2018
# Summary review of Iris data set, by class

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

    # Identify the lowest value of each attribute, by class
    print("Below is the lowest value of each attribute, by class: \n{}".format(df.groupby('class').min()))
    print('\n')

    # Identify the highest value of each attribute, by class
    print("Below is the highest value of each attribute, by class: \n{}".format(df.groupby('class').max()))
    print('\n')

    # Provides mean/average value of each attribute, by class
    print("Below is the mean value of each attribute, by class: \n{}".format(df.groupby('class').mean()))
    print('\n')

    # Provides median/midpoint value of each attribute, by class
    print("Below is the median value of each attribute, by class: \n{}".format(df.groupby('class').median()))
    print('\n')

    # Provides the standard deviation (std) for each attribute, by class
    print("Below is the standard deviation of each attribute, by class: \n{}".format(df.groupby('class').std()))
    print('\n')

    # Provides summary statistics for each class
    # Includes count, min, max, mean, std and percentiles for data in each column
    # Reformat inspired by https://stackoverflow.com/questions/42579148/get-columns-describe-from-group-by
    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.stack.html
    print("Statistical summary of data: \n{}".format(df.groupby('class').describe().stack()))
