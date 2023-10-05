#Date	Revenue ($bn)
#2018	1.3
#2019	2.3
#2020	5.5
#2021	8.7

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.array([2018,2019,2020,2021])
y = ([1.3,2.3,5.5,8.7])

plt.title("Whatsapp revenue in each year", color="Brown", size=20)
plt.plot(x,y, marker="o")
plt.xlabel("Years", color="Red")
plt.ylabel("Revenue in $billion")
plt.show()