import pygame

class Rocket:
    def __init__(self, image_path, grid_pos, gameMap):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.grid_pos = list(grid_pos)  # [x, y]
        self.gameMap = gameMap
        # if starting cell is terrain, find a free one
        if self.gameMap.coords.get(tuple(self.grid_pos)) == "terrain":
            self.grid_pos = self.find_empty(gameMap)

    def find_empty(self):
        for y in range(self.gameMap.size):
            for x in range(self.gameMap.size):
                if self.gameMap.coords.get((x, y)) != "terrain":
                    return [x, y]
        return [0, 0]  # fallback

    def move(self, dir:str, distance:int):
        dirs = ['forward', 'backward', 'up', 'down']
        if dir not in dirs:
            pass
        else:
            match dir:
                case 'forward':
                    self.grid_pos[0] = (self.grid_pos[0] + distance) % self.gameMap.size
                case 'backward':
                    self.grid_pos[0] = (self.grid_pos[0] - distance) % self.gameMap.size
                case 'up':
                    self.grid_pos[1] = (self.grid_pos[1] - distance) % self.gameMap.size
                case 'down':
                    self.grid_pos[1] = (self.grid_pos[1] + distance) % self.gameMap.size

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