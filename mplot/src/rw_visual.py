import matplotlib.pyplot as plt 
import pygal
from random_walk import RandomWalk 
rw = RandomWalk(5000) 
rw.fill_walk() 
point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=1)
#plt.scatter(0, 0, c='green', edgecolors='none', s=100)
#plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
#plt.axes().get_xaxis().set_visible(False) 
#plt.axes().get_yaxis().set_visible(False)
plt.show()