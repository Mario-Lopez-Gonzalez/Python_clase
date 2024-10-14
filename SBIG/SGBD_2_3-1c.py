import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

colors = random.choices(list(mcolors.CSS4_COLORS.values()),k = 6) # k = number of colors
options = ["1", "2", "3", "4", "5", "6"]
count = [5, 15, 20, 10, 8, 2]
plt.bar(options, count, color = colors)
plt.xlabel("Cantidad")
plt.ylabel("Número hijos")
plt.title("SGBD 2_3 1-c")
plt.show()
