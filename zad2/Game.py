from Meadow import Meadow
from jsonWriter import jsonWriter
from csvWriter import csvWriter
class Game:
    maxRounds = 50
    meadow = Meadow()
    jsonwriter = jsonWriter("pos.json")
    csvwriter = csvWriter("alive.csv")
    for i in range(maxRounds):
        meadow.makeARound()
        jsonwriter.posistionInfo(i, meadow.wolf.reportPosition(), meadow.getSheepsPositions())
        csvwriter.aliveSheeps(i, meadow.aliveSheepAmount())
        if meadow.aliveSheepAmount() == 0:
            print("Wolf won")
            break
    if meadow.aliveSheepAmount() != 0:
        print("Sheep won")
        print("Sheeps left:", meadow.aliveSheepAmount())
