# Importowane pliki
import pygame
from sys import exit
from pygame.locals import *
import math


#Pygame ustawiena
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('TanksGame')
clock = pygame.time.Clock()

#Orginalna textura do obrotu czołgu
original_hull = pygame.image.load('assets/tank_hull.png').convert_alpha()
original_turett = pygame.image.load('assets/tank_turett.png').convert_alpha()

#klasa 'Tank'
class Tank:
    def __init__(self):
        self.hull = pygame.image.load('assets/tank_hull.png').convert_alpha()
        self.turett = pygame.image.load('assets/tank_turett.png').convert_alpha()
        self.position_x_turett = 400
        self.position_y_turett = 200
        self.position_x_hull = 400
        self.position_y_hull = 200
        self.angle = 0
        self.speed = 3

    def rect(self):
        self.tank_hull_rect = self.hull.get_rect(center = (self.position_x_hull,self.position_y_hull))
        self.tank_turett_rect =  self.turett.get_rect(center = (self.position_x_turett,self.position_y_turett))

    def hull_rotate(self):
        self.hull_rotated = pygame.transform.rotate(original_hull, self.angle + 90)
        self.hull = self.hull_rotated

    def turett_rotate(self):
        self.turett_rotated = pygame.transform.rotate(original_turett, self.angle + 90)
        self.turett = self.turett_rotated

    def movement_front(self):
        self.direction_x = math.cos(math.radians(self.angle)) #cos
        self.direction_y = -math.sin(math.radians(self.angle)) #sin

        self.position_x_hull += self.direction_x * self.speed #x
        self.position_y_hull += self.direction_y * self.speed #y

        self.position_x_turett += self.direction_x * self.speed
        self.position_y_turett += self.direction_y * self.speed


    def movement_back(self):
        self.direction_x = math.cos(math.radians(self.angle)) #cos
        self.direction_y = -math.sin(math.radians(self.angle)) #sin

        self.position_x_hull -= self.direction_x * self.speed #x
        self.position_y_hull -= self.direction_y * self.speed #y

        self.position_x_turett -= self.direction_x * self.speed
        self.position_y_turett -= self.direction_y * self.speed

tank = Tank()
tank.rect()
#tło
back_ground = pygame.Surface((800,400))
back_ground.fill('Grey')


#Wyświetlanie obrazu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tank.hull_rotate()
    tank.turett_rotate()
    #Wyświetlanie tekstur i hitboxy
    screen.blit(back_ground,(0,0))

    screen.blit(tank.hull,tank.tank_hull_rect)
    screen.blit(tank.turett,tank.tank_turett_rect)

    #Sterowanie czołgiem.
    keys = pygame.key.get_pressed()


    if keys[pygame.K_w]:
        tank.movement_front()
        tank.rect()
        

    if keys[pygame.K_s]:
        tank.movement_back()
        tank.rect()

    if keys[pygame.K_a]:
        tank.angle += 2
        tank.hull_rotate()
        tank.turett_rotate()
        tank.rect()
        
        
    if keys[pygame.K_d]:
       tank.angle -= 2
       tank.hull_rotate()
       tank.turett_rotate()
       tank.rect()

    #Granica mapy

    while tank.position_x_hull and tank.position_x_turett <= 0:
        tank.position_x_hull += 5
        tank.position_x_turett += 5
    
    while tank.position_x_hull and tank.position_x_turett >= 800:
        tank.position_x_hull -= 5
        tank.position_x_turett -= 5

    while tank.position_y_hull and tank.position_y_turett <= 0:
        tank.position_y_hull += 5
        tank.position_y_turett += 5

    while tank.position_y_hull and tank.position_y_turett >= 400:
        tank.position_y_hull -= 5
        tank.position_y_turett -= 5

    pygame.display.update()
    clock.tick(60)


