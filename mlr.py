import numpy as np
import matplotlib as plt # Importing useful libraries
import pandas as pd
import sklearn as sklearn

df = pd.read_csv("data/raw/premier-player-23-24.csv") # Loading Data Set

def pearson_coeff(x, y):
    std_x, std_y = np.std(x), np.std(y)
    mean_x, mean_y, mean_xy = np.mean(x), np.mean(y), np.mean(x*y)
    cov_xy = mean_xy - (mean_x*mean_y)
    r = cov_xy / (std_x*std_y)
    print(r)

x = df['Age'] # Select your first variable in here using the table in the Notion file
y = df['90s'] # Select your second variable in here using the table in the Notion file

pearson_coeff(x, y)

