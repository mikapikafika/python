from math import sqrt

class Wolf:
    position = (0, 0)
    move_distance = 1

    def move(self, sheeps):
        targetedSheep = self.findTarget(sheeps)
        targetedSheepDistance = self.getEuclideanDistance(targetedSheep)

        if (targetedSheepDistance < self.move_distance):
            self.position = targetedSheep.position
            for sheep in sheeps:
                if sheep == targetedSheep:
                    sheep.alive = False
                    sheep.position = None
                    break
            print("I have eaten sheep number:", targetedSheep.seqenceNumber)
        else:
            delta_x = self.getXDistance(targetedSheep)
            delta_y = self.getYDistance(targetedSheep)
            ratio = self.move_distance / targetedSheepDistance
            new_x = self.position[0] + delta_x * ratio
            new_y = self.position[1] + delta_y * ratio
            self.position = (new_x, new_y)
            print("I am chasing sheep number:", targetedSheep.seqenceNumber)
        return sheeps

    def reportPosition(self):
        return "Wolf is at position:", round(self.position[0], 3), round(self.position[1], 3)
    def findTarget(self, sheeps):
        aliveSheeps = []
        for sheep in sheeps:
            if sheep.alive:
                aliveSheeps.append(sheep)
        target = aliveSheeps[0]
        minDistance = self.getEuclideanDistance(target)
        for sheep in aliveSheeps:
            if sheep.alive:
                distance = self.getEuclideanDistance(sheep)
                if distance < minDistance:
                    minDistance = distance
                    target = sheep
        return target

    def getXDistance(self, object):
        return object.position[0] - self.position[0]

    def getYDistance(self, object):
        return object.position[1] - self.position[1]

    def getEuclideanDistance(self, object):
        delta_x = self.getXDistance(object)
        delta_y = self.getYDistance(object)
        euclideanDistance = sqrt(delta_x ** 2 + delta_y ** 2)
        return euclideanDistance
