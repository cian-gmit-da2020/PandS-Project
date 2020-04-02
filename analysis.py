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

#dataFrameList = [df, setosa_df, versicolor_df, virginica_df]

for col in df.columns:
	fig = plt.figure()
	gs = gridspec.GridSpec(3, 3, figure=fig)
	ax = fig.add_subplot(gs[:2, :])
	ax.hist(df[col],bins=10, edgecolor="black",color="purple", label="Total "+col+" distribution")
	ax1 = fig.add_subplot(gs[2, 0])
	ax1.hist(setosa_df[col],bins=10, edgecolor="black", color="b", label="Setosa")
	ax2 = fig.add_subplot(gs[2, 1])
	ax2.hist(versicolor_df[col],bins=10, edgecolor="black", color="orange", label="Versicolor")
	ax3 = fig.add_subplot(gs[2, 2])
	ax3.hist(virginica_df[col],bins=10, edgecolor="black", color="g",label="Virginica")
	fig.suptitle(str(col)+" Total Distribution")
	# fig.ylabel("Frequency")
	# fig.xlabel(col)	
	fig.savefig(col+".png")
	#plt.clf()

sns.pairplot(df, hue="species")
plt.show()