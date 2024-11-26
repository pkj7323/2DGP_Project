import math
from Project import game_world
from Project.tile_map import TileMap
from pico2d import *
from enum_define import Layer
from enum_define import Blocks
from Project import game_framework

# conveyor action
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class ConveyorTile(TileMap):
    frameMax = 4
    speed = 10
    deltaFrame = 0.0
    offset = 32
    tile_pixel_size = 32
    dir_x, dir_y = 1, 0
    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, state = Layer(1), blocks = Blocks(2)
                 , flip='', degree=0):
        super().__init__(x,y,camera_x,camera_y,state, blocks,flip,degree)
        self.image = load_image('Resource/conveyor-0-0-Sheet.png')
        if degree == 0 or degree == 360:
            self.dir_x, self.dir_y = 1, 0
            self.bb_size_x = self.size
            self.bb_size_y = 0
        elif degree == -90 or degree == 270:
            self.dir_x, self.dir_y = 0, -1
            self.bb_size_x = 0
            self.bb_size_y = self.size
        elif degree == 90 or degree == -270:
            self.dir_x, self.dir_y = 0, 1
            self.bb_size_x = 0
            self.bb_size_y = self.size
        elif degree == 180 or degree == -180:
            self.dir_x, self.dir_y = -1, 0
            self.bb_size_x = self.size
            self.bb_size_y = 0
        game_world.add_collision_pair("ore:CONVEYOR1", None, self)

        self.transfer_speed = 20.0
        self.colliding = False
    def draw(self):
        super().draw()
        draw_rectangle(*self.get_bb())
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frameMax


    def get_bb(self):
        return self.x - self.bb_size_x/2, self.y + self.bb_size_y/2, self.x + self.bb_size_x/2, self.y - self.bb_size_y/2

    def handle_collision(self, group, other):
        if group == 'ore:CONVEYOR1':
            pass
        self.colliding = True

    def handle_collision_end(self):
        self.colliding = False