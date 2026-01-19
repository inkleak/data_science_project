import numpy as np
import matplotlib as plt # Importing useful libraries
import pandas as pd
import sklearn as sklearn

df = pd.read_csv("data/raw/premier-player-23-24.csv") # Loading Data Set

def pearson_coeff(x, y, y_name):
    std_x, std_y = np.std(x), np.std(y)
    mean_x, mean_y, mean_xy = np.mean(x), np.mean(y), np.mean(x*y)
    cov_xy = mean_xy - (mean_x*mean_y)
    r = cov_xy / (std_x*std_y)
    print(str(x_search)," vs "+str(y_name)+ ". R = " +str(r)) #Outputs correlation coefficient values

x_search = 'CrdR' #Change this depending on what you want to compare
x = df[x_search] #Selects the appropriate column

for col in df.columns:
    if col!= x_search: #Excluding self-comparison
        y = df[col]
        if pd.api.types.is_numeric_dtype(y): #Makes sure variables are numerical in order for analysis
            pearson_coeff(x,y, col) #Running correlation coefficients 