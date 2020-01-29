from animals import Animal
from interfaces import Identifiable
from interfaces.animal.open_field import IOpen_Field

class Nene_Goose(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IOpen_Field.__init__(self)
        Identifiable.__init__(self)
        self.__diet = { "vegetation" }

    @property
    def diet(self):
        return self.__diet
        
    def feed(self, diet):
        if diet in self.__diet:
            print(f'The Nene Goose ate {diet} for a meal')
        else:
            print(f'The Nene Goose rejects the {diet}')

    def __str__(self):
        return f'Nene Goose {self.id}. Honk, Honk'