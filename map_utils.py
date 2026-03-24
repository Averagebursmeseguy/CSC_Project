import pygame

def centreFinder(display_object: pygame.display):
    centre = (display_object.width / 2, display_object.height / 2)
    return centre

def drawGrid(screen: pygame.display, spacing: int, color: tuple[int, int, int]): #Spacing gets fucking weird when doing things that are not 10^x. 
    centre = centreFinder(screen) #Pretty self-explaintory

    #establish centre lines first
    pygame.draw.line(screen, color, (centre[0], 0), (centre[0], screen.height))
    pygame.draw.line(screen, color, (0, centre[1]), (screen.width, centre[1]))

    #establish bounding boxes
    pygame.draw.rect(screen, color, (0, 0, screen.width, screen.height), 1)

    #subdivide
    increment = spacing
    (endx, endy) = (screen.width, screen.height)

    for i in range(0, endx):
        pygame.draw.line(screen, color, (0, increment*i), (endx, increment*i))

    for i in range(0, endy):
        pygame.draw.line(screen, color, (increment*i, 0), (increment * i, endy))




# def drawGrid(startpos, endpos, scaling, screen, linecolor):

#     startx, starty = startpos
#     endx, endy = endpos

#     #Make vertical and horiz lines first
#     pygame.draw.line(screen, linecolor, (startx, starty), (endx, starty), 1)
#     pygame.draw.line(screen, linecolor, (startx, starty), (startx, endy), 1)
#     pygame.draw.line(screen, linecolor, (endx, endy), (startx, endy), 1)
#     pygame.draw.line(screen, linecolor, (endx, endy), (endx, starty), 1)

#     for i in range(int(endx / scaling)):
#         increment = startx + (scaling * i)
#         pygame.draw.line(screen, linecolor, (increment, starty), (increment, endy))

#     for i in range(int(endy / scaling)):
#         increment = starty + (scaling * i)
#         pygame.draw.line(screen, linecolor, (startx, increment), (endx, increment))