from pico2d import *

import milestone_mode
from BackGround import *
from Camera import Camera
from Project.Oreitem import Oreitem
from Project.enum_define import Layer, Items
from Project.MouseIcon import MouseIcon
import game_world
import tile_map_manager
import game_framework
# Game object class here

Camera_Instance = Camera()
tile_map_instance = tile_map_manager.TileMapManager()
cursor = MouseIcon()





def handle_events():

    global Camera_Instance

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_mode(milestone_mode)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
            ore = Oreitem('beryllium_ore',event.x, (get_canvas_height() - event.y),Items(1))
            game_world.add_object(ore,Layer.ore)
            game_world.add_collision_pair("ore:CONVEYOR1",ore,None)
        else:
            Camera_Instance.handle_event(event)
            tile_map_instance.handle_event(event, Camera_Instance)
            cursor.handle_event(event)

            pass


def init():
    global running
    global Camera_Instance
    global cursor
    Camera_Instance = Camera()
    background = BackGround()
    game_world.add_object(background,Layer.backGround)

    tile_map_instance.open_tile('tiles.txt')

    cursor.image=load_image('Resource/cursor.png')



def update():
    global Camera_Instance
    cursor.update()
    Camera_Instance.move()
    game_world.update()
    game_world.handle_collision()


def draw():
    clear_canvas()
    game_world.draw()
    cursor.draw()
    # font = Font('Resource/KCC_dodaumdodaum.ttf', 20)
    # font.draw(0,get_canvas_height() - 10,"자원 현황",(255,255,255))
    # font.draw(0,get_canvas_height() - 30,"자원",(255,255,255))

    update_canvas()

def finish(): # finalization code
    tile_map_manager.save_no_duplication('tiles.txt')
    #close_canvas()

def pause():
    pass

def resume():
    pass






# open_canvas()
# hide_cursor()
# reset_world()
#
# # game loop
# while running:
#     handle_events()
#     update_world()
#     render_world()
#     delay(0.01)
#
#
# destroy()
