#Region	        Percentage of users
#Asia	                38
#Europe	                27
#Latin America	        21
#MEMA	                 8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.array([38,27,21,8])
data_label = ["Asia","Europe","North/South America", "Middle east"]
data_explode = [0.2,0,0,0]
plt.title("Telegram users by region", color="Green", size=30)
plt.pie(data, labels=data_label, explode=data_explode, autopct='%1.1f%%', shadow=True, startangle=55)
plt.legend()
plt.show()
