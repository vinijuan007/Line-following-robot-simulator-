# Pygame template - skeleton for a new platform
import pygame
import math





WIDTH = 1400
HEIGHT = 700
FPS = 30
HORIZONTAL_DISTANCE = 35
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


class Sensor():
    def __init__(self, horizontal, vertical, value_of_sensor):
        self.xo = 300
        self.yo = 100
        self.x1 = 500
        self.y1 = 250
        self.position = (self.xo, self.yo)
        self.color = BLUE
        self.rot = 1.57 
        self.horizontal = horizontal
        self.vertical = vertical
        self.radius = RADIUS_SENSOR
        self.status = 0
        #to rememeber value of sensor swhile not true
        self.value_of_sensor1 = value_of_sensor
        self.value_of_sensor = 0
        self.turning_status = 0
        self.forward_status = 0
        self.display()
        
        
    def repaint(self, color):
        self.color = color 
        if self.color == RED:
            self.status = 1
            self.value_of_sensor = self.value_of_sensor1
        else:
            self.status = 0
            self.value_of_sensor = 0
        
        
        
    def display(self):
        pygame.draw.circle(screen, self.color, (self.position), self.radius)
    
    
    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.speedrot = 0
        
        keystate = pygame.key.get_pressed()
        #Rotation 
        if keystate[pygame.K_a] or self.turning_status == 1:
            self.speedrot = -0.1

        elif keystate[pygame.K_d] or self.turning_status == 2:
            self.speedrot =  0.1
        else:
            self.speedrot = 0
            
        self.rot = (self.rot + self.speedrot)

        #Forward
        if keystate[pygame.K_SPACE]:
            self.speedy =   0
            self.speedx =   0
        elif keystate[pygame.K_w] or self.forward_status == 1:
            self.speedy =  -10*math.cos(self.rot)
            self.speedx =   10*math.sin(self.rot)
        else:
            self.speedy = 0
            self.speedx = 0
            
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


move_foward = list()
move_foward.append(1)
move_foward.append(32)
move_foward.append(33)

move_rigth = list()
move_rigth.append(2)
move_rigth.append(3)
move_rigth.append(34)
move_rigth.append(35)
###
move_rigth.append(8)
move_rigth.append(9)
move_rigth.append(10)
move_rigth.append(11)
move_rigth.append(40)
move_rigth.append(41)
move_rigth.append(42)
move_rigth.append(43)

move_left = list()
move_left.append(4)
move_left.append(5)
move_left.append(16)
move_left.append(17)
move_left.append(20)
move_left.append(21)
move_left.append(36)
move_left.append(37)
move_left.append(48)
move_left.append(49)
move_left.append(52)
move_left.append(52)


def compare_list(a, errorx):
    new_list = []
    for i in range(0, len(a)):
        new_list.append(errorx == a[i])
    return new_list
        


def Control(s1s, s2s, s3s, s4s, s5s, s6s):
    error = 0
    sensors = list()
    sensors.append(s1s)
    sensors.append(s2s)
    sensors.append(s3s)
    sensors.append(s4s)
    sensors.append(s5s)
    sensors.append(s6s)
    for i in range(0, len(sensors)):
        error += sensors[i].value_of_sensor
        a = "Error = " + str(error)
        sensors[i].turning_status = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render( a, True, BLACK, WHITE )
    textRect = text.get_rect()
    textRect.center = (1200, 50)
    screen.blit(text, textRect)

        
    
    if any(compare_list(move_foward, error)):
        for i in range(0, len(sensors)):
            sensors[i].forward_status = 1
            sensors[i].turning_status = 0
    elif any(compare_list(move_rigth, error)):
        for i in range(0, len(sensors)):
            sensors[i].forward_status = 1
            sensors[i].turning_status = 2
    elif any(compare_list(move_left, error)):
        for i in range(0, len(sensors)):
            sensors[i].forward_status = 1
            sensors[i].turning_status = 1
        
    
       
#initialize pygame and create window 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SIMULATOR")
clock = pygame.time.Clock()


##SENSORS##
s1 = Sensor(0, 0, 1)
s2 = Sensor(HORIZONTAL_DISTANCE, VERTICAL_DISTANCE ,2)
s3 = Sensor(-HORIZONTAL_DISTANCE, VERTICAL_DISTANCE, 4)
s4 = Sensor(2*HORIZONTAL_DISTANCE-25, 0, 8)
s5 = Sensor(-2*HORIZONTAL_DISTANCE+25, 0, 16)
s6 = Sensor(0, 2*VERTICAL_DISTANCE, 32)

sensors = list()
sensors.append(s1)
sensors.append(s2)
sensors.append(s3)
sensors.append(s4)
sensors.append(s5)
sensors.append(s6)

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
            
    #Update
    for i in range(0, len(sensors)):
        for j in range(0, len(lines)):
            a = check_distance(lines[j].x, lines[j].y, sensors[i].x1, sensors[i].y1, lines[j].radius, sensors[i].radius)
            if a == True:
                sensors[i].repaint(RED)
                break
            else:
                sensors[i].repaint(BLUE)  
            
    screen.fill(BLACK)
    
    Control(s1, s2, s3, s4, s5, s6)
   
    #Draw / render 
    
    
    for j in range(0, len(lines)):
        lines[j].display()
        
    for i in range(0, len(sensors)):
        sensors[i].calculate_pos()
    
    
    #After drawing everything, flip display
    pygame.display.update()
    
pygame.quit()


