"""
The plant class organizes all the functionality that is specific to a single plant
"""

class Plant:
    def __init__(self, name, last_watered, water_per_week):
        self.name = name
        self.last_watered = last_watered
        self.water_per_week = water_per_week

    def print_plant(self):
        # Prints plant data under table header (Name, Last Watered, Watered Per Week)
        print("{:<20} {:<20} {:<20}".format(self.name, self.last_watered, self.water_per_week))
