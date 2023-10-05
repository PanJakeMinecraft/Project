import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Date	Users (mm)
#2015	370
#2016	500
#2017	700
#2018	1000
#2019	1210
#2020	1520
#2021	1890

name = np.array([2015,2016,2017,2018,2019,2020,2021])
data = np.array([370,500,700,1000,1210,1520,1890])

plt.title("Instragram Users", color="Orange", size=28)
colors = np.array(["red","blue","green"])
plt.bar(name, data, color=colors)
plt.xlabel("Year", color="Blue")
plt.ylabel("Users in million", color="black")
plt.legend()
plt.show()