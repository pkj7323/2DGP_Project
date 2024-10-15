from pico2d import *

from Project.tile_map import tileMap
from Project.tile_map_manager import TileMapManager

# Game object class here
world = []#게임 오브젝트 리스트
tile_map_instance = TileMapManager()
def handle_events():
    global running
    global world
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            new_Tile = tile_map_instance.click(event.x, pico2d.get_canvas_height() - event.y)
            world.append(new_Tile)
        else:
            pass


def reset_world():
    global running
    global world

    running = True
    world = []




def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()