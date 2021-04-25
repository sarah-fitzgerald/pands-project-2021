#This program outpus a summary of each variable of the Iris Dataset into a single text file, then saves a histogram of each variable, and outputs a scatter plot of each pair of variables
#Author: Sarah Fitzgerald

import numpy as numpy #Needed to 
import matplotlib as plt
import pandas as pd #Used to read the .csv file for the data set
import seaborn as sns 

data = pd.read_csv("irisDataset.csv") # Reads the data from this file

data.head() #This previews the first 5 lines of the data from the .csv file: https://www.shanelynn.ie/python-pandas-read-csv-load-data-from-csv-files/

def summary (filename): 

    file = open(filename, "w+") #To write to and read the file

print (data)