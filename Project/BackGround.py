from pico2d import load_image


class BackGround:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = load_image("Resource\\Red_Sandstone.png")
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x,self.y,800*4,600*4)
    def move(self, x ,y):
        self.x += x
        self.y += y