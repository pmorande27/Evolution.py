import random
from individual import Individual
from population import Population
from food import Food
class Simulation(object):
    def __init__(self, number_of_individuals, number_of_pais):
        self.population = Population(number_of_individuals)
        self.food = Food(number_of_pais)
    def assing_food(self):
        unoccupied_pairs = self.food.food[:]
        for individual in self.population.individuals:
            if not unoccupied_pairs:
                return
            food_pair = random.choice(unoccupied_pairs)
            while food_pair.is_occupied():
                 unoccupied_pairs.remove(food_pair)
                 if not unoccupied_pairs:
                    return
                 food_pair = random.choice(unoccupied_pairs)
            food_pair.occupants.append(individual)
           
    def feed(self):
        for pair in self.food.food:
            if len(pair.occupants) == 1:
                individual = pair.occupants[0]
                individual.behaviour_alone()
            elif len(pair.occupants) == 2:
                individual_one = pair.occupants[0]
                individual_two = pair.occupants[1]
                Individual.behaviour(individual_one,individual_two)


        
    def run(self, number_of_generations):
        print(len(self.population.individuals))
        for i in range(number_of_generations):
            self.food.set_up()
            self.assing_food()
            self.feed()
            self.population.next_generation()
            print(len(self.population.individuals))
def main():
    sim = Simulation(10,28000)
    sim.run(20)

main()
