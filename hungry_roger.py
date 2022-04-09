import random
import pygame


from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_RIGHT, K_LEFT, MOUSEBUTTONDOWN


pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()



# ---------------------------
# Initialize global variables

scene_title_font = pygame.font.SysFont('Arial', 50)
end_scene_font = pygame.font.SysFont('Arial', 20)
current_screen = 0
roger_x = 280
roger_y = 280
roger_leg_1_x = 254
roger_leg_1_y = 292
roger_leg_2_x = 254
roger_leg_2_y = 311
roger_leg_3_x = 318
roger_leg_3_y = 292
roger_leg_4_x = 319
roger_leg_4_y = 311
roger_rect = pygame.Rect(280, 280, 40, 40)
roger_leg_rect = pygame.Rect(254,292,100,100)
fly_rect = pygame.Rect(315, 167, 20, 20)
boarder_1_rect = pygame.Rect(0,0,670,5)
boarder_2_rect = pygame.Rect(0,3,5,480)
boarder_3_rect = pygame.Rect(4,477,685,5)
boarder_4_rect = pygame.Rect(637,3,5,480)
score = 0


score_font = pygame.font.SysFont('Comic Sans MS', 50)

# ---------------------------
running = True
while running:
    # EVENT HANDLING
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RIGHT:
                current_screen += 1
                print(current_screen)
            elif event.key == K_LEFT:
                current_screen -= 1
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
     
    
    if roger_rect.colliderect(fly_rect):
        score += 1 
        fly_rect.x = random.randint(50,200)
        fly_rect.y = random.randint(50,200)
      
            
    
      
         
    elif roger_rect.colliderect(boarder_1_rect):
        score -= 0.5
    elif roger_rect.colliderect(boarder_2_rect):
        score -= 0.5 
    elif roger_rect.colliderect(boarder_3_rect):
        score -= 0.5 
    elif roger_rect.colliderect(boarder_4_rect):
        score -= 0.5 
   
        
    
        
                
    

    # GAME STATE UPDATES
    keys = pygame.key.get_pressed()
    if keys[119]:  # w
        roger_y -= 5
        roger_rect.y -= 5
    if keys[97] == True:  # a
        roger_x -= 5
        roger_rect.x -= 5
        
    if keys[115] == True:  # s
        roger_y += 5
        roger_rect.y += 5
    if keys[100] == True:  # d
        roger_x += 5
        roger_rect.x += 5
        
    
        

    if score >= 20: 
        current_screen = 3 
        
    
        
        


    screen.fill((255, 255, 255))  # always the first drawing command
    
    
   
        # Scene 0 (Menu screen)
    if current_screen == 0:
        screen.fill((25, 255, 25))  # always the first drawing command
        scene_title = scene_title_font.render( 'Hungry Roger', True, (255,255,255))
        screen.blit(scene_title, (0, 0))

    elif current_screen == 1:
        # Scene 1 (Instructions screen)
        screen.fill((128, 0, 0)) 
        scene_title = scene_title_font.render('How to Play', True, (255, 255, 255))
        screen.blit(scene_title, (0, 0))
        screen_title = scene_title_font.render('Move with W A S D', True, (255,255,255))
        screen.blit(screen_title, (0,99))
        screen_title = scene_title_font.render('Collect 20 black flies to win', True, (255,255,255))
        screen.blit(screen_title, (0,289))

    if current_screen == 2:
        # scene 2 (game screen)
        screen.fill((86,125,70))
    
        # RIVER
        pygame.draw.line(screen, (38,102,145), (329,6), (241, 191), 60)
        pygame.draw.line(screen, (38,102,145), (241, 181), (306,260), 60)
        pygame.draw.line(screen, (38,102,145), (303, 244), (335,480), 52)

        # BUSH
       
        for x_offset in range(100, 670, 345):
            for y_offset in range(100, 320, 170): 
                pygame.draw.circle(screen, (11,102,35), (x_offset, y_offset), 25)
                pygame.draw.circle(screen, (11,102,35), (x_offset + 20, y_offset + 20), 25)
                pygame.draw.circle(screen, (11,102,35), (x_offset - 20, y_offset + 20), 25)
        pygame.draw.rect(screen,(0,0,0),(fly_rect),50)
   
        pygame.draw.rect(screen, (255,0,0), (0,0,670,5),600)
        pygame.draw.rect(screen, (255,0,0), (0,3,5,480),600)
        pygame.draw.rect(screen, (255,0,0), (4,477,685,5),600)
        pygame.draw.rect(screen, (255,0,0), (637,3,5,480),600)
        pygame.draw.rect(screen, (0,0,0), (fly_rect),50)

        # ROGER
        pygame.draw.rect(screen, (215,250,215), (roger_x, roger_y, 40,40),25)
        score_text = score_font.render(f'Score: {score}', False, (0, 0, 0))
        screen.blit(score_text,(67,340))
        
    elif current_screen == 3: 
        # scene 3 (end) 
        screen.fill((128,16,200))
        scene_title = scene_title_font.render('CONGRATULATIONS', True, (255, 255, 255))
        screen.blit(scene_title, (88,31))
        scene_title = end_scene_font.render('Roger The Frog is now full from flies', True, (255,255,255))
        screen.blit(scene_title, (158,212))
    

    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
