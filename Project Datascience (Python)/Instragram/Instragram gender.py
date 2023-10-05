#Gender	Percentage of Users
#Male	    49.2
#Female	    50.8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.array([46.2,50.8])
data_label = ["Male","Female"]
data_explode = [0.1,0]

plt.title("Instragram users classify by gender", color="Indigo", size=20)
plt.pie(data, labels = data_label, explode = data_explode, autopct='%1.1f%%', shadow=True)
plt.legend()
plt.show()