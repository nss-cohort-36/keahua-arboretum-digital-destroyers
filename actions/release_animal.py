# should display a list of animals to release
# TODO: import ofther animals
from animals.animal import Animal
from animals.river_dolphin import RiverDolphin
from animals.gold_dust_day_gecko import Gold_Dust_Day_Gecko
from animals.nene_goose import Nene_Goose
from animals.kikakapu import Kikakapu
from animals.pueo import Pueo
from animals.ulae import Ulae
from animals.opeapea import Opeapea
from animals.happy_face_spider import Happy_Face_Spider
from environments.forest import Forest

# Function of chosing animals to release
def release_animal(arboretum):
    # animal_released = None

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
        forest = Forest("f")
        Gecko= Gold_Dust_Day_Gecko()
        forest.add_animal(Gecko)
        forest.listAnimal()

    if choice == "2":
        pass
        # animal_released = RiverDolphin()

    if choice == "3":
        pass
        # animal_released = Nene_Goose()

    if choice == "4":
        pass
        # animal_released = Kikakapu()
        release_animal(arboretum)

    if choice == "5":
        pass
        # animal_released = Pueo()

    if choice == "6":
        pass
        # animal_released = Ulae()

    if choice == "7":
        pass
        # animal_released = Opeapea()

    if choice == "8":
        pass
        # animal_released = Happy_Face_Spider()

    # Iterates & displays through each biome and how many
    # animals are in the biome
    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # adds the animal you choose to the biome
    # arboretum.rivers[int(choice) - 1].animals.append(animal)
    #  TODO: Conditional that limits animals in a biome