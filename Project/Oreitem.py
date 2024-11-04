from lib2to3.btm_utils import reduce_tree

from pico2d import load_image, get_time

from Project.enum_define import Layer, Items, Blocks
from Project.state_machine import StateMachine, on_conveyor, leave_conveyor
import game_world

class Move:
    @staticmethod
    def enter(ore, e):
        pass
    @staticmethod
    def exit(ore, e):
        pass
    @staticmethod
    def do(ore):

        ore.x += ore.dir_x * 0.5
        ore.y += ore.dir_y * 0.5

        ore.timer = 0
        if ore.timer < 100:
            ore.y -= 0.001
            ore.timer += 1
        elif ore.timer < 200:
            ore.y += 0.001
            ore.timer += 1
        else:
            ore.timer = 0
        ore.collision_check()
    @staticmethod
    def draw(ore):
        ore.image.draw(ore.x, ore.y, 16, 16)
class Idle:
    @staticmethod
    def enter(ore, e):
        ore.dir_x , ore.dir_y = 0, 0

    @staticmethod
    def exit(ore, e):
        pass

    @staticmethod
    def do(ore):

        ore.timer = 0
        if ore.timer < 100:
            ore.y -= 0.001
            ore.timer += 1
        elif ore.timer < 200:
            ore.y += 0.001
            ore.timer += 1
        else:
            ore.timer = 0

        ore.collision_check()

    @staticmethod
    def draw(ore):
        #left, bottom, width, height, x, y, w = None, h = None
        #draw(self, x, y, w=None, h=None):
        ore.image.draw(ore.x, ore.y, 16, 16)


class Oreitem:
    image = None
    pixel_size = 32
    dir_x,dir_y = 0,0
    def __init__(self, name, x, y, oretype = Items(1)):
        #필요한거: 위치, 이미지, state(레이어 나누기 위한 블럭state), 이름, state머신
        self.oretype = oretype
        self.x = x
        self.y = y
        self.state_machine = StateMachine(self)
        self.name = name
        self.layer = Layer(2)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: { on_conveyor : Move ,leave_conveyor : Idle},
                Move: { leave_conveyor : Idle, on_conveyor : Move},
            }
        )
        if self.oretype == Items(1):
            self.image = load_image("Resource/item-beryllium.png")
        elif self.oretype == Items(2):
            self.image = load_image("Resource/item-coal.png")
        elif self.oretype == Items(3):
            self.image = load_image("Resource/item-copper.png")
        elif self.oretype == Items(4):
            self.image = load_image("Resource/item-pyratite.png")
        elif self.oretype == Items(5):
            self.image = load_image("Resource/item-titanium.png")
        elif self.oretype == Items(6):
            self.image = load_image("Resource/item-tungsten.png")

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        #event : 입력 이벤트
        #우리가 넘겨줄거 튜플 형식
        self.state_machine.add_event(('INPUT',event))

    def draw(self):
        self.state_machine.draw()

    def move(self,x,y):
        self.x += x
        self.y += y

    def collision_check(self):
        conveyor_list = []
        for o in game_world.get_world()[Layer.tile.value]:
            if o.blocks == Blocks.conveyor:
                conveyor_list.append(o)

        for conveyor in conveyor_list:
            if conveyor.x + conveyor.size > self.x > conveyor.x - conveyor.size and conveyor.y + conveyor.size > self.y > conveyor.y - conveyor.size:
                self.state_machine.add_event(('ON_CONVEYOR',0))
                self.dir_x,self.dir_y = conveyor.dir_x,conveyor.dir_y
                return

        self.state_machine.add_event(('LEAVE_CONVEYOR',0))
        self.dir_x, self.dir_y = 0,0