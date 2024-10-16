from pico2d import *

from BackGround import *
from Project.Grid import Grid
from Project.tile_map import TileMap
from Project.tile_map_manager import TileMapManager

# Game object class here
world = []#게임 오브젝트 리스트


running = True
class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, x, y):
        self.x += x
        self.y += y


def handle_events():
    global running
    global world
    tile_map_instance = TileMapManager()
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            new_tile = tile_map_instance.click(event.x, event.y)
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
            for o in world:
                o.move(20,0)
        else:
            pass


def reset_world():
    global running
    global world

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