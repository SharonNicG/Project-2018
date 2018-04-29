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

    # Box and whisker plot to show range and median of data
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot.html
    df.plot(kind='box', layout=(2,2), subplots=True)
    
    # Set title and axes labels
    plt.suptitle("Iris Data Set Box and Whisker Plot")
    plt.xlabel("Measurement in cms")
    plt.ylabel("Number of instances")

    # Histogram plot presenting data as a bar chart showing a continuous range of data values
    df.hist(edgecolor='black')

    # Set title and axes labels
    plt.suptitle("Iris Data Set Histogram")
    plt.xlabel("Measurement in cms")
    plt.ylabel("Number of instances")

    # Display plots
    plt.show()
