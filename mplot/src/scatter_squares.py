
import matplotlib.pyplot as plt 
x_values = list(range(5001))
y_values = [x**3 for x in x_values] 

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14) 
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14) 
plt.scatter(x_values, y_values, c=y_values, edgecolor='none', s=40)
plt.show()
