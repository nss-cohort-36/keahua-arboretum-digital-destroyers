from interfaces.animal.terrestrial import ITerrestrial

class Altitude(ITerrestrial):
    def __init__(self):
        super().__init__()
        self.elevation = "3000ft"