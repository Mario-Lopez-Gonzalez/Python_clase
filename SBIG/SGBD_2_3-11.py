import matplotlib.pyplot as plt

data = [9,12,6,11,19,5,8,13,2,8,5,12,0,9,4,15,18,10,6,16]
plt.hist(data, bins = 4, range = (0, 20), color = "#ff85b0", edgecolor = "k")
plt.show()