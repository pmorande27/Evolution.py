class Individual(object):
    def __init__(self):
        self.food = 0
    def behaviour_alone(self):
        self.food = 2
    @staticmethod
    def behaviour(individual_one,individual_two):
        individual_one.food = 1
        individual_two.food = 1
    def reproduction(self):
        if self.food == 2:
            return True
        return False
    def death(self):
        if self.food == 0:
            return True
        return False