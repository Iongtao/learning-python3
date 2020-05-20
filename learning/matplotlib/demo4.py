import matplotlib.pyplot as plt

'''
使用scatter绘制散点图
s=10 设置点的大小
'''
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.scatter(x_values, y_values, s=10)

plt.title('title', fontsize=24)

plt.xlabel('xxxxx', fontsize=14)
plt.ylabel('yyyyy', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()