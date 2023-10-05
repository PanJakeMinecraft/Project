import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Apps = ['Spotify', 'Capcut', 'Messenger',
        'Zoom', 'Snapchat', 'Telegram','whatsapp','Facebook','Instragram','Tiktok']
 
data = [203,255,268,300,327,329,395,416,545,656]
 
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = Apps)

plt.title("Top 10 Applications", color="Green", size=25)
plt.pie(data, labels=Apps, autopct='%1.1f%%')
plt.show() 

plt.show()