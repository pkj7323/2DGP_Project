from pico2d import clear_canvas, update_canvas, get_events, load_music
from sdl2 import SDL_KEYDOWN, SDLK_i, SDLK_ESCAPE, SDL_QUIT

from Project.enum_define import Layer
from Project.pannel import Pannel, EndingPannel
from Project import game_world
from Project import game_framework

def init():
    global pannel
    pannel = EndingPannel()

    game_world.add_object(pannel, Layer.milestone)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.quit()

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