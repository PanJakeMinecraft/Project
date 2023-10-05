#Age	Percentage of Users
#13-17	    7
#18-24	    30
#25-34	    33
#35-44	    16
#45-54	    8
#55-64	    4
#65+	    2

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

days = [0.0,0.0,0.1]

x1 =[2]
x2 = [4]
x3 =[7]
x4 =[8]
x5 =[16]
x6 =[30]
x7 =[33]

plt.plot([],[],color='Blue', label='Morethan 65 years old', linewidth=5)
plt.plot([],[],color='Green', label='Age 55-64 years old', linewidth=5)
plt.plot([],[],color='red', label='Age 13-17', linewidth=5)
plt.plot([],[],color='Cyan', label='Age 45-54', linewidth=5)
plt.plot([],[],color='Pink', label='Age 35-44', linewidth=5)
plt.plot([],[],color='Yellow', label='Age 18-24', linewidth=5)
plt.plot([],[],color='Orange', label='Age 25-34', linewidth=5)


plt.title("Instragram Users by age", color="Purple", size=28)
plt.stackplot(days, x1,x2,x3,x4,x5,x6,x7, colors=['Blue','Green','Red','Cyan','Pink',"yellow","Orange"])

plt.xlabel('')
plt.ylabel('Percentage of users by age')
plt.legend()
plt.show()
