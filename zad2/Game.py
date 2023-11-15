from Meadow import Meadow
from jsonWriter import JsonWriter
from csvWriter import csvWriter


class Game:
    maxRounds = 50
    meadow = Meadow()
    jsonwriter = JsonWriter("pos.json")
    csvwriter = csvWriter("alive.csv")
    for i in range(maxRounds):
        meadow.makeARound()
        jsonwriter.position_info(i, meadow.wolf.reportPosition(),
                                 meadow.get_sheep_positions())
        csvwriter.aliveSheep(i, meadow.aliveSheepAmount())
        if meadow.aliveSheepAmount() == 0:
            print("Wolf won")
            break
    if meadow.aliveSheepAmount() != 0:
        print("Sheep won")
        print("Sheep left:", meadow.aliveSheepAmount())
