import math

from Project.tile_map import TileMap
from pico2d import *
from enum_define import Layer
from enum_define import Blocks


class ConveyorTile(TileMap):
    frameMax = 4
    speed = 0.1
    deltaFrame = 0.0
    offset = 32
    tile_pixel_size = 32
    dir_x, dir_y = 1, 0
    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, state = Layer(1), blocks = Blocks(1)
                 , flip='', degree=0):
        super().__init__(x,y,camera_x,camera_y,state, blocks,flip,degree)
        self.image = load_image('Resource/conveyor-0-0-Sheet.png')
        if degree == 0 or degree == 360:
            self.dir_x, self.dir_y = 1, 0
        elif degree == -90 or degree == 270:
            self.dir_x, self.dir_y = 0, -1
        elif degree == 90 or degree == -270:
            self.dir_x, self.dir_y = 0, 1
        elif degree == 180 or degree == -180:
            self.dir_x, self.dir_y = -1, 0
    def update(self):
        self.deltaFrame += self.speed
        if self.frameMax != 0:
            self.frame = int(self.frame + self.deltaFrame) % (self.frameMax)
        if self.deltaFrame >= 1:
            self.deltaFrame = 0