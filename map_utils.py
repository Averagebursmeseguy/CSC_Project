import pygame
import random

def centreFinder(display_object: pygame.display):
    centre = (display_object.width / 2, display_object.height / 2)
    return centre

def drawGrid(screen: pygame.display, spacing: int, color: tuple[int, int, int]): #Spacing gets fucking weird when doing things that are not 10^x. 
    centre = centreFinder(screen) #Pretty self-explaintory

    #establish centre lines first
    pygame.draw.line(screen, color, (centre[0], 0), (centre[0], screen.height))
    pygame.draw.line(screen, color, (0, centre[1]), (screen.width, centre[1]))

    #establish bounding box
    pygame.draw.rect(screen, color, (0, 0, screen.width, screen.height), 1)

    #subdivide
    (endx, endy) = (screen.width, screen.height)

    for y in range(0, endy, spacing): 
        pygame.draw.line(screen, color, (0, y), (endx, y))

    for x in range(0, endx, spacing):
        pygame.draw.line(screen, color, (x, 0), (x, endy))


#TODO: Dedupe me you fuck
def generateObstacles(terrain, obstacleSize:int, rootCoord: tuple|int):
    oldPoint = [rootCoord[0], rootCoord[1]]
    points = []
    locations = []

    #This generates the points
    for i in range(1, obstacleSize):
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
        points.append(newPoint)

    print(points)

    #This thing stitches the texture and point together
    for point in points:
        locations.append([terrain, (point[0], point[1])])

    print(locations)
    return locations
            