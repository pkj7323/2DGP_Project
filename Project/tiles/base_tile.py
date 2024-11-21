from pico2d import load_image, draw_rectangle
from pygame.examples.cursors import image

from Project import game_framework, game_world
from Project.enum_define import Layer, Blocks
from Project.tile_map import TileMap
import math



TIME_PER_ACTION = 2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2



class BaseTile(TileMap):
    image = load_image("Resource/container-Sheet.png")  # 드릴 이미지
    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, layer = Layer.building, blocks = Blocks.base_tile
                 , flip='', degree=0):
        super().__init__(x,y, camera_x, camera_y, layer, blocks, flip, degree)
        self.bb_size_x = 40
        self.bb_size_y = 40


        game_world.add_collision_pair("Base:Ore", self, None)
        if degree == 0 or degree == 360:
            self.discharge_dir_x, self.discharge_dir_y = 1, 0
        elif degree == -90 or degree == 270:
            self.discharge_dir_x, self.discharge_dir_y = 0, -1
        elif degree == 90 or degree == -270:
            self.discharge_dir_x, self.discharge_dir_y = 0, 1
        elif degree == 180 or degree == -180:
            self.discharge_dir_x, self.discharge_dir_y = -1, 0


    def update(self):
        super().update()


    def draw(self):

        self.image.clip_composite_draw(int(self.frame) * self.offset, 0, self.tile_pixel_size, self.tile_pixel_size,
                                       math.radians(self.degree), self.flip, self.x, self.y, self.size, self.size)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.bb_size_x / 2, self.y + self.bb_size_y / 2, self.x + self.bb_size_x / 2, self.y - self.bb_size_y / 2

    def handle_collision(self, group, other):
        if group == 'Base:Ore':
            if other.blocks == Blocks.beryllium_ore:
                pass

    def handle_collision_end(self):
        pass