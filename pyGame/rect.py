import pgzrun
import random

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = random.randint(100,255)
    
    width = WIDTH
    height = HEIGHT-200
    
    for i in range(20):
        rect = Rect((0,0),(width,height))
        rect.center=150, 150
        screen.draw.rect(rect,(r,g,b))
        width-=10
        height+=10
        r-=10
        g+=10
pgzrun.go()        