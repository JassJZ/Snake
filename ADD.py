from time import sleep

def speed(a_snake):
    if len(a_snake)<7:
        sleep(0.2)
    if 11>len(a_snake)>6:
        sleep(0.15)
    if 15>len(a_snake)>10:
        sleep(0.1)
    if 18>len(a_snake)>14:
        sleep(0.085)
    if len(a_snake)>17:
        sleep(0.055)

import curses

curses.initscr()

curses.start_color()

curses.use_default_colors()

def Colors():
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_MAGENTA)

def gameover(a_heigth, a_width, a_stdscr):
    Game = []
    G = [round(a_heigth/2), round((a_width/2)-7)]
    Game.append(G)

    a_stdscr.addstr(Game[0][0],Game[0][1], "GAME OVER", curses.color_pair(3))

import random

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

def enemy(a_snake, a_snake_comp, a_new_head, a_food, a_stdscr, a_height, a_width):
    
    if a_new_head == a_food:

        if 7>len(a_snake)>5:
        
            enemylist = []

            randomex= random.randint(2,(a_height-3))
                
            randomey= random.randint(2,(a_width-3))
                
            enemy1 = [randomex, randomey]

            enemy2 = [(randomex-1),(randomey-1)]

            enemylist.insert(0, enemy1)

            enemylist.insert(0, enemy2)

            while enemylist in a_snake_comp:
            
                enemylist = []

                randomex= random.randint(2,(HEIGHT-3))
                    
                randomey= random.randint(2,(WIDTH-3))
                    
                enemy1 = [randomex, randomey]

                enemy2 = [(randomex-1),(randomey-1)]

                enemylist.insert(0, enemy1)

                enemylist.insert(0, enemy2)

            a_stdscr.addstr(enemylist[0][0], enemylist [0][1], "&", curses.color_pair(3))
            a_stdscr.addstr(enemylist[1][0], enemylist [1][1], "&", curses.color_pair(3))






