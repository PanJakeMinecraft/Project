#TikTok cumulative downloads
#Year	Downloads
#2017	130 million
#2018	750 million
#2019	1.5 billion
#2020	2.6 billion
#2021	3.3 billion

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [2017,2018,2019,2020,2021]
y = [130,750,1500,2600,3300]

colors = np.array([0,10,20,30,40,50,60,70,80,90])

plt.scatter(x,y, color="Purple", s=100)
plt.title("Tiktok Cumulative Downloads", color="Red", size=25)
plt.xlabel("Year", color="blue")
plt.ylabel("Downloads in (millions)", color="Blue")
plt.show()
