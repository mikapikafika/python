import keyboard

from Meadow import Meadow
from Jsonwriter import Jsonwriter
from Csvwriter import Csvwriter


class Game:
    maxRounds = 50
    break_after_round = False
    jsonwriter = Jsonwriter("data/pos.json")
    csvwriter = Csvwriter("data/alive.csv")

    def __init__(self):
        self.meadow = Meadow()

    def run(self):
        for i in range(self.maxRounds):
            self.meadow.makeARound()
            self.jsonwriter.position_info(i, self.meadow.wolf.reportPosition(),
                                          self.meadow.get_sheep_positions())
            self.csvwriter.aliveSheep(i, self.meadow.aliveSheepAmount())
            if self.meadow.aliveSheepAmount() == 0:
                print("Wolf won")
                break
            if self.break_after_round:
                input("Press any key to continue \n")
        if self.meadow.aliveSheepAmount() != 0:
            print("Sheep won")
            print("Sheep left:", self.meadow.aliveSheepAmount())

        print(self.maxRounds)
        print(self.meadow.sheepQuantity)