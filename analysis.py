# Cian Hogan
# Final project, Programming and Scripting Module
# Write a program called analysis.py that:
# • outputs a summary of each variable to a single text file,
# • saves a histogram of each variable to png files, and
# • outputs a scatter plot of each pair of variables.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("iris.csv")

setosa_df = df[df["species"] == "setosa"]
versicolor_df = df[df["species"] == "versicolor"]
virginica_df = df[df["species"] == "virginica"]

dfSum = str(df.describe())
setosaSum = str(setosa_df.describe())
versicolorSum = str(versicolor_df.describe())
virginicaSum = str(virginica_df.describe())

with open("summary.txt", "w+") as f:
	f.write("Total data set summary \n"+dfSum+"\n")
	f.write("\nSetosa Species summary \n"+setosaSum+"\n")
	f.write("\nVersicolor Species summary \n"+versicolorSum+"\n")
	f.write("\nVirginica Species summary \n"+virginicaSum+"\n")



for col in df.columns:
	plt.hist(setosa_df[col],bins=10, color="b", label="Setosa")
	plt.hist(versicolor_df[col],bins=10, color="orange", label="Versicolor")
	plt.hist(virginica_df[col],bins=10, color="g",label="Virginica")
	plt.title(col)
	plt.legend()
	plt.ylabel("Frequency")
	plt.xlabel(col)	
	plt.savefig(col+".png")
	plt.clf()

sns.pairplot(df, hue="species")
plt.show()