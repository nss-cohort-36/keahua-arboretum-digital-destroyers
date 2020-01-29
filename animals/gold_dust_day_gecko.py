from animals import Animal
from interfaces import Identifiable
from interfaces import ITree

class Gold_Dust_Day_Gecko(Animal, Identifiable, ITree):
    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Identifiable.__init__(self)
        ITree.__init__(self)
        self.__prey = { "Dragonfly", "fly", "Stick Bug" }

    @property
    def prey(self):
        return self.__prey
        
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Gold Dust Day Gecko ate {prey} for a meal')
        else:
            print(f'The Gold Dust Day Gecko rejects the {prey}')

    def __str__(self):
        return f'Gold Dust Day Gecko {self.id}. Slurp, Slurp '