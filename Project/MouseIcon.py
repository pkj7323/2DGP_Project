from pico2d import *


from Project.enum_define import Layer


class MouseIcon:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = Layer.mouse
        self.image = None
    def draw(self):
        self.image.draw(self.x,self.y,64,64)
    def update(self):
        pass
    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, (get_canvas_height() - event.y)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_F1:
                self.image = load_image('Resource/cursor.png')
            elif event.key == SDLK_F2:
                self.image = load_image('Resource/hand.png')
            elif event.key == SDLK_F3:
                self.image = load_image('Resource/target.png')
            elif event.key == SDLK_F4:
                self.image = load_image('Resource/drill.png')
            elif event.key == SDLK_0:
                self.image = load_image('Resource/cursor-tile.png')
            elif event.key == SDLK_1:
                self.image = load_image('Resource/cursor-conveyor.png')
            elif event.key == SDLK_2:
                self.image = load_image('Resource/cursor-beryllium-ore.png')
            elif event.key == SDLK_3:
                self.image = load_image('Resource/cursor-blast-drill.png')
            elif event.key == SDLK_4:
                self.image = load_image('Resource/cursor-container.png')
            elif event.key == SDLK_5:
                self.image = load_image('Resource/cursor-crafter.png')