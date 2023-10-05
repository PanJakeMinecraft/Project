#Year	Users (mm)
#2014	35
#2015	50
#2016	80
#2017	150
#2018	200
#2019	300
#2020	400
#2021	500

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x1 = [2014,2015,2016,2017]
y1 =[35,50,80,150]

x2 = [2018,2019,2020,2021]
y2= [200,300,400,500]

plt.title("Telegram users", color="Cyan", size=20)
plt.subplot(1,2,1).set_title("Telegram user in 2014-2017", color="Magenta", size=15) 

plt.plot(x1,y1, marker="o", color="Orange")
plt.subplot(1,2,2).set_title("Telegram users in million from 2018-2021", color="Red", size=15)

plt.plot(x2,y2, marker="o", color="Red")
plt.show()