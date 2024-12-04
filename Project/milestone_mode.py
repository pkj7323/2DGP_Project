from pico2d import clear_canvas, update_canvas, get_events
from sdl2 import SDL_KEYDOWN, SDLK_i, SDLK_ESCAPE

from Project.enum_define import Layer
from Project.pannel import Pannel
from Project import game_world
from Project import game_framework

def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel, Layer.milestone)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass

def finish():
    global pannel
    game_world.remove_object(pannel)
    del pannel