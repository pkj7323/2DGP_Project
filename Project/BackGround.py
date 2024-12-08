import math

from pico2d import load_image, load_music, get_canvas_height

from Project.enum_define import Layer
from Project import game_world


class BackGround:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 3200
        self.height = 2400
        self.image = load_image("Resource\\Red_Sandstone.png")
        #self.arrow_image = load_image("Resource/arrow.png")
        self.layer = Layer.backGround
        self.music = load_music('Resource/Sounds/fine.ogg')
        self.music.set_volume(30)
        self.music.play()
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x,self.y,self.width,self.height)
    def move(self, x ,y):
        self.x += x
        self.y += y