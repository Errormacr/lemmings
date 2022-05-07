from random import randint
from .Platforms import Platforms
from .Gate import Gate
from .Constants import Constants


class Gameboard:
    def __init__(self):  # инициализация

        self.Constants = Constants()
        self.cell_size = self.Constants.cell_size

        self.grid = self.create_grid()

        self.Platform = Platforms()
        self.platforms = self.Platform.generate_platforms()

    def is_inside_platform(self: int, y: int, platforms: list):  # проверка на плотформу
        is_inside = False

        for platform in platforms:
            x_in_platform = platform.x <= self <= platform.x + platform.width
            y_in_platform = y == platform.y
            if x_in_platform and y_in_platform:
                is_inside = True

        return is_inside

    def create_grid(self):  # создание игрового поля

        grid = []
        for row in range(self.Constants.grid_rows):
            for column in range(self.Constants.grid_columns):
                row_coordinate = self.cell_size * (row + 2)
                column_coordinate = self.cell_size * column

                grid.append([column_coordinate, row_coordinate])

        return grid

    def generate_gate(self, platforms, entry_gate_index=0, exit_gate=False):  # генерация ворот входа и выхода
        self.platforms = self.Platform.generate_platforms()

        row_index = randint(0, self.Constants.platforms_num - 1)

        if exit_gate:
            for platform in platforms:
                while row_index == entry_gate_index:
                    row_index = randint(0, self.Constants.platforms_num - 1)

        else:
            pass
        print()
        some = True
        gate_y = platforms[row_index].y
        gate_x = randint(platforms[row_index].x // self.cell_size + 1,
                         (platforms[row_index].x + platforms[row_index].width)
                         // self.cell_size - 1)
        gate_x *= self.cell_size
        while some:
            some = False
            for platform in platforms:
                y_in_platform = platform.y - 16 < gate_y <= platform.y
                if y_in_platform:
                    for platform2 in platforms:
                        x_in_platform = platform2.x < gate_x < platform.x + platform2.width
                        y_in_second_platform = platform2.y - 16 <= gate_y - 16 <= platform2.y
                        if y_in_second_platform and x_in_platform:
                            gate_y -= 16
                            some = True
                            break
        gate_y += 16

        return Gate(gate_x, gate_y, row_index)
