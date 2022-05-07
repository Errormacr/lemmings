

class Gate:
    def __init__(self, x: int, y: int, row_index: int):
        self.x = x
        self.y = y
        self.entry_img = (0, 0, 32, 16, 16, 0)
        self.exit_img = (0, 16, 32, 16, 16, 0)
        self.row_index = row_index
