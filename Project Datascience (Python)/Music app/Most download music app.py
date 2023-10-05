# most-downloaded music and audio apps for 2021:
#Spotify:               203 million
#Resso:                 85 million
#YouTube Music:          79 million
#StarMaker:             76 million
#SoundCloud:            52 million

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name = np.array(["Spotify","Resso","YouTube music","StarMaker", "Soundcloud"])
data=np.array([203,85,79,76,52])

plt.title("Top 5 download music apps", color="Deepskyblue", size=20)
plt.xlabel("Name of the application", size=18, color="Salmon")
plt.ylabel("Downloads in million", size=18, color="salmon")

plt.bar(name, data, color=["Red","Salmon","Magenta","Pink","Yellow","gold"])
plt.show()