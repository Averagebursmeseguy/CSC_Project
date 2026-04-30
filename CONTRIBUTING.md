Hello there. I did not expect anyone to read ts. 

# How you contribute:
Fork > clone > submit pull request

# Syntax conventions:
- Use PEP-8 lah
- Camel case for functions lah
- Use type hints for args lah
- Snake case for .py file names lah

# Asset conventions:
 - Sprites meant to fit in the grid must always be 256x256 px
 - Sprite backgrounds must also be transparent

# What each .py does:

 - main.py is where the main game loop is stored. Only put event listeners and high level utility calls here
    - NO function defs here
 - map.py is where you put stuff that manipulates the "map" of the game.
   - generating map
 - rocket.py is where stuff that deals with RocketLang, player controller and collision checker lives
   - RocketLang parsing and processing happens here
   
# obvious stuff:
 - all images go into the assets folder
 - To prevent any weirdness from happening, please refrain from using anything that's not a .png in the game assets
 - If you add a new script, write documentation about it in a .md file about how it works, how to use it and what are its limitations.