# Pygame template - skeleton for a new platform
import pygame
import math


WIDTH = 1200
HEIGHT = 700
FPS = 30
HORIZONTAL_DISTANCE = 15
VERTICAL_DISTANCE = 20
RADIUS_SENSOR = 7

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
        self.x1 = 500
        self.y1 = 250
        self.position = (self.xo, self.yo)
        self.color = BLUE
        self.rot = 0 
        self.horizontal = horizontal
        self.vertical = vertical
        self.radius = RADIUS_SENSOR
        
        self.display()
        
        
    def repaint(self, color):
        self.color = color 
        
        
    def display(self):
        pygame.draw.circle(screen, self.color, (self.position), self.radius)
    
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
        self.display()
    
       
class Line():
    def __init__(self, x, y):
        
        self.x = x
        self.y = y 
        self.position = (self.x , self.y)
        self.radius = 20
        
        self.display()
        

    def display(self):
        pygame.draw.circle(screen, WHITE, (self.position), self.radius)
    


                
      
 
def check_distance(xl, yl, xs, ys, rl, rs):
    distance = math.hypot(xl-xs, yl-ys)
    if distance <= (rs+rl) :
        return True
    else :
        return False 


       
#initialize pygame and create window 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SIMULATOR")
clock = pygame.time.Clock()


##SENSORS##
s1 = Sensor(0, 0)
s2 = Sensor(HORIZONTAL_DISTANCE, VERTICAL_DISTANCE)
s3 = Sensor(-HORIZONTAL_DISTANCE, VERTICAL_DISTANCE)
s4 = Sensor(2*HORIZONTAL_DISTANCE, 0)
s5 = Sensor(-2*HORIZONTAL_DISTANCE, 0)
s6 = Sensor(0, 2*VERTICAL_DISTANCE)

sensors = list()
sensors.append(s1)
sensors.append(s2)
sensors.append(s3)
sensors.append(s4)
sensors.append(s5)
sensors.append(s6)

##LINE##
lines = list()
for i in range(0, 600):
    lines.append(Line(350, i))

    
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
    for i in range(0, len(sensors)):
        for j in range(0, len(lines)):
            a = check_distance(lines[j].x, lines[j].y, sensors[i].x1, sensors[i].y1, lines[j].radius, sensors[i].radius)
            if a == True:
                sensors[i].repaint(RED)
                break
            else:
                sensors[i].repaint(BLUE)  
            
    #Draw / render 
    screen.fill(BLACK)
    
    for j in range(0, len(lines)):
        lines[j].display()
        
    for i in range(0, len(sensors)):
        sensors[i].calculate_pos()
    
    
    #After drawing everything, flip display
    pygame.display.update()
    
pygame.quit()


