import logging

from Wolf import Wolf
from Sheep import Sheep


class Meadow:
    sheepQuantity = 15

    def __init__(self):
        self.sheep = []
        self.wolf = Wolf()
        for sheep in range(self.sheepQuantity):
            self.sheep.append(Sheep(sheep))
        logging.info("Initial  positions  of all sheep were determined ")

    def makeARound(self):
        for sheep in self.sheep:
            if sheep.alive:
                sheep.move()
        logging.info("All sheep moved")
        self.wolf.move(self.sheep)
        print(self.wolf.reportPosition())
        print("Sheep left:", self.aliveSheepAmount())
        logging.info("Round ended alive sheep: %d", self.aliveSheepAmount())

    def aliveSheepAmount(self):
        counter = 0
        for sheep in self.sheep:
            if sheep.alive:
                counter += 1
        return counter

    def get_sheep_positions(self):
        positions = []
        for sheep in self.sheep:
            positions.append(sheep.reportPosition())
        return positions
