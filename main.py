import pygame
import pygame_gui
import map
import rocket

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((900, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((900, 800))
gameMap = map.Map(15, 2, 40, screen)
gameMap.scatterDebris()
player = rocket.Rocket('./assets/placeholder_rocket.png',(0, 0) , gameMap)

saveButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(0,0, 100, 50),
    text=("Check code"),
    manager=manager,
    anchors = {"top-left"}
)
runButton = pygame_gui.elements.UIButton(
    relative_rect = pygame.Rect(100, 0, 100, 50),
    text = ("execute"),
    manager = manager,
    anchors = {"top-left"}
)
codeEntryWindow = pygame_gui.elements.UITextEntryBox(
    relative_rect=pygame.Rect((0, 50), (screen.width * 0.3, screen.height * 0.6)),
    manager = manager
)
rocketLangterminal = pygame_gui.elements.UITextBox(
    relative_rect = pygame.Rect((0, screen.height*0.7), (screen.width * 0.3, screen.height * 0.3)),
    manager = manager,
    html_text= "rocketLang engine V0.0.1\n ©RocketLang, all rights reserved"
)

running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    screen.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            manager.set_window_resolution((event.w, event.h))
            codeEntryWindow.set_dimensions((event.w * 0.5, event.h * 0.6))
            rocketLangterminal.set_dimensions((event.w * 0.5, event.h * 0.3))
            rocketLangterminal.set_relative_position((0, event.h * 0.7))

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == saveButton:
                print('button pressed')
        
        manager.process_events(event)
    
    
    manager.update(time_delta)
    manager.draw_ui(screen)
    gameMap.drawMap()
    player.move("down", 6)
    player.move("forward", 2)
    player.draw()
    pygame.display.flip() #renders all the sprites and displays them in window. Don't fuck with this one.
pygame.quit()
