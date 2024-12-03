
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
    def draw(self):
        if self.image is None:
            return
        elif self.block == Blocks.furnace:
            self.image.draw(self.x+16,self.y-16,32,32)
        elif self.block == Blocks.iron_ore:
            self.image.draw(self.x+16,self.y-16,32,32)
        else:
            self.image.draw(self.x,self.y,64,64)
    def update(self):
        pass
    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, (get_canvas_height() - event.y)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_F1:
                self.image = load_image('Resource/cursor.png')
                self.block = None
            elif event.key == SDLK_F2:
                self.image = load_image('Resource/hand.png')
                self.block = None
            elif event.key == SDLK_F3:
                self.image = load_image('Resource/target.png')
                self.block = None
            elif event.key == SDLK_F4:
                self.image = load_image('Resource/drill.png')
                self.block = None
            elif event.key == SDLK_0:
                self.image = load_image('Resource/cursor-tile.png')
                self.block = Blocks.wall
            elif event.key == SDLK_1:
                self.image = load_image('Resource/cursor-conveyor.png')
                self.block = Blocks.conveyor
            elif event.key == SDLK_2:
                self.image = load_image('Resource/cursor-beryllium-ore.png')
                self.block = Blocks.beryllium_ore
            elif event.key == SDLK_3:
                self.image = load_image('Resource/cursor-blast-drill.png')
                self.block = Blocks.drill
            elif event.key == SDLK_4:
                self.image = load_image('Resource/cursor-container.png')
                self.block = Blocks.base_tile
            elif event.key == SDLK_5:
                self.image = load_image('Resource/cursor-crafter.png')
                self.block = Blocks.crafter
            elif event.key == SDLK_6:
                self.image = load_image('Resource/tile-furnace.png')
                self.block = Blocks.furnace
            elif event.key == SDLK_7:
                self.image = load_image('Resource/cursor-ore-coal-tile.png')
                self.block = Blocks.coal_ore
            elif event.key == SDLK_8:
                self.image = load_image('Resource/ore-iron-tile.png')
                self.block = Blocks.iron_ore