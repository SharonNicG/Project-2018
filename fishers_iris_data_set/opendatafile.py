# Sharon Gibbons, 23-04-2018
# Iris dataset
# http://archive.ics.uci.edu/ml/datasets/Iris

# Python script that opens, checks and prints the Iris dataset

# opens data file in current workflow
f = open('iris.csv')

# Returns True if the file stream can be read from.
# https://www.programiz.com/python-programming/file-operation
f.readable()

# output of information in file
print(f.read())

# closes opened file
f.close