# Импортируем классы Blocker, Stairs, Umbrella
from .Blocker import Blocker
from .Stairs import Stairs
from .Umbrella import Umbrella

# Создаем класс Tools
class Tools:
    # Инициализируем класс с координатами x и y и инструментом tool
    def __init__(self, x: int, y: int, tool: "str"):
        self.x = x
        self.y = y
        self.tool = tool

    # Создаем getter и setter для инструмента tool
    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool):
        # Если инструмент - зонт, вызываем метод umbrella()
        if tool == "umbrella":
            self.umbrella()
        # Если инструмент - блокиратор, вызываем метод blocker()
        elif tool == "blocker":
            self.blocker()
        # Если инструмент - правая лестница, вызываем метод right_stair()
        elif tool == "right_stair":
            self.right_stair()
        # Если инструмент - левая лестница, вызываем метод left_stair()
        elif tool == "left_stair":
            self.left_stair()

    # Метод для создания зонта
    def umbrella(self):
        umbrella = Umbrella(self.x, self.y)
        return umbrella.x, umbrella.y, umbrella.img

    # Метод для создания блокиратора
    def blocker(self):
        blocker = Blocker(self.x, self.y)
        return blocker.x, blocker.y, blocker.img

    # Метод для создания правой лестницы
    def right_stair(self):
        right_s = Stairs(self.x, self.y, "right")
        return right_s.x, right_s.y, right_s.img, right_s.right

    # Метод для создания левой лестницы
    def left_stair(self):
        left_s = Stairs(self.x, self.y, "left")
        return left_s.x, left_s.y, left_s.img, left_s.right
