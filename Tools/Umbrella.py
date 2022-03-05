
class Umbrella:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = (0, 16, 0, 16, 16, 0)
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        else:
            self.__x = x
