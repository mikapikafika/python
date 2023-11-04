from Wolf import Wolf
from Sheep import Sheep

class Meadow:
    sheepQuantity = 15

    def __init__(self):
        self.sheeps = []
        self.wolf = Wolf()
        for sheep in range(self.sheepQuantity):
            self.sheeps.append(Sheep(sheep))


    def makeARound(self):
        for sheep in self.sheeps:
            if sheep.alive:
                sheep.move()
        self.wolf.move(self.sheeps)
        print(self.wolf.reportPosition())
        print("Sheeps left:", self.aliveSheepAmount())

    def aliveSheepAmount(self):
        counter = 0
        for sheep in self.sheeps:
            if sheep.alive:
                counter += 1
        return counter

    def getSheepStatus(sheep):
        dataRow = (sheep.seqenceNumber, sheep.position, sheep.alive)
        return dataRow

    def displaySheeps(self):
        for sheep in self.sheeps:
            dataRow = Meadow.getSheepStatus(sheep)
            print(dataRow)