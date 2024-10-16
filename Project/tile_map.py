from pico2d import *

class TileMap():
    image = None
    def __init__(self,x=0,y=0,camera_x=0,camera_y=0):
        self.x = x
        self.y = y
        self.adjust_x = camera_x
        self.adjust_y = camera_y
        self.size = 20
    def draw(self):
        if self.image is None:
            return
        self.image.draw(self.x,self.y,self.size,self.size)
    def update(self):
        pass
    def move(self,x,y):
        self.x += x
        self.y += y
