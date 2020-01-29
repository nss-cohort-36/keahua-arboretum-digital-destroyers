from .aquatic import IAquatic

class ISalt_fresh(IAquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "euryhaline"
        