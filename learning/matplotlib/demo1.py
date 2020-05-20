import matplotlib.pyplot as plt

# 提供一组平方数
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
'''
绘制对应的图形
plt.plot([1,4,9,16,25]) 指定了所绘图形的纵坐标, 横坐标未指定，默认为[0,1,2,3....,n-1]
plt.plot([2,4,6,8,10],[1,4,9,16,25]) 指定了横坐标 list1将和list2一一对应 (2,1),(4,4),(6,9),...,(10, 25)
linewidth=5 指定 线条的宽度为5
'''
plt.plot(input_values, squares, linewidth=5)

'''
设置图表标题
第一个字段为图表标题
fontsize的字体大小为24
'''
plt.title('square numbers',fontsize=24)

'''
给坐标轴加上标签
第一个字段为标签名
fontsize的字体大小为14
'''
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

'''
设置刻度标记的大小
axis="both" 加粗
labelsize=14 设置刻度标签的文字大小
'''
plt.tick_params(axis="both", labelsize=14)
# 显示图形
plt.show()