#Gender	    Percentage of users
#Male	        43.2
#Female	        56.8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.array([43.2,56.8])
data_label = ["Male","Female"]
data_explode = [0,0.2]

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.pie(data, labels = data_label, explode= data_explode, autopct='%1.1f%%', shadow="True")
plt.legend()
plt.show()