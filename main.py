# TODO: Make a "map" dict that scales with display size 

import pygame
import pygame_gui
import map

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((800, 800))

button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(0,0, 200, 200),
    text=("click me"),
    manager=manager,
    anchors = {'center': 'center'}
)

running = True

gameMap = map.Map(15, 2, 50, screen)
gameMap.scatterDebris()

while running:
    time_delta = clock.tick(60) / 1000.0
    screen.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            manager.set_window_resolution((event.w, event.h))

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button:
                print('button pressed')
        
        manager.process_events(event)
    
    
    manager.update(time_delta)
    manager.draw_ui(screen)
    gameMap.drawMap()
    pygame.display.flip() #renders all the sprites and displays them in window. Don't fuck with this one.
pygame.quit()
