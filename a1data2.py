# From Zhenyang Ding

import pandas as pd
import numpy as np

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
adult = fetch_ucirepo(id=2) 
  
# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 
  
# metadata 
# print(adult.metadata) 
  
# variable information 
print(adult.variables)

# print(X.head())
# print(y)

# Google "pandas metadata"
# Google "numpy data cleaning"
# Google "pandas see dataframe"


#Look at https://realpython.com/python-data-cleaning-numpy-pandas/
# look at https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/

# import data
# make data into numpy
# one hot encode cat vars
# note missing data in report
# remove missing data
# note malformed data in report
# remove malformed data
# compute basic stats
    #what are the distributions of the positive vs.
    #negative classes, what are the distributions of some of the numerical features? what are the correlations between
    #the features? how do the scatter plots of pair-wise features look like for some subset of features?


