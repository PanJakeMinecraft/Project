import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Date	Revenue ($bn)
#2010	1.97
#2011	3.71
#2012	5.08
#2013	7.87
#2014	12.46
#2015	17.92
#2016	27.63
#2017	40.65
#2018	55.83
#2019	70.69
#2020	85.96
#2021	117.92

x = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
y = [1.97,3.71,5.08,7.87,12.46,17.92,27.63,40.65,55.83,70.69,85.96,117.92]

plt.title("Facebook Revenue per year", color="Indigo", size=20)
plt.xlabel("Years", color="Red", size="20")
plt.ylabel("Revenue in $billion", color="red", size="20")
plt.plot(x,y, linestyle="dashed", color="brown", marker="o")
plt.grid()
plt.show()
