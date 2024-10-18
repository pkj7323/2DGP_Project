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
    def open_tile(self, path):
        tiles = open(path, 'r')
        world =[]
        for line in tiles.readlines():
            x, y , state = map(int, line.split(','))
            state = BlockState(state)
            tileMap = TileMap(x, y,0,0, state)
            tileMap.image = load_image('Resource/tile1.png')
            world.append(tileMap)
        return world

    def save(self,world, path, mode):
        if mode == 0:
            f = open(path, 'a')
            for o in world:
                if isinstance(o, TileMap):
                    f.write(f'{o.adjust_x},{o.adjust_y},{o.state.value}\n')
            f.close()
        elif mode == 1:
            f = open(path, 'w')
            for o in world:
                if isinstance(o, TileMap):
                    f.write(f'{o.adjust_x},{o.adjust_y},{o.state.value}\n')
            f.close()

    def handle_event(self, event, world, Camera_Instance):
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            new_tile = self.click(event.x, (get_canvas_height() - event.y), Camera_Instance)
            if new_tile != None:
                world.append(new_tile)
            else:
                pass
        # elif event.type == SDL_KEYDOWN and event.key == SDLK_F9:
        #     self.save(world, 'tiles.txt', 0)
        #     # 타일맵 추가 저장
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F8:
            self.save(world, 'tiles.txt', 1)
            # 타일맵 다시저장