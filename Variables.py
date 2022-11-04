"""
    A variable file used by multiple code files
"""

# region Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
Colors = {
    'White': WHITE,
    'Black': BLACK,
    'Red': RED,
    'Green': GREEN
}
# endregion

# region Sizes
TILE_SIDE_LENGTH = 25
TILE_AMOUNT = 40
WINDOW_WIDTH_HEIGHT = TILE_AMOUNT * TILE_SIDE_LENGTH
Sizes = {
    'TileLength': TILE_SIDE_LENGTH,
    'WindowWidth': WINDOW_WIDTH_HEIGHT,
    'WindowSize': [WINDOW_WIDTH_HEIGHT, WINDOW_WIDTH_HEIGHT],
}
# endregion

# region Miscellaneous
SNAKE_SPEED = 15
STARTING_POINT = {'x': Sizes['WindowWidth']/2, 'y': Sizes['WindowWidth']/2}
# endregion
