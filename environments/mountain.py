

# from interfaces import IAquatic
from interfaces.animal.identifiable import Identifiable
from interfaces.habitat.contains_animals import IContainsAnimals
from interfaces.habitat.contains_plants import IContainsPlants
from interfaces.animal.altitudes import Altitude

# Defining the class river and inheriting three interfaces: IContainsAnimals, IContainsPlants, and Identifiable
class Mountain(IContainsAnimals, IContainsPlants, Identifiable):

# defines the initial properties of River class
    def __init__(self, name):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.name = name

    def __str__(self):
        return(f"{self.name}")

# A setter that (add and fix setter decorator syntax)
# TODO: this needs a getter)
    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add aquatic, or saltwater animals to a swamp")

    def add_plant(self, plant):
        try:
            if Altitude:
                self.plants.append(plant)
                print("plant has been added")
        except AttributeError:
            raise AttributeError("Cannot add plants that require high altitude")
