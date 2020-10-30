import pygame as pg
from math import sqrt

__author__ = "Kartmaan"
__version__ = "1.0"

pg.init()

#-------- Window settings (1027x768)
win_width = 1027
win_height = 768
win_res = win_width * win_height
win = pg.display.set_mode((win_width,win_height)) # Surface
pg.display.set_caption("Bouncing Cube") # Window title
refresh = 20

#--------  Info text settings
infoDisplay = False # Show info or not
font = pg.font.Font(None,20)
#stats_sep = 15

#--------  Object settings
# Central obstacle settings
# The proportion values were obtained from a screen size of 1024x768
obst_width = win_width
obst_height = int(win_height/15.36) # The obstacle height is proportional to the window height
obst_x = int((win_width/2) - (obst_width/2)) # Centering x
obst_y = int((win_height/2) - (obst_height/2)) # Centering y
obst_min_width = int(win_width/20.48) # The obstacle min width is proportional to the window width
obst_contraction = int(obst_width/obst_min_width) 
obst_contraction = -obst_contraction # Contraction level
obst = pg.Rect(obst_x, obst_y, obst_width, obst_height)

# Moving cube settings
# The proportion values were obtained from a screen size of 1024x768
cube_x = 5 # Initial cube x axis
cube_y = 5 # Initial cube y axis
cube_size = int(win_res/1966.08) # The cube area is proportional to the window area
cube_size = int(sqrt(cube_size)) # The square root of the cube area gives the value of his side
cube = pg.Rect(cube_x, cube_y, cube_size, cube_size)
vector = [16,20] # Cube vector direction

#--------  Color settings
# Color pallet
colors = {"red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), 
"white":(255,255,255), "pink":(255,0,255), "cyan":(0,255,255),
"yellow":(255,255,0), "orange":(255, 143, 87)}

cube_color = colors["white"] # Cube color

# 'obst' color gradient
obst_G_color = 255 # Green color modulation
obst_G_color_init = obst_G_color # Color benchmark
color_steps = obst[2] - obst_min_width # Difference between 'obst' max width & min width
color_steps = int(color_steps / abs(obst_contraction)) # Steps to reach 'obst' min width
color_steps = int(obst_G_color/color_steps) # Decrementation value of green color gradient

#--------  Function
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

    if side == "top" or side =="bottom": # cube is up or down obst 
        if cube.colliderect(obst): # Collision detected
            if side == "top" :
                cube_color = colors["pink"]
            else :
                cube_color = colors["cyan"]
            vector[1] = -vector[1] # Inverting the y vector
    
    if side == "left" or side =="right": # cube is to the left or right of obst
        if cube.colliderect(obst):
            if side == "top" :
                cube_color = colors["red"]
            else :
                cube_color = colors["green"]
            vector[0] = -vector[0] # Inverting the x vector

    #-------- The cube is in contact with an edge of the surface
    # Each time the cube comes into contact with an edge of the surface, 
    # "obst" contracts to a minimum before returning to its initial size.

    # Left side or right side
    if cube_x < 0 or cube_x > win_width - cube_size: #Side edges of the window
        cube_color = colors["white"]
        vector[0] = -vector[0] # Inverting x vector
        if obst[2] > obst_min_width: # While 'obst' width is greater than 'obst_min_width'
            obst.inflate_ip(obst_contraction,0) # 'obst' width contraction (-x)
            obst_G_color -= color_steps # Decrement the G value of the RGB of 'obst'
        else : # 'obst' width is smaller or equal than 'obst_min_width'
            obst.inflate_ip(win_width-obst[2], 0) # 'obst' returns to its original width (+x)
            obst_G_color = obst_G_color_init # 'obst' returns to its original color

    # Up side or down side
    if cube_y < 0 or cube_y > win_height - cube_size:
        cube_color = colors["yellow"]
        vector[1] = -vector[1] # Inverting y vector
        if obst[2] > obst_min_width:
            obst.inflate_ip(obst_contraction,0)
            obst_G_color -= color_steps
        else :
            obst.inflate_ip(win_width-obst[2], 0)
            obst_G_color = obst_G_color_init

    #-------- Info display
    if infoDisplay == True:
        #-------- General info
        # Window size
        win_size_text = "Win. size : ({}x{})".format(win_width, win_height)
        win_size_text = font.render(win_size_text, True, (colors["white"]))
        win_size_text_rect = win_size_text.get_rect()

        # Refresh frequency
        refresh_text = "Refresh freq. : {}".format(refresh)
        refresh_text = font.render(refresh_text, True, (colors["white"]))
        refresh_text_rect = refresh_text.get_rect()

        #-------- Cube info
        # Cube position (x,y)
        cube_pos_text = "Cube pos. : (x:{}, y:{})".format(cube_x, cube_y)
        cube_pos_text = font.render(cube_pos_text, True, (colors["white"]))
        cube_pos_text_rect = cube_pos_text.get_rect()

        # Cube vector
        vect_text = "Cube vector : [{}, {}]".format(vector[0], vector[1])
        vect_text = font.render(vect_text, True, (colors["white"]))
        vect_text_rect = vect_text.get_rect()

        # Cube relative position
        side_text = "Cube relat. pos. : {}".format(side)
        side_text = font.render(side_text, True, (colors["white"]))
        side_text_rect = side_text.get_rect()

        # Cube size
        cube_size_text = "Cube size : {}".format(cube_size)
        cube_size_text = font.render(cube_size_text, True, (colors["white"]))
        cube_size_text_rect = cube_size_text.get_rect()

        # Cube color
        cube_color_text = "Cube color : {}".format(cube_color)
        cube_color_text = font.render(cube_color_text, True, (colors["white"]))
        cube_color_text_rect = cube_color_text.get_rect()

        #-------- Obstacle info
        # Central obstacle width
        obst_width_text = "Obst. width/min : {}/{}".format(obst[2], obst_min_width)
        obst_width_text = font.render(obst_width_text, True, (colors["white"]))
        obst_width_text_rect = obst_width_text.get_rect()

        # Central obstacle height
        obst_height_text = "Obst. height : {}".format(obst_height)
        obst_height_text = font.render(obst_height_text, True, (colors["white"]))
        obst_height_text_rect = obst_height_text.get_rect()

        # Central obstacle color
        obst_color_text = "Obst color : (255,{},0)".format(obst_G_color)
        obst_color_text = font.render(obst_color_text, True, (colors["white"]))
        obst_color_text_rect = obst_color_text.get_rect()

    #-------- Drawing
    win.fill((0,0,0))
    pg.draw.rect(win, (255, obst_G_color, 0), obst)
    pg.draw.rect(win, cube_color, cube)
    cube.move_ip(vector[0], vector[1])

    # Info texts drawing
    if infoDisplay == True:
        win.blit(win_size_text, (0,0), win_size_text_rect)
        win.blit(refresh_text, (0,15), refresh_text_rect)

        win.blit(cube_pos_text, (0,45), cube_pos_text_rect)
        win.blit(vect_text, (0,60), vect_text_rect)
        win.blit(side_text, (0,75), side_text_rect)
        win.blit(cube_size_text, (0,90), cube_size_text_rect)
        win.blit(cube_color_text, (0,105), cube_color_text_rect)
        
        win.blit(obst_width_text, (0,135), obst_width_text_rect)
        win.blit(obst_height_text, (0,150), obst_height_text_rect)
        win.blit(obst_color_text, (0,165), obst_color_text_rect)
        
    pg.display.update()

pg.quit()
