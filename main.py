import pyxel
import pygame
from time import time
from Lemming import Lemming
from Gameboard import Gameboard
from Draw import Draw
from Tools import Tools
from Scoreboard import Scoreboard

# переменная проверки проигрыша или победы для звуки
audnorepeat, a = 1, 0
pasha = ""
pygame.mixer.init()
pygame.mixer.Sound('fon.wav').play(0)


class App:
    pygame.init()

    def __init__(self):  # инициализация объектов, интерфейса, курсора игрока
        self.initial_time = time()
        self.level = 0
        self.lose = 0
        self.start = False
        self.game_over = [False, ""]

        # объявление констант
        self.Gameboard = Gameboard()
        self.constants = self.Gameboard.Constants
        self.width = self.constants.width
        self.height = self.constants.height
        self.cell_size = self.constants.cell_size
        self.grid = self.Gameboard.grid

        self.scoreboard = Scoreboard()

        # объявление ворот входа выхода
        self.platforms = self.Gameboard.platforms
        self.entry_gate = self.Gameboard.generate_gate(self.platforms)
        self.exit_gate = self.Gameboard.generate_gate(self.platforms,
                                                      self.entry_gate.row_index, exit_gate=True)

        # курсор игрока и инструменты
        self.user_x = 0
        self.user_y = self.scoreboard.height
        self.cursor_displacement = self.cell_size
        self.tools = {
            "umbrella": [],
            "blocker": [],
            "right_s": [],
            "left_s": []
        }

        # лемминги
        self.alive = []
        self.saved = []
        self.dead = []
        self.Lemming = Lemming(self.entry_gate.x, self.entry_gate.y, self.platforms)
        self.lemmings_num = self.Lemming.lemmings_num

        self.Draw = Draw(self.platforms, self.entry_gate,
                         self.exit_gate)

        # загаловок
        self.pyxel_window_title = "Lemmings"
        pyxel.init(self.width, self.height)

        pyxel.load("./assets/resources.pyxres")  # изображения всего

        pyxel.run(self.interaction, self.update)

    def interaction(self):
        # управление кнопками
        global audnorepeat, pasha, a
        print(pasha)
        if pasha not in "UUDDLRLRBA":
            pasha = ""
        if pasha == "UUDDLRLRBA" and a == 0:
            a += 1
            pygame.mixer.pause()
            pygame.mixer.Sound('pasha.wav').play(1)
        if pyxel.btnp(pyxel.KEY_SPACE):
            # начало игры

            self.start = True
        elif pyxel.btnp(pyxel.KEY_A):
            pasha += "A"
        elif pyxel.btnp(pyxel.KEY_O):
            self.start = False
            audnorepeat = 1
            pygame.mixer.pause()
            pygame.mixer.Sound('fon.wav').play(0)
            self.game_over[0] = False
            self.game_over[1] = ""
            # объявление ворот входа выхода
            self.platforms = self.Gameboard.platforms
            self.entry_gate = self.Gameboard.generate_gate(self.platforms)
            self.exit_gate = self.Gameboard.generate_gate(self.platforms,
                                                          self.entry_gate.row_index, exit_gate=True)

            # лемминги
            self.user_x = 0
            self.user_y = self.scoreboard.height
            self.cursor_displacement = self.cell_size
            self.tools = {
                "umbrella": [],
                "blocker": [],
                "right_s": [],
                "left_s": []
            }
            self.alive = []
            self.saved = []
            self.dead = []
            self.Lemming = Lemming(self.entry_gate.x, self.entry_gate.y, self.platforms)
            self.lemmings_num = self.Lemming.lemmings_num

            self.Draw = Draw(self.platforms, self.entry_gate,
                             self.exit_gate)

            # загаловок

        elif pyxel.btnp(pyxel.KEY_Z):
            # удаление интсрумента
            self.disable_tool(self.user_x, self.user_y)
        elif pyxel.btnp(pyxel.KEY_LEFT) and self.user_x > 0:
            # передвижение влево
            pasha += "L"
            self.user_x -= self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_RIGHT) and self.user_x < self.width - 16:
            # передвижение вправо
            pasha += "R"
            self.user_x += self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_UP) and self.user_y > 32:
            # передвижение вверх
            pasha += "U"
            self.user_y -= self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.user_y < self.height - 16:
            # передвиние вниз
            pasha += "D"
            self.user_y += self.cursor_displacement

        elif pyxel.btnp(pyxel.KEY_U):
            # создание зонтика
            tools = Tools(self.user_x, self.user_y, "umbrella")
            umbrella_x, umbrella_y, umbrella_img = tools.umbrella()

            idx, is_tool = self.same_tool_there(umbrella_x, umbrella_y, self.tools["umbrella"])

            if not self.tool_in_tools(umbrella_x, umbrella_y):
                self.tools["umbrella"].append([umbrella_x, umbrella_y, umbrella_img])

        elif pyxel.btnp(pyxel.KEY_B):
            # создадние блокировщика
            tools = Tools(self.user_x, self.user_y, "blocker")
            blocker_x, blocker_y, blocker_img = tools.blocker()
            pasha += "B"

            idx, is_tool = self.same_tool_there(blocker_x, blocker_y, self.tools["blocker"])
            if not self.tool_in_tools(blocker_x, blocker_y):
                self.tools["blocker"].append([blocker_x, blocker_y, blocker_img])
        elif pyxel.btnp(pyxel.KEY_R):
            # создание правой лестницы
            tools = Tools(self.user_x, self.user_y, "right_stair")
            right_s_x, right_s_y, right_s_right, right_s_img = tools.right_stair()

            if not self.tool_in_tools(right_s_x, right_s_y):
                self.tools["right_s"].append([right_s_x, right_s_y, right_s_right, right_s_img])
        elif pyxel.btnp(pyxel.KEY_L):
            # создание левой лестницы
            tools = Tools(self.user_x, self.user_y, "left_stair")
            left_s_x, left_s_y, left_s_left, left_s_img = tools.left_stair()

            if not self.tool_in_tools(left_s_x, left_s_y):
                self.tools["left_s"].append([left_s_x, left_s_y, left_s_left, left_s_img])
        elif pyxel.btnp(pyxel.KEY_Q):
            # кнопка выхода
            pyxel.quit()

    def disable_tool(self, tool_x, tool_y):
        # функция удаления инстркмента
        for umbrella in self.tools["umbrella"]:
            # если зонтик
            if umbrella[0] == tool_x and umbrella[1] == tool_y:
                self.tools["umbrella"].remove([tool_x, tool_y, (0, 16, 0, 16, 16, 0)])
        for blocker in self.tools["blocker"]:
            # если блокировщик
            if blocker[0] == tool_x and blocker[1] == tool_y:
                self.tools["blocker"].remove([tool_x, tool_y, (0, 0, 16, 16, 16, 0)])
        for right_s in self.tools["right_s"]:

            # если правая лестница
            if right_s[0] == tool_x and right_s[1] == tool_y:
                self.tools["right_s"].remove([tool_x, tool_y, (0, 0, 0, 16, 16, 0),
                                              {'bottom_left': [tool_x, tool_y + 16],
                                               'top_right': [tool_x + 16, tool_y]}])
        for left_s in self.tools["left_s"]:
            # если левая лестница
            if left_s[0] == tool_x and left_s[1] == tool_y:
                self.tools["left_s"].remove([tool_x, tool_y, (0, 0, 0, -16, 16, 0),
                                             {'bottom_left': [tool_x, tool_y], 'top_right': [tool_x, tool_y]}])

    def tool_in_tools(self, tool_x, tool_y):
        # проверка на нахождение инструмента в клетке
        for umbrella in self.tools["umbrella"]:
            # зонт
            if umbrella[0] == tool_x and umbrella[1] == tool_y:
                return True
        for blocker in self.tools["blocker"]:
            # блокировщик
            if blocker[0] == tool_x and blocker[1] == tool_y:
                return True
        for right_s in self.tools["right_s"]:
            # правая лестница
            if right_s[0] == tool_x and right_s[1] == tool_y:
                return True
        for left_s in self.tools["left_s"]:
            # левая лестница
            if left_s[0] == tool_x and left_s[1] == tool_y:
                return True
        return False

    @staticmethod
    def same_tool_there(tool_x, tool_y, tool_list):
        # проверка на нахождение того же инструмента, который ставишь
        is_tool = False
        idx = 0
        for i in range(len(tool_list)):
            if tool_x == tool_list[i][0] and tool_y == tool_list[i][1]:
                is_tool = True
                idx = i

        return idx, is_tool

    def update(self):

        if self.start and not self.game_over[0]:  # если игра начата

            lemmings = self.Lemming.update_player(self.tools)
            for i in range(len(lemmings)):  # проверка состояния леммингов, перераспределение при необходимости
                if (lemmings[i].x == self.exit_gate.x and
                        lemmings[i].y == self.exit_gate.y and
                        i not in self.saved):

                    self.saved.append(i)
                    if i in self.alive:
                        self.alive.remove(i)
                elif lemmings[i].alive and i not in self.alive:

                    self.alive.append(i)
                elif not lemmings[i].alive and i not in self.dead:

                    self.dead.append(i)
                    if i in self.alive:
                        self.alive.remove(i)
        global audnorepeat
        if len(self.saved) >= self.lemmings_num * 0.65:  # победа
            self.game_over[0] = True
            self.game_over[1] = "win"
            if audnorepeat == 1:
                pygame.mixer.pause()
                audnorepeat += 1
                self.level += 1
                pygame.mixer.Sound('win.wav').play(0)

        elif len(self.dead) >= self.lemmings_num * 0.35:  # проигрыш
            self.game_over[0] = True
            self.game_over[1] = "lose"
            if audnorepeat == 1:
                audnorepeat += 1
                self.lose += 1
                pygame.mixer.pause()
                pygame.mixer.Sound('lose.wav').play(0)

        # обновление интерфейса
        total_alive = len(self.alive)
        total_saved = len(self.saved)
        total_dead = len(self.dead)
        total_stairs = len(self.tools["right_s"]) + len(self.tools["left_s"])
        total_umbrellas = len(self.tools["umbrella"])
        total_blockers = len(self.tools["blocker"])
        self.scoreboard = Scoreboard(self.level, self.lose, total_alive, total_saved, total_dead,
                                     total_stairs, total_umbrellas, total_blockers)

        if self.start and self.game_over[0]:  # игра не начата
            self.Draw.draw_game(self.scoreboard, self.Lemming.before_start(),
                                self.user_x, self.user_y, self.tools, self.start, self.game_over[1])
        elif self.start:  # игра начата
            self.Draw.draw_game(self.scoreboard, lemmings,
                                self.user_x, self.user_y, self.tools, self.start)
        else:
            self.Draw.draw_game(self.scoreboard, self.Lemming.before_start(),
                                self.user_x, self.user_y, self.tools, self.start)


App()
