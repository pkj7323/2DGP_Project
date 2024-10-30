from Project.tile_map import TileMap
from pico2d import *
from enum_define import Layer
from enum_define import Blocks
class ConveyorTile(TileMap):
    frameMax = 4
    speed = 0.1
    deltaFrame = 0.0
    frame = 0
    offset = 32
    tile_pixel_size = 32
    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, state = Layer(1), blocks = Blocks(1)
                 , flip='', rad=0.0):
        super().__init__(x,y,camera_x,camera_y,state, blocks,flip,rad)
        self.image = load_image('Resource/conveyor-0-0-Sheet.png')

    def update(self):
        self.deltaFrame += self.speed
        if self.frameMax != 0:
            self.frame = int(self.frame + self.deltaFrame) % (self.frameMax)
        if self.deltaFrame >= 1:
            self.deltaFrame = 0