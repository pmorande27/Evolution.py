from individual import Individual
class Population:
    def __init__(self,number_of_individuals):
        self.individuals = []
        for i in range(number_of_individuals):
            self.individuals.append(Individual())
    def next_generation(self):
        for individual in self.individuals:
            if individual.death():
                self.individuals.remove(individual)
        new_generation = self.individuals[:]
        for individual in self.individuals:
            if individual.reproduction():
                self.individuals.append(Individual())
    def get_number_of_individuals(self):
        return(len(self.individuals))
