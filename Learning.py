# Pygame template - skeleton for a new platform
import pygame
import math


WIDTH = 1000
HEIGHT = 500
FPS = 30

#define colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)



class Sensor():
    def __init__(self, position_of_sensor):
        self.xo = 500
        self.yo = 250
        self.position = (self.xo, self.yo)
        self.display(self.position)
        self.rot = 0 
        self.pos = position_of_sensor
        

    def display(self, position):
        pygame.draw.circle(screen, BLUE, (position), 15)
    
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

        self.xo += int(self.speedx)
        self.yo += int(self.speedy)
        
    
    def calculate_pos(self):
        self.update()
        if self.pos == 0:
            self.position = (self.xo, self.yo)
            self.display(self.position)
        
        if self.pos == 1:
            self.x1 = self. xo + int(45 * math.cos(self.rot) )
            self.y1 = self.yo + int(45 * math.sin(self.rot) )
            self.position = (self.x1, self.y1)
            self.display(self.position)
        
        if self.pos == 2:
            self.x1 = self. xo + int(-45 * math.cos(self.rot) )
            self.y1 = self.yo + int(-45 * math.sin(self.rot) )
            self.position = (self.x1, self.y1)
            self.display(self.position)
        
        if self.pos == 3:
            self.x1 = self. xo + int(45 * math.sin(self.rot) )
            self.y1 = self.yo - int(45 * math.cos(self.rot) )
            self.position = (self.x1, self.y1)
            self.display(self.position)
            
            
            
      
        
#initialize pygame and create window 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SIMULATOR")
clock = pygame.time.Clock()



my_first_sensor = Sensor(0)
my_second_sensor = Sensor(1)
my_third_sensor = Sensor(2)
my_forth_sensor = Sensor(3)


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
    
            
    #Draw / render 
    screen.fill(BLACK)
    my_first_sensor.calculate_pos()
    my_second_sensor.calculate_pos()
    my_third_sensor.calculate_pos()
    my_forth_sensor.calculate_pos()
    
    #After drawing everything, flip display
    pygame.display.flip()
    
pygame.quit()


