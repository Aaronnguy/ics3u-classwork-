# Pygame Compund Shapes

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_x = 0
cloud_y = 53

sun_x = -200
sun_y = 53

moon_x = -900
moon_y = 53 



# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
        if cloud_x > WIDTH: 
            cloud_x = 20
        

    # GAME STATE UPDATES

    # All game math and comparisons happen here
    cloud_x += 3.5
    if cloud_x > WIDTH + 40: 
       cloud_x = -400
    sun_x += 2.5
    if sun_x > WIDTH + 730:
        sun_x = - 30
    moon_x += 2.5
    if moon_x > WIDTH + 40:
        moon_x = - 700
    if moon_x >= 1:
        screen.fill("#222d5a")
    else:
        screen.fill("#87ceeb")
    if sun_x < 112:
        screen.fill("#ffca7c")
        
   
    
    
    # DRAWING
    
# cloud 1 
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x, cloud_y), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 14, cloud_y + 2), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 19, cloud_y - 21), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 52, cloud_y - 4), 25)
# cloud 2
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x +380, cloud_y + 2), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x +433, cloud_y + 3), 25)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x +415, cloud_y -20), 27)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x +410, cloud_y +10), 25)
# green ground 
    pygame.draw.rect(screen, (34,139,34), pygame.Rect(0, 350, 640, 600), 500)

# house 
    pygame.draw.rect(screen, (118,0,0), pygame.Rect(190,230,200,130), 100)
    pygame.draw.rect(screen, (168,204,215), pygame.Rect(225,267,40,40), 20)
    pygame.draw.rect(screen, (168,204,215), pygame.Rect(320,267,40,40), 20)
    pygame.draw.line(screen, (255,255,255), (243,268), (243,306), 2)
    pygame.draw.line(screen, (255,255,255), (224,288), (264,288), 2)
    pygame.draw.line(screen, (255,255,255), (339,268), (339,304), 2)
    pygame.draw.line(screen, (255,255,255), (320,288), (360,288), 2)
    pygame.draw.rect(screen, (150,10,100), pygame.Rect(160,200,260,30),100)
    pygame.draw.polygon(screen, (150,50,100),[(161, 201), (418, 201), (290, 108)])
    pygame.draw.rect(screen, (234, 221, 202), pygame.Rect(272,290,40,70), 30)
    pygame.draw.circle(screen, (165,42,42),(279,324), 5)

# tree
    pygame.draw.rect(screen, (128,96,77), (43,267, 40,100),30 )
    pygame.draw.circle(screen,(1,66,33), (54,282), 25)
    pygame.draw.circle(screen,(1,66,33), (29,257), 25)
    pygame.draw.circle(screen,(1,66,33), (81,272), 25)
    pygame.draw.circle(screen,(1,66,33), (57,250), 25)
    pygame.draw.circle(screen,(1,66,33), (90,240), 20)
    pygame.draw.circle(screen,(1,66,33), (56,226), 20)
    pygame.draw.circle(screen,(1,66,33), (26,220), 20)
    pygame.draw.circle(screen,(1,66,33), (77,223), 20)
    
# tree 2 
    pygame.draw.rect(screen,(128,96,77), (533, 255, 40, 100), 30) 
    pygame.draw.circle(screen,(1,66,33), (541,264), 25)
    pygame.draw.circle(screen,(1,66,33), (571,257), 25)
    pygame.draw.circle(screen,(1,66,33), (520,259), 25)
    pygame.draw.circle(screen,(1,66,33), (588,258), 18)
    pygame.draw.circle(screen,(1,66,33), (545,221), 25)
    pygame.draw.circle(screen,(1,66,33), (583,224), 20)
    pygame.draw.circle(screen,(1,66,33), (514,233), 20)
    pygame.draw.circle(screen,(1,66,33), (77,223), 20)

# sun
    pygame.draw.circle(screen, (254,212,38),(sun_x, sun_y),40 )

# moon 
    pygame.draw.circle(screen, (50,50,50), (moon_x, moon_y),40) 
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
