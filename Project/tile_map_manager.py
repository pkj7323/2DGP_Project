from Project.tile_map import TileMap
from pico2d import *
from Grid import *

class TileMapManager:

    def __init__(self):
        self.grid = Grid(800,600,20)
    def click(self, x, y):
        center_x, center_y = self.grid.adjust_to_nearest_center(x, get_canvas_height() - y)
        if self.grid.is_center_available((center_x, center_y)):
            self.grid.mark_center_used((center_x, center_y))
            new_tile = TileMap(center_x, center_y)
            if new_tile.image == None:
                new_tile.image = load_image('Resource\\tile1.png')
            return new_tile
        else:
            return None