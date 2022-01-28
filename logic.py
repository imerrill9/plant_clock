import filewriter
from plant import Plant

"""
The logic file contains all the functions that drive the functionality of the app.
It will use the imported filewriter to save plant data and fetch plant data from the json file.
"""


def print_plant_header():
    print("{:<20} {:<20} {:<20}".format("Name", "Last Watered", "Water per Week") + "\n")


def print_all_plants():
    plants = filewriter.get_plants()
    for plant in plants:
        plant.print_plant()


def save_new_plant(plant):
    print("save new plant to json")
    filewriter.save_plant(plant)


def update_plant():
    print("update plant with new info")


def delete_plant():
    print("delete plant from json")
