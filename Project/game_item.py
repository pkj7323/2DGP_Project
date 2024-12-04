import random

from pico2d import load_image, draw_rectangle, load_wav

from Project import game_framework, game_world
from Project.enum_define import Items, Layer
from Project.state_machine import StateMachine, on_conveyor, leave_conveyor
from Project import ending_mode

class Move:
    @staticmethod
    def enter(item, e):
        item.timer = 0.0
    @staticmethod
    def exit(item, e):
        pass
    @staticmethod
    def do(item):
        item.x += item.dir_x * item.speed * game_framework.frame_time
        item.y += item.dir_y * item.speed * game_framework.frame_time
        item.timer += game_framework.frame_time
        if item.timer >= 5 and item.item_type == Items.diamond_sword:
            game_framework.push_mode(ending_mode)
    @staticmethod
    def draw(item):
        item.image.draw(item.x, item.y, item.size, item.size)
class Idle:
    @staticmethod
    def enter(item, e):
        item.dir_x , item.dir_y = 0, 0
        item.timer = 0.0

    @staticmethod
    def exit(item, e):
        pass

    @staticmethod
    def do(item):
        item.timer += game_framework.frame_time
        if item.timer >= 5:
            game_world.remove_object(item)

    @staticmethod
    def draw(item):
        #left, bottom, width, height, x, y, w = None, h = None
        #draw(self, x, y, w=None, h=None):
        item.image.draw(item.x, item.y, item.size, item.size)


class GameItem:
    image = None
    pixel_size = 32
    dir_x,dir_y = 0,0
    size = 16
    def __init__(self, name, x, y, itemType):
        #필요한거: 위치, 이미지, state(레이어 나누기 위한 블럭state), 이름, state머신
        self.colliding = False
        self.item_type = itemType
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
        game_world.add_collision_pair("Item:CONVEYOR1", self, None)
        game_world.add_collision_pair("Base:Item", None, self)
        if self.item_type == Items.rod:
            self.image = load_image("Resource/item-breeze_rod.png")
            game_world.add_collision_pair("Diamond:Rod", None, self)
        elif self.item_type == Items.diamond_sword:
            self.image = load_image("Resource/item-diamond_sword.png")
            sound = load_wav('Resource/levelup.wav')
            sound.set_volume(10)
            sound.play()
            self.size = 128


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
        if group == 'Item:CONVEYOR1':
            self.state_machine.add_event(('ON_CONVEYOR', 0))
            self.dir_x, self.dir_y = other.dir_x, other.dir_y
            self.speed = other.transfer_speed

        if group == 'Base:Item':
            game_world.remove_object(self)

        if group == 'Diamond:Rod':
            game_world.remove_object(self)
            result = random.randrange(1,100)
            if result == 1:
                sword = GameItem("diamond_sword",self.x,self.y,Items.diamond_sword)
                game_world.add_object(sword,Layer.end)


        self.colliding = True


    def handle_collision_end(self):
        self.colliding = False
        self.state_machine.add_event(('LEAVE_CONVEYOR', 0))