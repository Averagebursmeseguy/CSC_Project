import pygame
import pygame_gui
import map, rocket, entity, random, tutorial

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
alice = entity.Entity(True, "./assets/objective.png", gameMap, "objective")

tutoImages = tutorial.loadImages()
currentIndex = 0

validateButton = pygame_gui.elements.UIButton(
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
gameOverPanel = pygame_gui.elements.UIPanel(
    relative_rect = pygame.Rect((0, 0), (300, 200)),
    manager = manager, 
    anchors = {"center": "center"}
)

gameOverLable = pygame_gui.elements.UILabel(
    relative_rect = pygame.Rect((0, 0), (300, 100)),
    manager = manager,
    text = "Game Over. You crashed.",
    container = gameOverPanel
)

retryButton = pygame_gui.elements.UIButton(
    relative_rect = pygame.Rect((10, 120), (100, 50)),
    text = "Retry",
    manager = manager,
    container = gameOverPanel
)

exitButton = pygame_gui.elements.UIButton(
    relative_rect = pygame.Rect((180, 120), (100, 50)),
    text = "Quit",
    manager = manager,
    container = gameOverPanel
)

TutorialPanel = pygame_gui.elements.UIPanel(
    relative_rect= pygame.Rect((0, 0), (800, 600)),
    manager = manager,
    anchors={"center": "center"}
)

tutorialButton = pygame_gui.elements.UIButton(
    relative_rect = pygame.Rect((200, 0), (100, 50)),
    text = "Show Tutorial",
    manager = manager

)

tutorialNextButton = pygame_gui.elements.UIButton(
    relative_rect = pygame.Rect((100, 0), (100, 50)),
    manager = manager,
    container = TutorialPanel,
    text = "Next slide"
)

tutorialPreviousButton = pygame_gui.elements.UIButton(
    relative_rect = pygame.Rect((0, 0), (100, 50)),
    manager = manager,
    container = TutorialPanel,
    text = "Previous slide"
)

tutorialSlideshowDisplay = pygame_gui.elements.UIImage(
    relative_rect=pygame.Rect(0, 0, 700, 400),
    image_surface = tutoImages[currentIndex],
    anchors = {"center": "center"},
    manager = manager,
    container=TutorialPanel
)

win = False
running = True
gameOver = False
tutorial = False

while running:
    time_delta = clock.tick(60) / 1000.0
    screen.fill((50, 50, 50))

    if gameOver:
        gameOverPanel.enable()
        gameOverPanel.show()

    elif not gameOver:
        gameOverPanel.disable()
        gameOverPanel.hide()

    if tutorial:
        tutorialButton.set_text('Hide Tutorial')
        TutorialPanel.enable()
        TutorialPanel.show()

    elif not tutorial:
        tutorialButton.set_text('Show Tutorial')
        TutorialPanel.disable()
        TutorialPanel.hide()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            manager.set_window_resolution((event.w, event.h))
            codeEntryWindow.set_dimensions((event.w * 0.3, event.h * 0.6))
            rocketLangterminal.set_dimensions((event.w * 0.3, event.h * 0.3))
            rocketLangterminal.set_relative_position((0, event.h * 0.7))

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            if event.ui_element == tutorialButton:
                if tutorial:
                    tutorial = False
                elif not tutorial:
                    tutorial = True

            if event.ui_element == validateButton and codeEntryWindow.get_text() == "":
                rocketLangterminal.set_text(f"<p><font color=#0000FF> Nothing to run </font></p>")

            elif event.ui_element == tutorialNextButton:
                try:
                        currentIndex += 1
                        tutorialSlideshowDisplay.set_image(tutoImages[currentIndex])
                except:
                    currentIndex = 0
                    tutorialSlideshowDisplay.set_image(tutoImages[currentIndex])

            elif event.ui_element == tutorialPreviousButton:
                try:
                        currentIndex += 1
                        tutorialSlideshowDisplay.set_image(tutoImages[currentIndex])
                except:
                    currentIndex = 0
                    tutorialSlideshowDisplay.set_image(tutoImages[currentIndex])

            elif event.ui_element == validateButton:
                commands = player.parseRL(codeEntryWindow.get_text())
                errors = player.validateRL(commands)

                if errors != []:
                    rocketLangterminal.set_text(f"<p><font color=#FF0000>{'\n'.join(errors)}</font></p>")
                else:
                    rocketLangterminal.set_text(f"<p><font color=#00FF00>Code executed successfully</font></p>")

            elif event.ui_element == runButton:
                commands = player.parseRL(codeEntryWindow.get_text())
                errors = player.validateRL(commands)

                if codeEntryWindow.get_text() == "":
                    rocketLangterminal.set_text(f"<p><font color=#0000FF> Nothing to run </font></p>")
                elif errors != []:
                    rocketLangterminal.set_text(f"<p><font color=#FF0000>{'\n'.join(errors)}</font></p>")
                else:
                    rocketLangterminal.set_text(f"<p><font color=#00FF00>Code executed successfully</font")
                    player.executeRL(commands)
                    if player.collided:
                        gameOver = True

            elif event.ui_element == retryButton and win == True:
                    gameMap = map.Map(15, 2, 40, screen)
                    gameMap.scatterDebris()
                    player = rocket.Rocket('./assets/placeholder_rocket.png',(0, 0) , gameMap)
                    alice = entity.Entity(True, "./assets/objective.png", gameMap, "objective")
                    gameOver = False
                    win = False

            elif event.ui_element == retryButton:
                player = rocket.Rocket('./assets/placeholder_rocket.png',(0, 0) , gameMap)
                alice = entity.Entity(True, "./assets/objective.png", gameMap, "objective")
                gameOver = False

            elif event.ui_element == exitButton:
                running = False

        manager.process_events(event)

    if tuple(player.grid_pos) == alice.pointCoords:
        gameOver = True
        win = True
        gameOverLable.set_text('Bravo! You have reached the objective!')
        retryButton.set_text('Next Sector!')
    
    gameMap.drawMap()
    player.draw()
    alice.draw()
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
