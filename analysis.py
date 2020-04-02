# Cian Hogan
# Final project, Programming and Scripting Module
# Write a program called analysis.py that:
# • outputs a summary of each variable to a single text file,
# • saves a histogram of each variable to png files, and
# • outputs a scatter plot of each pair of variables.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

def makehist(dict, col_name, title, fileout):
	fig = plt.figure()
	gs = gridspec.GridSpec(3, 3, figure=fig)
	ax = fig.add_subplot(gs[:2, :])
	ax.hist(dict["Entire Dataset"][col_name], bins=15, edgecolor="black",color="purple", label="Entire Dataset")
	ax.set_title(title)
	ax1 = fig.add_subplot(gs[2, 0])
	ax1.hist(dict["Setosa"][col_name],bins=10, edgecolor="black", color="b", label="Setosa")
	ax1.set_title("Setosa ")
	ax2 = fig.add_subplot(gs[2, 1])
	ax2.hist(dict["Versicolor"][col_name],bins=10, edgecolor="black", color="orange", label="Versicolor")
	ax2.set_title("Versicolor ")
	ax3 = fig.add_subplot(gs[2, 2])
	ax3.hist(dict["Virginica"][col_name],bins=10, edgecolor="black", color="g",label="Virginica")
	ax3.set_title("Virginica ")
	fig.tight_layout()
	fig.savefig(fileout)

df = pd.read_csv("iris.csv")

setosa_df = df[df["species"] == "setosa"]
versicolor_df = df[df["species"] == "versicolor"]
virginica_df = df[df["species"] == "virginica"]

dfSum = str(df.describe())
setosaSum = str(setosa_df.describe())
versicolorSum = str(versicolor_df.describe())
virginicaSum = str(virginica_df.describe())

df_dict = {"Entire Dataset": df, "Setosa": setosa_df, 
		"Virginica": virginica_df, "Versicolor": versicolor_df}

with open("summary.txt", "w+") as f:
	f.write("Total data set summary \n"+dfSum+"\n")
	f.write("\nSetosa Species summary \n"+setosaSum+"\n")
	f.write("\nVersicolor Species summary \n"+versicolorSum+"\n")
	f.write("\nVirginica Species summary \n"+virginicaSum+"\n")

makehist(df_dict, "petal_length", "Petal Length Distribution", "Petal Length Histogram.png")
makehist(df_dict, "petal_width", "Petal Width Distribution", "Petal Width Histogram.png")
makehist(df_dict, "sepal_width", "Sepal Width Distribution", "Sepal Width Histogram.png")
makehist(df_dict, "sepal_length", "Sepal Length Distribution", "Sepal Length Histogram.png")


sns.pairplot(df, hue="species")
plt.show()