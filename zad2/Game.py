from Meadow import Meadow


class Game:
    maxRounds = 50
    meadow = Meadow()

    for i in range (maxRounds):
        meadow.makeARound()
        if len(meadow.sheeps) == 0:
            print("Wolf won")
            break
    if(len(meadow.sheeps) != 0):
        print("Sheep won")
        print("Sheeps left:", len(meadow.sheeps))

