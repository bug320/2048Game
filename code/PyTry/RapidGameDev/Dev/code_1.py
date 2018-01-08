# -*- coding:utf-8 -*-

import pygame, math, sys
from pygame.locals import *

screen = pygame.display.set_mode((1024, 768))
car = pygame.image.load('./Sprites/Player.png')
clock = pygame.time.Clock()
k_up = k_down = k_left = k_right = 0
speed = direction = 0
position = (100, 100)
TURN_SPEED = 5
ACCELERATION = 2
MAX_FORWARD_SPEED = 10
MAX_REVERSE_SPPED = -5
BLACK = (0, 0, 0)

while 1:
    # USER INPUT
    clock.tick(30)
    for evnet in pygame.event.get():
        if not hasattr(evnet, 'key'):continue
        down = evnet.type == KEYDOWN
        if evnet.key == K_RIGHT: k_right = down * -5
        elif evnet.key == K_LEFT: k_left = down *5
        elif evnet.key == K_UP: k_up = down * 2
        elif evnet.key == K_DOWN: k_down = down * -2
        elif evnet.key == K_ESCAPE: sys.exit(0)    # quit the game
    screen.fill(BLACK)

    # SIMULATION
    # ... new speed and direction based on acceleration and TURN_SPEED
    speed += (k_up + k_down)
    if speed > MAX_FORWARD_SPEED: speed = MAX_FORWARD_SPEED
    if speed < MAX_REVERSE_SPPED: speed = MAX_REVERSE_SPPED
    direction += (k_right + k_left)
    
    # ... new position based on current position, speed and direction
    x,y = position
    rad = direction * math.pi / 180
    x += -speed*math.sin(rad)
    y += -speed*math.cos(rad)
    position = (x, y)

    # RENDERING
    # ... rotate the car image for direction
    rotated = pygame.transform.rotate(car, direction)
    
    # ... position the car on screen
    rect = rotated.get_rect()
    rect.center = position

    # ... render the car to screen
    screen.blit(rotated,rect)
    pygame.display.flip()

    pass
