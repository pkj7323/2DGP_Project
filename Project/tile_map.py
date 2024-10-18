from pico2d import *

from Project.BlockState import BlockState


class TileMap():
    image = None
    def __init__(self,x=0,y=0,camera_x=0,camera_y=0,state = BlockState(0)):
        self.x = x # 카메라 기준 상대적 현재 좌표
        self.y = y # 카메라 기준 상대적 현재 좌표
        self.adjust_x = camera_x + self.x # 월드 기준 절대 좌표
        self.adjust_y = camera_y + self.y # 월드 기준 절대 좌표
        self.state = state
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
