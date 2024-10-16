from pico2d import load_image


class BackGround:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.image = load_image("Resource\\Brick.png")
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x,self.y,800,600)
    def move(self, x ,y):
        self.x += x
        self.y += y