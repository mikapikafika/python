from math import sqrt


class Wolf:
    move_distance = 1
    position = (0, 0)

    def __init__(self):
        pass

    def move(self, sheep):
        targeted_sheep = self.findTarget(sheep)
        targeted_sheep_distance = self.getEuclideanDistance(targeted_sheep)

        if targeted_sheep_distance < self.move_distance:
            self.position = targeted_sheep.position
            for sheep in sheep:
                if sheep == targeted_sheep:
                    sheep.alive = False
                    sheep.position = None
                    break
            print("I have eaten sheep number:", targeted_sheep.seqence_number)
        else:
            delta_x = self.getXDistance(targeted_sheep)
            delta_y = self.getYDistance(targeted_sheep)
            ratio = self.move_distance / targeted_sheep_distance
            new_x = self.position[0] + delta_x * ratio
            new_y = self.position[1] + delta_y * ratio
            self.position = (new_x, new_y)
            print("I am chasing sheep number:", targeted_sheep.seqence_number)
        return sheep

    def reportPosition(self):
        return round(self.position[0], 3), round(self.position[1], 3)

    def findTarget(self, sheep):
        alive_sheep = []
        for sheep in sheep:
            if sheep.alive:
                alive_sheep.append(sheep)
        target = alive_sheep[0]
        min_distance = self.getEuclideanDistance(target)
        for sheep in alive_sheep:
            if sheep.alive:
                distance = self.getEuclideanDistance(sheep)
                if distance < min_distance:
                    min_distance = distance
                    target = sheep
        return target

    def getXDistance(self, animal):
        return animal.position[0] - self.position[0]

    def getYDistance(self, animal):
        return animal.position[1] - self.position[1]

    def getEuclideanDistance(self, animal):
        delta_x = self.getXDistance(animal)
        delta_y = self.getYDistance(animal)
        euclidean_distance = sqrt(delta_x ** 2 + delta_y ** 2)
        return euclidean_distance
