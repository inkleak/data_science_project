import numpy as np
import matplotlib as plt # Importing useful libraries
import pandas as pd

df = pd.read_csv("premier_league_1819.csv") # Loading Data Set

df = df.drop(df.columns[[2,3,4,5,270,269,268]], axis = 1) #Droppi

print(df.columns.tolist())