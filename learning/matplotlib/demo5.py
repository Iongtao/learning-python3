import matplotlib.pyplot as plt
import numpy as np

values = np.arange(1, 1001)

'''
通过计算得到 纵坐标的值 
'''
plt.scatter(values, [value**2 for value in values], s=10)

plt.axis([0, 1100, 0, 1100000])

plt.show()
