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
        self.coastlines = []
        self.biomes = [self.rivers, self.grasslands, self.mountains, self.forests, self.swamps, self.coastlines]

    def __str__(self): 
        return(f"{self.name}")

    def listBiomes(self):
        for biome in self.biomes:
            for instance in biome:
                print(f"{instance} {str(instance.id)[:6]} {instance.plants} {instance.animals}")

    def listRivers(self):
        for river in self.rivers:
            print(f"{river}")

    def listGrasslands(self):
        for grassland in self.grasslands:
            print(f"{grassland}")

    def listSwamps(self):
        for swamp in self.swamps:
            print(f"{swamp}")

    def listMountains(self):
        for mountain in self.mountains:
            print(f"{mountain}")

    def listCoastlines(self):
        for coastline in self.coastlines:
            print(f"{coastline}")

    def listForests(self):
        for forest in self.forests:
            print(f"{forest}")