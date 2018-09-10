import curses

from time import sleep

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

import random



HEIGHT = 20

WIDTH = 60



curses.initscr()

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



stdscr.addch(food[0], food[1], '*')



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





    sleep(0.2)



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



    if newHeadY > WIDTH - 2: break

    if newHeadY < 1: break

    if newHeadX < 1: break

    if newHeadX > HEIGHT -2: break

    snake_comp.insert(0, newHead)

    #foooooodd

    if newHead == food:

        while food in snake_comp:  

            RandomX= random.randint(1,(HEIGHT-2))
            
            RandomY= random.randint(1,(WIDTH-2))
            
            food = [RandomX, RandomY]

            stdscr.addch(food[0], food[1], '*')

    else:

        oldTail = snake.pop()

        snake_comp.pop()

        stdscr.addch(oldTail[0], oldTail[1], ' ')


   
    snake.insert(0,newHead)

    stdscr.addch(newHead[0], newHead[1], 'X')







curses.endwin()

print("Score: You've eaten", (len(snake)-3), "apples")
print("You ran out of the game")

