#Date	Users (mm)
#2012	103
#2013	213
#2014	409
#2015	719
#2016	1076
#2017	1323
#2018	1560
#2019	1813
#2020	2102
#2021	2289

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x1 =[2012,2013,2014,2015,2016]
y1 =[103,213,409,719,1076]

x2 = [2017,2018,2019,2020,2021]
y2 =[1323,1560,1813,2102,2289]

plt.title("Whatsapp users in each year", color="Firebrick", size=20)
plt.xlabel("Years", color="Navy")
plt.ylabel("Users in million", color="Navy")
plt.scatter(x1,y1)
plt.scatter(x2,y2) 
plt.legend()
plt.show()