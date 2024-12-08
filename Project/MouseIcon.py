
from pico2d import *

from Project import game_world
from Project.enum_define import Layer, Blocks


class MouseIcon:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = Layer.mouse
        self.image = None
        self.block = None
        self.arrow_image = load_image("Resource/arrow.png")
    def draw(self):
        self.arrow_image.clip_composite_draw(0, 0, 32, 32, math.radians(game_world.degree), '', 10,
                                             get_canvas_height() - 15, 32, 32)
        if self.image is None:
            return
        elif (self.block == Blocks.furnace or self.block == Blocks.iron_ore or self.block == Blocks.copper_ore
              or self.block == Blocks.titanium_ore or self.block == Blocks.beacon):
            self.image.draw(self.x+16,self.y-16,32,32)
        else:
            self.image.draw(self.x,self.y,64,64)
    def update(self):
        pass
    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, (get_canvas_height() - event.y)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_1:
                self.image = load_image('Resource/cursor-conveyor.png')
                self.block = Blocks.conveyor
            elif event.key == SDLK_2:
                self.image = load_image('Resource/cursor-blast-drill.png')
                self.block = Blocks.drill
            elif event.key == SDLK_3:
                self.image = load_image('Resource/cursor-crafter.png')
                self.block = Blocks.crafter
            elif event.key == SDLK_4:
                self.image = load_image('Resource/cursor-container.png')
                self.block = Blocks.base_tile
            elif event.key == SDLK_5:
                self.image = load_image('Resource/tile-furnace.png')
                self.block = Blocks.furnace
            elif event.key == SDLK_6:
                self.image = load_image('Resource/tile-beacon.png')
                self.block = Blocks.beacon
