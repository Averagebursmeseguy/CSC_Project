# Map information
Here's some information about how the map system is implemented, how to work it and how to make use of it to control the game. Yes, the current way the code is set up is really inefficient as the function will re-do all calculations even when the window isn't rescaled. I don't plan to fix it as optimisation will take too long and 2D math can easily be ran on most modern PCs.

## Architecture
The whole game is built around the map object and the player object with the other functionalities just being interactions between the two. The game depends on the map object as a global truth table about what is where and where the player is. Most of the game's functions rely on this map object.

## Part - 1 the map object:
Here's a view of the map object. If you want to work it, there's four attributes you have to keep an eye on:
 - size
 - coords
 - screen
 - scaling
```py
class Map():
    def __init__(self, size: int, debriSize:int, density, screen:pygame.display):
        self.size = size               #size
        self.density = density
        self.debriSize = debriSize
        self.coords = {}               #Coords
        self.terrain_piece = pygame.image.load('assets/terrain.png').convert_alpha()
        self.screen = screen           #Screen
        self.scaling = 0               #Scaling
```

### Size
This determines the area of the map. You can see in main.py that this attribute is set to 15. This makes a map object that is 15x15 cells in area. Each of the cells in that area is represented by the map's *coords* attribute.

### Coords
The "truth table" aspect of the map. This is a dictionary that contains a tuple for coordinates and string for terrain. So, it looks like this: {(x, y): "terrain_name"}. This way, you can check if a terrain or any object is there by just calling Map.coords.get((x, y))

### Screen
This is the Pygame.Screen object that the Map() object puts its render pipeline into where the renderer converts the truth table coordinates to actual screen code. Check following for more info.

### Scaling
This is the scaling factor for scaling the 256x256 sprite to fit into the grid. The scale factor only works if the sprite is 256x256. Otherwise, adjustments are needed.

## Part - 2 The renderer:
The map renderer converts the coords dict stored in Map() to actual screen codes and paints the screen. ~~I wrote this at 3 in the morning and half of its operations involve copious amounts of caffeine, black magic and wondering why I chose to do CS voluntarily.~~ DO NOT MODIFY

### How it works
~~I have no idea how. Just read the code and hope for the best~~
The map is rendered on the window in about three steps.

#### Step - 1: Render the map viewport
```py    
    def drawMap(self):
        mapViewPort = pygame.Surface((self.screen.height * 0.9, self.screen.height * 0.9))
        viewWidth, viewHeight = mapViewPort.width, mapViewPort.height
        mapViewPort.fill((0, 0, 20))
        self.scaling = viewWidth // self.size
```
First the function creates a pygame.Surface object and calculates how big it has to be relative to the whole window of the game by taking the height and width of the window. This is why the *screen* attribute mentioned above is important. Next we determine the scaling factor needed to convert the map coordinates to screen code. This is done by the scaling variable you see here

#### Step - 2: Render the Grid
```py
        for x in range(0, viewWidth, self.scaling):
            pygame.draw.line(mapViewPort, (255, 255, 255), (x, 0), (x, viewHeight))

        for y in range(0, viewHeight, self.scaling):
            pygame.draw.line(mapViewPort, (255, 255, 255), (0, y), (viewWidth, y))

        pygame.draw.rect(mapViewPort, (255, 255, 255), (0, 0, viewWidth, viewHeight), 1)
```
The renderer then draws the gridlines on that ViewPort object that we created earlier by doing a loop for each x and y coordinates. The loops start drawing from their respective origins to the max width and height of viewport every y and x value which are incremented by the scaling variable.

#### Step - 3: the terrain renderer
```py
        for point in self.coords:
            if self.coords[point] == "terrain":
                mapViewPort.blit(pygame.transform.scale(self.terrain_piece, (self.scaling, self.scaling)), (point[0]*self.scaling, point[1]*self.scaling))

        self.screen.blit(mapViewPort, ((self.screen.width - mapViewPort.width) - 20 , 20))
```
Okay. This is the fun part. The function then checks through the truth table to place each terrain block. As mentioned before, the coords attribute of the Map() object has a tuple of (x, y) that refers to a terrain type. This loops through each *point* (x, y) and then if there is a "terrain" to be placed there, the function scales each terrain block and then renders them with mapViewPort.blit(). Then, finally it renders the viewport object on to the window the game is running inside of.

All rendering assume grid positions are int() and not float() ~~Do not use float as this will crash game~~

### Part - 3 How to work it:
So we know about how it works. Here's how to work it. How to check map coords, input map terrain and use the object to place whatever you're placing.

#### How the coordinate system works:
Due to how pygame is made, increasing X will go right but increasing Y will go down instead of up. So, in a 100x100 grid, 0, 0 is top left and 100, 100 is bottom right.

#### How to use Map.scaling: 
The self.scaling attribute of Map() converts the truth table codes to actual pixel code. Objects will not fit within the grid if they are not resized by multiplying their original size with this attribure.

So, if you want to make your own renderer for adding on to the game(which I suggest you do), you will need to multiply the final size of whatever you render with this attribute if it needs to appear on the map viewport.

#### Get terrain info from Map():
let's say you want to check collision or something and want to see if a *terrain* exists on the cell/point on the map. You simply call Map.coords.get((x, y)) which will return anything that it is assigned to. Keep in mind that this architecture may change and the design isn't final.

#### What the other attributes of Map() do:
 - *terrain_piece* stores each of the terrain textures that will be made into debri and scattered around the map as obstacles.
 - *density* is information about how many pieces of debris should be present at all time
 - *debriSize* is how big (in terrain textures) will each piece of debris be
 - Each debris object is randomly generated based on debriSize and scattered using density.

### Part - 4 Known limitations:
Yes I know that
 - The map cannot be anything but a square
 - The map is redrawn every frame
 - There's no bounding checks on coords
 - Scaled textures are not cached

This is a minimal viable product for the time being, so I'm just getting it to work first.
