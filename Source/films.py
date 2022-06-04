from turtle import up
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import sys

# create few visual graphs to best analyze the csv file.
# ideas:

# data frame
df = pd.read_csv('Best_Films.csv', parse_dates = ["Year"], index_col = "Year")
df.describe()
# set the index column 
#df = df.set_index('Year')
#set the index columndf = df[(df[""])]
df = df[(df["Gross_earning (in millions)"] >= df["Gross_earning (in millions)"].quantile(0.025))
 & (df["Gross_earning (in millions)"] <= df["Gross_earning (in millions)"].quantile(0.975))]

# def heat_map():
#     corr = df.corr(method = "pearson")
#     fig = plt.subplots(figsize=(10,10))
#     #sn.heatmap(corr, linewidth = 1, annot = True), mask = np.triu(corr))
#     fig.savefig('heapmap.png')
#     return 

def line_plot():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.plot(df.index, df['Gross_earning (in millions)'], 'r', linewidth = 1)
    plt.xlabel("Year", fontsize = 15)
    plt.ylabel("Revenue (in millions)", fontsize = 15)
    plt.title("Top 100 films of all time")
    fig.savefig('line_plot.png')
    return fig
    

# def bar_graph():
    # parsing and make a top 10 films of all time.
    # df.loc[df['rating'] > 9.5] ...
#     return  

# Must finish by 6/4/22. 
# So, plan:
# 1. wake up
# 2. breakfast.
# 3. Quick exercise 
# 4. Prepare for lunch items and start working on it. No nap torrmow.


line_plot()
# bar_graph()
# heat_map()