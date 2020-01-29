

# from interfaces import IAquatic
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants

# Defining the class river and inheriting three interfaces: IContainsAnimals, IContainsPlants, and Identifiable
class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

# defines the initial properties of River class
    def __init__(self, name):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.name = name

# A setter that (add and fix setter decorator syntax)
# TODO: this needs a getter)
    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add aquatic, or saltwater animals to a grasslands")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
