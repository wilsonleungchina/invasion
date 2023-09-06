#coding:utf-8
import pygal
from die import Die
# ����һ��D6 

die = Die() 
# ���������ӣ���������洢��һ���б���
results = [] 
#for roll_num in range(100): 
#    result = die.roll()
#    results.append(result) 

results=[(die.roll() + die.roll())for roll_number in range(1000)]
print(results)
# 分析结果
frequencies = [] 
#for value in range(1, die.num_sides+1): 
#    frequency = results.count(value) 
#    frequencies.append(frequency) 
frequencies=[results.count(value) for value in range(2,die.num_sides*2+1)]
 
# 对结果进行可视化
hist = pygal.Bar() 
hist.title = "Results of rolling one D6 1000 times." 
hist.x_labels = ['2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16'] 
hist.x_title = "Result" 
hist.y_title = "Frequency of Result" 
hist.add('D6', frequencies) 
hist.render_to_file('die_visual.svg')