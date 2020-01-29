from interfaces.animal.aquatic import IAquatic

class ICurrent(IAquatic):

    def __init__(self):
        super().__init__()
        self.current = "hypertonic"
