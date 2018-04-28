# Sharon Gibbons, 21-04-2018
# Check and output details of Python environment
# https://docs.python.org/3/tutorial/inputoutput.html

# Checks and outputs version number of the Python interpreter
# https://docs.python.org/2/library/sys.html#sys.version
import sys
print('Python version: {}'.format(sys.version))

# Imports module and outputs version details
# https://pythontips.com/2013/08/28/finding-the-module-version/
import scipy
print('SciPy version: {}'.format(scipy.__version__))

import pandas
print('pandas version: {}'.format(pandas.__version__))

import matplotlib
print('Matplotlib version: {}'.format(matplotlib.__version__))
