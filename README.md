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


# 1. Introduction
The Iris flower data set, commonly known as Fischer’s Iris data set, is a collection of 150 samples of Iris flowers including measurements of the flower's **petal length, petal width, sepal length and sepal width** in centimeters. The flowers are further classified by their species type **Setosa, Virginica and Versicolor**. There are 50 samples of each species within the dataset.

<img src=https://raw.githubusercontent.com/RubixML/Iris/master/docs/images/iris-species.png>

The data set itself was first introduced by the British statistician and biologist Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems*[1]. The data was originally collected by the American Botanist Edgar Anderson and is sometimes called Anderson’s Iris data set.

Fisher in his paper used the dataset to perform a discriminant analysis in an attempt to find *“What linear function of the four measurements will maximize the ratio of the difference between the specific means to the standard deviations within species”*[1]. 
Linear discriminate analysis or Fishers discriminant method is used across scientific fields to separate 2 or more classes of objects based on a combination of features.[2] In this case the 3 Species are separated based on the measurements for petal length, petal width, sepal length and sepal width.

The dataset is widely used today as a training data for statistical analysis. The data provides a suitable beginners problem in machine learning[3]. While Iris Setosa can be easily distinguished from the other two species separating Iris Versicolor and Iris Virginica the later two species are more difficult to separate as there is more overlap between values.

# 2.[analysis.py]( https://github.com/cian-gmit-da2020/PandS-Project/blob/master/analysis.py)
analysis.py is a [Python 3](https://www.python.org/) script which takes the [Iris dataset from a CSV file]( https://github.com/cian-gmit-da2020/PandS-Project/blob/master/iris.csv) and performs the following 3 tasks on the data:

1.	Outputs the summary of each variable to a .txt file.
2.	Saves a histogram of each variable to .png files.
3.	Saves a scatter plot of each variable to .png files.

The script requires a number of external libraries, listed below, that are not included in standard python and need to be imported. This is done at the beginning of the programme. All of these libraries come as standard in the [anaconda distribution]( https://www.anaconda.com/) but can alternatively be installed with a package manager such as [pip](https://pypi.org/project/pip/) or [conda](https://docs.conda.io/en/latest/). 

Required Libraries
1.	[Numpy](https://numpy.org/)
2.	[Pandas]( https://pandas.pydata.org/)
3.	[Matplotlib’s pyplot module](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html)
4.	[Matplotlib’s gridspec module](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.gridspec.GridSpec.html)
5.	[Seaborn](https://seaborn.pydata.org/)

# 3. Defining the Function makehist()
The next block of code after the package imports is the definition of the programme function **makehist()** which will be called later in the programme to produce the output histograms for each variable in the Iris Dataset. *In previous drafts of analysis.py the histograms were built using a loop through the  variables, this was changed to a defined function to improve readability, reusability and to allow more customisation of each variables histogram[4]*. 

The goal of makehist() is to take a number of inputs and to produce 4 axes histograms plot on a single figure and save the output to a .png file. The main plot would take up 2/3 of the figure while the other 3 subplots would share the final 1/3. The main plot would be the entire dataset and one smaller plot for each species. The function takes 5 input variables **dict, col_name, bintup, title and fileout**.

**dict**
The variable dict will be a dictionary where the key/value pair is a label for the entire dataset and each variable along with its corresponding pandas dataframe. 

**col_name**
The variable col_name takes a string value that corresponds to a column in the iris dataset eg petal_length, petal_width.

**bintup**
Bintup is a tuple of integers. The first integer bintup[0] is used as the bin size for the larger histogram and the second value bintup[1] is sued for the smaller  histograms bin size.

**title**
title takes a string value and uses that as the title for the whole histogram figure

**fileout**
fileout takes a string filepath and saves the histogram to that file path.

The function begins by setting up the plot figure and the axes grid. First the plot style is set to the “Seaborn” style sheet using plt.style.use()[5]. The function initialises the plot figure **fig** using plt.figure()[6]. Next matplotlib’s gridspec method is used to initialised as object **gs** in the figure fig with layout of 3 rows and 3 columns[7][8].

Now that the setup is done the program can starts creating the individual histogram axes. The first plot **ax** is set to take up the first 2 rows and all 3 columns using the gs object. A histogram is plotted to ax using ax.hist() using the “Entire Dataset” key to access the full iris data dataframe held as the dictionary value. The col_name variable is used to plot a specific variable within the dataframe, the first element of bintup is used to set the amount of bins, the colour is set to yellow, edgecolour for the bins is added and a label for the histogram is added. Finally a title title is assigned to the axes with ax.set_title().

The next 3 axes **ax1, ax2 and ax3** are created in a very similar way to ax. The differences being a different dictionary key is used to access a different dataframe value, a different gridspec value is used to assign the smaller axes to the bottom row in a separate column each, a different colour is used for each axes and the second element of the bintup tuple is used for the bin value. Each axes is titled for the species it represents.

Finally the function ends with two more methods. fig.tight_layout() is used to improve the spacing between the 4 axes [9]. Finally the function ends with a call of fig.savefig() and uses the **fileout** filepath variable to write the image to the specified filename.

**Example**
Later in the programme the function is called as follows:

<pre><code>makehist(df_dict, "petal_length", (15, 10), "Petal Length Distribution All Species", "Petal Length Histogram.png")</code></pre>

And creates the following output file "Petal Length Histogram.png":

<img src=https://github.com/cian-gmit-da2020/PandS-Project/blob/master/Petal%20Length%20Histogram.png>

# 4. [Pandas Dataframes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

Pandas is python tool designed for high-level data manipulation. It is based on the Numpy package and uses a built-in data structure called a pandas DataFrame which is designed for handling tabular data like the data in iris.csv[10]. 

First the iris.csv data is loaded into the DataFrame object **df** using the pandas.read_csv() method[11]. 3 more DataFrames are initialised from df by assigning a new value to the result of checking that the value in column “species” is equal to either the setosa, virginica or versicolour species.

The pandas describe() method is used on each of the DataFrames to calculate general descriptive statistics for the given data. This includes count, minimum and maximum values, mean, standard deviation and 25th, 50th and 75th percentiles [12].

A file object **f** is created using a **with open** code block. The block opens a file *summary.txt* in write mode. Using a file object in this way ensures the file is closed when you are finished writing to it[13]. The summary statistics generated earlier are then written to the file along with some headings and with added newline characters to separate the different data.

# 5. Calling makehist()



References
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




