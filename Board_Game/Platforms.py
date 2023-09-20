from random import randint

from .Constants import Constants


class Platforms:
    def __init__(self):  # инициализация
        self.Constants = Constants()

        # Константы
        self.width = self.Constants.width
        self.height = self.Constants.cell_size
        self.cell_size = self.Constants.cell_size

        # Значение строк и столбцов
        self.grid_rows = self.Constants.grid_rows
        self.grid_columns = self.Constants.grid_columns

        # Платформы
        self.platform_min_size = self.Constants.platform_min_size
        self.platform_max_size = self.Constants.platform_max_size
        self.platforms_num = self.Constants.platforms_num

        self.img = (0, 48, 16, 16, 16, 0)

    def generate_platforms(self):  # создание платформ, возвращает список

        platforms = []
        row_coordinates = [0]

        for i in range(self.Constants.platforms_num):
            platforms.append(Platforms())
            platform_row = 0

            while platform_row in row_coordinates:
                platform_row = randint(1, self.Constants.grid_rows - 2)

            row_coordinates.append(platform_row)

            platforms[i].width = randint(platforms[i].platform_min_size,
                                         platforms[i].platform_max_size) * self.cell_size

            platform_x = ((self.Constants.grid_columns * self.cell_size) -
                          platforms[i].width) / self.cell_size

            platforms[i].x = randint(0, platform_x) * self.cell_size

            platforms[i].y = (platform_row * self.cell_size
                              + self.Constants.scoreboard_height)

        return platforms
