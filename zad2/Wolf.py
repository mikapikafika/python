from math import sqrt


class Wolf:
    position = (0, 0)
    move_distance = 1

    def move(self, sheepsList):
        findedSheep = self.findNearestSheep(sheepsList)
        if(findedSheep[1]<self.move_distance):
            self.position = findedSheep[0].position
            sheepsList.remove(findedSheep[0])
            print("I have eaten sheep number: ", findedSheep[0].seqenceNumber)
        return sheepsList

    def findNearestSheep(self, sheepsList):
        nearestSheep = []
        for sheep in sheepsList:
            distance = sqrt(pow(self.position[0] - sheep.position[0], 2) + pow(self.position[1] - sheep.position[1], 2))
            if(nearestSheep == [] or nearestSheep[1] > distance):
                nearestSheep = (sheep, distance)
        return nearestSheep
