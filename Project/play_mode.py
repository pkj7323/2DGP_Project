from pico2d import *

import milestone_mode
from Project.BackGround import *
from Project.Camera import Camera
from Project.Oreitem import Oreitem
from Project.enum_define import Layer, Items
from Project.MouseIcon import MouseIcon
from Project import game_world, milestone_mode2, how_to_menu_mode, how_to_mode
from Project import tile_map_manager
from Project import game_framework
from Project.game_item import GameItem

# Game object class here







def handle_events():

    global Camera_Instance

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            if game_world.milestones == 0:
                game_framework.push_mode(milestone_mode)
            elif game_world.milestones == 1:
                game_framework.push_mode(milestone_mode2)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_h:
            game_framework.push_mode(how_to_mode)
        # elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
        #     ore = Oreitem('diamond-ore-item',event.x, (get_canvas_height() - event.y),Items.diamond)
        #     game_world.add_object(ore,Layer.ore)
        # elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
        #     rod = GameItem('rod-item',event.x, (get_canvas_height() - event.y),Items.rod)
        #     game_world.add_object(rod,Layer.ore)
        else:
            Camera_Instance.handle_event(event)
            tile_map_instance.handle_event(event, Camera_Instance)
            cursor.handle_event(event)

            pass


def init():
    global running
    global Camera_Instance
    global cursor
    global tile_map_instance
    cursor = MouseIcon()
    tile_map_instance = tile_map_manager.TileMapManager()
    Camera_Instance = Camera()
    background = BackGround()
    game_world.add_object(background,Layer.backGround)
    game_world.load_items()
    tile_map_instance.open_tile('Resource/tiles.txt')

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


    update_canvas()

def finish(): # finalization code
    game_world.save_items()
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
