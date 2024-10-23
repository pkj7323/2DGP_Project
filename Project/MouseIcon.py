from pico2d import *

from Project.BlockState import BlockState


class MouseIcon:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = BlockState.mouse
        self.image = None
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        pass
    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, (get_canvas_height() - event.y)
            self.draw()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_F1:
                self.image = load_image('Resource/cursor.png')
            elif event.key == SDLK_F2:
                self.image = load_image('Resource/hand.png')
            elif event.key == SDLK_F3:
                self.image = load_image('Resource/target.png')
            elif event.key == SDLK_F4:
                self.image = load_image('Resource/drill.png')