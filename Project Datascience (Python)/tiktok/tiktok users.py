#TikTok users by region
#Year	South-EastAsia  North America	Europe
#2018	62 million	    28 million		21 million
#2019	130 million	    55 million		52 million
#2020	198 million	    105 million 	98 million

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x1 = [2018,2019,2020]
y1 = [62,130,198]

x2 = [2018,2019,2020]
y2 = [28,55,105]

x3 = [2018,2019,2020]
y3 = [21,52,98]

plt.plot(x1,y1, color = "Orange")
plt.plot(x2,y2, color = "red")
plt.plot(x3,y3, color = "Green")

plt.title("Tiktok Users in 2022", color="Red", size=28)
plt.plot(x1, y1, label="Southeast Asia")
plt.plot(x2, y2, label="North America")
plt.plot(x3, y3, label="Europe")

plt.xlabel("Year", color="blue")
plt.ylabel("Users in region in (millions)", color="blue")
plt.legend()
plt.show()