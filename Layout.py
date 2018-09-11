from time import sleep

import datetime

name= input("Enter a name:")

print("Your name is: ", name)

print()

print("... The game is loading ...")

sleep(3)

import curses

#from time import sleep

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

from ADD import speed 

from ADD import Colors

from ADD import enemy

from ADD import print_score

import random

from ADD import gameover



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


# attempt to solve problem with 
snake_comp=[]
snake_comp.insert(0, snake[len(snake)-1])
snake_comp.insert(0, snake[1])
snake_comp.insert(0, snake[0])

direction = KEY_RIGHT

from ADD import countdown

countdown(3,stdscr, HEIGHT, WIDTH)

food = [10,20]

score = 0

stdscr.addstr(food[0], food[1], ' ', curses.color_pair(2))

enemylist=[[0,0], [HEIGHT, WIDTH],[0,0], [HEIGHT, WIDTH],[0,0], [HEIGHT, WIDTH] ]

enemylist1 = enemylist

def end_game():
   elapsedTime = (datetime.datetime.now() - startTime).total_seconds()
   gameover(HEIGHT, WIDTH, stdscr, elapsedTime )
   stdscr.refresh()
   sleep(3)

startTime = datetime.datetime.now()


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



    if (newHeadY > WIDTH - 2) or  (newHeadY < 1) or (newHeadX < 1) or (newHeadX > HEIGHT -2) or (snake[0] in snake[1:]):
        
        end_game()
        
        break
    
    

    snake_comp.insert(0, newHead)


    enemy(5, snake, snake_comp, newHead, food, stdscr, HEIGHT, WIDTH, enemylist)


    if (snake_comp[0] == enemylist[0]) or (snake_comp[0] == enemylist[1]) or (snake_comp[0] == enemylist[2]) or (snake_comp[0] == enemylist[3]) or (snake_comp[0] == enemylist[4]) or (snake_comp[0] == enemylist[5]):

        end_game()

        break



    #foooooodd

    if  newHead==food:

        score = score + 1

        print_score(HEIGHT,WIDTH,stdscr,score)

        while food in snake_comp: 

            RandomX= random.randint(2,(HEIGHT-3))
                    
            RandomY= random.randint(2,(WIDTH-3))
                
            food = [RandomX, RandomY]

            stdscr.addstr(food[0], food[1], ' ', curses.color_pair(2))
        
        while food in enemylist:  

            RandomX= random.randint(2,(HEIGHT-3))
                
            RandomY= random.randint(2,(WIDTH-3))
                
            food = [RandomX, RandomY]

            stdscr.addstr(food[0], food[1], ' ', curses.color_pair(2))

    else:

        oldTail = snake.pop()

        snake_comp.pop()

        stdscr.addch(oldTail[0], oldTail[1], ' ')

   
    snake.insert(0,newHead)

    stdscr.addstr(newHead[0], newHead[1], '+', curses.color_pair(1))


curses.endwin()

print()

print("Score:", name, ", you've eaten", (len(snake)-3), "apples")
if (len(snake)-3)<5:
    print ("Do better!!!")
print("You ran out of the game")
score = len(snake)-3

f = open("score.txt", "a+")
f.write(name + ":" + str(score))
f.write("\n")
f.close

f=open("score.txt", "r")
if f.mode == 'r':
    contents =f.read()
print (contents)
f.close
