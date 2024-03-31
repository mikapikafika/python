import logging
from Wolf import Wolf
from Sheep import Sheep


class Meadow:
    sheep_quantity = 15

    def __init__(self):
        self.sheep = []
        self.wolf = Wolf()
        for sheep in range(self.sheep_quantity):
            self.sheep.append(Sheep(sheep))
        logging.info("Initial positions of all sheep were determined ")

    def make_a_round(self):
        for sheep in self.sheep:
            if sheep.alive:
                sheep.move()
        logging.info("All sheep moved")
        self.wolf.move(self.sheep)
        print(f"My position: {self.wolf.report_position()}")
        print(f"Sheep left: {self.alive_sheep_amount()}\n")
        logging.info("Round ended - alive sheep: %s", self.alive_sheep_amount())

    def alive_sheep_amount(self):
        counter = 0
        for sheep in self.sheep:
            if sheep.alive:
                counter += 1
        return counter

    def get_sheep_positions(self):
        positions = []
        for sheep in self.sheep:
            positions.append(sheep.report_position())
        return positions
