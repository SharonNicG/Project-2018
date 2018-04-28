# Sharon Gibbons, 23-04-2018
# Iris dataset
# http://archive.ics.uci.edu/ml/datasets/Iris

# Python script that opens, checks and prints the Iris dataset

# opens CSV file and extracts the data for reading
with open('iris.csv') as f:
    
    # iterates over each line of data in opened file
    for line in f:

       # outputs requested unpacked arguments as split list  
       print (*line.split(','))

# applies above script to backup data file to check content

# opens CSV file and extracts the data for reading
with open('iris_bup.csv') as bup:
    
    # iterates over each line of data in opened file
    for line in bup:

       # outputs requested unpacked arguments as split list  
       print (*line.split(','))
        
