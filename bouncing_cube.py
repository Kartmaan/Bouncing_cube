import pygame as pg
from random import choice

from pygame import display
from pygame import color
from pygame.display import update

win_width = 1024
win_height = 768

pg.init()

win = pg.display.set_mode((win_width,win_height))
pg.display.set_caption("Bounce")

obst_width = win_width
obst_height = 50
obst_x = (win_width/2) - (obst_width/2)
obst_y = (win_height/2) - (obst_height/2)
obst = pg.Rect(obst_x, obst_y, obst_width, obst_height)
obst_init = obst

cube_x = 5
cube_y = 5
cube_size = 20
cube = pg.Rect(cube_x, cube_y, cube_size, cube_size)

vector = [11,20]

colors = {"red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), 
"white":(255,255,255), "pink":(255,0,255), "cyan":(0,255,255),
"yellow":(255,255,0)}
c = colors["white"]

def witchSide(rect1, rect2):
    # Position of rect2 in relation to rect1
    if rect1.midtop[1] > rect2.midtop[1]:
        return "top"
    elif rect1.midleft[0] > rect2.midleft[0]:
        return "left"
    elif rect1.midright[0] < rect2.midright[0]:
        return "right"
    else:
        return "bottom"

run = True
while run:
    pg.time.delay(10)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    cube_x += vector[0]
    cube_y += vector[1]

    side = witchSide(obst, cube)
    #print(side)

    if side == "top" or side =="bottom":
        if cube.colliderect(obst):
            if side == "top" :
                c = colors["yellow"]
            else :
                c = colors["cyan"]

            vector[1] = -vector[1]
    
    if side == "left" or side =="right":
        if cube.colliderect(obst):
            if side == "top" :
                c = colors["red"]
            else :
                c = colors["green"]

            vector[0] = -vector[0]

    if cube_x < 0 or cube_x > win_width - cube_size:
        c = colors["white"]
        vector[0] = -vector[0]
        if obst[2] > 50:
            obst.inflate_ip(-20,0)
        else :
            obst.inflate_ip(win_width-obst[2], 0)
    
    if cube_y < 0 or cube_y > win_height - cube_size:
        c = colors["blue"]
        vector[1] = -vector[1]
        if obst[2] > 50:
            obst.inflate_ip(-20,0)
        else :
            obst.inflate_ip(win_width-obst[2], 0)

    win.fill((0,0,0))
    pg.draw.rect(win, (255,255,255), obst)
    pg.draw.rect(win, c, cube)
    cube.move_ip(vector[0], vector[1])
    pg.display.update()
    print(obst[2])

pg.quit()