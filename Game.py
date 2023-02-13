import pygame
import sys

pygame.init()

screen_width = 1024
screen_height = 700



#For getting the resolution of the users PC
def get_screen_resolution():
    mode = pygame.display.list_modes()
    return mode[0]
 
#Simple Screen Setup
resolution = get_screen_resolution()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Runner")
Run = True
fps = pygame.time.Clock()

#Allows the user to be able to go fullscreen
def fullscreen():
    key = pygame.key.get_pressed()
    if key[pygame.K_f]:
        screen = pygame.display.set_mode(resolution)

#Handles the Events of the game
def handle_events():
    global player_y,Gravity,Jump
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False 
            pygame.quit()
            exit()
        #Handles the Space bar event 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Gravity = -30
                

#Character,Rock and background
Hero = pygame.image.load("Hero2.png").convert_alpha()
#Declare the Hero Rect 
Hero_rect = Hero.get_rect(bottomleft = (10,630))
background = pygame.image.load("background.jpg").convert_alpha()
Rock = pygame.image.load("Game_rock.png").convert_alpha()
#Declare the Rocks Rect
Rock_rect = Rock.get_rect(bottomright = (1020,650))



#Gravity and Movement
Gravity = 0

#Rock Coordinates
Rock_x = 780
Rock_y = 500

#Rock movement        
def Rock_movement():
    Rock_rect.x -= 7 
    
    if Rock_rect.x <= 0:
        Rock_rect.x = 1020
        
#Mange Collision
def collision():
    global Score
    global score_text
    
        
def score_increment():
    global Score
    global score_text
    global Score_rect
    global Run
    
    #Score Text
    Score = pygame.time.get_ticks()
    score_font = pygame.font.Font(None,32)
    score_text = score_font.render(f"Your score is {Score}",None,"White","Black")
    Score_rect = score_text.get_rect(center = (400,50))
    
    if Hero_rect.colliderect(Rock_rect):
        score_text = score_font.render("You Have Lost",None,"White","Black")
        Run = False

        
    
    



while Run:
    pygame.display.flip()
    pygame.display.update()
    handle_events()           
    fullscreen()
    Rock_movement() 
    collision()
    score_increment()
    
    
    
    Gravity += 1
    Hero_rect.y += Gravity
    
    if Hero_rect.bottom >= 630: Hero_rect.bottom = 630
    print(Score)
    
    if Score >= 5000:
        Rock_rect.x -= 9

    
    fps.tick(60)
    screen.blit(background,(0,0))
    screen.blit(Hero,Hero_rect)
    screen.blit(Rock,Rock_rect)
    screen.blit(score_text,Score_rect)
    
    
    
    
    
    
    




