import enum_define
class Grid:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.used_centers = [set() for i in range(enum_define.Layer.end.value)]
    def adjust_to_nearest_center(self, x, y):
        grid_x = (x // self.cell_size) * self.cell_size + self.cell_size // 2
        grid_y = (y // self.cell_size) * self.cell_size + self.cell_size // 2
        return grid_x, grid_y

    def is_center_available(self, center, block_state):#block_state == type(layer)
        is_available = True
        for value in range(enum_define.Layer.end.value):
            for s in self.used_centers[value]:
                if center[0]==s[0] and center[1]==s[1]:
                    is_available = False
                    break
        return is_available

    def mark_center_used(self, center, block_state):#block_state == type(layer)
        self.used_centers[block_state.value].add(center)
    def remove_center_used(self, center):
        for block_state in range(enum_define.Layer.end.value):
            if center in self.used_centers[block_state]:
                self.used_centers[block_state].remove(center)