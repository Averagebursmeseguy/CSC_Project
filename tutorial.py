import pygame

def loadImages():
    tutorialImages = []

    for i in range(0, 4):
        tutorialImages.append(pygame.image.load(f'./assets/tutorial/image{i}.webp').convert_alpha())

    return tutorialImages