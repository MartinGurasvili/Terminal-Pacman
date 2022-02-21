"""
Terminal PacMan - Martin Gurasvili

-TO PLAY-
you have 3 lives
once game started use w/a/s/d - up/left/down/right and enter
if nothing is entered the player moves automatically in the facing direction within 2 seconds
score 70 points to win

▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉
▉∙ ∙ ∙ ∙ ∙ ▉▉∙ ∙ ∙ ∙ ▉▉∙ ∙ ∙ ∙ ∙ ▉
▉∙ ▉▉▉▉▉▉∙ ▉▉∙ ▉▉▉▉∙ ▉▉∙ ▉▉▉▉▉▉∙ ▉
▉∙ ▉▉∙ ∙ ∙ ∙ ∙ ▉▉▉▉∙ ∙ ∙ ∙ ∙ ▉▉∙ ▉
▉∙ ▉▉∙ ▉▉∙ ▉▉∙ ▉▉▉▉∙ ▉▉∙ ▉▉∙ ▉▉∙ ▉
▉∙ ∙ ∙ ▉▉∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ▉▉∙ ∙ ∙ ▉
▉▉▉∙ ▉▉▉▉∙ ▉▉▉▉▉▉▉▉▉▉▉▉∙ ▉▉▉▉∙ ▉▉▉
▉▉▉∙ ∙ ∙ ∙ ▉▉∙ ∙ ∙ ∙ ▉▉∙ ∙ ∙ ∙ ▉▉▉
▉▉▉∙ ▉▉▉▉∙ ▉▉∙ ∙ ∙ ∙ ▉▉∙ ▉▉▉▉∙ ▉▉▉
▉▉▉∙ ▉▉∙ ∙ ▉▉▉▉∙ ∙ ▉▉▉▉∙ ∙ ▉▉∙ ▉▉▉
▉∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ▉
▉∙ ▉▉∙ ▉▉▉▉∙ ▉▉∙ ∙ ▉▉∙ ▉▉▉▉∙ ▉▉∙ ▉
▉∙ ▉▉∙ ▉▉∙ ∙ ▉▉∙ ∙ ▉▉∙ ∙ ▉▉∙ ▉▉∙ ▉
▉∙ ▉▉∙ ▉▉∙ ▉▉▉▉▉▉▉▉▉▉▉▉∙ ▉▉∙ ▉▉∙ ▉
▉∙ ∙ ∙ ▉▉∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ▉▉∙ ∙ ∙ ▉
▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉
"""
import random
import time
from signal import signal, alarm, SIGALRM
from termcolor import colored


size = 16
lives = 3
score = "0"
direct ="N"
posx = 0
posy = 0
prev = "  "
dire = 2

winscore = 70

gx = 2
gy = 1

gameover = False

maze = [[" ","██"*(size)],
        ["█","∙ ","∙ ","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","∙ ","∙ ","█"],
        ["█","∙ ","██","██","██","∙ ","██","∙ ","██","██","∙ ","██","∙ ","██","██","██","∙ ","█"],
        ["█","∙ ","██","∙ ","∙ ","∙ ","∙ ","∙ ","██","██","∙ ","∙ ","∙ ","∙ ","∙ ","██","∙ ","█"],
        ["█","∙ ","██","∙ ","██","∙ ","██","∙ ","██","██","∙ ","██","∙ ","██","∙ ","██","∙ ","█"],
        ["█","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","█"],
        [" ","██","∙ ","██","██","∙ ","██","██","██","██","██","██","∙ ","██","██","∙ ","██"," "],
        [" "," █","∙ ","∙ ","∙ ","∙ ","██","  ","  ","  ","  ","██","∙ ","∙ ","∙ ","∙ ","█ "," "],
        [" "," █","∙ ","██","██","∙ ","██","  ","  ","  ","  ","██","∙ ","██","██","∙ ","█ "," "],
        [" ","██","∙ ","██","∙ ","∙ ","██","██","  ","  ","██","██","∙ ","∙ ","██","∙ ","██"," "],
        ["█","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","█"],
        ["█","∙ ","██","∙ ","██","██","∙ ","██","∙ ","∙ ","██","∙ ","██","██","∙ ","██","∙ ","█"],
        ["█","∙ ","██","∙ ","██","∙ ","∙ ","██","∙ ","∙ ","██","∙ ","∙ ","██","∙ ","██","∙ ","█"],
        ["█","∙ ","██","∙ ","██","∙ ","██","██","██","██","██","██","∙ ","██","∙ ","██","∙ ","█"],
        ["█","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","█"],
        [" ","██"*(size)],
        ]

