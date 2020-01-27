# defines the Arboretum class object 
class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rivers = []
        self.grasslands = []
        self.mountains = []
        self.forests = []
        self.swamps = []

    def listRivers(self):
        for river in self.rivers:
            print(f"{river}")

    def listForests(self):
        for forest in self.forests:
            print(f"{forest}")

    def listMountains(self):
        for mountain in self.mountains:
            print(f"{mountain}")
