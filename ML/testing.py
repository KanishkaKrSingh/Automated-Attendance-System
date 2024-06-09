import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2, 5, 6, 7, 9, 12, 16, 19])

a, b = np.polyfit(x, y, 1)

plt.scatter(x, y, color='purple')

plt.plot(x, a*x+b, color='steelblue', linestyle='--', linewidth=2)

plt.text(1, 17, 'y = ' '{:.2f}'.format(b) + ' {:.2f}'.format(a) + 'x', size=14)

plt.show()