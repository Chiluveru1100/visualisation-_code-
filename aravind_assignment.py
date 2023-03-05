import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_excel('gasoline_df.xlsx') # importing the data

data = pd.read_csv('cars.csv') # importing the data

# function for line plot
def line_plot(x,y,label):
    plt.plot(x,y)
    plt.xlabel(x.name)  #  X-axis label
    plt.ylabel(y.name)  #  Y-axis label
    plt.title(label)   #   title
    plt.show()
    
# function for box plot
def box_plot(x):
    props=dict(markerfacecolor = 'red',marker = 'o',markeredgecolor = 'green')
    plt.boxplot(x,flierprops= props,patch_artist= True)
    plt.xlabel(x.name) #  X-axis label
    plt.title('CARS')
    plt.show()
    
# function for histogram
def histogram(x):
    plt.hist(x, color = 'orange') 
    plt.xlabel(x.name) #  X-axis label
    plt.title('CARS')  # Title
    plt.show()
    
line_plot(df['date'],df['gasoline'],'Gasoline Consumption [2013 - 2019]') # Line_plot for gasoline consumption

box_plot(data['HP']) # Visualization of horse power of cars with the help of boxplot

histogram(data['SP']) # visualization of selling price of cars using Histogram
