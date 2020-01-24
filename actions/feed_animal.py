from animals.river_dolphin import RiverDolphin

# Function of chosing animals to release
def feed_animal(arboretum):
    animal = None

    # list of animals that are shouwn to users
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-face Spider")
    # TODO: insert remianing 6 animals

    choice = input("Choose animal to feed > ")
    # logic that creates an instance of the class
    if choice == "2":
        animal = RiverDolphin()