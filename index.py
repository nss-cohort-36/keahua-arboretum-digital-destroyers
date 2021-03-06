# *****************************************************************
# Builds and displays menu that can route you to different files
# *****************************************************************
import os
from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.report import build_facility_report
from actions.cultivate_new_plant import cultivate_new_plant
from actions.feed_animal import feed_animal
 
# It creates a single instance of the class Arboretum
keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

# build_menu() prints menu options that should be seen on terminal
def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Exit")

# Routes user to different modules based on numeric input
def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        cultivate_new_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

main_menu()
