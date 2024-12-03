from pico2d import *
from Project.BackGround import *
from Camera import Camera
from Project.enum_define import Layer, Items
from Project.MouseIcon import MouseIcon
from Project import game_world, game_framework, play_mode






def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_world.reset_world()
            game_framework.pop_mode()
            game_framework.push_mode(play_mode)



def init():
    global cursor
    cursor = MouseIcon()
    cursor.image=load_image('Resource/cursor.png')
    background = BackGround()
    background.image=load_image('Resource/logo.png')
    background.music=load_music('Resource/Sounds/menu.ogg')
    background.music.play()
    background.width=get_canvas_width()
    background.height=get_canvas_height()
    background.x = get_canvas_width()/2
    background.y = get_canvas_height()/2
    game_world.add_object(background,Layer.backGround)




def update():
    global Camera_Instance
    cursor.update()
    game_world.update()



def draw():
    clear_canvas()
    game_world.draw()
    cursor.draw()
    update_canvas()

def finish(): # finalization code
    pass


def pause():
    pass

def resume():
    pass






