from pico2d import load_image, draw_rectangle

from Project import game_framework, game_world
from Project.enum_define import Layer, Blocks, Items
from Project.tile_map import TileMap
import math



TIME_PER_ACTION = 2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5



class BaseTile(TileMap):
    image = None  # 드릴 이미지
    bb_size_x = 40
    bb_size_y = 40
    offset = 64
    tile_pixel_size = 64
    frameMax = 5
    blocks = Blocks.drill
    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, layer = Layer.building, blocks = Blocks.base_tile
                 , flip='', degree=0):
        super().__init__(x,y, camera_x, camera_y, layer, blocks, flip, degree)
        self.image = load_image("Resource/container-Sheet.png")
        game_world.add_collision_pair("Base:Ore", self, None)



    def update(self):
        super().update()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frameMax


    def draw(self):

        self.image.clip_composite_draw(int(self.frame) * self.offset, 0, self.tile_pixel_size, self.tile_pixel_size,
                                       math.radians(self.degree), self.flip, self.x, self.y, self.size, self.size)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.bb_size_x / 2, self.y + self.bb_size_y / 2, self.x + self.bb_size_x / 2, self.y - self.bb_size_y / 2

    def handle_collision(self, group, other):
        if group == 'Base:Ore':
            game_world.add_item_once(other.ore_type)

    def handle_collision_end(self):
        pass