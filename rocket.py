import pygame
class Rocket:
    def __init__(self, image_path, grid_pos, gameMap):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.grid_pos = list(grid_pos)  # [x, y]
        self.gameMap = gameMap
        self.RLcommands = {
            "move": self.move,
            "shoot": self.shoot
        }
        self.collided = False
        # if starting cell is terrain, find a free one
        if self.checkCollision() == True:
            self.grid_pos = self.findEmpty()
            print(self.grid_pos)

    def parseRL(self, raw):
        commands = raw.split("\n")
        def parseAgain(command):
            commandList = command.split(' ')
            name = commandList.pop(0)
            return {"name": name, "args": commandList}
        
        if raw == '':
            return [None]
        else: 
            return list(map(parseAgain, commands))
    
    def validateRL(self, commandList:list[dict]):
        errorList = []
        if None in commandList:
            print(errorList)
            return errorList
        
        for i, command in enumerate(commandList):
            line = i+1
            match command['name']:
                case 'move':
                    args = command['args']
                    if len(args) != 2:
                        errorList.append(f'Error: line:{line}: move expected 2 args, got {len(args)}.')
                    elif args[-1].isdecimal() == False:
                        errorList.append(f'Error: line{line}: distance must be a number')
                    elif args[0] not in ['right', 'left', 'up', 'down']:
                        errorList.append(f'Error: line{line}: unrecognised direction. Can only go right, left, up, down.')

                case 'shoot':
                    args = command['args']
                    if len(args) != 1:
                        errorList.append(f'Error: line{line}: shoot expected 1 arg, got {len(args)}')
                    elif args[-1] not in ['right', 'left', 'up', 'down']:
                        errorList.append(f'Error: line{line}: cannot shoot in that direction')

                case _:
                    errorList.append(f'Error: line{line}: Unknown command')
        return errorList
    
    def executeRL(self, commandList:list[dict]):

        for command in commandList:
            cmd = self.RLcommands.get(command.get("name"))
            args = command.get("args")
            cmd(*args)


    def checkCollision(self):
        print(self.gameMap.coords[tuple(self.grid_pos)]['terrain'])
        if self.gameMap.coords[tuple(self.grid_pos)]['terrain'] != None:
            self.collided = True
            return True
        else:
            self.collided = False
            return False

    def findEmpty(self):
        for y in range(self.gameMap.size):
            for x in range(self.gameMap.size):
                if self.gameMap.coords[(x, y)]['terrain'] == None:
                    return [x, y]
        return [0, 0]  # fallback

    def move(self, dir:str, distance:int): #VERY JANKY MOVEMENT SYSTEM. PLEASE FIX
        dirs = ['right', 'left', 'up', 'down']
        distance = int(distance)

        if dir not in dirs:
            pass
        else:
            match dir:
                case 'right':
                    for i in range(distance):
                        self.grid_pos[0] = (self.grid_pos[0] + 1) % self.gameMap.size
                        if self.checkCollision():
                            break
                case 'left':
                    for i in range(distance):
                        self.grid_pos[0] = (self.grid_pos[0] - 1) % self.gameMap.size
                        if self.checkCollision():
                            break
                case 'up':
                    for i in range(distance):
                        self.grid_pos[1] = (self.grid_pos[1] - 1) % self.gameMap.size
                        if self.checkCollision():
                            break
                case 'down':
                    for i in range(distance):
                        self.grid_pos[1] = (self.grid_pos[1] + 1) % self.gameMap.size
                        if self.checkCollision():
                            break


    def shoot(self, dir):
        pass

    def draw(self):
        view_size = int(self.gameMap.screen.get_height() * 0.9)
        scaling = self.gameMap.scaling

        offset_x = (self.gameMap.screen.get_width() - view_size) - 20
        offset_y = 20

        pixel_x = self.grid_pos[0] * scaling + offset_x
        pixel_y = self.grid_pos[1] * scaling + offset_y

        self.gameMap.screen.blit(
    pygame.transform.scale(self.image, (scaling, scaling)),
    (pixel_x, pixel_y)
)