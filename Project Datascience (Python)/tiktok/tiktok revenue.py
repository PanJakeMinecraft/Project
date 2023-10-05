import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [2017,2018,2019,2020,2021]
y =[63,150,350,1900,4600]


plt.title("Tiktok Revenue", color="Orange", size=28)
plt.plot(x,y, color ="Red")
plt.xlabel("Year", color="Magenta")
plt.ylabel("Revenue in million dollars", color="Magenta")
plt.grid()
plt.show()
plt.show() 