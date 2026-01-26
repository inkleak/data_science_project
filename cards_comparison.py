import pandas as pd   
import numpy as np
import matplotlib.pyplot as plt

#Libraries added, code below:

df = pd.read_csv("data/raw/premier-player-23-24.csv") # Loading Data Set

def card_comparison(position, yellow, red):
    save_results_to = 'C:/Projects/project_a/graphs/important/' #Setting directory for important graphs
    fig = plt.figure(figsize=(15,6)) #Graph was being squished, had to change the figure size
    plt.ylabel('Total cards')
    plt.title('Breakdown of yellow and red cards by position')
    plt.bar(position, yellow, color = 'yellow', label='Yellow Cards') # Titles, labels etc
    plt.bar(position, red, color = 'red', label = 'Red Cards')
    plt.legend()
    plt.savefig(save_results_to + 'cards_comparison.png', dpi=300) #Saving figure

positions = ['Goalkeeper','Defender', 'Defender/Midfielder', 'Defender/Forward', 'Midfielder', 'Midfielder/Forward', 'Forward'] #List of positions, for tidier x-axis in the plot
yellow_cards = [] #Empty lists to add card data into
red_cards = []

gk = df[df["Pos"] == 'GK']
yellows_gk = np.sum(gk['CrdY'])
reds_gk = np.sum(gk['CrdR'])
yellow_cards.append(yellows_gk) #Adding card data per position.
red_cards.append(reds_gk)

defenders = df[df["Pos"] == 'DF']
yellows_df = np.sum(defenders['CrdY'])
reds_df = np.sum(defenders['CrdR'])
yellow_cards.append(yellows_df)                                         #This whole process is likely VERY inefficient. I will look to condense this into as few lines of code as possible.
red_cards.append(reds_df)

defenders_midfielders = df[df['Pos'].isin(['DF,MF', 'MF,DF'])]
yellows_dfmf = np.sum(defenders_midfielders['CrdY'])
reds_dfmf = np.sum(defenders_midfielders['CrdR'])
yellow_cards.append(yellows_dfmf)
red_cards.append(reds_dfmf)

defenders_forwards = df[df['Pos'].isin(['DF,FW', 'FW,DF'])]
yellows_dffw = np.sum(defenders_forwards['CrdY'])
reds_dffw = np.sum(defenders_forwards['CrdR'])
yellow_cards.append(yellows_dffw)
red_cards.append(reds_dffw)

midfielders = df[df['Pos']=='MF']
yellows_mf = np.sum(midfielders['CrdY'])
reds_mf = np.sum(midfielders['CrdR'])
yellow_cards.append(yellows_mf)
red_cards.append(reds_mf)

midfielders_forward = df[df['Pos'].isin(['MF,FW', 'FW,MF'])]
yellows_mffw = np.sum(midfielders_forward['CrdY'])
reds_mffw=np.sum(midfielders_forward['CrdR'])
yellow_cards.append(yellows_mffw)
red_cards.append(reds_mffw)

forward = df[df['Pos']=='FW']
yellows_fw=np.sum(forward['CrdY'])
reds_fw =np.sum(forward['CrdR'])
yellow_cards.append(yellows_fw)
red_cards.append(reds_fw)


card_comparison(positions, yellow_cards, red_cards) #calling functioin