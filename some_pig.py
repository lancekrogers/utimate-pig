import random

class Player:

    def __init__(self):
        self.set_rolls = 32
        self.points = 0

    @property
    def roll(self):
        return random.randint(1,6)

    def turn(self):
        possible_points = 0
        throws = 0
        while throws < self.set_rolls:
            if self.roll == 1:
                possible_points = possible_points - possible_points
                break
            elif self.roll > 1:
                possible_points = possible_points + self.roll
            self.points = self.points + possible_points
        return self.points




player = Player()
player.turn()


class Game:

    def __init__(self):
        pass

    def roll(self):
        return random.randint(1,6)

    def turn(self):
        pass

    def hold(self):
        pass






