
class Stairs:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.cell_size = 16
        self.direction = direction
        
        self.left = {
            "bottom_right": [x, y],
            "top_left": [x, y],
        }
        if self.direction == "left":
            self.left["bottom_right"] = [self.x + self.cell_size, self.y + self.cell_size]
            self.left["top_left"] = [self.x, self.y]

            self.img = (0, 0, 0, -16, 16, 0)
        
        self.right = {
            "bottom_left": [x, y],
            "top_right": [x, y],
        }
        if self.direction == "right":
            self.right["bottom_left"] = [self.x, self.y + self.cell_size]
            self.right["top_right"] = [self.x + self.cell_size, self.y]

            self.img = (0, 0, 0, 16, 16, 0)

  