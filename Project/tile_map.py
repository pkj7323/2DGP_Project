from pico2d import *

class tileMap():
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 20
    def draw(self):
        if self.image is None:
            return
        self.image.draw(self.x,self.y,self.size,self.size)
    def update(self):
        pass
