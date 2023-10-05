# United States
#App	                Downloads 2021
#TikTok	                94 million
#Instagram	            64 million
#Snapchat	            56 million
#Cash App	            56 million
#Zoom	                52 million
#Facebook Messenger	    51 million#
#Facebook	            47 million
#WhatsApp	            47 million
#YouTube	            47 million

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name = np.array(["Tiktok", "Instragram","Snapchat","Cash App","Zoom","Messenger","Facebook","Whatsapp","Youtube"])
data = np.array([94,64,56,55,52,51,47,46.5,46.2])

plt.title("Most download app in United States", color="Magenta", size=22)
plt.xlabel("Name of an application", color="Orange", size=18)
plt.ylabel("Downloads in million", color="Brown", size=18)

plt.bar(name, data, color=["Yellow","Orange","Salmon"])
plt.legend()
plt.show()

