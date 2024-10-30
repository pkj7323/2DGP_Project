from pico2d import *

from BackGround import *
from Camera import Camera
from Project.BlockState import BlockState
from Project.MouseIcon import MouseIcon
from Project.tile_map import TileMap
import tile_map_manager

# Game object class here
world = []#게임 오브젝트 리스트
Camera_Instance = Camera()
tile_map_instance = tile_map_manager.TileMapManager()
cursor = MouseIcon()
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
            cursor.handle_event(event)
            pass


def reset_world():
    global running
    global world
    global Camera_Instance
    global cursor
    Camera_Instance = Camera()
    running = True
    background = BackGround()
    world = [[] for i in range(BlockState.end.value)]
    world[BlockState.backGround.value].append(background)
    tiles = tile_map_instance.open_tile('tiles.txt')
    for tile in tiles:
        if tile.state.value == BlockState.wall.value:
            world[BlockState.wall.value].append(tile)
        else:
            pass
    cursor.image=load_image('Resource/cursor.png')


def update_world():
    global Camera_Instance
    cursor.update()
    for i in range(BlockState.end.value):
        for o in world[i]:
            o.update()
    Camera_Instance.move(world)


def render_world():
    clear_canvas()
    for i in range(BlockState.end.value):
        for o in world[i]:
            o.draw()
    cursor.draw()
    update_canvas()

def destroy(): # finalization code
    tile_map_manager.save_no_duplication('tiles.txt')
    close_canvas()







open_canvas()
hide_cursor()
reset_world()

# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)


destroy()
