from math import sqrt
import logging


class Wolf:
    move_dist = 1.0
    position = (0.0, 0.0)

    def __init__(self):
        pass

    def move(self, sheep):
        targeted_sheep = self.find_target(sheep)
        targeted_sheep_distance = self.get_euclidean_distance(targeted_sheep)

        if targeted_sheep_distance < self.move_dist:
            self.position = targeted_sheep.position
            targeted_sheep.alive = False
            targeted_sheep.position = None
            print(f"I have eaten sheep number: "
                  f"{targeted_sheep.sequence_number}")
            logging.info("Sheep number %s was eaten", 
                         targeted_sheep.sequence_number)
        else:
            delta_x = self.get_x_distance(targeted_sheep)
            delta_y = self.get_y_distance(targeted_sheep)
            ratio = self.move_dist / targeted_sheep_distance
            new_x = self.position[0] + delta_x * ratio
            new_y = self.position[1] + delta_y * ratio
            self.position = (new_x, new_y)
            print(f"I am chasing sheep number: "
                  f"{targeted_sheep.sequence_number}")
            logging.info("Wolf is chasing sheep number %s", 
                         targeted_sheep.sequence_number)
        logging.debug("Wolf moved, new position is %s", self.position)
        logging.info("Wolf moved")
        return sheep

    def report_position(self):
        return round(self.position[0], 3), round(self.position[1], 3)

    def find_target(self, sheep):
        alive_sheep = []
        for sheep in sheep:
            if sheep.alive:
                alive_sheep.append(sheep)
        target = alive_sheep[0]
        min_distance = self.get_euclidean_distance(target)
        for sheep in alive_sheep:
            if sheep.alive:
                distance = self.get_euclidean_distance(sheep)
                if distance < min_distance:
                    min_distance = distance
                    target = sheep
        logging.debug("Wolf is chasing sheep number %s and distance is %s", 
                      target.sequence_number, min_distance)
        return target

    def get_x_distance(self, animal):
        return animal.position[0] - self.position[0]

    def get_y_distance(self, animal):
        return animal.position[1] - self.position[1]

    def get_euclidean_distance(self, animal):
        delta_x = self.get_x_distance(animal)
        delta_y = self.get_y_distance(animal)
        euclidean_distance = sqrt(delta_x ** 2 + delta_y ** 2)
        return euclidean_distance
