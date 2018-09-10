import curses

#from time import sleep

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

from ADD import speed 

from ADD import Colors

from ADD import enemy

import random

from ADD import gameover

from time import sleep


HEIGHT = 20

WIDTH = 60



curses.initscr()

Colors()

stdscr = curses.newwin(HEIGHT, WIDTH, 0, 0)

stdscr.keypad(True)

curses.noecho()

stdscr.border(0)

curses.curs_set(0)

stdscr.nodelay(True)



snake = [[4,10], [4,9], [4,8]]

food = [10,20]


# attempt to solve problem with 
snake_comp=[]
snake_comp.insert(0, snake[len(snake)-1])
snake_comp.insert(0, snake[1])
snake_comp.insert(0, snake[0])

direction = KEY_RIGHT



stdscr.addstr(food[0], food[1], ' ', curses.color_pair(2))



while(True):

    stdscr.refresh()



    # step update

    previousDirection = direction

    keyboardInput = stdscr.getch()



    # previousDirection KEY_RIGHT

    if keyboardInput in [KEY_UP, KEY_DOWN] and previousDirection == KEY_RIGHT:

        direction = keyboardInput

    # previousDirection KEY_LEFT

    if keyboardInput in [KEY_UP, KEY_DOWN] and previousDirection == KEY_LEFT:

        direction = keyboardInput

    # previousDirection KEY_RIGHT

    if keyboardInput in [KEY_RIGHT, KEY_LEFT] and previousDirection == KEY_UP:

        direction = keyboardInput

    # previousDirection KEY_RIGHT

    if keyboardInput in [KEY_RIGHT, KEY_LEFT] and previousDirection == KEY_DOWN:

        direction = keyboardInput





    
    speed(snake)



    newHead = []



    if direction == KEY_RIGHT:

        newHeadX = snake[0][0]

        newHeadY = snake[0][1] + 1

        newHead = [newHeadX, newHeadY]



    if direction == KEY_LEFT:

        newHeadX = snake[0][0]

        newHeadY = snake[0][1] - 1

        newHead = [newHeadX, newHeadY]



    if direction == KEY_UP:

        newHeadX = snake[0][0] - 1

        newHeadY = snake[0][1]

        newHead = [newHeadX, newHeadY]



    if direction == KEY_DOWN:

        newHeadX = snake[0][0] + 1

        newHeadY = snake[0][1]

        newHead = [newHeadX, newHeadY]



    if newHeadY > WIDTH - 2:

        gameover(HEIGHT, WIDTH, stdscr)

        stdscr.refresh()

        sleep(5)

        break

    if newHeadY < 1:

        gameover(HEIGHT, WIDTH, stdscr)

        stdscr.refresh()

        sleep(5)

        break

    if newHeadX < 1:

        gameover(HEIGHT, WIDTH, stdscr)

        stdscr.refresh()

        sleep(5)

        break

    if newHeadX > HEIGHT -2:

        gameover(HEIGHT, WIDTH, stdscr)

        stdscr.refresh()

        sleep(5)

        break

    if snake[0] in snake[1:]:

        gameover(HEIGHT, WIDTH, stdscr)

        stdscr.refresh()

        sleep(5)

        break
    
    

    snake_comp.insert(0, newHead)

    enemylist = []

    enemy(snake, snake_comp, newHead, food, stdscr, HEIGHT, WIDTH, enemylist)

    if snake in enemylist:
        
        gameover(HEIGHT, WIDTH, stdscr)

        stdscr.refresh()

        sleep(5)

        break

    #foooooodd

    if  newHead==food:

        while food in snake_comp:  

            RandomX= random.randint(1,(HEIGHT-3))
            
            RandomY= random.randint(1,(WIDTH-3))
            
            food = [RandomX, RandomY]

            stdscr.addstr(food[0], food[1], ' ', curses.color_pair(2))

    else:

        oldTail = snake.pop()

        snake_comp.pop()

        stdscr.addch(oldTail[0], oldTail[1], ' ')


   
    snake.insert(0,newHead)

    stdscr.addstr(newHead[0], newHead[1], '+', curses.color_pair(1))







curses.endwin()

print("Score: You've eaten", (len(snake)-3), "apples")
print("You ran out of the game")
