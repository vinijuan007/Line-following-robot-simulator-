# Pygame template - skeleton for a new platform
import pygame
import math


WIDTH = 1400
HEIGHT = 800
FPS = 30
HORIZONTAL_DISTANCE = 15
VERTICAL_DISTANCE = 20
RADIUS_SENSOR = 7
LINE_GAP = 65
SPACING = 4

#define colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)


       
class Line():
    def __init__(self, x, y):
        
        self.x = x
        self.y = y 
        self.position = (self.x , self.y)
        self.radius = 20
        
        self.display()
        

    def display(self):
        pygame.draw.circle(screen, WHITE, (self.position), self.radius)
    




       
#initialize pygame and create window 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SIMULATOR")
clock = pygame.time.Clock()


##DESIGN OF TRACK ##
lines = list()
####PART 1#####
for i in range(0, 400, SPACING):
    lines.append(Line(i+200, 100))

####PART 2#####
for i in range(0, 400, SPACING):
    lines.append(Line(i+600+LINE_GAP, 100))

####PART 3#####
for i in range(0, 400, SPACING):
    lines.append(Line(1050+int(200*math.sin(0.008*i)), 300+int(200*math.cos(0.008*i))))

####PART 4#####
for i in range(0, 850, SPACING):
    lines.append(Line(1050-i, 460+int(40*math.cos(0.017*i))))

####PART 5#####
for i in range(0, 330, SPACING):
    lines.append(Line(200, 440-i))




    
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

            
    #Draw / render 
    screen.fill(BLACK)
    
    for j in range(0, len(lines)):
        lines[j].display()
        

    
    #After drawing everything, flip display
    pygame.display.update()
    
pygame.quit()


