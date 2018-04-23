# Sharon Gibbons, 23-04-2018
# Iris dataset
# http://archive.ics.uci.edu/ml/datasets/Iris

# Python script that opens, checks and prints the Iris dataset

# opens CSV file and extracts the data for reading
with open('iris.csv') as f:
    
    # accesses 'f' file and prints output of content
    print (f.read())