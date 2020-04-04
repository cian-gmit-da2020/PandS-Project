# Cian Hogan
# Final project, Programming and Scripting Module
# Write a program called analysis.py that:
# • outputs a summary of each variable to a single text file,
# • saves a histogram of each variable to png files, and
# • outputs a scatter plot of each pair of variables.

# import needed libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# Defining a function for creating the output histograms
# The function takes a number of vars to allow for customisation
def makehist(dict, col_name, bintup, title, fileout):
	plt.style.use('seaborn') # using the seaborn style sheet
	# creating the plot figure fig
	fig = plt.figure()
	# using the grid spec method to create shape needed 
	# for the 1 large hist and 3 smaller hists in figure fig
	gs = gridspec.GridSpec(3, 3, figure=fig)
	# adding first and largest hist
	ax = fig.add_subplot(gs[:2, :])
	ax.hist(dict["Entire Dataset"][col_name], bins=bintup[0], 
	edgecolor="black",color="y", label="Entire Dataset")
	ax.set_title(title)
	# adding next three smaller species hists
	ax1 = fig.add_subplot(gs[2, 0])
	ax1.hist(dict["Setosa"][col_name],bins=bintup[1], 
	edgecolor="black", color="b", label="Setosa")
	ax1.set_title("Setosa")

	ax2 = fig.add_subplot(gs[2, 1])
	ax2.hist(dict["Versicolor"][col_name],bins=bintup[1], 
	edgecolor="black", color="g", label="Versicolor")
	ax2.set_title("Versicolor")

	ax3 = fig.add_subplot(gs[2, 2])
	ax3.hist(dict["Virginica"][col_name],bins=bintup[1], 
	edgecolor="black", color="r",label="Virginica")
	ax3.set_title("Virginica")
	# using the tight_layout method for better spacing of the plots
	fig.tight_layout()
	fig.savefig(fileout) # saving the figures to the file path fileout

# load the iris data csv into a dataframs using pandas
df = pd.read_csv("iris.csv")

# initialise a dataframe for each species type
setosa_df = df[df["species"] == "setosa"]
versicolor_df = df[df["species"] == "versicolor"]
virginica_df = df[df["species"] == "virginica"]

# create the a brief summary of each dataframe using the describe method
dfSum = str(df.describe())
setosaSum = str(setosa_df.describe())
versicolorSum = str(versicolor_df.describe())
virginicaSum = str(virginica_df.describe())

# write each summary datafram to the file summary.txt
with open("summary.txt", "w+") as f:
	f.write("All Species Summary \n"+dfSum+"\n")
	f.write("\nSetosa Species Summary \n"+setosaSum+"\n")
	f.write("\nVersicolor Species Summary \n"+versicolorSum+"\n")
	f.write("\nVirginica Species Summary \n"+virginicaSum+"\n")

# create a dictionary with a label as key and dataframe as value
df_dict = {"Entire Dataset": df, "Setosa": setosa_df, 
"Virginica": virginica_df, "Versicolor": versicolor_df}

# using the function makehist() create a histogram 
# for each variable for each dataframe
makehist(df_dict, "petal_length", (15, 10), 
"Petal Length Distribution All Species", "Petal Length Histogram.png")
makehist(df_dict, "petal_width", (15, 10), 
"Petal Width Distribution All Species", "Petal Width Histogram.png")
makehist(df_dict, "sepal_width", (15, 10), 
"Sepal Width Distribution All Species", "Sepal Width Histogram.png")
makehist(df_dict, "sepal_length", (15, 10), 
"Sepal Length Distribution All Species", "Sepal Length Histogram.png")

# using the seaborn pairplot method to plot 
# a scatter plot for each pair of variables in the data
scat = sns.pairplot(df, hue="species")
plt.savefig("Scatter Pairs.png")