#Content	Percentage of posts
#Photos	    35.6
#Videos	    15.1
#Links  	47.2
#Status	    2.1

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.array([35.6,15.1,47.2,2.1])
data_label = ["Photos","Videos","links","Status"]

plt.title("Facebook contents", color="Steelblue", size=20)
plt.pie(data, labels = data_label, autopct='%1.1f%%', shadow=True, startangle=32)
plt.legend()
plt.show()