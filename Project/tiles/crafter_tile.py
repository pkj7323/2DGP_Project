from pico2d import load_image, draw_rectangle, load_font

from Project import game_framework
from Project import game_world
from Project.Oreitem import Oreitem
from Project.enum_define import Layer, Blocks, Items
from Project.tiles.tile_map import TileMap
import math



TIME_PER_ACTION = 2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2



class CrafterTile(TileMap):
    image = None  # 크래프터 이미지
    bb_size_x = 30
    bb_size_y = 30
    offset = 64
    tile_pixel_size = 64
    frameMax = 2
    blocks = Blocks.crafter
    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, layer = Layer.building, blocks = Blocks.base_tile
                 , flip='', degree=0):
        super().__init__(x,y, camera_x, camera_y, layer, blocks, flip, degree)
        self.image = load_image("Resource/crafting_table_sheet.png")
        game_world.add_collision_pair("Crafter:Ore", self, None)
        self.beryllium_ore = 0
        self.coal_ore = 0
        self.dir_x, self.dir_y = 1, 0
        if degree == 0 or degree == 360:
            self.dir_x, self.dir_y = 1, 0
        elif degree == -90 or degree == 270:
            self.dir_x, self.dir_y = 0, -1
        elif degree == 90 or degree == -270:
            self.dir_x, self.dir_y = 0, 1
        elif degree == 180 or degree == -180:
            self.dir_x, self.dir_y = -1, 0


    def update(self):
        super().update()
        if self.coal_ore >= 5 and self.beryllium_ore >= 5:
            result = Oreitem('coal_ore_item', self.x + self.dir_x * self.bb_size_x / 2,
                               self.y + self.dir_y * self.bb_size_y / 2, Items.diamond)
            game_world.add_object(result, Layer.ore)
            self.coal_ore -= 5
            self.beryllium_ore -= 5
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frameMax


    def draw(self):

        self.image.clip_composite_draw(int(self.frame) * self.offset, 0, self.tile_pixel_size, self.tile_pixel_size,
                                       math.radians(self.degree), self.flip, self.x, self.y, self.size, self.size)
        draw_rectangle(*self.get_bb())
        font=load_font('Resource/KCC_dodaumdodaum.ttf')
        font.draw(self.x,self.y,f'베릴륨:{self.beryllium_ore} / 석탄:{self.coal_ore}')

    def get_bb(self):
        return self.x - self.bb_size_x / 2, self.y + self.bb_size_y / 2, self.x + self.bb_size_x / 2, self.y - self.bb_size_y / 2

    def handle_collision(self, group, other):
        if group == 'Crafter:Ore':
            if other.ore_type == Items.beryllium:
                self.beryllium_ore += 1
            if other.ore_type == Items.coal:
                self.coal_ore += 1

    def handle_collision_end(self):
        pass