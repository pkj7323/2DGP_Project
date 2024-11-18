from pico2d import load_image

from Project.enum_define import Layer, Blocks, Items
from Project.tile_map import TileMap
import random

class OreTile(TileMap):
    tile_pixel_size = 32
    item = None
    def __init__(self,x=0, y=0, camera_x=0, camera_y=0, layer = Layer.tile, blocks = Blocks.beryllium_ore
                 , flip='', degree=0):
        super().__init__(x, y, camera_x, camera_y, layer, blocks, flip, degree)

        if blocks == Blocks(3):
            rd = random.randint(0,2)
            self.item = Items.beryllium
            if rd == 0:
                self.image = load_image('Resource/ore-beryllium1-tile.png')
            elif rd == 1:
                self.image = load_image('Resource/ore-beryllium2-tile.png')
            elif rd == 2:
                self.image = load_image('Resource/ore-beryllium3-tile.png')
            else:
                self.image = load_image('Resource/error.png')
