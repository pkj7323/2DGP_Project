class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, x, y,world):
        self.x += x
        self.y += y
        for o in world:
            o.move(-x,-y)