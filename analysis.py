#This program outpus a summary of each variable of the Iris Dataset into a single text file, then saves a histogram of each variable, and outputs a scatter plot of each pair of variables
#Author: Sarah Fitzgerald

import numpy as numpy #Needed to 
import matplotlib.pyplot as plt
import pandas as pd #Used to read the .csv file for the data set
import seaborn as sns 

data = pd.read_csv("irisDataset.csv") # Reads the data from this file

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

#Plotting histograms for each variable

#Selecting the column "Species" from the .csv file and assigning it:https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
irisSetosa = data[data.Species == "Iris-setosa"]
irisVersicolor = data[data.Species == "Iris-versicolor"]
irisVirginica = data[data.Species == "Iris-virginica"]

#Used Seaborn built in fucntion to make the histograms
#The distplot function takes a column from the .csv file to make the histogram 
#First, make the histogram of one variable then add the next histogram to the existing plot object, this is added as an extra layer
#Colour names for histograms: https://stackoverflow.com/questions/22408237/named-colors-in-matplotlib

#Histogram for Sepal Length in CM
sns.distplot(irisSetosa['sepalLenghtCm'], kde = False, label = 'Iris Setosa', color = 'purple')
sns.distplot(irisVersicolor['sepalLenghtCm'], kde = False, label = 'Iris Versicolor', color = 'deeppink')
sns.distplot(irisVirginica['sepalLenghtCm'], kde = False, label = 'Iris Virginica', color = 'blueviolet')

#Didn't use plt.xlim or plt.ylim as it was unnecessary for these histograms

plt.xlabel ('Centimeters')
plt.ylabel ('Frequency') #Labels the Y-Axis
plt.title ('Sepal Length') #Titles the Histogram

plt.legend() #Adds a legend to the histogram
plt.savefig('Sepal Length in CM') #Save file: https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
plt.show()

#Histogram ofr Sepal Width in CM
sns.distplot(irisSetosa['sepalWidthCm'], kde = False, label = 'Iris Setosa', color = 'purple')
sns.distplot(irisVersicolor['sepalWidthCm'], kde = False, label = 'Iris Versicolor', color = 'deeppink')
sns.distplot(irisVirginica['sepalWidthCm'], kde = False, label = 'Iris Virginica', color = 'blueviolet')

plt.xlabel ('Centimeters')
plt.ylabel ('Frequency')
plt.title ('Sepal Width')

plt.legend()
plt.savefig('Sepal Width in CM')
plt.show()

#Histogram for Petal Length in CM
sns.distplot(irisSetosa['petalLengthCm'], kde = False, label = 'Iris Setosa', color = 'purple')
sns.distplot(irisVersicolor['petalLengthCm'], kde = False, label = 'Iris Versicolor', color = 'deeppink')
sns.distplot(irisVirginica['petalLengthCm'], kde = False, label = 'Iris Virginica', color = 'blueviolet')

plt.xlabel ('Centimeters')
plt.ylabel ('Frequency')
plt.title ('Petal Length')

plt.legend()
plt.savefig('Petal Length in CM')
plt.show()

#Histogram for Petal Width in CM
sns.distplot(irisSetosa['petalWidthCm'], kde = False, label = 'Iris Setosa', color = 'purple')
sns.distplot(irisVersicolor['petalWidthCm'], kde = False, label = 'Iris Versicolor', color = 'deeppink')
sns.distplot(irisVirginica['petalWidthCm'], kde = False, label = 'Iris Virginica', color = 'blueviolet')

plt.xlabel ('Centimeters')
plt.ylabel ('Frequency')
plt.title ('Petal Width')

plt.legend()
plt.savefig('Petal Width in CM')
plt.show()