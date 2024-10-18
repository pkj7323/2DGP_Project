import BlockState
class Grid:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.used_centers = [set() for i in range(BlockState.BlockState.end.value)]

    def adjust_to_nearest_center(self, x, y):
        grid_x = (x // self.cell_size) * self.cell_size + self.cell_size // 2
        grid_y = (y // self.cell_size) * self.cell_size + self.cell_size // 2
        return grid_x, grid_y

    def is_center_available(self, center, block_state):#block_state == type(BlockState)
        return center not in self.used_centers[block_state.value]

    def mark_center_used(self, center, block_state):#block_state == type(BlockState)
        self.used_centers[block_state.value].add(center)
