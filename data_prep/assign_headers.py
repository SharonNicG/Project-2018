# Sharon Gibbons, 21-04-2018
# Assign headers to columns in pandas datafrome

# Load pandas package
import pandas as pd

# Load csv data file in Python
datafile = 'fishers_iris_data_set/iris.csv'

# Assign headers to columns
headers = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

# Read csv data file with pandas read_csv function
df = pd.read_csv(datafile, names=headers)

# View column names
print(df.head())
