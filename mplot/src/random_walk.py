# coding:utf-8
from random import choice 
from game_functions import get_number_aliens_x
class RandomWalk(): 
    def __init__(self, num_points=5000): 

        self.num_points = num_points 
    # �������������ʼ��(0, 0) 
        self.x_values = [0] 
        self.y_values = [0]

    def fill_walk(self): 
    #"""��������������������е�""" 
    # ����������ֱ���б�ﵽָ���ĳ���
        while len(self.x_values) < self.num_points:
            # ����ǰ�������Լ����������ǰ���ľ���
            x_step = get_step()
            y_step = get_step() 
 
 # �ܾ�ԭ��̤��
            if x_step == 0 and y_step == 0:   
                continue 
 
 # ������һ�����x��yֵ
            next_x = self.x_values[-1] + x_step 
            next_y = self.y_values[-1] + y_step 
 
            self.x_values.append(next_x) 
            self.y_values.append(next_y)
    
def get_step(switchs='x'):
    if switchs == 'x':
       x_direction = choice([1, -1]) 
       x_distance = choice([0, 1, 2, 3, 4]) 
       return x_direction * x_distance
    else:
       y_direction = choice([1, -1]) 
       y_distance = choice([0, 1, 2, 3, 4]) 
       return y_direction * y_distance 