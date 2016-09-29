# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:20:19 2016

@author: sxq
"""
'''
Group C&D
'''

print(1)
'''
Search for the IRIS dataset on the internet. You should quickly find the UCI 
Machine Learning repository. Instead of downloading the files, figure out how 
to directly load the files from the internet into Python and add the column 
names using Python code instead of an editor.

'''

import pandas as pd
# we directly import the data from the internet.
# use header = -1 here to remove the header line
mydata = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                     header = -1)
                     
# we define the columns' names due to the data set description
mycolumns = ["sepal length(cm)", "sepal width(cm)", "petal length(cm)", 
             "petal width(cm)", "class"]
# assign the columns' names with the names we defined
             
mydata.columns = mycolumns

#print(mydata)

print(2)
'''
Using Pandas, display the first ten and the last ten rows of the data.
'''
# we directly use the DataFrame.head and DataFrame.tail functions from pandas
# to display the first and the last ten rows of the data
mydata.head(10)
mydata.tail(10)

print(3)
'''
Using Pandas, print simple location statistics (Count, Mean, STD, Min, 25%, 
50%, 75%, MAX). There is a single method call that will accomplish this.
'''
# we use the DataFrame.describe function from pandas to get these simple 
# location statistics.
mydata.describe()

print(4)
'''
Write a function that accepts a list of numbers that represent numbers of bins 
and, using Pandas, plots a histogram for each of the numeric columns at each 
bin size. For example, if I call your function with [10, 50, 100] as bin 
sizes, the function should plot 12 histograms (3 for each numeric variable). 
Group the histograms by the column name.
'''
# we define a function that accepts a list of numbers.

def myhist(list1):

def myhist(list1):
# we define a function that accepts a list of numbers.
# we group the histograms by columns' names
# and then for each bin size we set, print the histograms 
    for col in mycolumns[0:4]: 
        for i in list1: 
            mydata.hist(column = col, bins = i) 
            
# check if we could get 12 histograms(3 for each numeric variable)
myhist([10,50,100])

print(5)
'''
Plot a box plot for each of the numeric column.
'''
# we directly use the DataFrame.plot.box function to plot the boxplot.
mydata.plot.box()

print(6)
'''
Plot a bar chart for the nominal column.
'''
# we plot a bar chart for the nominal column which has the column name "class"
# use value_counts here to compute the frequency of each different class.

mydata["class"].value_counts().plot(kind="bar")





