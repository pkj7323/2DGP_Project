from Project.enum_define import Layer, Blocks
from Project.conveyor_tile import ConveyorTile
from ore_tile import OreTile
from Project.tile_map import TileMap
from pico2d import *
from Grid import *
from Project import game_world


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
        self.layer = Layer(1)
        self.nowBlocks = Blocks(1)
        self.flip = ''
        self.degree = 0
    def click(self, x, y, camera):#block_state == type(BlockState)

        tile_x, tile_y = self.grid.adjust_to_nearest_center(x,y)
        center_x, center_y = self.grid.adjust_to_nearest_center(x + camera.x, y + camera.y)
        #마우스 위치보정하는 코드

        if self.grid.is_center_available((center_x, center_y, self.nowBlocks.value, self.flip, self.degree), self.layer):
            self.grid.mark_center_used((center_x, center_y, self.nowBlocks.value, self.flip, self.degree), self.layer)
            new_tile = TileMap()
            if self.nowBlocks.value == Blocks.wall.value:
                new_tile = TileMap(tile_x, tile_y,camera.x, camera.y, self.layer, self.nowBlocks, self.flip, self.degree)
            elif self.nowBlocks.value == Blocks.conveyor.value:
                new_tile = ConveyorTile(tile_x, tile_y, camera.x, camera.y, self.layer, self.nowBlocks, self.flip, self.degree)
                game_world.add_collision_pair("ore:CONVEYOR1", None, new_tile)
            elif self.nowBlocks.value == Blocks.beryllium_ore.value:
                new_tile = OreTile(tile_x, tile_y, camera.x, camera.y, self.layer, self.nowBlocks, self.flip, self.degree)
            return new_tile
        else:
            return None
    def remove_click(self,x,y,camera):
        center_x, center_y = self.grid.adjust_to_nearest_center(x + camera.x, y + camera.y)
        tile_x, tile_y = self.grid.adjust_to_nearest_center(x, y)
        # 마우스 위치보정하는 코드
        for o in game_world.get_world()[self.layer.value]:
            if o.x == tile_x and o.y == tile_y and o.blocks.value == self.nowBlocks.value:
                game_world.remove_object(o)
                break
            print('삭제 안된듯')
        if not self.grid.is_center_available((center_x, center_y, self.nowBlocks.value, self.flip
                                              , self.degree), self.layer):
            self.grid.remove_center_used((center_x, center_y, self.nowBlocks.value, self.flip
                                          , self.degree), self.layer)

    def handle_event(self, event, camera_instance):
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            new_tile = self.click(event.x, (get_canvas_height() - event.y),
                                  camera_instance)
            if new_tile is not None:#is와 is not은 객체끼리 비교함 값이 같아도 다르게 비교함
                # 값끼리 비교하는 거면 원래 비교연산자 써야됨 주의주의
                game_world.add_object(new_tile, self.layer)
            else:
                pass
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
            self.remove_click(event.x, (get_canvas_height() - event.y), camera_instance)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_F8:
                self.save('tiles.txt', 0)
            elif event.key == SDLK_F9:
                self.save('tiles.txt', 1)
            elif event.key == SDLK_e:
                self.degree += 90
                if self.degree >= 360:
                    self.degree = 0
            elif event.key == SDLK_q:
                self.degree -= 90
                if self.degree <= -360:
                    self.degree = 0
            elif event.key == SDLK_1:
                self.nowBlocks = Blocks.conveyor
            elif event.key == SDLK_2:
                self.nowBlocks = Blocks.beryllium_ore

            # 타일맵 추가저장

    def open_tile(self,path):
        tiles = open(path, 'r')

        for line in tiles.readlines():
            values = line.strip().split(',')
            # 각 값을 적절한 타입으로 변환

            x = int(values[0])  # 첫 번째 값: 정수
            y = int(values[1])  # 두 번째 값: 정수
            image = Blocks(int(values[2]))  # 세 번째 값: 정수 각각 타일의 이름 Blocks의 저장됨
            flip = values[3] # 네 번째 값: 문자열 또는 None
            degree = int(values[4])  # 다섯 번째 값: 부동소수점 수
            layer=Layer(int(values[5]))  # 여섯 번째 값: 정수

            tile_map = TileMap()
            if image.value == Blocks.wall.value:
                tile_map = TileMap(x, y, 0, 0, layer, image, flip, degree)
            elif image.value == Blocks.conveyor.value:
                tile_map = ConveyorTile(x, y, 0, 0, layer, image, flip, degree)
                game_world.add_collision_pair("ore:CONVEYOR1",None,tile_map)
            elif image.value == Blocks.beryllium_ore.value:
                tile_map = OreTile(x,y,0,0,layer, image, flip, degree)
            self.grid.mark_center_used((x, y, image.value, flip, degree), layer) # 파일에서 타일 불러올때 그리드에도 업데이트를 함
            game_world.add_object(tile_map, layer)

    def save(self, path, mode):
        if mode == 0:
            pass
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