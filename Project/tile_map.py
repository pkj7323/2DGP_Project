import enum
from pico2d import *
from Project.BlockState import BlockState
class Blocks(enum.Enum):
    wall = 1
    conveyor = 2

class TileMap:
    image = None
    size = 20
    tile_pixel_size = 64
    frameMax = 0
    frame = 0
    offset = 0
    blocks = Blocks(1)
    flip = ''
    degree = 0
    speed = 0.0
    def __init__(self,x=0,y=0,camera_x=0,camera_y=0,state = BlockState(1), blocks = Blocks(1)):
        self.x = x # 카메라 기준 상대적 현재 좌표
        self.y = y # 카메라 기준 상대적 현재 좌표
        self.adjust_x = camera_x + self.x # 월드 기준 절대 좌표
        self.adjust_y = camera_y + self.y # 월드 기준 절대 좌표
        self.blocks = blocks
        self.state = state
        self.deltaFrame = 0.0

    def draw(self):
        if self.image is None:
            return
        self.image.clip_composite_draw(self.frame * self.offset, 0, self.tile_pixel_size, self.tile_pixel_size,
                                       self.degree, self.flip, self.x, self.y, self.size, self.size)
    def update(self):
        self.deltaFrame += self.speed
        if self.frameMax != 0:
            self.frame = int(self.frame + self.deltaFrame) % (self.frameMax)

        if self.deltaFrame >= 1:
            self.deltaFrame = 0
    def move(self,x,y):
        self.x += x
        self.y += y
    def loadImage(self):
        if self.image is None:
            if self.blocks.value == BlockState.wall.value:
                self.image = load_image('Resource/tile1.png')
            elif self.blocks.value == Blocks.conveyor.value:
                self.image = load_image('Resource/conveyor-0-0-Sheet.png')
                self.frame = 0
                self.offset = 32
                self.frameMax = 4
                self.speed = 0.08
                self.tile_pixel_size = 32
            else:
                pass
        else:
            pass