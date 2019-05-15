# Add your Python code here. E.g.
from microbit import *
import random

maze = "00000:00000:00000:00000:00000"
listMaze = list(maze) 
snake = [0]
droite = 1
gauche = -1
haut = -6
bas = 6
direction = droite
tempsDeDeplacement = 500
limites = [5, 11, 17, 23]
apple = 14
score = 0


def randomApple(listMaze):
    return random.choice([idx for idx,e in enumerate(listMaze) if e == "0"])


    
while snake[0] + direction not in limites and snake[0] + direction <= 28 and snake[0] + direction >= 0 and snake[0] + direction not in snake[1:]:
    
    listMaze[apple] = "9"
    
    if apple == snake[0]:
        score +=1
        snake = [apple + direction] + snake
        apple = randomApple(listMaze)
    else:
        listMaze[snake[-1]] = "0"
        if len(snake) > 1:
            for i in range(len(snake)-1, 0, -1):
                snake[i] = snake[i-1]  
        snake[0] += direction
    
    listMaze[snake[0]] = "6"
    maze = "".join(listMaze)
    display.show(Image(maze))

    a = button_a.get_presses()
    b = button_b.get_presses()
    
    sleep(tempsDeDeplacement) 
    
    if b < button_b.get_presses():
        if direction == haut: 
            direction = droite
        elif direction == droite: 
            direction = bas
        elif direction == bas: 
            direction = gauche
        elif direction == gauche: 
            direction = haut
    if a < button_a.get_presses():
        if direction == haut: 
            direction = gauche
        elif direction == droite: 
            direction = haut
        elif direction == bas: 
            direction = droite
        elif direction == gauche: 
            direction = bas
            
display.show(Image.SAD)
sleep(1000)
display.scroll(str(score))

