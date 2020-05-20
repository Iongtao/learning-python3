import matplotlib.pyplot as plt
import numpy as np


'''
np.arange(0, 5, 0.2) arange创建了一个0到5(不包括5)，以0.2为步长的列表 [0,0.2,0.4,...,4.4,4.6,4.8]
'''
t = np.arange(0, 5, 0.2)


'''
参数r--表示红色虚线，bs表示蓝色方块标记，g^表示绿色三角标记
t**2为t的平方 t**3为t的立方 以此类推
'''
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

# 显示图形
plt.show()
