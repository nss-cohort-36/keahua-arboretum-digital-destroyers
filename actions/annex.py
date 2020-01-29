# list of habitats
import os
from environments.river import River
from environments.grassland import Grassland
from environments.swamp import Swamp
from environments.mountain import Mountain
from environments.coastline import Coastline
from environments.forest import Forest
from arboretum import Arboretum

# prints list of habitats
def annex_habitat(arboretum):
    # os.system('cls' if os.name == 'nt' else 'clear')
    # habitats that are printed
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")
    # print("7. Return to Main Menu")

    choice = input("Choose your habitat > ")

    # conditional that adds a habitat to the appropriate arobertum list
    if choice == "1":
        mountain = Mountain("Very High Up")
        arboretum.mountains.append(mountain)
        arboretum.listMountains()
        annex_habitat(arboretum)

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
  
    if choice == "4":
        forest = Forest("Trees")
        arboretum.forests.append(forest)
        arboretum.listForests()
        annex_habitat(arboretum)
        
    if choice == "5":
        river = River("Water current")
        arboretum.rivers.append(river)
        arboretum.listRivers()
        annex_habitat(arboretum)

    if choice == "6":
        coastline = Coastline("Coastline")
        arboretum.coastlines.append(coastline)
        arboretum.listCoastlines()
        annex_habitat(arboretum)

    # if choice == "7":
    #     import index
    #     index.main_menu()
