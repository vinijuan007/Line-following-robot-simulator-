# Pygame template - skeleton for a new platform
import pygame
import math
import pygame.gfxdraw


WIDTH = 1200
HEIGHT = 700
FPS = 30
HORIZONTAL_DISTANCE = 15
VERTICAL_DISTANCE = 20
RADIUS = 7
SIZE_OF_LINE = 20

#define colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)

class Line(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE_OF_LINE, HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = (HEIGHT)
        self.rect.centerx = (WIDTH/2)

 

class Sensor(pygame.sprite.Sprite):
    def __init__(self, horizontal, vertical):
                
        self.xo = 500
        self.yo = 250
        self.position = (self.xo, self.yo)
        self.rot = 0 
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = GREEN
        
        
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2*RADIUS/1.41, 2*RADIUS/1.41))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (self.position)
        

    def repaint(self, color):
        self.color = color 
        self.image.fill(self.color)

    # def display(self, position):
    #     pygame.draw.circle(self.image, self.color, (position), RADIUS)
    #     self.image.fill(self.color)
    
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
        if keystate[pygame.K_s]:
            self.speedy =   10*math.cos(self.rot)
            self.speedx =   -10*math.sin(self.rot)

        self.xo += int(self.speedx)
        self.yo += int(self.speedy)
        
    
    def calculate_pos(self):
        self.update()
        self.x1 = self. xo + int(self.horizontal * math.cos(self.rot) )+ int(self.vertical * math.sin(self.rot) )
        self.y1 = self.yo + int(self.horizontal  * math.sin(self.rot) )- int(self.vertical * math.cos(self.rot) )
        self.position = (self.x1, self.y1)
        self.rect.center = (self.position)
        
        # self.display(self.position)
       
      
        
#initialize pygame and create window 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SIMULATOR")
clock = pygame.time.Clock()


my_first_sensor = Sensor(0, 0)
my_second_sensor = Sensor(HORIZONTAL_DISTANCE, VERTICAL_DISTANCE)
my_third_sensor = Sensor(-HORIZONTAL_DISTANCE, VERTICAL_DISTANCE)
my_forth_sensor = Sensor(2*HORIZONTAL_DISTANCE, 0)
my_fith_sensor = Sensor(-2*HORIZONTAL_DISTANCE, 0)
my_sixth_sensor = Sensor(0, 2*VERTICAL_DISTANCE)

line1 = Line()


all_sprites = pygame.sprite.Group()
all_sprites.add(line1)
all_sprites.add(my_first_sensor)
all_sprites.add(my_second_sensor)
all_sprites.add(my_third_sensor)
all_sprites.add(my_forth_sensor)
all_sprites.add(my_fith_sensor)
all_sprites.add(my_sixth_sensor)

all_lines = pygame.sprite.Group()
all_lines.add(line1)

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
            

  
    my_first_sensor.calculate_pos()
    my_second_sensor.calculate_pos()
    my_third_sensor.calculate_pos()
    my_forth_sensor.calculate_pos()
    my_fith_sensor.calculate_pos()
    my_sixth_sensor.calculate_pos()
    
    my_first_sensor.repaint(GREEN)
    collision_list = pygame.sprite.spritecollide(my_first_sensor,all_lines,False)
    for i in collision_list:
         my_first_sensor.repaint(RED)
    
    my_second_sensor.repaint(GREEN)
    collision_list = pygame.sprite.spritecollide(my_second_sensor,all_lines,False)
    for i in collision_list:
         my_second_sensor.repaint(RED)
    
    my_third_sensor.repaint(GREEN)
    collision_list = pygame.sprite.spritecollide(my_third_sensor,all_lines,False)
    for i in collision_list:
         my_third_sensor.repaint(RED)
    
    my_forth_sensor.repaint(GREEN)
    collision_list = pygame.sprite.spritecollide(my_forth_sensor,all_lines,False)
    for i in collision_list:
         my_forth_sensor.repaint(RED)
         
    my_fith_sensor.repaint(GREEN)
    collision_list = pygame.sprite.spritecollide(my_fith_sensor,all_lines,False)
    for i in collision_list:
         my_fith_sensor.repaint(RED)
    
    my_sixth_sensor.repaint(GREEN)
    collision_list = pygame.sprite.spritecollide(my_sixth_sensor,all_lines,False)
    for i in collision_list:
         my_sixth_sensor.repaint(RED)

    #Game Logic
    all_sprites.update()

 
    #Drawing on Screen
    screen.fill(BLACK)

    
    
    all_sprites.draw(screen)

 
    #Refresh Screen
    pygame.display.flip()
 
    #Number of frames per secong e.g. 60
    clock.tick(FPS)
 
pygame.quit() 