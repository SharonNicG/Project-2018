# Sharon Gibbons, 21-04-2018
# Check and output details of Python environment

# Checks and outputs version number of the Python interpreter
# https://docs.python.org/2/library/sys.html#sys.version
import sys
print(sys.version)

# Imports module and outputs version details
# https://pythontips.com/2013/08/28/finding-the-module-version/
import scipy
print(scipy.__version__)

import pandas
print(pandas.__version__)

import matplotlib
print(matplotlib.__version__)