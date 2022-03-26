from .Blocker import Blocker
from .Stairs import Stairs
from .Umbrella import Umbrella


class Tools:
    def __init__(self, x: int, y: int, tool: "str"):
        self.x = x
        self.y = y
        self.tool = tool

    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool):
        if tool == "umbrella":
            self.umbrella()
        elif tool == "blocker":
            self.blocker()
        elif tool == "right_stair":
            self.right_stair()
        elif tool == "left_stair":
            self.left_stair()

    def umbrella(self):

        umbrella = Umbrella(self.x, self.y)
        return umbrella.x, umbrella.y, umbrella.img

    def blocker(self):

        blocker = Blocker(self.x, self.y)
        return blocker.x, blocker.y, blocker.img

    def right_stair(self):

        right_s = Stairs(self.x, self.y, "right")
        return right_s.x, right_s.y, right_s.img, right_s.right

    def left_stair(self):

        left_s = Stairs(self.x, self.y, "left")
        return left_s.x, left_s.y, left_s.img, left_s.right
