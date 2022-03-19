class Constants:
    def __init__(self):
        self.width = 256
        self.height = 256
        self.grid_rows = 14
        self.grid_columns = 16
        self.cell_size = self.height / self.grid_columns  # 16px

        self.scoreboard_width = self.width
        self.scoreboard_height = self.cell_size * 2

        self.platform_min_size = 5
        self.platform_max_size = 10
        self.platforms_num = 7
