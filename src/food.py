from food_pair import FoodPair
class Food(object):
    def __init__(self, number_of_pais):
        self.food  = []
        self.number_of_pais = number_of_pais
    def set_up(self):
        self.food  = []
        for i in range(self.number_of_pais):
            self.food.append(FoodPair())




