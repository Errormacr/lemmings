from Board_Game.Constants import Constants


class Scoreboard:
    def __init__(self, level: int = 0, lose: int = 0, alive: int = 0, saved: int = 0, dead: int = 0,
                 stairs: int = 0, umbrellas: int = 0, blockers: int = 0):
        self.constants = Constants()

        self.y = 0
        self.x = 0
        self.level = f"Level: {level}"
        self.lose = f"Lose: {lose}"
        self.alive = f"Alive: {alive}"
        self.saved = f"Saved: {saved}"
        self.dead = f"Dead: {dead}"
        self.ladders = f"Stairs: {stairs}"
        self.umbrellas = f"Umbrellas: {umbrellas}"
        self.blockers = f"Blockers: {blockers}"
        self.width = self.constants.scoreboard_width
        self.height = self.constants.scoreboard_height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0 or type(x) != int:
            self.__x = 0
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, y):
        if y < 0 or type(y) != int:
            self.__y = 0
        else:
            self.__y = y

    @y.setter
    def y(self, value):
        self._y = value
