#This program outpus a summary of each variable of the Iris Dataset into a single text file, then saves a histogram of each variable, and outputs a scatter plot of each pair of variables
#Author: Sarah Fitzgerald

import numpy as numpy #Needed to 
import matplotlib as plt
import pandas as pd #Used to read the .csv file for the data set
import seaborn as sns 

data = pd.read_csv("irisDataset.csv") # Reads the data from this file

#def summary (filename): 

    #file = open(filename, "w+") #To write to and read the file

text = open ("analysisSummary.txt", "w") #Writes the information from the .csv file to the .txt file

data.head() #This previews the first 5 lines of the data from the .csv file: https://www.shanelynn.ie/python-pandas-read-csv-load-data-from-csv-files/

#file = text writes the data from the .csv file to the .txt file

print ("Analysis Summary", file = text)
print (" ", file = text)
print ("Overview of the whole dataset", file = text) #Adds title to this section
print ("    -Showing the first 5 and last 5 entries:", file = text) #Adds subtitle to this section
print (data, file = text) #Writes the actual data to the .txt file

print (" ", file = text)
print ("Summary of numerical values:", file = text)
print (data.describe(), file = text) #Gets a summary of numeric vales from the dataset and writes them to the .txt file: https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77
print (" ", file = text)

print ("Information about dataset:", file = text)
#print (data.info(verbose = True, null_counts = False), file = text) Prints a concise summary of the dataframe, but was unable to get to work right now: https://www.geeksforgeeks.org/python-pandas-dataframe-info/#:~:text=Python%20is%20a%20great%20language,concise%20summary%20of%20the%20dataframe
print (data.dtypes, file = text) #Prints summary about the DataFrame: https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77
print (" ", file = text)

print ("Types of iris species:", file = text)
print (data["Species"].value_counts(), file = text) #Prints the occurance of each species from the dataset
print (" ", file = text)

