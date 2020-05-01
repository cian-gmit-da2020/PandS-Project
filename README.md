# PandS-Project
# Cian Hogan
# HIGHER DIPLOMA IN SCIENCE IN COMPUTING (DATA ANALYTICS)
# Programming and Scripting Module, Final Project

Table of contents
1. Introduction
2. analysis.py
3. Defining the Function makehist() 
4. Pandas Dataframes
5. Calling makehist()
6. Seaborn pairplot
7. Conclusion
8. References

# 1. Introduction

The Iris flower data set, commonly known as Fischer’s Iris data set, is a collection of 150 samples of Iris flowers including measurements of the flower's **petal length, petal width, sepal length and sepal width** in centimeters. The flowers are further classified by their species type **Setosa, Virginica and Versicolor**. There are 50 samples of each species within the dataset.

<img src=https://raw.githubusercontent.com/RubixML/Iris/master/docs/images/iris-species.png>

The data set itself was most famously used by the British statistician and biologist Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems* [1]. The data was however originally collected by the American Botanist Edgar Anderson and is sometimes called Anderson’s Iris data set.

Fisher, in his paper, used the dataset to perform a discriminant analysis in an attempt to find *“What linear function of the four measurements will maximize the ratio of the difference between the specific means to the standard deviations within species”* [1]. 
Linear discriminate analysis or Fishers discriminant method is used across scientific fields to separate 2 or more classes of objects based on a combination of features [2]. In this case the 3 Species are separated based on the measurements for petal length, petal width, sepal length and sepal width.

The dataset is widely used today as a training dataset for statistical analysis. The data provides a suitable beginners problem in machine learning [3]. This is because the dataset itself is relatively small but the classification problem it presents is challenging enough for students.

# 2. [analysis.py]( https://github.com/cian-gmit-da2020/PandS-Project/blob/master/analysis.py)

