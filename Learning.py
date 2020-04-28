# Pygame template - skeleton for a new platform
import pygame
import math


WIDTH = 1200
HEIGHT = 700
FPS = 30
HORIZONTAL_DISTANCE = 15
VERTICAL_DISTANCE = 20

#define colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)



class Sensor():
    def __init__(self, horizontal, vertical):
        self.xo = 500
        self.yo = 250
        self.position = (self.xo, self.yo)
        self.display(self.position)
        self.rot = 0 
        self.horizontal = horizontal
        self.vertical = vertical
        

    def display(self, position):
        pygame.draw.circle(screen, BLUE, (position), 7)
    
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
        self.x1 = self. xo + int(self.horizontal * math.cos(self.rot) )+ int(self.vertical * math.sin(self.rot) )
        self.y1 = self.yo + int(self.horizontal  * math.sin(self.rot) )- int(self.vertical * math.cos(self.rot) )
        self.position = (self.x1, self.y1)
        self.display(self.position)
       
class Line():
    def __init__(self):
        self.display()

    def display(self):
        
        #top
        for i in range(200,800, 3):
            position = (i, 200)
            pygame.draw.circle(screen, WHITE, (position), 20)
        
        #bottom 
        for i in range(200,800, 3):
            position = (i, 500)
            pygame.draw.circle(screen, WHITE, (position), 20)
     #left
        for i in range(200,500, 3):
            position = (200, i)
            pygame.draw.circle(screen, WHITE, (position), 20)
        
        #bottom 
        for i in range(200,500, 3):
            position = (800, i)
            pygame.draw.circle(screen, WHITE, (position), 20)
                
      
        
#initialize pygame and create window 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SIMULATOR")
clock = pygame.time.Clock()


line = Line()
my_first_sensor = Sensor(0, 0)
my_second_sensor = Sensor(HORIZONTAL_DISTANCE, VERTICAL_DISTANCE)
my_third_sensor = Sensor(-HORIZONTAL_DISTANCE, VERTICAL_DISTANCE)
my_forth_sensor = Sensor(2*HORIZONTAL_DISTANCE, 0)
my_fith_sensor = Sensor(-2*HORIZONTAL_DISTANCE, 0)
my_sixth_sensor = Sensor(0, 2*VERTICAL_DISTANCE)


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
    line.display()
    my_first_sensor.calculate_pos()
    my_second_sensor.calculate_pos()
    my_third_sensor.calculate_pos()
    my_forth_sensor.calculate_pos()
    my_fith_sensor.calculate_pos()
    my_sixth_sensor.calculate_pos()
    
    #After drawing everything, flip display
    pygame.display.update()
    
pygame.quit()


