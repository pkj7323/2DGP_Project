from pico2d import load_image, load_music
from Project import game_world
from Project.enum_define import Items


class Pannel:
    def __init__(self):
        self.image = load_image('Resource/milestone.png')
        self.complete_image = load_image('Resource/yellow.png')
        self.collect_copper = False
        self.collect_beryllium = False
        self.collect_coal = False

    def update(self):
        if Items.copper in game_world.items and game_world.items[Items.copper] > 0:
            self.collect_copper = True
        if Items.beryllium in game_world.items and game_world.items[Items.beryllium] > 0:
            self.collect_beryllium = True
        if Items.coal in game_world.items and game_world.items[Items.coal] > 0:
            self.collect_coal = True
        if self.collect_copper and self.collect_beryllium and self.collect_coal:
            game_world.milestones = 1

    def draw(self):
        if self.collect_beryllium:
            self.complete_image.draw_to_origin(50,470,170,90)
        if self.collect_coal:
            self.complete_image.draw_to_origin(320,470,170,90)
        if self.collect_copper:
            self.complete_image.draw_to_origin(570,470,170,90)
        if self.collect_beryllium and self.collect_coal and self.collect_copper:
            self.complete_image.draw_to_origin(320,230,185,110)
        self.image.draw(400,300)

class Pannel_2:
    def __init__(self):
        self.image = load_image('Resource/milestone_2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,300)

class EndingPannel:
    def __init__(self):
        self.image = load_image('Resource/ending.png')
        self.sound = load_music('Resource/StellarDrone-Pluto.mp3')
        self.sound.set_volume(100)
        self.sound.play()

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,300)
