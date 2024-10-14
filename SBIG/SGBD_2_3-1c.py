import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

colors = random.choices(list(mcolors.CSS4_COLORS.values()),k = 6) # k = number of colors
options = ["1", "2", "3", "4", "5", "6"]
count = [5, 15, 20, 10, 8, 2]
plt.pie(count, colors = colors, labels = options, autopct = "%0.2f%%")
plt.title("")
plt.show()