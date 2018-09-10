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
        sleep(0.06)

import curses

curses.initscr()

curses.start_color()

curses.use_default_colors()

def Colors():
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_MAGENTA)