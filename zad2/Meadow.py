from Wolf import Wolf
from Sheep import Sheep

class Meadow:
    def __init__(self):
        self.sheeps = []  # Utwórz listę na owce
        self.wolf = Wolf()  # Utwórz wilka

    def addSheep(self, sheep):
        self.sheeps.append(sheep)

    def removeSheep(self, sheep):
        self.sheeps.remove(sheep)

meadow = Meadow()
for i in range(5):
    sheep = Sheep(i+1)
    meadow.addSheep(sheep)
print(meadow.sheeps)
while(len(meadow.sheeps)>0):
    meadow.wolf.move(meadow.sheeps)
print(meadow.sheeps)