#This program outpus a summary of each variable of the Iris Dataset into a single text file, then saves a histogram of each variable, and outputs a scatter plot of each pair of variables
#Author: Sarah Fitzgerald

import matplotlib.pyplot as plt #Used to make plots and add information to them
import pandas as pd #Used to read the .csv file for the data set
import seaborn as sns #Used to make histograms, scatter plots, and pairplots

data = pd.read_csv("irisDataset.csv") # Reads the data from this file

text = open ("analysisSummary.txt", "w") #Writes the information from the .csv file to the .txt file

data.head() #This previews the first 5 lines of the data from the .csv file: https://www.shanelynn.ie/python-pandas-read-csv-load-data-from-csv-files/

#file = text writes each line to the .txt file

print ("Analysis Summary", file = text)
print (" ", file = text) #Used to create a space between paragraphs
print ("Overview of the whole dataset", file = text) #Adds title to this section
print ("    -Showing the first 5 and last 5 entries:", file = text) #Adds subtitle to this section
print (data, file = text) #Writes the actual data to the .txt file

print (" ", file = text)
print ("Summary of numerical values:", file = text)
print (data.describe(), file = text) #Gets a summary of numeric vales from the dataset and writes them to the .txt file: https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77
print (" ", file = text)

print ("Information about dataset:", file = text)
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
#https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/
#First, make the histogram of one variable then add the next histogram to the existing plot object, this is added as an extra layer
#Colour names for histograms: https://stackoverflow.com/questions/22408237/named-colors-in-matplotlib

#Histogram for Sepal Length in CM
sns.distplot(irisSetosa['sepalLenghtCm'], kde = False, label = 'Iris Setosa', color = 'purple')
sns.distplot(irisVersicolor['sepalLenghtCm'], kde = False, label = 'Iris Versicolor', color = 'deeppink')
sns.distplot(irisVirginica['sepalLenghtCm'], kde = False, label = 'Iris Virginica', color = 'blueviolet')

#Didn't use plt.xlim or plt.ylim as it was unnecessary for these histograms

plt.xlabel ('Centimeters') #Labels the X-Axis
plt.ylabel ('Frequency') #Labels the Y-Axis
plt.title ('Sepal Length') #Titles the Histogram

plt.legend() #Adds a legend to the histogram
plt.savefig('Sepal Length in CM') #Save file: https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
plt.show()

#Histogram for Sepal Width in CM
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

#Scatter plot for Sepal Comparasion

#Used built in fucntion in Seaborn to make scatter plots
#https://pythonbasics.org/seaborn-scatterplot/
#https://seaborn.pydata.org/tutorial/relational.html
#https://seaborn.pydata.org/generated/seaborn.scatterplot.html#:~:text=scatterplot,-seaborn.&text=Draw%20a%20scatter%20plot%20with%20possibility%20of%20several%20semantic%20groupings.&text=It%20is%20possible%20to%20show,interpret%20and%20is%20often%20ineffective.
#https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
sns.scatterplot(x = "sepalLenghtCm", y = "sepalWidthCm", data = data, hue = "Species", palette = ['purple', 'deeppink', 'blueviolet']) # https://www.geeksforgeeks.org/scatterplot-using-seaborn-in-python/

plt.xlabel ('Length in Centimeters') #Labels X-Axis
plt.ylabel ('Width in Centimeters') #Labels Y-Axis

plt.title ('Sepal') #Titles the scatter plot

plt.legend() #Adds a legend to the scatter plot
plt.savefig('Sepal Scatter Plot')#Saves the graph as a .png
plt.show()

#Scatter plot for Petal Comparasion
sns.scatterplot(x = "petalLengthCm", y = "petalWidthCm", data = data, hue = "Species", palette = ['purple', 'deeppink', 'blueviolet']) # https://www.geeksforgeeks.org/scatterplot-using-seaborn-in-python/

plt.xlabel ('Length in Centimeters') 
plt.ylabel ('Width in Centimeters') 

plt.title ('Petal') 

plt.legend() 
plt.savefig('Petal Scatter Plot') 
plt.show()

#Pairplot for Sepal and Petal Comparasion
#Used pairplot to represent multidenminsional relationship between Sepal Lenght, Sepal Width, Petal Length, Petal Width, and their respective speies: https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
sns.pairplot(data, hue = 'Species', palette = ['purple', 'deeppink', 'blueviolet'])
plt.title ('Iris Pairplot') 
plt.savefig('Iris Pairplot') 
plt.show()