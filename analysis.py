#This program outpus a summary of each variable of the Iris Dataset into a single text file, then saves a histogram of each variable, and outputs a scatter plot of each pair of variables
#Author: Sarah Fitzgerald

import numpy as numpy
import matplotlib as plt
import pandas as pd

data = pd.read_csv('https://github.com/sarah-fitzgerald/pands-project-2021/blob/8981b4df14499ccd74de03f03b000770efba5ee2/irisDataset')

data.head()