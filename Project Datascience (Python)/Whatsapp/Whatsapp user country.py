#Date	        Users (mm)
#India	            390
#Brazil	            148
#Indonesia	        112
#United States	    98
#Philippines	    88
#Mexico	            77
#Turkey	            56
#Egypt	            55
#Germany	        44
#Nigeria	        40
#Italy	            35

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

name = np.array(["India","Brazil","Indonesia","United States","Philipines","Mexico","Turkey","Egypt","Germany","Nigeria","Italy"])
data = np.array([390,148,112,98,88,77,56,55,44,40,35])

plt.title("Whatsapp users in 2021 in different countries in 2022", color="Green", size=20)
colors = np.array(["red","Navy","Brown","Silver","Blue","Pink","gold","black","pink"])
plt.xlabel("Users in million", color="Red")
plt.ylabel("Countries", color="Navy")
plt.barh(name,data,color=colors)
plt.show()