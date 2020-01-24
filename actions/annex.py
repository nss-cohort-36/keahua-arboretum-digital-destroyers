# list of habitats
import os
from environments.river import River
from arboretum import Arboretum

# prints list of habitats
def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    # habitats that are printed
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")

    choice = input("Choose your habitat > ")

    # conditional that adds a habitat to the appropriate arobertum list
    # if choice == "2":
    #     pass
    if choice == "5":
        river = River()
        # print(river)
        arboretum.rivers.append(river)
        print(arboretum.listRivers())
