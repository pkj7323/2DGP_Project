
from Project.enum_define import Layer
from Project.state_machine import StateMachine

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class mine:
    @staticmethod
    def enter(drill):
        pass
    @staticmethod
    def exit(drill):
        pass
    @staticmethod
    def do():
        pass
    @staticmethod
    def draw():
        pass
class Drill:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = None
        self.layer = Layer.building
        self.timer = 0
        self.discharge_dir_x = 0
        self.discharge_dir_y = 0
        self.state_machine = StateMachine
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {on_conveyor: Move, leave_conveyor: Idle},
                Move: {leave_conveyor: Idle, on_conveyor: Move},
            }
        )

    def update(self):
        pass
    def draw(self):
        pass
