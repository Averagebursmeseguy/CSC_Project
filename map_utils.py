import pygame

def centreFinder(display_object: pygame.display):
    centre = (display_object.width, display_object.height)
    return centre

def drawGrid(startpos, endpos, scaling, surface, linecolor):

    startx, starty = startpos
    endx, endy = endpos

    #Make vertical and horiz lines first
    pygame.draw.line(surface, linecolor, (startx, starty), (endx, starty), 1)
    pygame.draw.line(surface, linecolor, (startx, starty), (startx, endy), 1)
    pygame.draw.line(surface, linecolor, (endx, endy), (startx, endy), 1)
    pygame.draw.line(surface, linecolor, (endx, endy), (endx, starty), 1)

    for i in range(int(endx / scaling)):
        increment = startx + (scaling * i)
        pygame.draw.line(surface, linecolor, (increment, starty), (increment, endy))

    for i in range(int(endy / scaling)):
        increment = starty + (scaling * i)
        pygame.draw.line(surface, linecolor, (startx, increment), (endx, increment))