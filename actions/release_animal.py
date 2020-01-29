# should display a list of animals to release
# TODO: import ofther animals
from animals.animal import Animal
from animals.river_dolphin import RiverDolphin
from animals.gold_dust_day_gecko import Gold_Dust_Day_Gecko
from animals.nene_goose import Nene_Goose
from animals.kikakapu import Kikakapu

# Function of chosing animals to release
def release_animal(arboretum):
    animal_released = None

    # list of animals that are shouwn to users
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-face Spider")


    choice = input("Choose animal to release > ")
    # logic that creates an instance of the class
    if choice == "1":
        animal_released = Gold_Dust_Day_Gecko()

    if choice == "2":
        animal_released = RiverDolphin()

    if choice == "3":
        animal_released = Nene_Goose()

    if choice == "4":
        animal_released = Kikakapu()

    if choice == "5":
        animal_released = Pueo()

    if choice == "6":
        animal_released = Ulae()

    if choice == "7":
        animal_released = Ope_ape_a()

    if choice == "8":
        animal_released = Happy_face_Spider()

    # Iterates & displays through each biome and how many
    # animals are in the biome
    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # adds the animal you choose to the biome
    # arboretum.rivers[int(choice) - 1].animals.append(animal)
    #  TODO: Conditional that limits animals in a biome


