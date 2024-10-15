from Project.tile_map import tileMap
from pico2d import *

class TileMapManager:

    def __init__(self):
        pass
    def click(self, x, y):
        new_tile = tileMap()
        new_tile.x = x
        new_tile.y = y
        if new_tile.image == None:
            new_tile.image = load_image('Resource\\tile1.png')
        return new_tile