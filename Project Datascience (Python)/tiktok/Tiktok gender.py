import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Gender	Percentage of users
#Female	60
#Male	40

data = np.array([60,40])
data_label = ["Female", "Male"]
sizes = [215, 130, 245, 210]

plt.title("Gender", color="Purple", size=25)
plt.pie(data, labels=data_label, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.legend()
plt.show()