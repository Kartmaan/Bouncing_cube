import pygame as pg

pg.init()

win_width = 1024
win_height = 768

win = pg.display.set_mode((win_width,win_height))
pg.display.set_caption("Bouncing Cube")

# Central obstacle settings
obst_width = win_width
obst_height = 50
obst_x = int((win_width/2) - (obst_width/2))
obst_y = int((win_height/2) - (obst_height/2))
obst = pg.Rect(obst_x, obst_y, obst_width, obst_height)
obst_init = obst
obst_min_width = 50
obst_contraction = -20

# Moving cube setting 
cube_x = 5 # Initial cube x axis
cube_y = 5 # Initial cube y axis
cube_size = 20
cube = pg.Rect(cube_x, cube_y, cube_size, cube_size)

# Cube vector direction
vector = [11,20]

# Color pallet
colors = {"red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), 
"white":(255,255,255), "pink":(255,0,255), "cyan":(0,255,255),
"yellow":(255,255,0)}
c = colors["white"]

def witchSide(rect1, rect2):
    # Return a relative position
    # Position of rect2 in relation to rect1
    if rect1.midtop[1] > rect2.midtop[1]:
        return "top"
    elif rect1.midleft[0] > rect2.midleft[0]:
        return "left"
    elif rect1.midright[0] < rect2.midright[0]:
        return "right"
    else:
        return "bottom"

#--------  Animation loop
run = True
while run:
    pg.time.delay(20) # Refresh ferequency

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    # Vertorial direction
    cube_x += vector[0]
    cube_y += vector[1]

    #-------- The cube is in contact with the central obstacle
    side = witchSide(obst, cube) # Position of cube in relation to obst
    #print(side)

    if side == "top" or side =="bottom": # cube is up or down obst 
        if cube.colliderect(obst): # Collision detected
            if side == "top" :
                c = colors["yellow"]
            else :
                c = colors["cyan"]
            vector[1] = -vector[1] # Inverting the y vector
    
    if side == "left" or side =="right": # cube is to the left or right of obst
        if cube.colliderect(obst):
            if side == "top" :
                c = colors["red"]
            else :
                c = colors["green"]
            vector[0] = -vector[0] # Inverting the x vector

    #-------- The cube is in contact with an edge of the surface
    # Each time the cube comes into contact with an edge of the surface, 
    # "obst" contracts to a minimum before returning to its initial size.

    # Left side or right side
    if cube_x < 0 or cube_x > win_width - cube_size: #Side edges of the window
        c = colors["white"]
        vector[0] = -vector[0] # Inverting x vector
        if obst[2] > obst_min_width: # While 'obst' width is greater than 'min_obst_width'
            obst.inflate_ip(obst_contraction,0) # 'obst' width contraction (-x)
        else : # 'obst' width is smaller or equal than 'min_obst_width'
            obst.inflate_ip(win_width-obst[2], 0) # 'obst' returns to its original width (+x)

    # Up side or down side
    if cube_y < 0 or cube_y > win_height - cube_size:
        c = colors["blue"]
        vector[1] = -vector[1] # Inverting y vector
        if obst[2] > obst_min_width:
            obst.inflate_ip(obst_contraction,0)
        else :
            obst.inflate_ip(win_width-obst[2], 0)

    #-------- Drawing
    win.fill((0,0,0))
    pg.draw.rect(win, (255,255,255), obst)
    pg.draw.rect(win, c, cube)
    cube.move_ip(vector[0], vector[1])
    pg.display.update()

pg.quit()