import tkinter
import pygame
import random
import map_utils

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
rocket = pygame.image.load("./assets/placeholder_rocket.png").convert_alpha()

print(map_utils.centreFinder(screen))

while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    map_utils.drawGrid(map_utils.centreFinder(screen), screen)
    
    # pygame.draw.line(screen, (255, 255, 255), (100, 100), (700, 100), 1)
    # pygame.draw.line(screen, (255, 255, 255), (100, 100), (100, 700), 1)

    pygame.display.flip() #renders all the sprites and displays them in window. Don't fuck with this one.
pygame.quit()
