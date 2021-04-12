class FoodPair(object):
    def __init__(self):
        self.occupants = []
    def is_occupied(self):
        if len(self.occupants) == 2:
            return True
        return False