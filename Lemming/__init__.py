from .Player import Player

one = 1
y_now = 0


class Lemming:
    def __init__(self, x: int, y: int, platforms: list):  # инициализация
        self.x = x
        self.y = y
        self.width = 256
        self.lemmings_num = 15
        self.blocker_active_idx = []
        self.players = self.create_players()
        self.counter = [0 for i in range(self.lemmings_num)]
        self.platforms = platforms

    def create_players(self):  # созданиe леммингов

        players = []

        for i in range(self.lemmings_num):
            players.append(Player(self.x, self.y))
            players[i].x_i = self.x

        return players

    def before_start(self):  # до начала
        return self.players

    def update_player(self, tools):  #

        umbrellas = tools["umbrella"]
        blockers = tools["blocker"]
        right_stairs = tools["right_s"]
        left_stairs = tools["left_s"]

        players_to_remove = []

        for i in range(len(self.players[:])):
            if (self.players[i].alive and
                    not self.players[i].blocker and
                    not self.players[i].saved):
                is_falling = self.is_falling(self.players[i])
                hit_platform_by_side = self.hit_platform_by_side(self.players[i])
                global one
                global y_now
                if one == 1 and is_falling:
                    one += 1
                    y_now = self.players[i].y
                is_touching_umbrella, umbrella_idx = self.is_touching_tool(self.players[i], umbrellas)
                is_touching_blocker, blocker_idx = self.is_touching_tool(self.players[i], blockers)
                is_touching_right_stair, right_stair_idx = self.is_touching_tool(self.players[i], right_stairs)
                is_touching_left_stair, left_stair_idx = self.is_touching_tool(self.players[i], left_stairs)

                if self.players[i].x > self.width - 12:

                    self.players[i].direction = "left"
                elif self.players[i].x < -4:

                    self.players[i].direction = "right"
                elif hit_platform_by_side and not is_falling:

                    self.change_direction(self.players[i])
                elif is_touching_blocker and not is_falling:

                    if blocker_idx not in self.blocker_active_idx:
                        self.convert_into_blocker(self.players[i], blocker_idx)
                        self.blocker_active_idx.append(blocker_idx)
                    else:
                        self.change_direction(self.players[i])

                if is_touching_right_stair and self.players[i].direction == "right":
                    self.players[i].stairs_r = True
                elif is_touching_left_stair and self.players[i].direction == "left":
                    self.players[i].stairs_l = True

                if not is_falling:
                    if self.players[i].stairs_r:
                        self.stairs(self.players[i], i, "right")
                    elif self.players[i].stairs_l:
                        self.stairs(self.players[i], i, "left")
                    elif self.players[i].direction == "left":
                        self.players[i].x -= self.players[i].speed
                    elif self.players[i].direction == "right":
                        self.players[i].x += self.players[i].speed

                    self.players[i].umbrella = False
                    self.players[i].img = (0, 32, 16, 16, 16, 0)

                if is_falling:
                    self.players[i].y += self.players[i].speed

                    if is_touching_umbrella:
                        self.players[i].umbrella = True
                        self.players[i].img = (0, 0, 48, 16, 24, 0)
                if not is_falling:
                    one = 1

                for platform in self.platforms:
                    if self.players[i].y == platform.y:

                        platform_x_f = platform.x + platform.width

                        player_in_platform = self.players[i].x >= platform.x and (
                                self.players[i].x <= platform_x_f)
                        if is_falling and player_in_platform and not self.players[i].umbrella:
                            if self.players[i].y - y_now > 20:
                                players_to_remove.append(i)

                if self.players[i].y > 255:
                    players_to_remove.append(i)

            elif self.players[i].blocker:
                pass

        if len(players_to_remove) >= 1:
            self.remove_player(players_to_remove)

        return self.players

    def is_falling(self, player):

        for platform in self.platforms:

            if player.y == platform.y:
                platform_x_f = platform.x + platform.width

                player_in_platform = player.x >= platform.x - 12 and (
                        player.x <= platform_x_f)

                if player_in_platform:
                    return False

        if player.stairs_r or player.stairs_l:
            return False
        else:
            return True

    def hit_platform_by_side(self, player):
        is_hitting_platform = False

        for platform in self.platforms:
            x_equal = player.x == platform.x or (player.x == platform.x + platform.width - 16)
            y_equal = player.y - 16 == platform.y

            if x_equal and y_equal:
                is_hitting_platform = True

        return is_hitting_platform

    @staticmethod
    def is_touching_tool(player, tool):

        is_touching = False
        tool_index = 0

        for i in range(len(tool)):
            x_near_tool = tool[i][0] - 2 < player.x < tool[i][0] + 4
            if x_near_tool and player.y - 16 == tool[i][1]:
                is_touching = True
                tool_index = i

        return is_touching, tool_index

    @staticmethod
    def change_direction(player):
        if player.direction == "right":
            player.direction = "left"
        elif player.direction == "left":
            player.direction = "right"

    @staticmethod
    def convert_into_blocker(player, blocker_idx):
        player.blocker = True
        player.blocker_idx = blocker_idx
        if player.direction == "right":
            player.img = (0, 32, 56, -16, 16, 0)
        else:
            player.img = (0, 32, 56, 16, 16, 0)

    def stairs(self, player, player_idx, stairs_direction):
        if self.counter[player_idx] < 17:
            player.y -= 1
            if stairs_direction == "right":
                player.x += 1
            elif stairs_direction == "left":
                player.x -= 1

            self.counter[player_idx] += 1
        else:
            self.counter[player_idx] = 0
            player.stairs_r = False
            player.stairs_l = False

    def remove_player(self, players: list):

        for i in players:
            self.players[i].alive = False
            self.players[i].img = (0, 32, 40, 16, 12, 0)
