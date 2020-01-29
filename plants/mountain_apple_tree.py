# Plant information

# TODO: Fix path
from plants.plant import Plant
from interfaces.animal.identifiable import Identifiable
from interfaces.animal.altitudes import Altitude

class Mountain_Apple_Tree(Plant, Identifiable):
# Took out IFreshwater from initialization
    # Your defining the class river dolphin has 3 parent classes using 
    # parents class .init instead of super.init when inheriting from 
    # multiple classes. you must pass self as a parameter when initializing
    # parents classes
    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree")
        Altitude.__init__(self)
        Identifiable.__init__(self)
        self.__sunlight = {"Partial"}
        self.__insecticideResistance = {"High"}

    #  decorator to add a read only to whats above ^ getter
    @property
    def sunlight(self):
        return self.__sunlight

    #  conditional for the plant diet
    def feed(self, sunlight):
        if sunlight in self.__sunlight:
            print(f'The Mountain Apple Tree ate {sunlight} for a meal')
        else:
            print(f'The Mountain Apple Tree rejects the {sunlight} sunlight')
    

    @property
    def insecticideResistance(self):
        return self.__insecticideResistance
        
    def repelant(self, repelant):
        if insecticideResistance in self.__insecticideResistance:
            print(f'The Mountain Apple Tree ate {insecticideResistance} for repelant')
        else:
            print(f'The Mountain Apple Tree rejects the {insecticideResistance} repelant')

    #  shows a strng of the object chosen
    def __str__(self):
        return f'Mountain Apple Tree {self.id}.!'