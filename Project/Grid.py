class Grid:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.used_centers = set()

    def adjust_to_nearest_center(self, x, y):
        grid_x = (x // self.cell_size) * self.cell_size + self.cell_size // 2
        grid_y = (y // self.cell_size) * self.cell_size + self.cell_size // 2
        return grid_x, grid_y

    def is_center_available(self, center):
        return center not in self.used_centers

    def mark_center_used(self, center):
        self.used_centers.add(center)
