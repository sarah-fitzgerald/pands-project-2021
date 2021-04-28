<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->





  <h1 align="center">pands-project2021</h1>

  <p align="center">
    Sarah Fitzgerald
    

#

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#Fisher's-Iris-data-set">Fisher's Iris Data Set</a>
      <ul>
        <li><a href="#history">History</a></li>
      </ul>
    </li>
    <li>
      <a href="#libraries-and-dataset-import">Libraries and Dataset Import</a>
      <ul>
        <li><a href="#libraries">Libraries</a></li>
      </ul>
      <ul>
        <li><a href="#dataset">Dataset</a></li>
      </ul>
      <ul>
        <ul>
          <li><a href="#dataset-import">Dataset Import</a></li>
          <li><a href="#analysis-summary-of-the-data">Analysis Summary of the Data</a></li>
        </ul>
    </li>
      </ul>
    </li>
    <li><a href="#histograms">Histograms</a></li>
    <ul>
        <li><a href="#histogram-code">Histogram Code</a></li>
      </ul>
      <ul>
        <li><a href="#histograms">Histograms</a></li>
      </ul>
    <li><a href="#scatter-plots">Scatter Plots</a></li>
    <ul>
        <li><a href="#scatter-plot-code">Scatter Plot Code</a></li>
      </ul>
      <ul>
        <li><a href="#scatter-plots">Scatter Plots</a></li>
      </ul>
      </ul>
    <li><a href="#pairplot">Pairplot</a></li>
    <ul>
      <ul>
        <li><a href="#pairplot-code">Pairplot Code</a></li>
      </ul>
      <ul>
        <li><a href="#pairplot">Pairplot</a></li>
      </ul>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>



<!-- Fisher's Iris Data Set -->
# Fisher's Iris Data Set


## History
Fisher's Iris Data Set, also known as the Irish Flower Data Set is a data set which consists of 3 classes of 50 instances from three species of Iris. In this data, the length and width of the sepals and petals were measured in ceteminters and a linear discriminant model was used to distinguis the species from each other. 



<!-- Libraries and Dataset Import-->
# Libraries and Dataset Import
Needed to import libraries and the dataset to analyse Fisher's Iris Data Set 

## Libraries
```sh
    import matplotlib.pyplot as plt
    import pandas as pd 
    import seaborn as sns 
```

  * _Matplotlib_ is used to create visualisations in Python. _Pyplot_ is a collection of functions that make matplotlib work like MATLAB. These was used extensivly in this project to add labels, titles, and legends to plots. It was also used to save and show plots.
  
  * _pandas_ is used for data manipulation and analysis in Python. It offers data structures and operations to manipulate numerical tables and time series.

  * _Seaborn_ is a data visualisation library based on matplotlib and it provides an interface for statistical graphics. In this project it was used to plot histograms, scatter plots, and pairplots in this project.

#

