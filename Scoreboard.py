from Board_Game.Constants import Constants


class Scoreboard:
    def __init__(self, level: int = 0, lose: int = 0, alive: int = 0, saved: int = 0, dead: int = 0,
                 stairs: int = 0, umbrellas: int = 0, blockers: int = 0):
        self.constants = Constants()

        self.y = 0
        self.x = 0
        self.level = f"Level: {level}" # Уровень игры
        self.lose = f"Lose: {lose}"  # Проигрышей
        self.alive = f"Alive: {alive}" # Живых леммингов
        self.saved = f"Saved: {saved}" # Спасенных
        self.dead = f"Dead: {dead}" # Мертвых
        self.ladders = f"Stairs: {stairs}" # Лестниц
        self.umbrellas = f"Umbrellas: {umbrellas}" # Зонтов
        self.blockers = f"Blockers: {blockers}" # Блокировщиков
        self.width = self.constants.scoreboard_width
        self.height = self.constants.scoreboard_height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):# Если координаты не соответствуют ограничениям, то ставим 0
        if x < 0 or type(x) != int:
            self.__x = 0
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, y):# Если координаты не соответствуют ограничениям, то ставим 0
        if y < 0 or type(y) != int:
            self.__y = 0
        else:
            self.__y = y

    @y.setter
    def y(self, value):
        self._y = value
