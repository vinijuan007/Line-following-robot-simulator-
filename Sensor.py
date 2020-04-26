import pygame
import math


WIDTH = 1000
HEIGHT = 500
FPS = 60

#define colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)



class Player(pygame.sprite.Sprite):
    #sprite for player 
    #constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        #sprite rectangle
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT
        
        self.speedx = 0
        self.speedy = 0
        self.speedrot = 0
        self.rot = 0
        
        
    
    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.speedrot = 0
        
        keystate = pygame.key.get_pressed()
        #Rotation w
        if keystate[pygame.K_a]:
            self.speedrot = -0.1
        if keystate[pygame.K_d]:
            self.speedrot =  0.1
            
        self.rot = (self.rot + self.speedrot)

        
        if keystate[pygame.K_w]:
            self.speedy =  -10*math.cos(self.rot)
            self.speedx =   10*math.sin(self.rot)

            
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy