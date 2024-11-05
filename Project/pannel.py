from pico2d import load_image


class Pannel:
    def __init__(self):
        self.image = load_image('Resource/milestone.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,300)