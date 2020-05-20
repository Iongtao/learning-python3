import matplotlib.pyplot as plt


'''
[1,2,3,4], [1,4,9,16]指定了所绘图形的横坐标和纵坐标
“ro” r代表red o代表使用圆形标记 而不是 线
'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')


'''
plt.axis([0, 6, 0, 20]) 设定了横坐标与纵坐标范围
'''
plt.axis([0, 6, 0, 20])

# 显示图形
plt.show()
