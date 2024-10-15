from pico2d import load_image


class BackGround:
    def __init__(self):
        self.image = load_image("Resource\\Brick.png")
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,300,800,600)