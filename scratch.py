# def 4Hist(dfList, col):
# 	ax1, ax2, ax3, ax4 = dfList

# 	fig, (ax1, ax2, ax3, ax4) = plt.subplots(2, 2)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

df = pd.read_csv("iris.csv")

setosa_df = df[df["species"] == "setosa"]
versicolor_df = df[df["species"] == "versicolor"]
virginica_df = df[df["species"] == "virginica"]

df_dict = {"Entire Dataset": df, "Setosa": setosa_df, 
		"Virginica": virginica_df, "Versicolor": versicolor_df}

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

makehist(df_dict, "petal_length", "Petal Length Distribution", "Petal Length Histogram.png")
input()

# for col in df.columns:
# 	fig = plt.figure()
# 	gs = gridspec.GridSpec(3, 3, figure=fig)
# 	ax = fig.add_subplot(gs[:2, :])
# 	ax.hist(df[col],bins=10, edgecolor="black",color="purple", label="Total "+col+" distribution")
# 	ax1 = fig.add_subplot(gs[2, 0])
# 	ax1.hist(setosa_df[col],bins=10, edgecolor="black", color="b", label="Setosa")
# 	ax2 = fig.add_subplot(gs[2, 1])
# 	ax2.hist(versicolor_df[col],bins=10, edgecolor="black", color="orange", label="Versicolor")
# 	ax3 = fig.add_subplot(gs[2, 2])
# 	ax3.hist(virginica_df[col],bins=10, edgecolor="black", color="g",label="Virginica")
# 	fig.suptitle(str(col)+" Total Distribution")
# 	# fig.ylabel("Frequency")
# 	# fig.xlabel(col)	
# 	fig.savefig(col+".png")
# 	#plt.clf()

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
	fig.tight_layout()
	fig.legend()
	# fig.ylabel("Frequency")
	# fig.xlabel(col)	
	fig.savefig(col+".png")
	#plt.clf()