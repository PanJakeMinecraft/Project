import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Device type	    Percentage of users
#Desktop only	            1.7
#Desktop and mobile	        17.3
#Mobile	                    81

name = np.array(["Desktop only","Desktop and mobile","Mobile only"])
data = np.array([1.7,17.3,81])
colors = np.array(["Red","Green","Blue"])

plt.title("Facebook users classify by device", color="Steelblue", size=20)
plt.xlabel("Type of device", color="Magenta")
plt.ylabel("Percentage of device", color="Green")
plt.barh(name, data, color=colors)
plt.legend()
plt.show()