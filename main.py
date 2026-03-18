import tkinter
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
rocket = pygame.image.load("./assets/placeholder_rocket.png")

y = 600
random_coords = random.choice([200, 500, 300, 400, 700, 800])

while running:

    screen.fill((20, 20, 20))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if y > 0:
        y -= 1
    else:
        y = 600
        random_coords = random.choice([200, 500, 300, 400, 700, 800])

    print(y)
    screen.blit(rocket, (random_coords, y))

    pygame.display.flip() #renders all the sprites and displays them in window. Don't fuck with this one.
pygame.quit()
