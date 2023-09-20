import pyxel
from Board_Game import Gameboard


class Draw:
    def __init__(self, platforms, entry_gate, exit_gate):
        # Создаем экземпляр класса Gameboard
        self.gameboard = Gameboard()
        # Получаем константы из экземпляра класса Gameboard
        self.constants = self.gameboard.Constants

        # Определяем цвета
        self.BLACK = 0
        self.DARK_BLUE = 1
        self.BROWN = 4
        self.WHITE = 7
        self.GREEN = 11
        self.BLUE = 12

        # Получаем размеры игрового поля и размер ячейки
        self.width = self.constants.width
        self.height = self.constants.height
        self.cell_size = self.constants.cell_size
        self.grid_columns = self.constants.grid_columns

        # Получаем платформы и вход и выход
        self.platforms = platforms
        self.entry_gate = entry_gate
        self.exit_gate = exit_gate

    def draw_game(self, scoreboard, players, user_x, user_y, tools, start, game_over_msg=None):
        # Очищаем экран
        pyxel.cls(5)

        # Рисуем счетчик
        scoreboard_bg_color = 1
        scoreboard_text_color = 7
        pyxel.rect(scoreboard.x, scoreboard.y,
                   scoreboard.width, scoreboard.height,
                   scoreboard_bg_color)

        # Рисуем первую строку счетчика
        first_row_height = scoreboard.height / 4
        pyxel.text(scoreboard.width / 30, first_row_height,
                   scoreboard.level, scoreboard_text_color)
        pyxel.text(scoreboard.width / 5, first_row_height,
                   scoreboard.lose, scoreboard_text_color)
        pyxel.text(scoreboard.width / 1.5, first_row_height,
                   scoreboard.saved, scoreboard_text_color)
        pyxel.text(scoreboard.width / 2, first_row_height,
                   scoreboard.alive, scoreboard_text_color)
        pyxel.text(scoreboard.width - 40, first_row_height,
                   scoreboard.dead, scoreboard_text_color)

        # Рисуем вторую строку счетчика
        second_row_height = scoreboard.height / 1.5
        pyxel.text(5, second_row_height,
                   scoreboard.ladders, scoreboard_text_color)
        pyxel.text(scoreboard.width / 2 - 40, second_row_height,
                   scoreboard.umbrellas, scoreboard_text_color)
        pyxel.text(scoreboard.width / 2 + 52, second_row_height,
                   scoreboard.blockers, scoreboard_text_color)

        # Рисуем платформы
        for platform in self.platforms:
            for i in range(int(platform.width / 16)):
                pyxel.blt(platform.x + i * 16, platform.y, *platform.img)
                pyxel.rect(platform.x + i * 16, platform.y, 1, 1, 0)

        # Рисуем вход и выход
        pyxel.blt(self.entry_gate.x, self.entry_gate.y -
                  self.entry_gate.entry_img[4], *self.entry_gate.entry_img)
        pyxel.rect(self.entry_gate.x, self.entry_gate.y, 1, 1, 0)

        pyxel.blt(self.exit_gate.x, self.exit_gate.y -
                  self.exit_gate.exit_img[4], *self.exit_gate.exit_img)
        pyxel.rect(self.exit_gate.x, self.exit_gate.y, 1, 1, 0)

        # Рисуем леммингов
        for player in players:
            pyxel.blt(player.x, player.y - player.img[4], *player.img)
            pyxel.rect(player.x, player.y, 1, 1, 0)

        # Рисуем текстовое обозначение инструментов
        tools_height = 242
        tools_color = self.WHITE

        pyxel.text(5, tools_height,
                   "U: Umbrella", tools_color)

        pyxel.text(5, tools_height + 6,
                   "Z: Disable", tools_color)

        pyxel.text(self.width / 4, tools_height,
                   "B: Blocker", tools_color)

        pyxel.text(self.width / 2 - 6, tools_height,
                   "R: Right Stairs", tools_color)

        pyxel.text(self.width - 63, tools_height,
                   "L: Left Stairs", tools_color)

        pyxel.text(self.width / 2 - 40, tools_height + 8,
                   "Q: Quit the game", tools_color)

        # Рисуем курсор пользователя
        pyxel.blt(user_x, user_y, 0, 48, 32, 16, 16, 0)

        # Рисуем зонты
        if len(tools["umbrella"]) > 0:
            for umbrella in tools["umbrella"]:
                pyxel.blt(umbrella[0], umbrella[1], *umbrella[2])

        # Рисуем блокеры
        if len(tools["blocker"]) > 0:
            for i in range(len(tools["blocker"])):
                player_with_i = False
                if tools["blocker"][i][0] != -32:

                    for player in players:
                        if player.blocker_idx == i:
                            player_with_i = True

                if not player_with_i:
                    pyxel.blt(tools["blocker"][i][0],
                              tools["blocker"][i][1], *tools["blocker"][i][2])

        # Рисуем правые лестницы
        if len(tools["right_s"]) > 0:
            for right_s in tools["right_s"]:
                pyxel.blt(right_s[0], right_s[1], *right_s[2])

        # Рисуем левые лестницы
        if len(tools["left_s"]) > 0:
            for left_s in tools["left_s"]:
                pyxel.blt(left_s[0], left_s[1], *left_s[2])

        # Рисуем сообщение о начале игры
        if not start:
            pyxel.rect(scoreboard.x, scoreboard.y,
                       scoreboard.width, scoreboard.height,
                       self.WHITE)
            pyxel.text(90, 15, "Press SPACE to start!", self.BLACK)

        # Рисуем сообщение о конце игры
        if game_over_msg is not None:
            pyxel.rect(0, 0, self.width, self.height, self.WHITE)

            if game_over_msg == "win":
                pyxel.text(110, 120, "CONGRATULATIONS!", self.BLACK)
                pyxel.text(105, 140, "Press O to restart", self.BLACK)
            elif game_over_msg == "lose":
                pyxel.text(93, 140, "Press O to restart", self.BLACK)
                pyxel.text(110, 120, "GAME OVER", self.BLACK)
