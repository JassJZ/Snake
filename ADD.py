from time import sleep

from math import floor

from pygame import *

import random

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN



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
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_MAGENTA)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_WHITE)

def gameover(a_heigth, a_width, stdscr, seconds):
    Game = []
    G = [round(a_heigth/2), round((a_width/2)-7)]
    A = [round((a_heigth/2)+2), round((a_width/2)-13)]
    Game.append(G)
    Game.append(A)

    stdscr.addstr(Game[0][0],Game[0][1], "GAME OVER")
    stdscr.addstr(Game[1][0],Game[1][1], "after " + str(seconds) + " seconds")

def final1(snake):

    return ("You've eaten " + str(len(snake)-3) + " apples")



def final2 (snake, name):

    if (len(snake)-3)<5:

        return ("You can do better " + name + " !!!")

    else:

        return ("Next tiiiime " + name + "!")





def printer_final(a_heigth, a_width, a_stdscr,snake,name):

    a_stdscr.addstr(round(5),round(a_width/2), "You ran out of the game")

    a_stdscr.addstr(round(a_heigth/2),round(a_width/2), final1(snake))

    a_stdscr.addstr(round(15),round(a_width/2), final2(snake,name))


def enemy(n, a_snake, a_snake_comp, a_new_head, a_food, stdscr, a_height, a_width, a_enemylist):

    if a_new_head == a_food:

        if len(a_snake) in [n,(2*n), (3*n)]:

            a_enemylist.pop()

            a_enemylist.pop()

            randomex= random.randint(2,(a_height-3))

            randomey= random.randint(2,(a_width-3))

            enemy1 = [randomex, randomey]

            enemy2 = [(randomex-1),(randomey-1)]

            a_enemylist.insert(0, enemy1)

            a_enemylist.insert(0, enemy2)

            if a_enemylist in a_snake_comp or a_enemylist in a_food:
                return enemy(n,a_snake, a_snake_comp, a_new_head, a_food, stdscr, a_height, a_width, a_enemylist)
            else:
                stdscr.addstr(a_enemylist[0][0], a_enemylist [0][1], "&", curses.color_pair(4))
                stdscr.addstr(a_enemylist[1][0], a_enemylist [1][1], "&", curses.color_pair(4))
                return a_enemylist





def countdown(n,stdscr,a_height, a_width) :

    for num in range(n,0,-1):

        string = str(num)

        stdscr.refresh()

        stdscr.addstr(round(a_height/2),round(a_width/2), string)

        sleep(0.8)

    stdscr.refresh()

    sleep(0.8)

    stdscr.addstr(round(a_height/2),round(a_width/2), "GO!")
    stdscr.refresh()
    sleep(0.3)
    stdscr.addstr(round(a_height/2),round(a_width/2), "      ")



def print_score(a_heigth, a_width, stdscr,a_score):

    text1 = "SCORE: " + str(a_score)

    stdscr.addstr(a_heigth-1,10, text1, curses.color_pair(3))


def level_fun(score):

    level = 1

    level = floor(score/5) + 1

    return level



def print_level(a_heigth, a_width, a_stdscr,a_score):

    #text2 = "LEVEL: " + str(a_score)



    a_stdscr.addstr(a_heigth -1 ,0, "LEVEL: " + str(level_fun(a_score)), curses.color_pair(5))




def music():
    mixer.init()
    mixer.music.load("chuck rock.ogg")
    mixer.music.play(loops=-1)
