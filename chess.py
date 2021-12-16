# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 02:29:39 2021

@author: 1229290416
"""

import matplotlib.pyplot as plt


class Bin():
    def __init__(self, x, y, player, code, name):
        self.x_coordinate = x
        self.y_coordinate = y
        self.color = '#000000'
        self.side = player
        self.code = code
        self.name = name
        
    def get_coordinates(self):
        return [self.x_coordinate, self.y_coordinate]
    
    def forward(self):
        if self.side == 'B':
            self.y_coordinate = min(self.y_coordinate + 2, 9)
            
        else: 
            self.y_coordinate = max(self.y_coordinate - 2, -9)
                
    def left(self):
        if self.side == 'B':
            if self.y_coordinate > 0:
                self.x_coordinate = max(self.x_coordinate - 2, -8)
                
            else:
                self.x_coordinate = self.x_coordinate
            
        else: 
            if self.y_coordinate < 0:
                self.x_coordinate = min(self.x_coordinate + 2, 8)   
            
            else:
                self.x_coordinate = self.x_coordinate
                
    def right(self):
        if self.side == 'B':
            if self.y_coordinate > 0:
                self.x_coordinate = min(self.x_coordinate + 2, 8)
                
            else:
                self.x_coordinate = self.x_coordinate
            
        else: 
            if self.y_coordinate < 0:
                self.x_coordinate = max(self.x_coordinate - 2, -8)   
            
            else:
                self.x_coordinate = self.x_coordinate
        

class Jv():
    def __init__(self, x, y, player, code, name):
        self.x_coordinate = x
        self.y_coordinate = y
        self.color = '#6F304A'
        self.side = player
        self.code = code
        self.name = name
    
    def get_coordinates(self):
        return [self.x_coordinate, self.y_coordinate]
    
    def forward(self, a):
        if self.side == 'B':
            self.y_coordinate = min(self.y_coordinate + 2*a, 9)
            
        else: 
            self.y_coordinate = max(self.y_coordinate - 2*a, -9)
            
    def backward(self, a):
        if self.side == 'B':
            self.y_coordinate = max(self.y_coordinate - 2*a, -9)
            
        else: 
            self.y_coordinate = min(self.y_coordinate + 2*a, 9)
            
    def left(self, a):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 2*a, -8)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 2*a, 8)
            
    def right(self, a):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 2*a, 8)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 2*a, -8)
    
    
    
class Ma():
    def __init__(self, x, y, player, code, name):
        self.x_coordinate = x
        self.y_coordinate = y
        self.color = '#0000FF'
        self.side = player
        self.code = code
        self.name = name
    
    def get_coordinates(self):
        return [self.x_coordinate, self.y_coordinate]
    
    def right_up(self):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 4, 8)
            self.y_coordinate = min(self.y_coordinate + 2, 9)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 4, -8)
            self.y_coordinate = max(self.y_coordinate - 2, -9)
    
    def right_down(self):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 4, 8)
            self.y_coordinate = max(self.y_coordinate - 2, -9)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 4, -8)
            self.y_coordinate = min(self.y_coordinate + 2, 9)
            
    def left_up(self):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 4, -8)
            self.y_coordinate = min(self.y_coordinate + 2, 9)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 4, 8)
            self.y_coordinate = max(self.y_coordinate - 2, -9)
            
    def left_down(self):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 4, -8)
            self.y_coordinate = max(self.y_coordinate - 2, -9)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 4, 8)
            self.y_coordinate = min(self.y_coordinate + 2, 9)
    
    def up_right(self):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 2, 8)
            self.y_coordinate = min(self.y_coordinate + 4, 9)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 2, -8)
            self.y_coordinate = max(self.y_coordinate - 4, -9)
    
    def up_left(self):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 2, -8)
            self.y_coordinate = min(self.y_coordinate + 4, 9)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 2, 8)
            self.y_coordinate = max(self.y_coordinate - 4, -9)
    
    def down_right(self):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 2, 8)
            self.y_coordinate = max(self.y_coordinate - 4, -9)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 2, -8)
            self.y_coordinate = min(self.y_coordinate + 4, 9)
    
    def down_left(self):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 2, -8)
            self.y_coordinate = max(self.y_coordinate - 4, -9)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 2, 8)
            self.y_coordinate = min(self.y_coordinate + 4, 9)


class Xiang():
    def __init__(self, x, y, player, code, name):
        self.x_coordinate = x
        self.y_coordinate = y
        self.color = '#FF0000'
        self.side = player
        self.code = code
        self.name = name
    
    def get_coordinates(self):
        return [self.x_coordinate, self.y_coordinate]
    
    def right_up(self):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 4, 8)
            self.y_coordinate = min(self.y_coordinate + 4, -1)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 4, -8)
            self.y_coordinate = max(self.y_coordinate - 4, 1)
    
    def right_down(self):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 4, 8)
            self.y_coordinate = max(self.y_coordinate - 4, -9)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 4, -8)
            self.y_coordinate = min(self.y_coordinate + 4, 9)
            
    def left_up(self):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 4, -8)
            self.y_coordinate = min(self.y_coordinate + 4, -1)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 4, 8)
            self.y_coordinate = max(self.y_coordinate - 4, 1)
            
    def left_down(self):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 4, -8)
            self.y_coordinate = max(self.y_coordinate - 2, -9)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 4, 8)
            self.y_coordinate = min(self.y_coordinate + 2, 9)


class Shi():
    def __init__(self, x, y, player, code, name):
        self.x_coordinate = x
        self.y_coordinate = y
        self.color = '#FFAA00'
        self.side = player
        self.code = code
        self.name = name
    
    def get_coordinates(self):
        return [self.x_coordinate, self.y_coordinate]
    
    def right_up(self):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 2, 2)
            self.y_coordinate = min(self.y_coordinate + 2, -5)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 2, -2)
            self.y_coordinate = max(self.y_coordinate - 2, 5)
    
    def right_down(self):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 2, 2)
            self.y_coordinate = max(self.y_coordinate - 2, -9)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 2, -2)
            self.y_coordinate = min(self.y_coordinate + 2, 9)
            
    def left_up(self):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 2, -2)
            self.y_coordinate = min(self.y_coordinate + 2, -5)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 2, 2)
            self.y_coordinate = max(self.y_coordinate - 2, 5)
            
    def left_down(self):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 2, -2)
            self.y_coordinate = max(self.y_coordinate - 2, -9)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 2, 2)
            self.y_coordinate = min(self.y_coordinate + 2, 9)
    
    


class Jiang():
    def __init__(self, x, y, player, code, name):
        self.x_coordinate = x
        self.y_coordinate = y
        self.color = '#00FFFF'
        self.side = player
        self.code = code
        self.name = name
    
    def get_coordinates(self):
        return [self.x_coordinate, self.y_coordinate]
    
    def forward(self):
        if self.side == 'B':
            self.y_coordinate = min(self.y_coordinate + 2, -5)
            
        else: 
            self.y_coordinate = max(self.y_coordinate - 2, 5)
            
    def backward(self):
        if self.side == 'B':
            self.y_coordinate = max(self.y_coordinate - 2, -9)
            
        else: 
            self.y_coordinate = min(self.y_coordinate + 2, 9)
            
    def left(self):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 2, -2)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 2, 2)
            
    def right(self):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 2, 2)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 2, -2)





class Pao():
    def __init__(self, x, y, player, code, name):
        self.x_coordinate = x
        self.y_coordinate = y
        self.color = '#FF00FF'
        self.side = player
        self.code = code
        self.name = name
    
    def get_coordinates(self):
        return [self.x_coordinate, self.y_coordinate]
    
    def forward(self, a):
        if self.side == 'B':
            self.y_coordinate = min(self.y_coordinate + 2*a, 9)
            
        else: 
            self.y_coordinate = max(self.y_coordinate - 2*a, -9)
            
    def backward(self, a):
        if self.side == 'B':
            self.y_coordinate = max(self.y_coordinate - 2*a, -9)
            
        else: 
            self.y_coordinate = min(self.y_coordinate + 2*a, 9)
            
    def left(self, a):
        if self.side == 'B':
            self.x_coordinate = max(self.x_coordinate - 2*a, -8)
            
        else: 
            self.x_coordinate = min(self.x_coordinate + 2*a, 8)
            
    def right(self, a):
        if self.side == 'B':
            self.x_coordinate = min(self.x_coordinate + 2*a, 8)
            
        else: 
            self.x_coordinate = max(self.x_coordinate - 2*a, -8)



class game_board():
    def __init__(self):
        #Black player
        self.black_bin1 = Bin(-8, -3, 'B', 1, 'Zu1')
        self.black_bin2 = Bin(-4, -3, 'B', 2, 'Zu2')
        self.black_bin3 = Bin(-0, -3, 'B', 3, 'Zu3')
        self.black_bin4 = Bin(4, -3, 'B', 4, 'Zu4')
        self.black_bin5 = Bin(8, -3, 'B', 5, 'Zu5')
        
        self.black_pao1 = Pao(-6, -5, 'B', 1, 'Pao1')
        self.black_pao2 = Pao(6, -5, 'B', 2, 'Pao2')
        
        self.black_jv1 = Jv(-8, -9, 'B', 1, 'Jv1')
        self.black_jv2 = Jv(8, -9, 'B', 2, 'Jv2')
        
        self.black_ma1 = Ma(-6, -9, 'B', 1, 'Ma1')
        self.black_ma2 = Ma(6, -9, 'B', 2, 'Ma2')
        
        self.black_xiang1 = Xiang(-4, -9, 'B', 1, 'Xiang1')
        self.black_xiang2 = Xiang(4, -9, 'B', 2, 'Xiang2')
        
        self.black_shi1 = Shi(-2, -9, 'B', 1, 'Shi1')
        self.black_shi2 = Shi(2, -9, 'B', 2, 'Shi2')
        
        self.black_jiang = Jiang(0, -9, 'B', 1, 'Jiang')
        
        #Red player
        self.red_bin1 = Bin(8, 3, 'R', 1, 'Bing1')
        self.red_bin2 = Bin(4, 3, 'R', 2, 'Bing2')
        self.red_bin3 = Bin(0, 3, 'R', 3, 'Bing3')
        self.red_bin4 = Bin(-4, 3, 'R', 4, 'Bing4')
        self.red_bin5 = Bin(-8, 3, 'R', 5, 'Bing5')
        
        self.red_pao1 = Pao(6, 5, 'R', 1, 'Pao1')
        self.red_pao2 = Pao(-6, 5, 'R', 2, 'Pao2')
        
        self.red_jv1 = Jv(8, 9, 'R', 1, 'Jv1')
        self.red_jv2 = Jv(-8, 9, 'R', 2, 'Jv2')
        
        self.red_ma1 = Ma(6, 9, 'R', 1, 'Ma1')
        self.red_ma2 = Ma(-6, 9, 'R', 2, 'Ma2')
        
        self.red_xiang1 = Xiang(4, 9, 'R', 1, 'Xiang1')
        self.red_xiang2 = Xiang(-4, 9, 'R', 2, 'Xiang2')
        
        self.red_shi1 = Shi(2, 9, 'R', 1, 'Shi1')
        self.red_shi2 = Shi(-2, 9, 'R', 2, 'Shi2')
        
        self.red_jiang = Jiang(0, 9, 'R', 1, 'Shuai')
        
    
        self.red = [self.red_bin1, self.red_bin2, self.red_bin3, self.red_bin4,
                    self.red_bin5,
        
                    self.red_pao1, self.red_pao2,
        
                    self.red_jv1, self.red_jv2,
        
                    self.red_ma1, self.red_ma2,
        
                    self.red_xiang1, self.red_xiang2,
        
                    self.red_shi1, self.red_shi2,
        
                    self.red_jiang]
        
        self.black = [self.black_bin1, self.black_bin2, self.black_bin3,
                      self.black_bin4, self.black_bin5,
        
                      self.black_pao1, self.black_pao2,
        
                      self.black_jv1, self.black_jv2,
        
                      self.black_ma1, self.black_ma2,
        
                      self.black_xiang1, self.black_xiang2,
        
                      self.black_shi1, self.black_shi2,
        
                      self.black_jiang]
        
        self.counter = 0

    def draw(self):
        for i in range(-8, 9, 2):
            plt.plot([i, i], [-9, 9], color = '#000000', linewidth=0.5)
            
        for i in range(-9, 10, 2):
            plt.plot([-8, 8], [i, i], color = '#000000', linewidth=0.5)
            
        plt.text(-5, 0, 'Chu', color='#000000', 
                     horizontalalignment='center', 
                     verticalalignment = 'center', fontsize=10)
        plt.text(-3, 0, 'River', color='#000000', 
                     horizontalalignment='center', 
                     verticalalignment = 'center', fontsize=10)
        
        plt.text(3, 0, 'Han', color='#000000', 
                     horizontalalignment='center', 
                     verticalalignment = 'center', fontsize=10)
        plt.text(5, 0, 'Boundary', color='#000000', 
                     horizontalalignment='center', 
                     verticalalignment = 'center', fontsize=10)
            
        for i in self.red :
            [x, y] = i.get_coordinates()
            plt.plot([x], [y], 's', color = i.color)
            plt.text(x, y, str(i.code), color='#FFFFFF', 
                     horizontalalignment='center', 
                     verticalalignment = 'center', fontsize=7)
                
        for i in self.black :
            [x, y] = i.get_coordinates()
            plt.plot([x], [y], 'o', color = i.color)
            plt.text(x, y, str(i.code), color='#FFFFFF', 
                     horizontalalignment='center', 
                     verticalalignment = 'center', fontsize=7)
        
        plt.xlim(-8.5, 8.5)
        plt.ylim(-9.5, 9.5)
        plt.show()
        
    def replace_by(self, a, b):
        b.x_coordinate = a.x_coordinate
        b.y_coordinate = a.y_coordinate
        if a in self.black:
            self.black.remove(a)
            
        elif a in self.red:
            self.red.remove(a)
            
    
    def possible_position_for_ma(self, ma):
        
        occupied_by_red = [i.get_coordinates() for i in self.red]
        occupied_by_black = [i.get_coordinates() for i in self.black]
        
        [x, y] = ma.get_coordinates()
        
        original_possible_positions = [[x + 4, y + 2], [x + 4, y - 2], 
                                       [x + 2, y + 4], [x - 2, y + 4], 
                                       [x - 4, y + 2], [x - 4, y - 2], 
                                       [x + 2, y - 4], [x - 2, y - 4] 
            ]
        
        eye_of_ma = [[x + 2, y],  
                     [x, y + 2], 
                     [x - 2, y], 
                     [x, y - 2]
                     ]
        
        delet_positions = []
        for i in range(0, 4, 1):
            if (eye_of_ma[i] in occupied_by_black or
                eye_of_ma[i] in occupied_by_red):
                first = original_possible_positions[2*i]
                second = original_possible_positions[2*i + 1]
                delet_positions.append(first)
                delet_positions.append(second)
              
        for i in delet_positions:
            original_possible_positions.remove(i)
        
        delet_positions = []
        for i in original_possible_positions:
            if ma.side == 'B':
                if i in occupied_by_black:
                    delet_positions.append(i)
                    
            if ma.side == 'R':
                if i in occupied_by_red:
                    delet_positions.append(i)
                
            if abs(i[0]) > 8 or abs(i[1]) > 9:
                delet_positions.append(i)
        
        for i in delet_positions:
            original_possible_positions.remove(i)
            
            
        return original_possible_positions
        
    def possible_position_for_jv(self, jv):
        occupied_by_red = [i.get_coordinates() for i in self.red]
        occupied_by_black = [i.get_coordinates() for i in self.black]
        
        [x, y] = jv.get_coordinates()
            
        possible_positions_h = []
        j = 1
        while ([x - 2*j, y] not in occupied_by_red and
               [x - 2*j, y] not in occupied_by_black and 
               (abs(x - 2 * j) <= 8 and abs(y) <= 9)):
            possible_positions_h.append([x - 2 * j, y])
            j = j + 1
        
        if jv.side == 'B':
            if [x - 2*j, y] in occupied_by_red:
                possible_positions_h.append([x - 2 * j, y])
                
        if jv.side == 'R':
            if [x - 2*j, y] in occupied_by_black:
                possible_positions_h.append([x - 2 * j, y])
        
        j = 1
        while ([x + 2*j, y] not in occupied_by_red and
               [x + 2*j, y] not in occupied_by_black and 
               (abs(x + 2 * j) <= 8 and abs(y) <= 9)):
            possible_positions_h.append([x + 2 * j, y])
            j = j + 1
        
        if jv.side == 'B':
            if [x + 2*j, y] in occupied_by_red:
                possible_positions_h.append([x + 2 * j, y])
                
        if jv.side == 'R':
            if [x + 2*j, y] in occupied_by_black:
                possible_positions_h.append([x + 2 * j, y])
        
        possible_positions_v = []
        
        k = 1
        while ([x, y - 2 * k] not in occupied_by_red and
               [x, y - 2 * k] not in occupied_by_black and 
               (abs(x) <= 8 and abs(y - 2 * k) <= 9)):
            possible_positions_v.append([x, y - 2 * k])
            k = k + 1
        
        if jv.side == 'B':
            if [x, y - 2 * k] in occupied_by_red:
                possible_positions_v.append([x, y - 2 * k])
                
        if jv.side == 'R':
            if [x, y - 2 * k] in occupied_by_black:
                possible_positions_v.append([x, y - 2 * k])
        
        k = 1
        while ([x, y + 2 * k] not in occupied_by_red and
               [x, y + 2 * k] not in occupied_by_black and 
               (abs(x) <= 8 and abs(y + 2 * k) <= 9)):
            possible_positions_v.append([x, y + 2 * k])
            k = k + 1
        
        if jv.side == 'B':
            if [x, y + 2 * k] in occupied_by_red:
                possible_positions_v.append([x, y + 2 * k])
                
        if jv.side == 'R':
            if [x, y + 2 * k] in occupied_by_black:
                possible_positions_v.append([x, y + 2 * k])
        
        return (possible_positions_h + possible_positions_v)
    
    
    def possible_position_for_pao(self, pao):
        occupied_by_red = [i.get_coordinates() for i in self.red]
        occupied_by_black = [i.get_coordinates() for i in self.black]
        
        [x, y] = pao.get_coordinates()
            
        possible_positions_h = []
        j = 1
        while ([x - 2*j, y] not in occupied_by_red and
               [x - 2*j, y] not in occupied_by_black and 
               (abs(x - 2 * j) <= 8 and abs(y) <= 9)):
            possible_positions_h.append([x - 2 * j, y])
            j = j + 1
        
        def p(f, g, s, h, a, b):
            if pao.side == s:
                if ([x - 2*f, y- 2 * g] in occupied_by_red or
                    [x - 2*f, y - 2 * g] in occupied_by_black):
                    f = f + a
                    g = g + b
                    while ([x - 2 * f, y - 2 * g] not in occupied_by_red and
                           [x - 2 * f, y - 2 * g] not in occupied_by_black and 
                           (abs(x - 2 * f) <= 8 and abs(y - 2 * g) <= 9)):
                    
                        f = f + a
                        g = g + b
                    if s == 'B':
                        if [x - 2 * f, y - 2 * g] in occupied_by_red:
                            h.append([x - 2 * f, y - 2 * g])
                    if s == 'R':
                        if [x - 2 * f, y - 2 * g] in occupied_by_black:
                            h.append([x - 2 * f, y - 2 * g])
        
        p(j, 0, 'B', possible_positions_h, 1, 0)
        p(j, 0, 'R', possible_positions_h, 1, 0)    

        
        j = 1
        while ([x + 2*j, y] not in occupied_by_red and
               [x + 2*j, y] not in occupied_by_black and 
               (abs(x + 2 * j) <= 8 and abs(y) <= 9)):
            possible_positions_h.append([x + 2 * j, y])
            j = j + 1
        
        p(-j, 0, 'B', possible_positions_h, -1, 0)
        p(-j, 0, 'R', possible_positions_h, -1, 0) 
        possible_positions_v = []
        
        k = 1
        while ([x, y - 2 * k] not in occupied_by_red and
               [x, y - 2 * k] not in occupied_by_black and 
               (abs(x) <= 8 and abs(y - 2 * k) <= 9)):
            possible_positions_v.append([x, y - 2 * k])
            k = k + 1
        
        p(0, k, 'B', possible_positions_v, 0, 1)
        p(0, k, 'R', possible_positions_v, 0, 1)
        
        k = 1
        while ([x, y + 2 * k] not in occupied_by_red and
               [x, y + 2 * k] not in occupied_by_black and 
               (abs(x) <= 8 and abs(y + 2 * k) <= 9)):
            possible_positions_v.append([x, y + 2 * k])
            k = k + 1

        p(0, -k, 'B', possible_positions_v, 0, -1)
        p(0, -k, 'R', possible_positions_v, 0, -1)        
        
        return (possible_positions_h + possible_positions_v)
        
        
    def possible_position_for_xiang(self, xiang):
        occupied_by_red = [i.get_coordinates() for i in self.red]
        occupied_by_black = [i.get_coordinates() for i in self.black]
        
        [x, y] = xiang.get_coordinates()
        possible_positions = [[x + 4, y + 4], [x + 4, y - 4], 
                              [x - 4, y - 4], [x - 4, y + 4]]
        
        eyes = [[x + 2, y + 2], [x + 2, y - 2], 
                              [x - 2, y - 2], [x - 2, y + 2]]
        
        delet = []
        for i in range(0, 4, 1):
            if eyes[i] in occupied_by_black or eyes[i] in occupied_by_red:
                delet.append(possible_positions[i])
                
        for j in delet:
            possible_positions.remove(j)
                
        delet = []
        for i in possible_positions:
            if xiang.side == 'B':
                if i in occupied_by_black or (
                        abs(i[0]) > 8 or abs(i[1] + 5) > 4):
                    delet.append(i)
                    
            if xiang.side == 'R':
                if i in occupied_by_red or (
                        abs(i[0]) > 8 or abs(i[1] - 5) > 4):
                    delet.append(i)
                    
        
        for j in delet:
            possible_positions.remove(j)
        
        return possible_positions


    
    def possible_position_for_shi(self, shi):
        
        occupied_by_red = [i.get_coordinates() for i in self.red]
        occupied_by_black = [i.get_coordinates() for i in self.black]
        
        [x, y] = shi.get_coordinates()
        possible_positions = [[x + 2, y + 2], [x + 2, y - 2], 
                              [x - 2, y - 2], [x - 2, y + 2]]
        
        delet = []
        for i in possible_positions:
            if shi.side == 'B':
                if i in occupied_by_black or (
                        abs(i[0]) > 2 or abs(i[1] + 7) > 2):
                    delet.append(i)
                    
            if shi.side == 'R':
                if i in occupied_by_red or (
                        abs(i[0]) > 2 or abs(i[1] - 7) > 2):
                    delet.append(i)
                    
        for j in delet:
            possible_positions.remove(j)
        
        return possible_positions
        
        pass
    
    
    def possible_position_for_jiang(self, jiang):
        
        occupied_by_red = [i.get_coordinates() for i in self.red]
        occupied_by_black = [i.get_coordinates() for i in self.black]
        
        [x, y] = jiang.get_coordinates()
        possible_positions = [[x + 2, y], [x - 2, y], 
                              [x, y - 2], [x, y + 2]]
        
        delet = []
        for i in possible_positions:
            if jiang.side == 'B':
                if i in occupied_by_black or (
                        abs(i[0]) > 2 or abs(i[1] + 7) > 2):
                    delet.append(i)
                    
            if jiang.side == 'R':
                if i in occupied_by_red or (
                        abs(i[0]) > 2 or abs(i[1] - 7) > 2):
                    delet.append(i)
                    
        for j in delet:
            possible_positions.remove(j)
        
        return possible_positions
    
    
    def possible_position_for_bin(self, bing):
        
        occupied_by_red = [i.get_coordinates() for i in self.red]
        occupied_by_black = [i.get_coordinates() for i in self.black]
        
        [x, y] = bing.get_coordinates()
        if bing.side == 'B':
            possible_positions = [[x + 2, y], [x - 2, y], [x, y + 2]]
            
            if y < 0:
                possible_positions.remove([x + 2, y])
                possible_positions.remove([x - 2, y])
            for i in possible_positions:
                if i in occupied_by_black or (
                        abs(i[0]) > 8 or abs(i[1]) > 9 ):
                    possible_positions.remove(i)
                        
        
        if bing.side == 'R':
            possible_positions = [[x - 2, y], [x + 2, y], [x, y - 2]]
            
            if y < 0:
                possible_positions.remove([x + 2, y])
                possible_positions.remove([x - 2, y])
                
            for i in possible_positions:
                if i in occupied_by_red or (
                        abs(i[0]) > 8 or abs(i[1]) > 9 ):
                    possible_positions.remove(i)
        
        return possible_positions
    
    
    def all_possible_position(self, qi):
        if type(qi) == Jv:
            return self.possible_position_for_jv(qi)

        
        if type(qi) == Ma:
            return self.possible_position_for_ma(qi)

        
        if type(qi) == Xiang:
            return self.possible_position_for_xiang(qi)

        
        if type(qi) == Shi:
            return self.possible_position_for_shi(qi)

        
        if type(qi) == Jiang:
            return self.possible_position_for_jiang(qi)

        
        if type(qi) == Pao:
            return self.possible_position_for_pao(qi)
        
        
        if type(qi) == Bin:
            return self.possible_position_for_bin(qi)


    def move_to(self, qi, x, y):
        occupied_by_red = [i.get_coordinates() for i in self.red]
        occupied_by_black = [i.get_coordinates() for i in self.black]
        
        positions = self.all_possible_position(qi)
        if [x, y] not in positions:
            pass
        
        else:
            if qi.side == 'B' and ([x, y] in occupied_by_red):
                self.replace_by(
                self.red[occupied_by_red.index([x, y])], qi)
                self.counter = self.counter + 1
            
            if qi.side == 'R' and ([x, y] in occupied_by_black):
                self.replace_by(
                self.black[occupied_by_black.index([x, y])], qi)
                self.counter = self.counter + 1
                
            else:
                qi.x_coordinate = x
                qi.y_coordinate = y
                self.counter = self.counter + 1
                
    
    def check(self, s):
        result = False
        check_piece = []
        if s == 'B':
            jiang_position = self.black_jiang.get_coordinates()
            for i in self.red :
                if jiang_position in self.all_possible_position(i):
                    result = True
                    check_piece.append(i)
            
        if s == 'R':
            jiang_position = self.red_jiang.get_coordinates()
            for i in self.black :
                if jiang_position in self.all_possible_position(i):
                    result = True
                    check_piece.append(i)
                    
        return ([result, check_piece])
    
    
    def check_mate(self, s):
        
        
        
        pass
    




