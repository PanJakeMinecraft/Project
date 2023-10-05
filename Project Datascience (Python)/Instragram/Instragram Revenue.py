import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Year	Revenue ($bn)
#2015	0.5
#2016	1.8
#2017	4.1
#2018	10.3
#2019	19.4
#2020	26.8
#2021	47.6

x = [2015,2016,2017,2018,2019,2020,2021]
y = [0.5,1.8,4.1,10.3,19.4,26.8,47.6]


plt.title("Instragram revenue", color="Purple", size=28)
plt.plot(x,y, color ="Red")
plt.xlabel("Year", color="Blue")
plt.ylabel("Revenue in BILLION dollars", color="Magenta")
plt.grid()
plt.show()
plt.show() 

