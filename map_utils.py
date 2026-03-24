import pygame

def centreFinder(display_object: pygame.display):
    centre = (display_object.width / 2, display_object.height / 2)
    return centre

def drawGrid(centre: tuple[int, int], surface: pygame.display):
    pygame.draw.line(surface, (255, 255, 255), (centre[0], 0), (centre[0], 600))
    pygame.draw.line(surface, (255, 255, 255), (0, centre[1]), (800, centre[1]))


# def drawGrid(startpos, endpos, scaling, surface, linecolor):

#     startx, starty = startpos
#     endx, endy = endpos

#     #Make vertical and horiz lines first
#     pygame.draw.line(surface, linecolor, (startx, starty), (endx, starty), 1)
#     pygame.draw.line(surface, linecolor, (startx, starty), (startx, endy), 1)
#     pygame.draw.line(surface, linecolor, (endx, endy), (startx, endy), 1)
#     pygame.draw.line(surface, linecolor, (endx, endy), (endx, starty), 1)

#     for i in range(int(endx / scaling)):
#         increment = startx + (scaling * i)
#         pygame.draw.line(surface, linecolor, (increment, starty), (increment, endy))

#     for i in range(int(endy / scaling)):
#         increment = starty + (scaling * i)
#         pygame.draw.line(surface, linecolor, (startx, increment), (endx, increment))