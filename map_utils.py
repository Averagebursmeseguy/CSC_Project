import pygame

def centreFinder(display_object: pygame.display):
    centre = (display_object.width / 2, display_object.height / 2)
    return centre

def drawGrid(surface: pygame.display, spacing: int):
    color = (255, 255, 255)
    centre = centreFinder(surface) #Pretty self-explaintory

    #establish centre lines first
    pygame.draw.line(surface, color, (centre[0], 0), (centre[0], surface.height))
    pygame.draw.line(surface, color, (0, centre[1]), (surface.width, centre[1]))

    #establish bounding boxes
    pygame.draw.rect(surface, color, (0, 0, surface.width, surface.height), 1)

    #subdivide
    increment = spacing
    (endx, endy) = (surface.width, surface.height)

    for i in range(0, endx):
        pygame.draw.line(surface, color, (0, increment*i), (endx, increment*i))

    for i in range(0, endy):
        pygame.draw.line(surface, color, (increment*i, 0), (increment * i, endy))




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