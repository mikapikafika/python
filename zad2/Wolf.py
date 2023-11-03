from math import sqrt


class Wolf:
    position = (0, 0)
    move_distance = 1

    def move(self, sheepsList):
        findedSheep = self.findNearestSheep(sheepsList)
        if(findedSheep[1]<self.move_distance):
            self.position = findedSheep[0].position
            sheepsList.remove(findedSheep[0])
            print("I have eaten sheep number:", findedSheep[0].seqenceNumber)
        else:
            delta_x = findedSheep[0].position[0] - self.position[0]
            delta_y = findedSheep[0].position[1] - self.position[1]
            distance_to_sheep = sqrt(delta_x ** 2 + delta_y ** 2)
            ratio = self.move_distance / distance_to_sheep
            new_x = self.position[0] + delta_x * ratio
            new_y = self.position[1] + delta_y * ratio
            self.position = (new_x, new_y)
            print("I am chasing sheep number:", findedSheep[0].seqenceNumber)
        return sheepsList

    def findNearestSheep(self, sheepsList):
        nearestSheep = []
        for sheep in sheepsList:
            delta_x = sheep.position[0] - self.position[0]
            delta_y = sheep.position[1] - self.position[1]
            distance = sqrt(delta_x ** 2 + delta_y ** 2)
            if(nearestSheep == [] or nearestSheep[1] > distance):
                nearestSheep = (sheep, distance)
        return nearestSheep
