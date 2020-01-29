import os
from arboretum import Arboretum
from environments.river import River
#builds reports for status of each biome and what it contains
# TODO:build out fo the rest of the existing biomes and listing out all animals and plants in each biome 
def build_facility_report(arboretum):
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print("cereal")
    # print(arboretum)
    print(arboretum)
    arboretum.listRivers()
    # for river in arbor.rivers:
    #     print(f'River [{river.id}]')
        # print(f'River [{river.plants}]')
        # print(f'River {river.name}')
        # print(f'River {river}')

    input("\n\nPress any key to continue...")
    # import index
    # index.main_menu()