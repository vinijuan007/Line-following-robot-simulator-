import pygame
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)

WIDTH = 360
HEIGHT = 480
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    #sprite for player 
    #constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        #sprite rectangle
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT
        self.speedx = 0
        self.speedy = 0
        self.speedrot = 0
        self.rot = 0
        
    
    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.speedrot = 0
        keystate = pygame.key.get_pressed()
        #Rotation 
        if keystate[pygame.K_a]:
            self.speedrot = 5
        if keystate[pygame.K_d]:
            self.speedrot = -5
            
        self.rot += self.speedrot%360
        print("angle=",self.rot)
        #pygame.transform.rotate(self.rect ,self.rot)
        
        
        if keystate[pygame.K_w]:
            self.speedy = -5*math.cos(self.rot)
            self.speedx =  5*math.sin(self.rot)
        if keystate[pygame.K_s]:
            self.speedy =  5*math.cos(self.rot)
            self.speedx =  5*math.sin(self.rot)
            
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
            
    
