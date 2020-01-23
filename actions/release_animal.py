# should display a list of animals to release
from animals import RiverDolphin
# TODO: import ofther animals

# Function of chosing animals to release
def release_animal(arboretum):
    animal = None

    # list of animals that are shouwn to users
    print("1. River Dolphin")
    print("2. Dragonfly")
    # TODO: insert remianing 6 animals

    choice = input("Choose animal to release > ")
    # logic that creates an instance of the class
    if choice == "1":
        animal = RiverDolphin()
    
    if choice == "2":
        pass
    #  TODO: finish list of animals

    # Iterates & displays through each biome and how many 
    # animals are in the biome
    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')

    print("Release the animal into which biome?")
    choice = input("> ")

    # adds the animal you choose to the biome
    arboretum.rivers[int(choice) - 1].animals.append(animal)
    #  TODO: Conditional that limits animals in a biome


