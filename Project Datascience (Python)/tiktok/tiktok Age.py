import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# TikTok age demographics
#Under 18	28
#19-29	    35
#30-39	    18
#39+	    19

data = np.array([28,35,18,19])
data_label = ["Under 18", "Between 19-29", "Between 30-39", "Morethan 39"]
data_explode = [0,0.3,0,0]

plt.title("Tiktok user by age", color="Purple", size=25)

plt.pie(data, labels = data_label, explode = data_explode,  autopct='%1.1f%%')
plt.legend()
plt.show()