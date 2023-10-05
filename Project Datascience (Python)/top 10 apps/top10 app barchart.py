import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#TikTok: 656 million
#Instagram: 545 million
#Facebook: 416 million
#WhatsApp: 395 million
#Telegram: 329 million
#Snapchat: 327 million
#Zoom: 300 million
#Messenger: 268 million
#CapCut: 255 million
#Spotify: 203 million

name = np.array(["Tiktok","Instragram","Facebook","WhatsApp","Telegram","Snapchat","Zoom","Messenger","Capcut","Spotify"])
data = np.array([656,545,416,395,329,327,300,268,255,203])

plt.barh(name, data, color='Gray')
plt.title("Top 10 most download applications", color="Gold", size=21)
plt.xlabel("Downloads in millions")
plt.ylabel("Applications")
plt.legend()
plt.show()