# Sharon Gibbons, 29-04-2018
# Visualisation of data analysis on Iris data set

# Load NumPy package
import numpy as np 

# Load pandas package
import pandas as pd

# Load libraries for visualisation
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load csv data file in Python using with statement to ensure files closes after functions complete
with open('fishers_iris_data_set/iris.csv') as datafile:

    # Assign headers to columns
    headers = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

    # Read csv data file with pandas read_csv function
    df = pd.read_csv(datafile, header=None, names=headers)

    # Scatterplot matrix to help identify linear correlation between multiple variables
    scatter_matrix(df)

    # Set title
    plt.suptitle("Iris Data Set Histogram")

    plt.show()
