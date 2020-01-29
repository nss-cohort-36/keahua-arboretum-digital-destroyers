from animals import Animal
from interfaces import Identifiable
from interfaces.animal.freshwater import IFreshwater
from interfaces.animal.stagnant import IStagnant

class Kikakapu(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Kikakapu")
        IFreshwater.__init__(self)
        IStagnant.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "coral polyps", "sea anemones" }

    @property
    def prey(self):
        return self.__prey
        
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Kikakapu ate {prey} for a meal')
        else:
            print(f'The Kikakapu rejects the {prey}')

    def __str__(self):
        return f'Kikakapu {self.id}. Bloop, Bloop '