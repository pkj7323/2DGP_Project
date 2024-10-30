from pico2d import load_image

from Project.BlockState import BlockState


class BackGround:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 3200
        self.height = 2400
        self.image = load_image("Resource\\Red_Sandstone.png")
        self.state = BlockState.backGround
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x,self.y,self.width,self.height)
    def move(self, x ,y):
        self.x += x
        self.y += y