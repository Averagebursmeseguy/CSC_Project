import pygame
import map_utils
import random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((800, 800))
gridSize = 100
running = True

terrain = pygame.image.load("./assets/terrain.png").convert_alpha()
terrain = pygame.transform.scale(terrain, (gridSize, gridSize))

#This makes the blocks
blocks = map_utils.generateObstacles(terrain, 5, (random.randint(0, 6), random.randint(0, 8)))


while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    for block in blocks:
        screen.blit(block[0], (block[1][0]*gridSize, block[1][1]*gridSize))

    map_utils.drawGrid(screen, gridSize, WHITE)
    pygame.display.flip() #renders all the sprites and displays them in window. Don't fuck with this one.
pygame.quit()
