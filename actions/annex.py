# list of habitats
import os
from environments import River

# prints list of habitats
def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    # habitats that are printed
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")

    choice = input("Choose your habitat > ")

    # conditional that adds a habitat to the appropriate arobertum list
    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        pass
