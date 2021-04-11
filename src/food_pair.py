class FoodPair(object):
    def __init__(self):
        self.number_of_occupants = 0
    def is_occupied(self):
        if self.number_of_occupants < 2:
            return True
        return False