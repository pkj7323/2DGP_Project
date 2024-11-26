import math

from pico2d import load_image, draw_rectangle

from Project import game_framework
from Project.Oreitem import Oreitem
from Project.enum_define import Layer, Blocks, Items
from Project.state_machine import StateMachine, on_ore
from Project.tile_map import TileMap
from Project import game_world

# Boy Action Speed
TIME_PER_ACTION = 2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2


class Mine:
    @staticmethod
    def enter(drill,e):
        pass
    @staticmethod
    def exit(drill,e):
        pass
    @staticmethod
    def do(drill):
        drill.frame = (drill.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % drill.frameMax
        drill.timer += game_framework.frame_time
        if drill.timer >= drill.drilling_speed:
            drill.timer = 0
            ore_item = None
            if drill.ore_type == Items.beryllium:
                ore_item = Oreitem('beryllium_ore_item', drill.x + drill.discharge_dir_x * drill.bb_size_x / 2,
                               drill.y + drill.discharge_dir_y * drill.bb_size_y / 2, Items.beryllium)
            elif drill.ore_type == Items.coal:
                ore_item = Oreitem('coal_ore_item', drill.x + drill.discharge_dir_x * drill.bb_size_x / 2,
                               drill.y + drill.discharge_dir_y * drill.bb_size_y / 2, Items.coal)
            game_world.add_object(ore_item, Layer.ore)
    @staticmethod
    def draw(drill):
        pass
class Idle:
    @staticmethod
    def enter(drill,e):
        pass

    @staticmethod
    def exit(drill,e):
        pass

    @staticmethod
    def do(drill):
        # drill.frame = (drill.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % drill.frameMax
        pass
    @staticmethod
    def draw(drill):
        pass
class Drill(TileMap):
    ore_type = None
    bb_size_x = 40
    bb_size_y = 40
    offset = 128
    timer = 0
    tile_pixel_size = 128
    frameMax = 2
    blocks = Blocks.drill
    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, layer = Layer(1), blocks = Blocks(2)
                 , flip='', degree=0, drilling_speed = 3):
        super().__init__(x,y,camera_x,camera_y,layer,blocks,flip,degree)
        self.image = load_image("Resource/blast-drill-Sheet.png") # 드릴 이미지
        self.layer = Layer.building
        self.drilling_speed = drilling_speed
        self.discharge_dir_x = 1
        self.discharge_dir_y = 0
        game_world.add_collision_pair("Drill:Ore", self, None)
        if degree == 0 or degree == 360:
            self.discharge_dir_x, self.discharge_dir_y = 1, 0
        elif degree == -90 or degree == 270:
            self.discharge_dir_x, self.discharge_dir_y = 0, -1
        elif degree == 90 or degree == -270:
            self.discharge_dir_x, self.discharge_dir_y = 0, 1
        elif degree == 180 or degree == -180:
            self.discharge_dir_x, self.discharge_dir_y = -1, 0

        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle : {on_ore : Mine},
                Mine : {on_ore : Mine},
            }
        )


    def update(self):
        super().update()
        self.state_machine.update()
    def draw(self):
        self.image.clip_composite_draw(int(self.frame) * self.offset, 0,self.tile_pixel_size, self.tile_pixel_size,
                                       math.radians(self.degree), self.flip, self.x, self.y, self.size, self.size)
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.bb_size_x / 2, self.y + self.bb_size_y / 2, self.x + self.bb_size_x / 2, self.y - self.bb_size_y / 2

    def handle_collision(self, group, other):
        if group == 'Drill:Ore':
            if other.blocks == Blocks.beryllium_ore:
                self.ore_type = Items.beryllium
                self.state_machine.add_event(('ON_ORE',0))
            elif other.blocks == Blocks.coal_ore:
                self.ore_type = Items.coal
                self.state_machine.add_event(('ON_ORE',0))


    def handle_collision_end(self):
        pass
