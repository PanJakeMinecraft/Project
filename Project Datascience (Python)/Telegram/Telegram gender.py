#41.4% female users and 58.6% male users

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.array([41.4,58.6])
data_label =["Female","Male"]

plt.title("Telegram user classify by gender", color="Salmon", size=22)
plt.pie(data, labels=data_label, autopct='%1.1f%%', shadow=True, startangle=55)
plt.legend()
plt.show()

