from Meadow import Meadow


class Game:
    maxRounds = 50
    meadow = Meadow()
    meadow.makeARound()
    for i in range(maxRounds):
        meadow.makeARound()
        if meadow.aliveSheepAmount() == 0:
            print("Wolf won")
            break
    if meadow.aliveSheepAmount() != 0:
        print("Sheep won")
        print("Sheeps left:", meadow.aliveSheepAmount())
    meadow.displaySheeps()