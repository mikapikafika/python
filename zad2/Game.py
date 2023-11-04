from Meadow import Meadow
from Writer import Writer

class Game:
    maxRounds = 50
    meadow = Meadow()
    writer = Writer("pos.json")
    for i in range(maxRounds):
        meadow.makeARound()
        writer.roundInfo(i, meadow.wolf.reportPosition(), meadow.getSheepsPositions())
        if meadow.aliveSheepAmount() == 0:
            print("Wolf won")
            break
    if meadow.aliveSheepAmount() != 0:
        print("Sheep won")
        print("Sheeps left:", meadow.aliveSheepAmount())
