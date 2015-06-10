import random

class Player:



    def __init__(self):
        self.set_rolls = 1
        self.points = 0
        self.data_list = []


    @property
    def roll(self):
        return random.randint(1,6)

    def turn(self):
        possible_points = 0
        throws = 0
        while throws < self.set_rolls:
            temp_roll = self.roll
            if temp_roll == 1:
                possible_points = possible_points - possible_points
                break
            elif temp_roll > 1:
                possible_points = possible_points + temp_roll
                throws = throws + 1

        self.points = self.points + possible_points

    @property
    def turn_data(self):
        return self.points


    def run(self):
        for _ in range(7):
            self.turn()
            self.data_list.append(self.turn_data)
        return sum(self.data_list[-1:])




