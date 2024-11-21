from enum import nonmember

from pico2d import load_image, get_time, draw_rectangle

from Project.enum_define import Layer, Items, Blocks
from Project.state_machine import StateMachine, on_conveyor, leave_conveyor
from Project import game_world
from Project import game_framework
class Move:
    @staticmethod
    def enter(ore, e):
        pass
    @staticmethod
    def exit(ore, e):
        pass
    @staticmethod
    def do(ore):
        ore.x += ore.dir_x * ore.speed * game_framework.frame_time
        ore.y += ore.dir_y * ore.speed * game_framework.frame_time

    @staticmethod
    def draw(ore):
        ore.image.draw(ore.x, ore.y, ore.size, ore.size)
class Idle:
    @staticmethod
    def enter(ore, e):
        ore.dir_x , ore.dir_y = 0, 0

    @staticmethod
    def exit(ore, e):
        pass

    @staticmethod
    def do(ore):
        pass

    @staticmethod
    def draw(ore):
        #left, bottom, width, height, x, y, w = None, h = None
        #draw(self, x, y, w=None, h=None):
        ore.image.draw(ore.x, ore.y, ore.size, ore.size)


class Oreitem:
    image = None
    pixel_size = 32
    dir_x,dir_y = 0,0
    size = 16
    def __init__(self, name, x, y, oretype = Items.beryllium):
        #필요한거: 위치, 이미지, state(레이어 나누기 위한 블럭state), 이름, state머신
        self.colliding = False
        self.ore_type = oretype
        self.x = x
        self.y = y
        self.state_machine = StateMachine(self)
        self.name = name
        self.speed = 10
        self.layer = Layer.ore
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: { on_conveyor : Move ,leave_conveyor : Idle},
                Move: { leave_conveyor : Idle, on_conveyor : Move},
            }
        )
        if self.ore_type == Items.beryllium:
            self.image = load_image("Resource/item-beryllium.png")
        elif self.ore_type == Items.coal:
            self.image = load_image("Resource/item-coal.png")
        elif self.ore_type == Items.copper:
            self.image = load_image("Resource/item-copper.png")
        elif self.ore_type == Items.pyratite:
            self.image = load_image("Resource/item-pyratite.png")
        elif self.ore_type == Items.titanium:
            self.image = load_image("Resource/item-titanium.png")
        elif self.ore_type == Items.tungsten:
            self.image = load_image("Resource/item-tungsten.png")
        game_world.add_collision_pair("ore:CONVEYOR1", self, None)
        game_world.add_collision_pair("Base:Ore", None, self)
    def update(self):
        self.state_machine.update()
        self.check_collision_end()

    def handle_event(self, event):
        #event : 입력 이벤트
        #우리가 넘겨줄거 튜플 형식
        self.state_machine.add_event(('INPUT',event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def move(self,x,y):
        self.x += x
        self.y += y

    def check_collision_end(self):
        if self.colliding:
            self.handle_collision_end()

    def get_bb(self):
        return self.x - self.size/2, self.y + self.size/2, self.x + self.size/2, self.y - self.size/2

    def check_collision(self,other):
        if (other.x + other.size >= self.x + self.size / 2 >= other.x
                and other.y + other.size >= self.y + self.size / 2 >= other.y):
            return True
        else:
            return False


    def handle_collision(self, group,other):
        if group == 'ore:CONVEYOR1':
            self.state_machine.add_event(('ON_CONVEYOR', 0))
            self.dir_x, self.dir_y = other.dir_x, other.dir_y
            self.speed = other.transfer_speed
        if group == 'Base:Ore':
            game_world.remove_object(self)
        self.colliding = True


    def handle_collision_end(self):
        self.colliding = False
        self.state_machine.add_event(('LEAVE_CONVEYOR', 0))