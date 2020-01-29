from animals import Animal
from interfaces.animal.identifiable import Identifiable
from interfaces.animal.terrestrial import ITerrestrial
from interfaces.animal.tree import ITree
from interfaces.animal.open_field import IOpen_Field


class Pueo(Animal, Identifiable, ITerrestrial, ITree, IOpen_Field):
    def __init__(self):
        Animal.__init__(self, "Pueo")
        Identifiable.__init__(self)
        ITree.__init__(self)
        IOpen_Field.__init__(self)
        self.__prey = { "Rodents" }

    #  decorator to add a read only to whats above ^ getter
    @property
    def prey(self):
        return self.__prey

    #  conditional for the animals diet
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The owl ate {prey} for a meal')
        else:
            print(f'The owl rejects the {prey}')

    #  shows a strng of the object chosen
    def __str__(self):
        return f'Owl {self.id}. They\'re cute!'