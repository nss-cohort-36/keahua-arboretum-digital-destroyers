# Animal information

# TODO: Fix path
from animals import Animal
from interfaces.animal import IFreshwater
from interfaces import Identifiable

class RiverDolphin(Animal, IFreshwater, Identifiable):

    # Your defining the class river dolphin has 3 parent classes using 
    # parents class .init instead of super.init when inheriting from 
    # multiple classes. you must pass self as a parameter when initializing
    # parents classes
    def __init__(self):
        Animal.__init__(self, "River dolphin")
        IFreshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    #  decorator to add a read only to whats above ^ getter
    @property
    def prey(self):
        return self.__prey

    #  conditional for the animals diet
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')

    #  shows a strng of the object chosen
    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
