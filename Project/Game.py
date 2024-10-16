from tkinter import Canvas

from pico2d import *

from BackGround import *
from Camera import Camera
from tile_map import TileMap
from tile_map_manager import TileMapManager

# Game object class here
world = []#게임 오브젝트 리스트
Camera_Instance = Camera()

running = True


def handle_events():
    global running
    global world
    global Camera_Instance
    tile_map_instance = TileMapManager()
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            new_tile = tile_map_instance.click(event.x, (get_canvas_height() - event.y))
            #이벤트 x입력은 오른쪽 아래 기준 0,0부터 시작 
            # 만약 카메라를 왼쪽으로 갔다면? x를 -20 갔다는 가정하에
            # 다시 0,0 에다가 점을 찍으면 좌표값이 -20,0 에 찍혀야됨
            # 실제로 -20, 0 에 잘 찍히는데 문제는 실제 캔버스가 움직인것은 아니라 이상한곳에 찍힘
            # 저장할때 조절해서 저장
            if new_tile != None:
                world.append(new_tile)
            else:
                pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F9:
            for o in world:
                if isinstance(o, TileMap):
                    f = open('tiles.txt', 'a')
                    f.write(f'{o.x},{o.y}\n')
                    f.close()
                    #타일맵 추가 저장
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F8:
            for o in world:
                if isinstance(o, TileMap):
                    f = open('tiles.txt', 'w')
                    f.write(f'{o.x},{o.y}\n')
                    f.close()
                    #타일맵 다시저장
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Camera_Instance.move(-20,0,world)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Camera_Instance.move(20,0,world)
        else:
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
    tiles = open("tiles.txt", 'r')
    for line in tiles.readlines():
        x, y = map(int, line.split(','))
        tileMap = TileMap(x, y)
        tileMap.image = load_image('Resource/tile1.png')
        world.append(tileMap)


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