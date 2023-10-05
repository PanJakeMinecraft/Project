# Games mobile                      Downloads
#Subway Surfers:                    191 million
#Roblox:                            182 million
#Bridge Race:                        169 million
#Garena Free Fire - New Age:        154 million
#Among Us:                          152 million

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name = np.array(["Subway Surfers","Roblox","Bridge Race","Freefire","Amongus"])
data = np.array([191,182,169,154,152])

plt.title("Top 5 download mobile games", color="Silver", size=25)
plt.xlabel("Download in million", size=20, color="red")
plt.ylabel("Games", color="red", size=20)

plt.barh(name,data, color=["Blue","orchid","pink","Violet","Purple"])
plt.show()