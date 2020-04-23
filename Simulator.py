# Pygame template - skeleton for a new platform
import pygame
from Sensor import Player

WIDTH = 360
HEIGHT = 480
FPS = 30

#define colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)


#initialize pygame and create window 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SIMULATOR")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

#Game Loop 
running = True 
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    #Proces inputs (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
            
    #Update
    all_sprites.update()
            
    #Draw / render 
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #After drwing everything, flip display
    pygame.display.flip()
    
pygame.quit()