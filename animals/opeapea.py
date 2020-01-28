from animals import Animal
from interfaces.animal.identifiable import Identifiable
from interfaces.animal.terrestrial import ITerrestrial
from interfaces.animal.altitudes import Altitude
from interfaces.animal.tree import ITree


class Opeapea(Animal, Identifiable, ITerrestrial, Altitude, ITree):
    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        Identifiable.__init__(self)
        Altitude.__init__(self)
        ITree.__init__(self)
        self.__prey = { "Insects", "Vegeation" }

    #  decorator to add a read only to whats above ^ getter
    @property
    def prey(self):
        return self.__prey

    #  conditional for the animals diet
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The bat ate {prey} for a meal')
        else:
            print(f'The bat rejects the {prey}')

    #  shows a strng of the object chosen
    def __str__(self):
        return f'Bat {self.id}. It\'s in your hair!'