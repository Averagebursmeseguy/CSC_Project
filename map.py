import pygame, random

class Map():
    def __init__(self, size: int, debriSize:int, density, screen:pygame.display):
        self.size = size
        self.density = density
        self.debriSize = debriSize
        self.coords = {}
        self.terrain_piece = pygame.image.load('assets/terrain.png').convert_alpha()
        self.screen = screen
        self.scaling = 0

        for y in range(self.size):
            for x in range(self.size):
                self.coords[(x, y)] = None

    def makeDebris(self, root:tuple[int, int]):
        i = 0
        points = []
        oldPoint = root
        while i < self.debriSize:
            dir = random.randint(0, 2)
            match dir:
                case 0:         
                    newPoint = (oldPoint[0] + 1, oldPoint[1])
                    oldPoint = newPoint
                case 1:
                    newPoint = (oldPoint[0], oldPoint[1] + 1)
                    oldPoint = newPoint
                case 2:
                    newPoint = (oldPoint[0], oldPoint[1] - 1)
                    oldPoint = newPoint
            
            if newPoint not in points:
                points.append(newPoint)
                i += 1

        for point in points:
            self.coords[point] = 'terrain'

    def scatterDebris(self):
        visitedLocations = []
        i = 0
        while i < self.density:
            newCoord = (random.randint(0, self.size), random.randint(0, self.size))
            if newCoord not in visitedLocations:
                i += 1
                visitedLocations.append(newCoord)

        for location in visitedLocations:
            self.makeDebris(location) 


        
    def drawMap(self):
        mapViewPort = pygame.Surface((self.screen.height * 0.9, self.screen.height * 0.9))
        viewWidth, viewHeight = mapViewPort.width, mapViewPort.height
        mapViewPort.fill((0, 0, 20))

        self.scaling = viewWidth // self.size

        for x in range(0, viewWidth, self.scaling):
            pygame.draw.line(mapViewPort, (255, 255, 255), (x, 0), (x, viewHeight))

        for y in range(0, viewHeight, self.scaling):
            pygame.draw.line(mapViewPort, (255, 255, 255), (0, y), (viewWidth, y))

        pygame.draw.rect(mapViewPort, (255, 255, 255), (0, 0, viewWidth, viewHeight), 1)

        for point in self.coords:
            if self.coords[point] == "terrain":
                mapViewPort.blit(pygame.transform.scale(self.terrain_piece, (self.scaling, self.scaling)), (point[0]*self.scaling, point[1]*self.scaling))

        self.screen.blit(mapViewPort, ((self.screen.width - mapViewPort.width) - 20 , 20))



