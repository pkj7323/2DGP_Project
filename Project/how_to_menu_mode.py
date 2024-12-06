from pico2d import clear_canvas, update_canvas, get_events
from sdl2 import SDL_KEYDOWN, SDLK_i, SDLK_ESCAPE, SDL_QUIT

from Project.enum_define import Layer
from Project.pannel import Pannel, Pannel_2, HowToPlannel
from Project import game_world, play_mode
from Project import game_framework

def init():
    global pannel
    pannel = HowToPlannel()
    game_world.add_object(pannel, Layer.milestone)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_world.reset_world()
            game_framework.pop_mode()
            game_framework.push_mode(play_mode)


def update():
    global pannel
    pannel.update()

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