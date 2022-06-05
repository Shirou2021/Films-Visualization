import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys


# create few visual graphs to best analyze the csv file.
# ideas:

# data frame
df = pd.read_csv('Best_Films.csv', parse_dates = ["Year"], index_col = "Year")
df.describe()

#set the index columndf = df[(df[""])]
df = df[(df["Gross_earning (in millions)"] >= df["Gross_earning (in millions)"].quantile(0.025))
 & (df["Gross_earning (in millions)"] <= df["Gross_earning (in millions)"].quantile(0.975))]

df2 = df[(df["Rating"] >= df["Rating"].quantile(0.025))
 & (df["Rating"] <= df["Rating"].quantile(0.975))]
#df = df.loc[df(df['Year'] >= 1900 & df['Year'] <= 2020)]


def heat_map():
    df_heat = df[(df["Gross_earning (in millions)"] >= df["Gross_earning (in millions)"].quantile(0.025))
 & (df["Gross_earning (in millions)"] <= df["Gross_earning (in millions)"].quantile(0.975)) & (df["Rating"] >= df["Rating"].quantile(0.025))
 & (df["Rating"] <= df["Rating"].quantile(0.975))]

    correlation = df_heat.corr()
    
    mask = np.triu(correlation)
    fig = plt.subplots(figsize=(7,7))
    sns.heatmap(correlation, linewidth = 1, annot = True, square = True, mask = mask, cbar_kws = {'shrink' : .60})
    title = 'Heatmap of Films'
    plt.title(title, fontsize = 13)
    plt.show()
    return 

def line_plot():
    fig, ax = plt.subplots(figsize=(12, 10))
    
    ax.plot(df.index, df['Gross_earning (in millions)'], 'r', linewidth = 1)
    
    plt.xlabel("Year",  fontsize = 15)
    plt.ylabel("Revenue (in millions)", fontsize = 15)
    plt.title("Top 100 films of all time")
    fig.savefig('line_plot.png')
    return fig
    

def bar_graph():
    fig = plt.subplots(figsize=(10, 10))
    sns.barplot(x = "Rating", y = "Films",data= df2.head(10),color= "red", alpha=0.5,label ="Rating")
    plt.xlabel("Rating",  fontsize = 15)
    plt.ylabel("Films", fontsize = 15)
    plt.title("Top 10 films")
    plt.show()
    return 

heat_map()
line_plot()
bar_graph()
