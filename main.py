#!/bin/python3

import os
from connect4 import connect4
import random
                        
def random_col():
    return random.randint(1,7)



def main():
    game = connect4()
    colors = game.colors
    color = colors[0]

    while True:
        try:
            
            os.system("clear")
            game.show_board()
            if color==colors[0]:
                color=colors[1]
                column_num = int(input(f"\n\n{color}: ")) - 1
            
            elif color==colors[1]:
                color=colors[0]
                column_num = random_col()
            
            game.add_ball(column_num, colors.index(color))
            win = game.check_win()
            if win != None:
                os.system("clear")
                game.show_board()
                print(f"\n{win} Wins!")
                exit()
        except Exception as e:
            print(e)
            continue

if __name__=="__main__":
    main()