## Dataset
The data was downloaded from the UCI Machine Learning Repository and can be found on this repository as [irisDataset.csv](https://github.com/sarah-fitzgerald/pands-project-2021/blob/17ddd734dca97ba34af52dcee3160b8ad3cce094/irisDataset.csv) 

### Dataset Import
```sh
    data = pd.read_csv("irisDataset.csv")
```
This line of code is used to read the data from the .csv file using _pandas_. It was stored as the variable _data_.

### Analysis Summary of the Data
After the data has been loaded from the .csv file we needed to analyse the data and write information from it to a .txt file. The first and last 5 rows from the .csv were added to the .txt file using data.head().
```sh
    text = open ("analysisSummary.txt", "w")
    data.head()
```

This next section add text to title and subtitle the information in the .txt file

```sh
    print ("Analysis Summary", file = text)
    print (" ", file = text)
    print ("Overview of the whole dataset", file = text) 
    print ("    -Showing the first 5 and last 5 entries:", file = text) 
    print (data, file = text) 
```


data.describe() prints out a summary of the Dataframe.
```sh
    print (" ", file = text)
    print ("Summary of numerical values:", file = text)
    print (data.describe(), file = text) 
    print (" ", file = text)
```
data["Species"].value_counts() prints out the occurance of each species of iris from the "Species" column in the dataset.
```sh
    print ("Types of iris species:", file = text)
    print (data["Species"].value_counts(), file = text) 
    print (" ", file = text)
```

<!-- Histograms -->
# Histograms
## Histogram Code
Defined the species using the data variable and selecting the column "Species" from the .csv file
```sh
    irisSetosa = data[data.Species == "Iris-setosa"]
    irisVersicolor = data[data.Species == "Iris-versicolor"]
    irisVirginica = data[data.Species == "Iris-virginica"]
```
Used the built in function Seaborn to make the histograms using the inforamtion from the dataset.

The displot function pulls the information from various named columns in the dataset. The histograms are layered on top of each other. This is done by making a histogram of one variable then adding hte next historgram to an existing plot.  
```sh
    sns.distplot(irisSetosa['sepalLenghtCm'], kde = False, label = 'Iris Setosa', color = 'purple')
    sns.distplot(irisVersicolor['sepalLenghtCm'], kde = False, label = 'Iris Versicolor', color = 'deeppink')
    sns.distplot(irisVirginica['sepalLenghtCm'], kde = False, label = 'Iris Virginica', color = 'blueviolet')
```
Labled the X-Axis and Y-Axis respectively and added a title to the histogram.
```sh
    plt.xlabel ('Centimeters')
    plt.ylabel ('Frequency') 
    plt.title ('Sepal Length')
```
Lastly, for this histogram, added a legend, then code to automatically save the histogram as a .png, and show the histogram.
```sh
    plt.legend() 
    plt.savefig('Sepal Length in CM') 
    plt.show()
```
This process is repeated for each histogram with the variables changed.

## Histograms

![Sepal Length in CM](https://github.com/sarah-fitzgerald/pands-project-2021/blob/17ddd734dca97ba34af52dcee3160b8ad3cce094/Sepal%20Length%20in%20CM.png)

![Sepal Width in CM](https://github.com/sarah-fitzgerald/pands-project-2021/blob/17ddd734dca97ba34af52dcee3160b8ad3cce094/Sepal%20Width%20in%20CM.png)

![Petal Length in CM](https://github.com/sarah-fitzgerald/pands-project-2021/blob/17ddd734dca97ba34af52dcee3160b8ad3cce094/Petal%20Length%20in%20CM.png)

![Petal Width in CM](https://github.com/sarah-fitzgerald/pands-project-2021/blob/17ddd734dca97ba34af52dcee3160b8ad3cce094/Petal%20Width%20in%20CM.png)

<!-- Scatter Plots -->
# Scatter Plots
## Scatter Plot Code

Used Seaborn to create scatter plots. In this case, the X-Axis is the Sepal Length in Centimeters and the Y-Axis is Sepal Width in Centimeters, data is taken from the .csv file, hue is taken from the Species column in the .csv file.

```sh
    sns.scatterplot(x = "sepalLenghtCm", y = "sepalWidthCm", data = data, hue = "Species", palette = ['purple', 'deeppink', 'blueviolet']) 
```
Next, the X-Axis and Y-Axis were labled and the scatter plot was titled.

```sh
    plt.xlabel ('Length in Centimeters')  
    plt.ylabel ('Width in Centimeters')   
    plt.title ('Sepal')
```
Finally, a legend was added to the scatter plot, the .png file is saved automaticaly when the code is run.
```sh
    plt.legend() 
    plt.savefig('Sepal Scatter Plot')
    plt.show()    
```
This process was repeated for the Petal Comparasion scatter plot.

## Scatter Plots
![Sepal Scatter Plot](https://github.com/sarah-fitzgerald/pands-project-2021/blob/17ddd734dca97ba34af52dcee3160b8ad3cce094/Sepal%20Scatter%20Plot.png)

![Petal Scatter Plot](https://github.com/sarah-fitzgerald/pands-project-2021/blob/17ddd734dca97ba34af52dcee3160b8ad3cce094/Petal%20Scatter%20Plot.png)

<!-- Pairplot -->
# Pairplot 
## Pairplot Code

Decided to use a pairplot to the represent multidimensional relationships between Sepal Lenght, Sepal Width, Petal Lenght, Petal Width for each species. After which, the pair plot is saved.

```sh
    sns.pairplot(data, hue = 'Species', palette = ['purple', 'deeppink', 'blueviolet'])
    plt.title ('Iris Pairplot') 
    plt.savefig('Iris Pairplot') 
    plt.show()
```


## Pairplot

![Iris Pairplot](https://github.com/sarah-fitzgerald/pands-project-2021/blob/17ddd734dca97ba34af52dcee3160b8ad3cce094/Petal%20Paitplot.png)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()

<!-- REFERENCES -->
## References:
 #### . https://en.wikipedia.org/wiki/Iris_flower_data_set
 #### . https://archive.ics.uci.edu/ml/datasets/iris
 #### . https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
 #### . https://matplotlib.org
 #### . https://en.wikipedia.org/wiki/Matplotlib
 #### . https://matplotlib.org/stable/tutorials/introductory/pyplot.html#:~:text=pyplot%20is%20a%20collection%20of,the%20plot%20with%20labels%2C%20etc.
 #### . https://en.wikipedia.org/wiki/Pandas_(software)
 #### . https://seaborn.pydata.org
 #### . https://www.shanelynn.ie/python-pandas-read-csv-load-data-from-csv-files/
 #### . https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77
 #### . https://www.geeksforgeeks.org/python-pandas-dataframe-info/#:~:text=Python%20is%20a%20great%20language,concise%20summary%20of%20the%20dataframe
 #### . https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77
 #### . https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
 #### . https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/
 ####  .https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib
 #### . https://stackoverflow.com/questions/22408237/named-colors-in-matplotlib
 #### . https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
 #### . https://www.geeksforgeeks.org/scatterplot-using-seaborn-in-python/
 #### . https://pythonbasics.org/seaborn-scatterplot/
 #### . https://seaborn.pydata.org/tutorial/relational.html
 #### . https://www.geeksforgeeks.org/scatterplot-using-seaborn-in-python/
 #### . https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
