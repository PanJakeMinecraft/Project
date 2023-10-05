#Region	Users (mm)
#Asia-Pacific	    893
#Europe     	    338
#South America	    289
#North America  	222
#Middle East	    112
#Africa	            96
#Australia    	    22

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data1 = np.array([893,338,289,222,112,96,22])
data_label1 = ["Asia","Europe","South America","North America","Middle east","Africa","Australia"]

plt.title("Instragram Users in region in 2022 ", color="Navy", size=20)
plt.pie(data1, labels = data_label1, autopct='%1.1f%%', shadow=True, startangle=30)
plt.legend()
plt.show()

