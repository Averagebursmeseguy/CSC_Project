import pygame
import map_utils

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((800, 800))
gridSize = 50
running = True

print(map_utils.centreFinder(screen))

while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    map_utils.drawGrid(screen, gridSize, WHITE)

    pygame.display.flip() #renders all the sprites and displays them in window. Don't fuck with this one.
pygame.quit()
