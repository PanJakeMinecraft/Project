#App	                Downloads 2021
#Netflix	            173 million
#YouTube	            166 million
#Google Play Games	    131 million
#Disney+	            126 million
#Amazon Prime Video	    120 million
#YouTube music	        91 million
#HBO Max	            73 million
#Twitch	                69 million
#Hotstar	            56 million
#Pluto TV	            54 million

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name = np.array(["Netflix","Youtube","Googlegames","Disney+","Amazonvideo","Youtube music","HBO max","Twitch","Hotstar","Pluto TV"])
data = np.array([173,166,131,126,120,91,73,69,56,54])

plt.title("Most popular entertain apps", color="Magenta", size=22)
plt.xlabel("Name of an application", color="Orange", size=18)
plt.ylabel("Downloads in million", color="Blue", size=18)

plt.bar(name, data, color=["Yellow","pink","salmon","red","Brown","Gold","Silver","Cyan"])
plt.show()