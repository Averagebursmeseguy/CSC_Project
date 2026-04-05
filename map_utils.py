import pygame
import random

def drawGrid(screen: pygame.display, spacing: int, color: tuple[int, int, int]): #Spacing gets fucking weird when doing things that are not 10^x. 
    #establish bounding box
    pygame.draw.rect(screen, color, (0, 0, screen.width, screen.height), 1)

    #subdivide
    (endx, endy) = (screen.width, screen.height)

    for y in range(0, endy, spacing): 
        pygame.draw.line(screen, color, (0, y), (endx, y))

    for x in range(0, endx, spacing):
        pygame.draw.line(screen, color, (x, 0), (x, endy))


#TODO: Algorithm needs polish
def generateObstacles(terrain, obstacleSize:int, rootCoord: tuple|int):
    oldPoint = [rootCoord[0], rootCoord[1]]
    points = []
    locations = []

    #This generates the points
    i = 0
    while i < obstacleSize:
        dir = random.randint(0, 2)
        match dir:
            case 0:         
                newPoint = [oldPoint[0] + 1, oldPoint[1]]
                oldPoint = newPoint
            case 1:
                newPoint = [oldPoint[0], oldPoint[1] + 1]
                oldPoint = newPoint
            case 2:
                newPoint = [oldPoint[0], oldPoint[1] - 1]
                oldPoint = newPoint
        
        if newPoint not in points:
             points.append(newPoint)
             i += 1
        else:
            pass


    #This thing stitches the texture and point together
    for point in points:
        locations.append([terrain, (point[0], point[1])])

    return locations

def generateMap(count, terrain):
    obstacleList = []
    i = 0
    while i < count:
        obstacle = generateObstacles(terrain, 7, (random.randint(i , 20), random.randint(i, 20)))
        if obstacle not in obstacleList:
            obstacleList.append(obstacle)
            i += 1
        
    return obstacleList
            