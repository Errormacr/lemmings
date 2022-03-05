from Gameboard.Constants import Constants
class Scoreboard:
    def __init__(self, level: int = 0, alive: int = 0, saved: int = 0, dead: int = 0,
                stairs: int = 0, umbrellas: int = 0, blockers: int = 0):
        self.constants = Constants()
        
        self.x = 0
        self.y = 0
        self.width = self.constants.scoreboard_width
        self.height = self.constants.scoreboard_height
        self.level = f"Level: {level}"
        self.alive = f"Alive: {alive}"
        self.saved = f"Saved: {saved}"
        self.dead = f"Dead: {dead}"
        self.ladders = f"Stairs: {stairs}"
        self.umbrellas = f"Umbrellas: {umbrellas}"
        self.blockers = f"Blockers: {blockers}"


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
