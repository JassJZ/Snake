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
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLUE)

def gameover(a_heigth, a_width, a_stdscr):
    Game = []
    G = [round(a_heigth/2), round((a_width/2)-7)]
    Game.append(G)

    a_stdscr.addstr(Game[0][0],Game[0][1], "GAME OVER", curses.color_pair(3))

import random

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

def enemy(n, a_snake, a_snake_comp, a_new_head, a_food, a_stdscr, a_height, a_width, a_enemylist):
    
    if a_new_head == a_food:

        if len(a_snake)==n:

            a_enemylist.pop()

            a_enemylist.pop()

            randomex= random.randint(2,(a_height-3))
                
            randomey= random.randint(2,(a_width-3))
                
            enemy1 = [randomex, randomey]

            enemy2 = [(randomex-1),(randomey-1)]

            a_enemylist.insert(0, enemy1)

            a_enemylist.insert(0, enemy2)

            while a_enemylist in a_snake_comp:

                while a_enemylist in a_food:

                    randomex= random.randint(2,(a_height-3))
                        
                    randomey= random.randint(2,(a_width-3))
                        
                    enemy1 = [randomex, randomey]

                    enemy2 = [(randomex-1),(randomey-1)]

                    a_enemylist.insert(0, enemy1)

                    a_enemylist.insert(0, enemy2)

            while a_enemylist in a_food:

                while a_enemylist in a_snake_comp:
            
                    randomex= random.randint(2,(a_height-3))
                        
                    randomey= random.randint(2,(a_width-3))
                        
                    enemy1 = [randomex, randomey]

                    enemy2 = [(randomex-1),(randomey-1)]

                    a_enemylist.insert(0, enemy1)

                    a_enemylist.insert(0, enemy2)

            a_stdscr.addstr(a_enemylist[0][0], a_enemylist [0][1], "&", curses.color_pair(4))
            a_stdscr.addstr(a_enemylist[1][0], a_enemylist [1][1], "&", curses.color_pair(4))
    
    return a_enemylist

def countdown(n,a_stdscr,a_height, a_width) :

    for num in range(n,-1,-1):

        string = str(num)

        a_stdscr.refresh()

        a_stdscr.addstr(round(a_height/2),round(a_width/2), string, curses.color_pair(3))

        sleep(0.7)

        a_stdscr.refresh()

        sleep(0.7)

        a_stdscr.addstr(round(a_height/2),round(a_width/2), "GO!", curses.color_pair(3))

        a_stdscr.addstr(round(a_height/2),round(a_width/2), "      ")
    


def print_score(a_heigth, a_width, a_stdscr,a_score):

    text = "SCORE: " + str(a_score)

    a_stdscr.addstr(a_heigth-1,0, text, curses.color_pair(3))



