import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #Importing libraries
import seaborn as sns

def heatmap(data):
    save_results_to = 'C:/Projects/project_a/graphs/important/' #Directory for saving figure
    fig = plt.figure(figsize=(25,20)) #Large fig size necessary to plot all together
    data = data.select_dtypes(include='number') 
    correlation_matrix = data.corr() #Calculating correlation matrix
    ax = sns.heatmap(correlation_matrix, cmap="Blues", annot = True,  center=0)
    plt.title('Correlation Matrix Heatmap') #Title
    plt.savefig(save_results_to + f'VariablesHeatmap.png', dpi = 300)

df = pd.read_csv('data/raw/premier-player-23-24.csv') #Our data set

heatmap(df) #Calling function