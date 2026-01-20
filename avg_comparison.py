import numpy as np
import pandas as pd
import matplotlib as plt

df = pd.read_csv('data/raw/premier-player-23-24.csv') #Open DataFrame

df['Gls_PerMin'] = (df['Gls'] / (df['90s']))*90 #Calculate goals scored per minute
print(df['Gls_PerMin'])