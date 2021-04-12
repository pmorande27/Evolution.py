from population import Population
from food import Food
import random
class Simulation(object):
    def __init__(self, number_of_individuals, number_of_pais):
        self.population = Population(number_of_individuals)
        self.food = Food(number_of_pais)
    def assing_food(self):
        unoccupied_pairs = self.food[:]
        for individual in self.population:
            food_pair = random.choice(unoccupied_pairs)
            food_pair.occupants.append(individual)
            if food_pair.is_occupied():
                unoccupied_pairs.remove(food_pair)


