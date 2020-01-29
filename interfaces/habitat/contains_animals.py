class IContainsAnimals():

    def __init__(self):
        self.animals = ["test animal", "flouncy the snake"]
        
    def __str__(self):
        return(f"{self.name} ({len(self)} animals)")

    def __len__(self):
        return len(self.animals)
