from pico2d import load_image, draw_rectangle
from Project import game_world
from Project.enum_define import Layer, Blocks, Items
from Project.tiles.tile_map import TileMap
import random

class OreTile(TileMap):
    tile_pixel_size = 32
    item = None
    bb_size_x = 20
    bb_size_y = 20
    def __init__(self,x=0, y=0, camera_x=0, camera_y=0, layer = Layer.tile, blocks = Blocks.beryllium_ore
                 , flip='', degree=0):
        super().__init__(x, y, camera_x, camera_y, layer, blocks, flip, degree)
        self.colliding = False

        if blocks == Blocks.beryllium_ore:
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
        elif blocks == Blocks.coal_ore:
            self.image = load_image('Resource/ore-coal-tile.png')
        game_world.add_collision_pair("Drill:Ore", None, self)

    def draw(self):
        super().draw()
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - self.bb_size_x/2, self.y + self.bb_size_y/2, self.x + self.bb_size_x/2, self.y - self.bb_size_y/2

    def handle_collision(self, group, other):
        if group == 'Drill:Ore':
            pass
        self.colliding = True

    def handle_collision_end(self):
        self.colliding = False

class IronOreTile(OreTile):
    def __init__(self,x=0, y=0, camera_x=0, camera_y=0, layer = Layer.tile, blocks = Blocks.iron_ore
                 , flip='', degree=0):
        super().__init__(x, y, camera_x, camera_y, layer, blocks, flip, degree)
        self.colliding = False

        if blocks == Blocks.iron_ore:
            self.image = load_image('Resource/ore-iron-tile.png')
        game_world.add_collision_pair("Drill:Ore", None, self)
    def draw(self):
        super().draw()
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - self.bb_size_x/2, self.y + self.bb_size_y/2, self.x + self.bb_size_x/2, self.y - self.bb_size_y/2

    def handle_collision(self, group, other):
        if group == 'Drill:Ore':
            pass
        self.colliding = True

    def handle_collision_end(self):
        self.colliding = False

class CopperOreTile(OreTile):
    def __init__(self,x=0, y=0, camera_x=0, camera_y=0, layer = Layer.tile, blocks = Blocks.copper_ore
                 , flip='', degree=0):
        super().__init__(x, y, camera_x, camera_y, layer, blocks, flip, degree)
        self.colliding = False

        if blocks == Blocks.copper_ore:
            self.image = load_image('Resource/tile-copper-ore.png')
        game_world.add_collision_pair("Drill:Ore", None, self)
    def draw(self):
        super().draw()
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - self.bb_size_x/2, self.y + self.bb_size_y/2, self.x + self.bb_size_x/2, self.y - self.bb_size_y/2

    def handle_collision(self, group, other):
        if group == 'Drill:Ore':
            pass
        self.colliding = True

    def handle_collision_end(self):
        self.colliding = False

class TitaniumOreTile(OreTile):
    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, layer=Layer.tile, blocks=Blocks.titanium_ore
                 , flip='', degree=0):
        super().__init__(x, y, camera_x, camera_y, layer, blocks, flip, degree)
        self.colliding = False

        if blocks == Blocks.titanium_ore:
            self.image = load_image('Resource/tile-titanium-ore.png')
        game_world.add_collision_pair("Drill:Ore", None, self)

    def draw(self):
        super().draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.bb_size_x / 2, self.y + self.bb_size_y / 2, self.x + self.bb_size_x / 2, self.y - self.bb_size_y / 2

    def handle_collision(self, group, other):
        if group == 'Drill:Ore':
            pass
        self.colliding = True

    def handle_collision_end(self):
        self.colliding = False