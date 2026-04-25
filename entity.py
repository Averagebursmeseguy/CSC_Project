import pygame, random
import map
class Entity:
    def __init__(self, friendly:bool, sprite:str, gameMap:map.Map, type: str):
        self.gameMap = gameMap
        self.friendly = friendly
        self.sprite = pygame.image.load(f'{sprite}').convert_alpha()
        self.pointCoords = (None, None)
        self.type = type
        self.scatter()

    def scatter(self):
        self.pointCoords = (random.randint(0, self.gameMap.size), random.randint(0, self.gameMap.size))
        while self.gameMap.coords[self.pointCoords]['terrain'] != None:
            self.pointCoords = (random.randint(0, self.gameMap.size), random.randint(0, self.gameMap.size))

    #No idea how code conversion works. It just does. DO NOT TOUCH
    def draw(self):
        viewSize = int(self.gameMap.screen.get_height()*.9)
        scaling = self.gameMap.scaling

        offset_x = (self.gameMap.screen.get_width() - viewSize) - 20
        offset_y = 20

        pixel_x = self.pointCoords[0] * scaling + offset_x
        pixel_y = self.pointCoords[1] * scaling + offset_y

        self.gameMap.screen.blit(pygame.transform.scale(self.sprite, (scaling, scaling)), (pixel_x, pixel_y))