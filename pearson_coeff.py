import numpy as np
import matplotlib.pyplot as plt # Importing useful libraries
import pandas as pd

df = pd.read_csv("data/raw/premier-player-23-24.csv") # Loading Data Set

def pearson_coeff(x, y, y_name):
    std_x, std_y = np.std(x), np.std(y)
    mean_x, mean_y, mean_xy = np.mean(x), np.mean(y), np.mean(x*y)
    cov_xy = mean_xy - (mean_x*mean_y)
    r = cov_xy / (std_x*std_y)
    print(str(x_search)," vs "+str(y_name)+ ". R = " +str(r)) #Outputs correlation coefficient values

def graph(x, y, y_name, x_search):
    save_results_to = 'C:/Projects/project_a/graphs/'
    x_bar, y_bar = np.mean(x), np.mean(y) #Calculating means for x and y
    fig = plt.figure()
    plt.scatter(x, y, s=8, color='black') #Scatter plot chosen
    plt.axvline(x=x_bar, linestyle='--', color='blue', linewidth=1, label='X_Mean'), plt.axhline(y=y_bar, linestyle='--', color ='red', linewidth=1, label='Y_Mean')
    plt.legend()
    plt.xlabel(f'{x_search}') #Labelling
    plt.ylabel(f'{y_name}')
    plt.title(f'Plot of {y_name} against {x_search}')
    plt.savefig(save_results_to + f'{y_name}vs{x_search}.png', dpi=300) #Saves graph to "Graphs" folder

x_search = input('Enter your first variable to compute with.\n') #Change this depending on what you want to compare
#y_search = input('Enter a variable to compare with your chosen x value.\n') #Other variable

x = df[x_search] #Selects the appropriate column

for col in df.columns:
    if col!= x_search: #Excluding self-comparison
        y = df[col]
        if pd.api.types.is_numeric_dtype(y): #Makes sure variables are numerical in order for analysis
            pearson_coeff(x,y, col) #Running correlation coefficients 

for col in df.columns:
    if col!= x_search:
        y = df[col]
        if pd.api.types.is_numeric_dtype(y):
            graph(x, y, col, x_search)


#if y_search in df.columns:
 #   y = df[y_search]
#    graph(x, y, y_search, x_search)
#else:
 #   print("Not in DataFrame")
 #   quit
