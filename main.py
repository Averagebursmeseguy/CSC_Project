import tkinter
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

running = True
rocket = pygame.image.load("./assets/placeholder_rocket.png").convert_alpha()

def drawGrid(startpos, endpos, scaling, surface, linecolor):

    startx, starty = startpos
    endx, endy = endpos

    #Make vertical and horiz lines first
    pygame.draw.line(surface, linecolor, (startx, starty), (endx, starty), 1)
    pygame.draw.line(surface, linecolor, (startx, starty), (startx, endy), 1)
    pygame.draw.line(surface, linecolor, (endx, endy), (startx, endy), 1)
    pygame.draw.line(surface, linecolor, (endx, endy), (endx, starty), 1)

    for i in range(int(endx / scaling)):
        increment = startx + (scaling * i)
        pygame.draw.line(surface, linecolor, (increment, starty), (increment, endy))

    for i in range(int(endy / scaling)):
        increment = starty + (scaling * i)
        pygame.draw.line(surface, linecolor, (startx, increment), (endx, increment))


while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawGrid((100, 100), (700, 700), 50, screen, (255, 255, 255))
    
    # pygame.draw.line(screen, (255, 255, 255), (100, 100), (700, 100), 1)
    # pygame.draw.line(screen, (255, 255, 255), (100, 100), (100, 700), 1)


    
    


    pygame.display.flip() #renders all the sprites and displays them in window. Don't fuck with this one.
pygame.quit()
