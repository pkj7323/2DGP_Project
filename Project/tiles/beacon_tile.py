import math

from pico2d import load_image, draw_rectangle, load_font

from Project import game_world, game_framework
from Project.Oreitem import Oreitem
from Project.enum_define import Blocks, Layer, Items
from Project.game_item import GameItem
from Project.tiles.tile_map import TileMap

TIME_PER_ACTION = 4
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class BeaconTile(TileMap):
    image = None  # 신호기
    bb_size_x = 30
    bb_size_y = 30
    offset = 32
    tile_pixel_size = 32
    frameMax = 2
    blocks = Blocks.crafter

    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, layer=Layer.building, blocks=Blocks.base_tile
                 , flip='', degree=0):
        super().__init__(x, y, camera_x, camera_y, layer, blocks, flip, degree)
        self.image = load_image("Resource/tile-beacon-Sheet.png")
        game_world.add_collision_pair("Beacon:Ore", self, None)
        self.titanium_ore = 0
        self.iron_ingot = 0
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
        if self.iron_ingot >= 2 and self.titanium_ore >= 5:
            result = GameItem('rod_item', self.x + self.dir_x * self.bb_size_x / 2
                              , self.y + self.dir_y * self.bb_size_y / 2, Items.rod)
            game_world.add_object(result, Layer.ore)
            self.iron_ingot -= 2
            self.titanium_ore -= 5
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frameMax
        else:
            self.frame = 0

    def draw(self):

        self.image.clip_composite_draw(int(self.frame) * self.offset, 0, self.tile_pixel_size, self.tile_pixel_size,
                                       math.radians(self.degree), self.flip, self.x, self.y, self.size, self.size)
        draw_rectangle(*self.get_bb())
        font = load_font('Resource/KCC_dodaumdodaum.ttf')
        font.draw(self.x, self.y, f'철주괴:{self.iron_ingot} / 티타늄:{self.titanium_ore}')

    def get_bb(self):
        return self.x - self.bb_size_x / 2, self.y + self.bb_size_y / 2, self.x + self.bb_size_x / 2, self.y - self.bb_size_y / 2

    def handle_collision(self, group, other):
        if group == 'Beacon:Ore':
            if other.ore_type == Items.titanium:
                self.titanium_ore += 1
            if other.ore_type == Items.iron_ingot:
                self.iron_ingot += 1

    def handle_collision_end(self):
        pass