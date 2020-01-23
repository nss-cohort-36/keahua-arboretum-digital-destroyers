#builds reports for status of each biome and what it contains
# TODO:build out fo the rest of the existing biomes and listing out all animals and plants in each biome 
def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River [{river.id}]')

    input("\n\nPress any key to continue...")