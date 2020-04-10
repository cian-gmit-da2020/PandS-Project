# Cian Hogan
# Final project, Programming and Scripting Module
# Write a program called analysis.py that:
# • outputs a summary of each variable to a single text file,
# • saves a histogram of each variable to png files, and
# • outputs a scatter plot of each pair of variables.

# import needed libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# Defining a function for creating the output histograms
# The function takes a number of vars to allow for customisation
def makehist(dict, col_name, bintup, title, fileout):
	plt.style.use('seaborn') # using the seaborn style sheet
	# Creating the plot figure fig
	fig = plt.figure()
	# Using the grid spec method to create shape needed 
	# For the 1 large hist and 3 smaller hists in figure fig
	gs = gridspec.GridSpec(3, 3, figure=fig)
	# Adding first and largest hist
	ax = fig.add_subplot(gs[:2, :])
	ax.hist(dict["Entire Dataset"][col_name], bins=bintup[0], 
	edgecolor="black",color="y", label="Entire Dataset")
	ax.set_title(title)
	# Adding next three smaller species hists
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
	# Using the tight_layout method for better spacing of the plots
	fig.tight_layout()
	fig.savefig(fileout) # saving the figures to the file path fileout

# Load the iris data csv into a dataframe using pandas
df = pd.read_csv("iris.csv")

# Initialise a dataframe for each species type
setosa_df = df[df["species"] == "setosa"]
versicolor_df = df[df["species"] == "versicolor"]
virginica_df = df[df["species"] == "virginica"]

# Create the a brief summary of each dataframe using the describe method
dfSum = str(df.describe())
setosaSum = str(setosa_df.describe())
versicolorSum = str(versicolor_df.describe())
virginicaSum = str(virginica_df.describe())

# Calculating means by species
avg = df.groupby("species").mean()

# Write each summary dataframe to the file summary.txt
with open("summary.txt", "w+") as f: 
	f.write("Mean values by Species\n"+str(avg)+"\n")
	f.write("\nAll Species Summary \n"+dfSum+"\n")
	f.write("\nSetosa Species Summary \n"+setosaSum+"\n")
	f.write("\nVersicolor Species Summary \n"+versicolorSum+"\n")
	f.write("\nVirginica Species Summary \n"+virginicaSum+"\n")
	

# Create a dictionary with a label as key and dataframe as value
df_dict = {"Entire Dataset": df, "Setosa": setosa_df, 
"Virginica": virginica_df, "Versicolor": versicolor_df}

# Using the function makehist() create a histogram 
# For each variable for each dataframe
makehist(df_dict, "petal_length", (15, 10), 
"Petal Length Distribution All Species", "Petal Length Histogram.png")
makehist(df_dict, "petal_width", (15, 10), 
"Petal Width Distribution All Species", "Petal Width Histogram.png")
makehist(df_dict, "sepal_width", (15, 10), 
"Sepal Width Distribution All Species", "Sepal Width Histogram.png")
makehist(df_dict, "sepal_length", (15, 10), 
"Sepal Length Distribution All Species", "Sepal Length Histogram.png")

# Using the seaborn pairplot method to plot 
# a scatter plot for each pair of variables in the data
sns.pairplot(df, hue="species")
plt.savefig("Scatter Pairs.png")