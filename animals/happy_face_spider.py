from animals import Animal
from interfaces.animal.identifiable import Identifiable
from interfaces.animal.terrestrial import ITerrestrial
from interfaces.animal.stagnant import Stagnant


class Happy_Face_Spider(Animal, Identifiable, ITerrestrial, Stagnant):
    def __init__(self):
        Animal.__init__(self, "Happy Face Spider")
        Identifiable.__init__(self)
        ITerrestrial.__init__(self)
        Stagnant.__init__(self)
        self.__prey = { "Insects" }

    #  decorator to add a read only to whats above ^ getter
    @property
    def prey(self):
        return self.__prey

    #  conditional for the animals diet
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The spider ate {prey} for a meal')
        else:
            print(f'The spider rejects the {prey}')

    #  shows a strng of the object chosen
    def __str__(self):
        return f'Spider {self.id}. Ahhhhhh!'