# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 00:43:27 2021

@author: 1229290416
"""

import chess as ch

game = ch.game_board()

while True:
    
    game.draw()
    
    if divmod(game.counter, 2)[1] == 0:
        choosen_list = [str(game.black.index(i))+ '.  ' + i.name for i in game.black]
        valid_index = [game.black.index(i) for i in game.black]
        for i in range(0, len(choosen_list), 1):
            print(choosen_list[i])
    
        choose_qi_index = int(input("Choose a piece you want to move:  "))
        while choose_qi_index not in valid_index:
            choose_qi_index = int(input("Choose a piece you want to move:  "))
        
        choose_qi = game.black[choose_qi_index]
        x = int(input("x-coordinate:  "))
        y = int(input("y-coordinate:  "))
        game.move_to(choose_qi, x, y)
        
        while divmod(game.counter, 2)[1] == 0:
            x = int(input("x-coordinate:  "))
            y = int(input("y-coordinate:  "))
            game.move_to(choose_qi, x, y)
    
        if game.check('B')[0] == True:
            print('Check ! ')
    
    elif divmod(game.counter, 2)[1] == 1:
        choosen_list = [str(game.red.index(i))+ '.  ' + i.name for i in game.red]
        valid_index = [game.red.index(i) for i in game.red]
        for i in range(0, len(choosen_list), 1):
            print(choosen_list[i])
    
        choose_qi_index = int(input("Choose a piece you want to move:  "))
        while choose_qi_index not in valid_index:
            choose_qi_index = int(input("Choose a piece you want to move:  "))
        
        choose_qi = game.red[choose_qi_index]
        x = int(input("x-coordinate:  "))
        y = int(input("y-coordinate:  "))
        game.move_to(choose_qi, x, y)
        
        while divmod(game.counter, 2)[1] == 1:
            x = int(input("x-coordinate:  "))
            y = int(input("y-coordinate:  "))
            game.move_to(choose_qi, x, y)
    
        if game.check('R')[0] == True:
            print('Check ! ')



