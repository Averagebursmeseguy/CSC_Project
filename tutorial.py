import pygame

def loadImages():
    tutorialImages = []

    for i in range(0, 5):
        tutorialImages.append(pygame.image.load(f'./assets/tutorial/image{i}.png').convert_alpha())

    return tutorialImages