def game_space ():
    
    print((" "*int(size/2-1)),"Martin's - PacMan")
    print((" "*int(size/1.3)),"Score",score)
    print((" "*int(size-2)),(str(lives)+" ❤"))
    
    for x in range(len(maze)):
     for y in range(len(maze[x])):
         if(maze[x][y] == "▶ " or maze[x][y] == "◀ " or maze[x][y] == "▲ " or maze[x][y] == "▼ "):
             print(colored(maze[x][y],"yellow"),end="")
         elif(maze[x][y]=="∙ "):
             print(maze[x][y],end="")
         elif(maze[x][y]=="◓ "):
             print(colored(maze[x][y],"red"),end="")
              
         else:
             print(maze[x][y],end="")
     print()
     
def spawn():
    global direct,maze,posx,posy
    good_loc = False
    while good_loc == False:
        x = random.randint(1,size-2)
        y = random.randint(1,size-2)
        if(maze[x][y]=="∙ "):
            good_loc = True
    try:
        if(maze[x][y+1]=="∙ "):
            maze[x][y] = "▶ "
            direct ="R"
        if(maze[x][y-1]=="∙ "):
            maze[x][y] = "◀ "
            direct ="L"
        if(maze[x-1][y]=="∙ "):
            maze[x][y] = "▲ "
            direct ="U"
        if(maze[x+1][y]=="∙ "):
            maze[x][y] = "▼ "
            direct ="D"
    except:
        print(" ")
    posx = x
    posy = y

def move():
    global direct,maze,posx,posy,score,gameover
    
    x = None
    signal(SIGALRM, lambda x, y: 1/0)
    try:
        
        alarm(1)
        x = str(input(">>>"))
        
    except ZeroDivisionError:
        print("")
        
    if(x!=None):
        if (x == "w"):
            direct = "U"
        if (x == "a"):
            direct = "L"
        if (x == "s"):
            direct = "D"
        if (x == "d"):
            direct = "R"
    running = True
    while running:
        if(direct =="L"):
            maze[posx][posy] = "  "
            score = int(score)+1
            posy-=1
            if(maze[posx][posy] == "  " or maze[posx][posy] == "∙ "):
                maze[posx][posy] = "◀ "
                
            else:
                gameover =True

            running = False
            
        if(direct =="R"):
            maze[posx][posy] = "  "
            score = int(score)+1
            posy+=1

            if(maze[posx][posy] == "  " or maze[posx][posy] == "∙ "):
                maze[posx][posy] = "▶ "
            else:
                gameover =True
            running = False
            break
                
        if(direct =="U"):
            maze[posx][posy] = "  "
            score = int(score)+1
            posx-=1
            
            if(maze[posx][posy] == "  " or maze[posx][posy] == "∙ "):
                maze[posx][posy] = "▲ "
            else:
                gameover =True
            
            running = False
            break
            
        if(direct =="D"):
            maze[posx][posy] = "  "
            score = int(score)+1
            posx+=1
            if(maze[posx][posy] == "  " or maze[posx][posy] == "∙ "):
                maze[posx][posy] = "▼ "
            else:
                gameover =True

            running = False
    game_space()

def ghost_ai():
    global maze,gx,gy,gameover,prev,dire
    running = True
    while running:
        
        if(dire == 0):
            if(maze[gx][gy+1]  == "  " or maze[gx][gy+1]== "∙ "):
                
                maze[gx][gy] = prev
                prev = maze[gx][gy+1]
                maze[gx][gy+1] = "◓ "
                gy+=1
                running = False
                break   
                
        elif(dire == 1):
            if(maze[gx][gy-1]  == "  " or maze[gx][gy-1]== "∙ "):
                
                maze[gx][gy] = prev
                prev = maze[gx][gy-1]
                maze[gx][gy-1] = "◓ "
                gy-=1
                running = False
                break
        elif(dire == 2):
            if(maze[gx+1][gy]  == "  " or maze[gx+1][gy]== "∙ "):
                maze[gx][gy] = prev
                prev = maze[gx+1][gy]
                maze[gx+1][gy] = "◓ "
                gx+=1
                running = False
                break
        elif(dire == 3):
            try:
                if(maze[gx-1][gy] == "  " or maze[gx-1][gy]== "∙ "):
                    maze[gx][gy] = prev
                    prev = maze[gx-1][gy]
                    maze[gx-1][gy] = "◓ "
                    gx-=1
                    running = False
                    break
            except:
                dire = random.randint(0,4)
        dire = random.randint(0,4)    
        
if __name__ == "__main__":
    spawn() 
    game_space()
    
    input("Press Enter To Start Game")
    print(" ")
    
    for x in range(3+1):
        if score == winscore:
            break
        while gameover == False:
            move()
            ghost_ai()
            if score == winscore:
                print("You Won")
                input("enter to exit")
                break
            
        if gameover ==True:
            if(lives > 0):
                print("You Died")
                lives-=1
                spawn() 
                gameover = False
    if score != winscore:
        print("GameOver")




            
