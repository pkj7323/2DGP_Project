from pico2d import *
from Project.enum_define import Layer, Blocks


class TileMap:
    image = None
    size = 20
    tile_pixel_size = 64
    frame = 0
    offset = 0

    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, layer = Layer(1), blocks = Blocks(1)
                 , flip='', degree=0):
        self.x = x # 카메라 기준 상대적 현재 좌표
        self.y = y # 카메라 기준 상대적 현재 좌표
        self.adjust_x = camera_x + self.x # 월드 기준 절대 좌표
        self.adjust_y = camera_y + self.y # 월드 기준 절대 좌표
        self.blocks = blocks
        self.layer = layer
        self.flip = flip
        self.degree = degree
        if self.image is None:
            if self.blocks.value == Layer.tile.value:
                self.image = load_image('Resource/tile1.png')
            else:
                self.image = load_image('Resource/error.png')

    def draw(self):
        if self.image is None:
            return
        self.image.clip_composite_draw(int(self.frame * self.offset), 0, self.tile_pixel_size, self.tile_pixel_size,
                                       math.radians(self.degree), self.flip, self.x, self.y, self.size, self.size)
    def update(self):
        pass
    def move(self,x,y):
        self.x += x
        self.y += y