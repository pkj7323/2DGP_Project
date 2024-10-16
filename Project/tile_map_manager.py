from Project.BlockState import BlockState
from Project.tile_map import TileMap
from pico2d import *
from Grid import *


def save_no_duplication(path):
    f1 = open(path, 'r')
    lines = f1.readlines()
    lines = list(set(lines))
    lines.sort()

    f2 = open(path, 'w')#오픈 하는 즉시 모든 정보 사라짐
    for line in lines:
        f2.write(line)
    f2.close()

    f2.close()



def save(world, path, mode):
    if mode == 0:
        f = open(path, 'a')
        for i in range(BlockState.BlockState.end.value):
            for o in world[i]:
              if isinstance(o, TileMap):
                    f.write(f'{o.adjust_x},{o.adjust_y},{o.state.value}\n')
        f.close()
    elif mode == 1:
        f = open(path, 'w')
        for o in world:
            if isinstance(o, TileMap):
                f.write(f'{o.adjust_x},{o.adjust_y},{o.state.value}\n')
        f.close()


class TileMapManager:

    def __init__(self):
        self.tile_size = 20
        self.grid = Grid(self.tile_size)
        self.state = BlockState.BlockState(1)
    def click(self, x, y, camera,block_state):#block_state == type(BlockState)

        center_x, center_y = self.grid.adjust_to_nearest_center(x + camera.x, y + camera.y)
        tile_x, tile_y = self.grid.adjust_to_nearest_center(x,y)
        #마우스 위치보정하는 코드

        if self.grid.is_center_available((center_x, center_y), block_state):
            self.grid.mark_center_used((center_x, center_y), block_state)
            new_tile = TileMap(tile_x, tile_y,camera.x, camera.y,block_state)
            new_tile.loadImage()
            return new_tile
        else:
            return None

    def handle_event(self, event, world, camera_instance):
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            new_tile = self.click(event.x, (get_canvas_height() - event.y),
                                  camera_instance, self.state)
            if new_tile is not None:#is와 is not은 객체끼리 비교함 값이 같아도 다르게 비교함
                # 값끼리 비교하는 거면 원래 비교연산자 써야됨 주의주의
                world[self.state.value].append(new_tile)
            else:
                pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F8:
            save(world, 'tiles.txt', 0)
            # 타일맵 추가저장

    def open_tile(self,path):
        tiles = open(path, 'r')
        world = []
        for line in tiles.readlines():
            x, y, state = map(int, line.split(','))
            state = BlockState.BlockState(state)
            tile_map = TileMap(x, y, 0, 0, state)
            self.grid.mark_center_used((x, y), state) #파일에서 타일 불러올때 그리드에도 업데이트를 함
            tile_map.loadImage()
            world.append(tile_map)
        return world