# list of habitats
import os
from environments.river import River
from environments.grassland import Grassland
from environments.swamp import Swamp
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
    print("7. Return to Main Menu")

    choice = input("Choose your habitat > ")

    # conditional that adds a habitat to the appropriate arobertum list
    if choice == "2":
        swamp = Swamp("Muddy")
        arboretum.swamps.append(swamp)
        arboretum.listSwamps()
        annex_habitat(arboretum)
    
    if choice == "3":
        grassland = Grassland("Green")
        arboretum.grasslands.append(grassland)
        arboretum.listGrasslands()
        annex_habitat(arboretum)
    
    if choice == "5":
        river1 = River("Jimmy Dean")
        # print(river)
        arboretum.rivers.append(river1)
        arboretum.listRivers()
        annex_habitat(arboretum)

    if choice == "7":
        import index
        index.main_menu()
