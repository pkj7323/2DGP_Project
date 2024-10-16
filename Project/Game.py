from pico2d import *

from BackGround import *
from Camera import Camera
from tile_map_manager import TileMapManager


# Game object class here
world = []#게임 오브젝트 리스트
Camera_Instance = Camera()
tile_map_instance = TileMapManager()
running = True


def handle_events():
    global running
    global world
    global Camera_Instance

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            Camera_Instance.handle_event(event)
            tile_map_instance.handle_event(event,world, Camera_Instance)
            pass


def reset_world():
    global running
    global world
    global Camera_Instance
    Camera_Instance = Camera()
    running = True
    background = BackGround()
    world = []
    world.append(background)
    tile_map_instance.open_tile(world,'tiles.txt')


def update_world():
    global Camera_Instance
    for o in world:
        o.update()
    Camera_Instance.move(world)


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