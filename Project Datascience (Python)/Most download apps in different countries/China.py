#App	                 Downloads
#WeChat	                1,005 million
#AliPay	                845 million
#Taobao                 750 million
#Pinduoduo	            740 million
#Douyin	                686 million

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

name = np.array(["Wechat","Alipay","Taobao","Pingduoduo","Douyin"])
data = np.array([1005,845,750,740,686])

plt.title("Most download app in China", color="Magenta", size=22)
plt.xlabel("Name of an application", color="Orange", size=18)
plt.ylabel("Downloads in million", color="Brown", size=18)

plt.bar(name, data, color=["Blue","Green","Gold"])
plt.legend()
plt.show()