analysis.py is a [Python 3](https://www.python.org/) script which takes the [Iris dataset from a CSV file]( https://github.com/cian-gmit-da2020/PandS-Project/blob/master/iris.csv) and performs the following 3 tasks on the data:

1.	Outputs the summary of each variable to a .txt file.
2.	Saves a histogram of each variable to .png files.
3.	Saves a scatter plot of each variable to .png files.

The script requires a number of external libraries, listed below, that are not included in the standard python distribution and need to be imported. This is done at the beginning of the program. All of these libraries come as standard in the [anaconda distribution]( https://www.anaconda.com/) but can alternatively be installed with a package manager such as [pip](https://pypi.org/project/pip/) or [conda](https://docs.conda.io/en/latest/). 

Required Libraries
1.	[Pandas]( https://pandas.pydata.org/)
2.	[Matplotlib’s pyplot module](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html)
3.	[Matplotlib’s gridspec module](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.gridspec.GridSpec.html)
4.	[Seaborn](https://seaborn.pydata.org/)

# 3. Defining the Function makehist()

The next block of code after the package imports is the definition of the program function **makehist()**. This function will be called later in the program to produce the output histograms for each variable in the Iris Dataset. *In previous drafts of analysis.py the histograms were built using a loop through the  variables, this was changed to a defined function to improve readability, reusability and to allow more customisation of each variables histogram [4]*. 

The goal of makehist() is to take a number of inputs and to produce 4 axes histogram plots on a single figure and save the output to a .png file. The main plot would take up 2/3 of the figure while the other 3 subplots would share the final 1/3. The main plot would be the entire dataset and one smaller plot for each species. The function takes 5 input variables **dict, col_name, bintup, title and fileout**.

**dict** -
The variable dict will be a dictionary where the key/value pair is a label for the entire dataset and each variable along with its corresponding pandas dataframe. 

**col_name** -
The variable col_name takes a string value that corresponds to a column in the iris dataset eg petal_length, petal_width.

**bintup** -
Bintup is a tuple of integers. The first integer **bintup[0]** is used as the bin size for the larger histogram and the second value **bintup[1]** is used for the smaller  histograms bin size.

**title** - 
title takes a string value and uses that string as the title for the whole histogram figure

**fileout** -
fileout takes a string filepath and saves the histogram to that file path.

The function begins by setting up the plot figure and the axes grid. First the plot style is set to the “Seaborn” style sheet using plt.style.use() [5]. The function initialises the plot figure **fig** using plt.figure() [6]. Next matplotlib’s gridspec method is used to initialise an object **gs** in the figure fig with layout of 3 rows and 3 columns [7][8].

Now that the setup is done the program can start creating the individual histogram axes. The first plot **ax** is set to take up the first 2 rows and all 3 columns using the gs object. A histogram is plotted to ax using ax.hist() using the “Entire Dataset” key to access the full iris dataset dataframe held as the dictionary value. 

The col_name variable is used to plot a specific variable within the dataframe, the first element of bintup is used to set the amount of bins, the colour is set to yellow, edgecolour for the bins is added and a label for the histogram is added. Finally a title is assigned to the axes with ax.set_title().

The next 3 axes **ax1, ax2 and ax3** are created in a very similar way to ax. The differences being a different dictionary key is used to access a different dataframe value, a different gridspec value is used to assign the smaller axes to the bottom row in a separate column each, a different colour is used for each axes and the second element of the bintup tuple is used for the bin value. Each axes is titled for the species it represents.

Finally the function ends with two more methods. fig.tight_layout() is used to improve the spacing between the 4 axes [9]. The function ends with a call of fig.savefig() and uses the **fileout** filepath variable to write the image to the specified filename.

**Example**
Later in the program the function is called as follows:

<pre><code>makehist(df_dict, "petal_length", (15, 10), "Petal Length Distribution All Species", "Petal Length Histogram.png")</code></pre>

And creates the following output file "[Petal Length Histogram.png](https://github.com/cian-gmit-da2020/PandS-Project/blob/master/Petal%20Length%20Histogram.png)":

<img src=https://github.com/cian-gmit-da2020/PandS-Project/blob/master/Petal%20Length%20Histogram.png width="400">

# 4. [Pandas Dataframes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

Pandas is a python tool designed for high-level data manipulation. It is based on the [Numpy package](https://numpy.org/) and uses a built-in data structure called a Pandas DataFrame which is designed for handling tabular data like the data in iris.csv [10]. 

First the iris.csv data is loaded into the DataFrame object **df** using the pandas.read_csv() method [11]. 3 more DataFrames are initialised from df by assigning a new value to the result of checking that the value in column “species” is equal to either the setosa, virginica or versicolour species.

The pandas describe() method is used on each of the DataFrames to calculate general descriptive statistics for the given data. This includes count, minimum and maximum values, mean, standard deviation and 25th, 50th and 75th percentiles [12]. Additionally another DataFrame object **avg** is created using two pandas methods, **[groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) and [mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html)**. groupby allows us to set a variable to separate the data on, in this case "species". mean() calculates the mean for each variable of the groups. The result is a DataFrame of 3 rows and 4 columns containing the mean values for each variable for each given species.

A file object **f** is created using a **with open** code block. The block opens a file *[summary.txt](https://github.com/cian-gmit-da2020/PandS-Project/blob/master/summary.txt)* in write mode. Using a file object in this way ensures the file is closed when you are finished writing to it [13]. <pre><code>with open("summary.txt", "w+") as f:</code></pre>
The summary statistics generated earlier are then written to the file along with some headings and with added newline characters to separate the different data.

# 5. Calling makehist()

Before calling the makehist() function defined earlier, first we have to create a dictionary of DataFrames. We do this by assigning **df_dict** to a dictionary object with the following key/value pairs.

| Key             | Value         |
|-----------------|---------------|
|”Entire Dataset” | df            |
|”Setosa”         | setosa_df     |
|”Virginica”      | virginica_df  |
|“Versicolor”	  | versicolor_df |

Now that the dictionary is defined the makehist() function is called four separate times. Once for each variable in the dataset. The second parameter in the function specifies which variable we are looking to process in each DataFrame in df_dict. The bintup value is set to 15 for the larger plot and 10 for the 3 smaller plots. The plot titles and file path variables are also assigned in the function. *As the file path entered here does not included an absolute path, the file will be written to the current directory. A full path could be specified if needed*.

# 6. [Seaborn pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html)
<pre><code>sns.pairplot(df, hue="species")
plt.savefig("Scatter Pairs.png")</code></pre>

The final part of the program involves using the Seaborn external library to create a scatter plot of each pair of variables. Seaborn is a data visualization library that is based on matplotlib. It provides a high-level user interface for drawing statistical graphics [14]. The Seaborn method used here is **pairplot()**. pairplot by default will create a grid of axes that plots each numerical variable in the data across a single row in the y-axis and a single column in the x-axis [15].

The program calls pairplot with only two parameters **df** and **hue="species"**. df is the variable which contains the data to be plotted in the form of a Pandas DataFrame. This alone would plot a scatter plot of each pair of variables and the diagonal axes would plot a histogram of the distribution of the data. The parameter **hue** gives us the option to separate the data based on some specified categorical variable, in this case we use the species variable. Using the hue option changes the default diagonal axes to a KDE (Kernal Desity Estimate) of the given variable. A KDE is a representation of the distribution of data on a smoother curve which unlike histograms doesnt used defined bins [16]. The final command in the script is to save the figure generated by pairplot to the file **[Scatter Pairs.png](https://github.com/cian-gmit-da2020/PandS-Project/blob/master/Scatter%20Pairs.png)**. 


# 7. Conclusion

The results generated by analysis.py allow us to perform an [exploratory analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis) on the iris data. Each of the three outputs, the summary, the histograms and the scatter plots highlight different features of the data and when used together provide a decent picture of the general attributes of the studied iris flowers.

## summary.txt
The data in summary.txt shows some basic statistics for the data and separates them out based on species type which allows for some comparison between the 3 types. From the data here we can easily see that the setosa measurements vary significantly from the other two species. They are smaller across all 4 measurements but see the largest difference in petal length and petal width (fig.1). 

While the virginica species tends to be larger than versicolor on average across all measurements they are not as easily separated as Setosa. Looking at the results of the summary of both species we can see there is significant overlap in the [interquartile ranges](https://en.wikipedia.org/wiki/Interquartile_range) [18] of the two species. This poses a difficult challenge if we were given an unclassified flower and had to identify what species it was based it's measurements alone as many virginica and versicolor flowers would share similar values.

**fig.1** Species Means
|Species       | sepal_length | sepal_width | petal_length | petal_width |                                                        
|--------------|--------------|-------------|--------------|-------------|
|setosa        |   5.006      |  3.418      |   1.464      |  0.244      |
|versicolor    |   5.936      |  2.770      |   4.260      |  1.326      |
|virginica     |   6.588      |  2.974      |   5.552      |  2.026      |

## Histograms

In general the variables present with a [Multimodal Distribution](https://en.wikipedia.org/wiki/Multimodal_distribution) [19] where there are more than one peak. The exception here is seen below in the Sepal Width Histogram which shows a [Normal Distribution](https://en.wikipedia.org/wiki/Normal_distribution) [20]. This multi-peak can be explained by looking at the individual species in the sub-graphs. In the Petal Length plot, for example, we can see a peak between 1 and 2 which corresponds exactly with the Setosa Species where all the measurements fall between these values. The individual species have much more normal distorbutions on their own than the entire dataset presents.

| fig.2 Histograms   |  |
|---------|-------|
|Petal Length| Petal Width  |
| <img src=https://github.com/cian-gmit-da2020/PandS-Project/blob/master/Petal%20Length%20Histogram.png width="400"> | <img src=https://github.com/cian-gmit-da2020/PandS-Project/blob/master/Petal%20Width%20Histogram.png width="400"> |
|Sepal Length |Sepal Width |
| <img src=https://github.com/cian-gmit-da2020/PandS-Project/blob/master/Sepal%20Length%20Histogram.png width="400"> | <img src=https://github.com/cian-gmit-da2020/PandS-Project/blob/master/Sepal%20Width%20Histogram.png width="400"> |

## Scatter Pairs

One of the benefits of using pairplot to plot all the axes together in a single grid as opposed to in individual files is that it is very easy to view and compare the plots side-by-side and see which variables more noticeably separate the species from one another. It is possible to see from the image in fig.3 below that the setosa species is easily separated from the other two in almost all the axes.

The only variable pair where the three species are closely clustered is sepal_length vs sepal_width. If we look at the diagonal KDE representing sepal width we can see a lot of overlap between the species which suggest that it would be difficult to distinguish between the species on this variable measurement alone.

If we look again at the relationship between Versicolor and Virginica Species we can again see that in general Virginica tend to be larger than their Versicolor counterparts. However there is a lack of clear separation between the variables and in the case of sepal length vs sepal width the species are almost indistinguishable.

**fig.3** Scatter Plots

<img src="https://github.com/cian-gmit-da2020/PandS-Project/blob/master/Scatter%20Pairs.png?raw=true" width=550>

## Final Thoughts

From the results of the analysis above there are 3 main points we can takeaway about the Iris data.

1. The Setosa Species can be separated from other 2 species on the basic analysis done here. They tend to be on average significantly smaller on 3 of the four measurements and when a scatter plot of any pair of variables, except sepal length vs sepal width, can be easily separated from the other species.
2. The Virginica Species on average tend to be larger across all measurements than the Versicolor. However there is significant overlap between the two species and they are not easily separated on the plots created here. 
3. If we wanted to classify iris flowers without knowing their species it is not possible to distinguish between Virginica and Versicolor based on this analysis alone. Further more complex analysis of the relationships between all four variables is required to see if such a classification problem could be solved.


# 8. References
1. https://digital.library.adelaide.edu.au/dspace/bitstream/2440/15227/1/138.pdf
2. https://en.wikipedia.org/wiki/Linear_discriminant_analysis
3. https://en.wikipedia.org/wiki/Iris_flower_data_set
4. https://realpython.com/defining-your-own-python-function/#the-importance-of-python-functions
5. https://matplotlib.org/tutorials/introductory/customizing.html
6. https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html
7. https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.gridspec.GridSpec.html
8. https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/gridspec_multicolumn.html#sphx-glr-gallery-subplots-axes-and-figures-gridspec-multicolumn-py
9. https://matplotlib.org/3.2.1/tutorials/intermediate/tight_layout_guide.html
10. https://www.learnpython.org/en/Pandas_Basics
11. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
12. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
13. https://docs.python.org/3/tutorial/inputoutput.html
14. https://seaborn.pydata.org/
15. https://seaborn.pydata.org/generated/seaborn.pairplot.html
16. https://medium.com/@dcomp/histograms-and-kernels-density-estimates-a2c41eb08de3
17. https://en.wikipedia.org/wiki/Exploratory_data_analysis
18. https://en.wikipedia.org/wiki/Interquartile_range
19. https://en.wikipedia.org/wiki/Multimodal_distribution
20. https://en.wikipedia.org/wiki/Normal_distribution
