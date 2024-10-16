from Project.BlockState import BlockState
from Project.tile_map import TileMap
from pico2d import *
from Grid import *

class TileMapManager:

    def __init__(self):
        self.grid = Grid(20)
    def click(self, x, y, Camera):
        center_x, center_y = self.grid.adjust_to_nearest_center(x + Camera.x, y + Camera.y)
        tile_x, tile_y = self.grid.adjust_to_nearest_center(x,y)
        if self.grid.is_center_available((center_x, center_y)):
            self.grid.mark_center_used((center_x, center_y))
            new_tile = TileMap(tile_x, tile_y,Camera.x, Camera.y,BlockState(0))
            if new_tile.image == None:
                new_tile.image = load_image('Resource\\tile1.png')
            return new_tile
        else:
            return None
    def open_tile(self, world, path):
        tiles = open(path, 'r')
        for line in tiles.readlines():
            x, y = map(int, line.split(','))
            tileMap = TileMap(x, y)
            tileMap.image = load_image('Resource/tile1.png')
            world.append(tileMap)

    def save(self,world, path, mode):
        if mode == 0:
            f = open(path, 'a')
            for o in world:
                if isinstance(o, TileMap):
                    f.write(f'{o.adjust_x},{o.adjust_y}\n')
            f.close()
        elif mode == 1:
            f = open(path, 'w')
            for o in world:
                if isinstance(o, TileMap):
                    f.write(f'{o.adjust_x},{o.adjust_y}\n')
            f.close()

    def handle_event(self, event, world, Camera_Instance):
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            new_tile = self.click(event.x, (get_canvas_height() - event.y), Camera_Instance)
            # 이벤트 x입력은 오른쪽 아래 기준 0,0부터 시작
            # 만약 카메라를 왼쪽으로 갔다면? x를 -20 갔다는 가정하에
            # 다시 0,0 에다가 점을 찍으면 좌표값이 -20,0 에 찍혀야됨
            # 실제로 -20, 0 에 잘 찍히는데 문제는 실제 캔버스가 움직인것은 아니라 이상한곳에 찍힘
            # 저장할때 조절해서 저장
            if new_tile != None:
                world.append(new_tile)
            else:
                pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F9:
            self.save(world, 'tiles.txt', 0)
            # 타일맵 추가 저장
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F8:
            self.save(world, 'tiles.txt', 1)
            # 타일맵 다시저장