class IContainsPlants():

    def __init__(self):
        self.plants = ["weeping willow", "orchid"]

    def __str__(self):
        return(f"{self.name} ({len(self)} plants)")

    def __len__(self):
        return len(self.plants)