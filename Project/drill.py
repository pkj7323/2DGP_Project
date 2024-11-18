from pico2d import load_image

from Project import game_framework
from Project.enum_define import Layer, Blocks
from Project.state_machine import StateMachine
from Project.tile_map import TileMap


# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2


class Mine:
    @staticmethod
    def enter(drill):
        pass
    @staticmethod
    def exit(drill):
        pass
    @staticmethod
    def do(drill):
        drill.timer = (drill.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % drill.frameMax
    @staticmethod
    def draw():
        pass
class Idle:
    @staticmethod
    def enter(drill):
        pass

    @staticmethod
    def exit(drill):
        pass

    @staticmethod
    def do(drill):
        drill.timer = (drill.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % drill.frameMax

    @staticmethod
    def draw():
        pass
class Drill(TileMap):
    ore = None
    def __init__(self, x=0, y=0, camera_x=0, camera_y=0, layer = Layer(1), blocks = Blocks(2)
                 , flip='', degree=0):
        super().__init__(x,y,camera_x,camera_y,layer,blocks,flip,degree)
        self.image = load_image("Resource/blast-drill-Sheet.png") # 드릴 이미지
        self.layer = Layer.building
        self.timer = 0
        self.discharge_dir_x = 0
        self.discharge_dir_y = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle : {Mine : Idle},
            }
        )

    def update(self):
        super().update()
        self.state_machine.update()
    def draw(self):
        super().draw()
        self.state_machine.draw()
