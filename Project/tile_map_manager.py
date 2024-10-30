import enum
import math

from Project.BlockState import BlockState
from Project.tile_map import TileMap
from tile_map import Blocks
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






class TileMapManager:

    def __init__(self):
        self.tile_size = 20
        self.grid = Grid(self.tile_size)
        self.state = BlockState.BlockState(1)
        self.nowBlocks = Blocks(1)
        self.flip = ''
        self.rad = 0
    def click(self, x, y, camera):#block_state == type(BlockState)

        center_x, center_y = self.grid.adjust_to_nearest_center(x + camera.x, y + camera.y)
        tile_x, tile_y = self.grid.adjust_to_nearest_center(x,y)
        #마우스 위치보정하는 코드

        if self.grid.is_center_available((center_x, center_y, self.nowBlocks.value, self.flip, self.rad), self.state):
            self.grid.mark_center_used((center_x, center_y, self.nowBlocks.value, self.flip, self.rad), self.state)
            new_tile = TileMap(tile_x, tile_y,camera.x, camera.y, self.state, self.nowBlocks, self.flip, self.rad)
            new_tile.loadImage()
            return new_tile
        else:
            return None
    def remove_click(self,x,y,camera,world):
        center_x, center_y = self.grid.adjust_to_nearest_center(x + camera.x, y + camera.y)
        tile_x, tile_y = self.grid.adjust_to_nearest_center(x, y)
        # 마우스 위치보정하는 코드
        for o in world[self.state.value]:
            if o.x == tile_x and o.y == tile_y:
                world[self.state.value].remove(o)
                break
        if not self.grid.is_center_available((center_x, center_y, self.nowBlocks.value, self.flip, self.rad),
                                             self.state):
            self.grid.remove_center_used((center_x, center_y, self.nowBlocks.value, self.flip, self.rad), self.state)

    def handle_event(self, event, world, camera_instance):
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            new_tile = self.click(event.x, (get_canvas_height() - event.y),
                                  camera_instance)
            if new_tile is not None:#is와 is not은 객체끼리 비교함 값이 같아도 다르게 비교함
                # 값끼리 비교하는 거면 원래 비교연산자 써야됨 주의주의
                world[self.state.value].append(new_tile)
            else:
                pass
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
            self.remove_click(event.x, (get_canvas_height() - event.y), camera_instance,world)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_F8:
                self.save(world, 'tiles.txt', 0)
            elif event.key == SDLK_F9:
                self.save(world, 'tiles.txt', 1)
            elif event.key == SDLK_e:
                self.rad += math.radians(90)
            elif event.key == SDLK_q:
                self.rad += math.radians(-90)
            elif event.key == SDLK_1:
                self.nowBlocks = Blocks.conveyor

            # 타일맵 추가저장

    def open_tile(self,path):
        tiles = open(path, 'r')
        world = []

        for line in tiles.readlines():
            values = line.strip().split(',')

            # 각 값을 적절한 타입으로 변환

            x = int(values[0])  # 첫 번째 값: 정수
            y = int(values[1])  # 두 번째 값: 정수
            image = Blocks(int(values[2]))  # 세 번째 값: 정수
            flip = values[3] # 네 번째 값: 문자열 또는 None
            rad = float(values[4])  # 다섯 번째 값: 부동소수점 수
            state=BlockState.BlockState(int(values[5]))  # 여섯 번째 값: 정수



            tile_map = TileMap(x, y, 0, 0, state, image, flip, rad)
            self.grid.mark_center_used((x, y, image.value, flip, rad), state) #파일에서 타일 불러올때 그리드에도 업데이트를 함
            tile_map.loadImage()
            world.append(tile_map)
        return world

    def save(self,world, path, mode):
        if mode == 0:
            f = open(path, 'a')
            for i in range(BlockState.BlockState.end.value):
                for o in world[i]:
                    if isinstance(o, TileMap):
                        f.write(f'{o.adjust_x},{o.adjust_y},{o.blocks.value},{o.state.value}\n')
            f.close()
        elif mode == 1:
            f = open(path, 'w')
            i = 0
            for used_center_set in self.grid.used_centers:
                if len(used_center_set) == 0:
                    i += 1
                    continue
                for used_center_tuple in used_center_set:
                    f.write(f'{used_center_tuple[0]},{used_center_tuple[1]}'
                            f',{used_center_tuple[2]},{used_center_tuple[3]},'
                            f'{used_center_tuple[4]},{i}\n')
                i += 1
            f.close()