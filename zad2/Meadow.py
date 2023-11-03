from Wolf import Wolf
from Sheep import Sheep

class Meadow:
    sheepQuantity = 15
    def __init__(self):
        self.sheeps = []
        self.wolf = Wolf()
        for sheep in range(self.sheepQuantity):
            self.sheeps.append(Sheep(sheep+1))


    def makeARound(self):
        for sheep in self.sheeps:
            sheep.move()
        self.wolf.move(self.sheeps)
        self.wolf.reportPosition()
        print("Sheeps left:", len(self.sheeps))

