import curses
from time import sleep

begin_x = 0
begin_y = 0
height = 100
width = 100


curses.initscr()

curses.noecho()

curses.cbreak()

stdscr = curses.newwin(height, width, begin_y, begin_x)

stdscr.keypad(True)

dog = [10,10]

new_height= 3

new_width = 3

while(True):
    stdscr.addch(dog[0], dog[1], "X")
    stdscr.refresh()
    stdscr.timeout(150)
    new_DogX = dog[0]
    new_DogY = dog[1]+1
    dog.pop()
    dog.insert(0,new_DogY)
    dog.insert(0,new_DogX)

    
