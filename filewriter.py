import json
from os.path import exists
from plant import Plant

"""
The filewriter uses the json python package to write data and read data from plants.json.
"""


def save_plant(plant):
    if exists("plants.json"):
        with open("plants.json") as json_file:
            plant_data = dict(json.load(json_file))
            plant_data["plants"].append(
                {
                    "name": plant.name,
                    "last_watered": plant.last_watered,
                    "water_per_week": plant.water_per_week,
                }
            )
            __save_plants(plant_data)
    else:
        plant_data = {
            "plants": [
                {
                    "name": plant.name,
                    "last_watered": plant.last_watered,
                    "water_per_week": plant.water_per_week,
                }
            ]
        }
        __save_plants(plant_data)


def update_plant(plant):
    print("update a plant's info")


def delete_plant(plant):
    print("remove a plant from data")


def get_plants():
    if exists("plants.json"):
        with open("plants.json") as json_file:
            plant_data = dict(json.load(json_file))
            return list(map(lambda p: Plant(p["name"], p["last_watered"], p["water_per_week"]), plant_data["plants"]))
    else:
        print("No plants.json was found!")


def __save_plants(plant_data):
    json_string = json.dumps(plant_data, indent=4)
    with open("plants.json", "w") as outfile:
        outfile.write(json_string)
