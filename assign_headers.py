# Sharon Gibbons, 21-04-2018
# Assign headers to columns in pandas datafrome


# Load pandas package
import pandas as pd

# Load csv data file in Python
datafile = 'fishers_iris_data_set/iris.csv'

# Read csv data file with pandas read_csv function
df = pd.read_csv(datafile)

# View output of read by pandas
print(df)