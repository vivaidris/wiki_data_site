import matplotlib.pyplot as plt
import math
import numpy as np

labels = ["Films and Videogames", "People", "Music", "Sport", "Countries and Politics","Tech/Misc"]
sizes = np.array([19, 12, 8, 5, 4, 2])
explode = [0.2, 0.0, 0.0, 0.0, 0.0, 0.0]
colors = ['#fffb8f', '#ffd48f', '#ffa18c', '#ce0906', '#a50906', '#510906']

plt.pie(sizes, labels=labels, explode=explode, colors=colors)
plt.axis('equal')
plt.show()

