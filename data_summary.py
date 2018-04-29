# Sharon Gibbons, 21-04-2018
# Summary review of Iris data set using pandas library
# https://www.datacamp.com/community/blog/python-pandas-cheat-sheet

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

    # View first 5 rows and headers 
    print(df.head())
    print('\n')

    # View instances i.e the number of rows and columns
    print(df.shape)
    print('\n')

    # Summary of basic data about Dataframe and it's data
    print(df.info())
    print('\n')

    # Check for missing attribute values
    print(df.count())
    print('\n')
