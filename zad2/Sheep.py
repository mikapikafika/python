import random
import logging


class Sheep:
    move_dist = 0.5
    init_pos_limit = 10.0
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self, number):
        new_x = random.uniform(-self.init_pos_limit, self.init_pos_limit)
        new_y = random.uniform(-self.init_pos_limit, self.init_pos_limit)
        self.position = (new_x, new_y)
        self.sequence_number = number + 1
        self.alive = True
        logging.debug("Sheep number %s was created at position %s", 
                      self.sequence_number, self.position)

    def move(self):
        direction = random.choice(self.directions)
        logging.debug("Sheep number %s moves in direction %s", 
                      self.sequence_number, direction)
        new_x = self.position[0] + (direction[0] * self.move_dist)
        new_y = self.position[1] + (direction[1] * self.move_dist)
        self.position = (new_x, new_y)
        logging.debug("Sheep number %s is now at position %s", 
                      self.sequence_number, self.position)

    def report_position(self):
        if self.position is not None:
            return round(self.position[0], 3), round(self.position[1], 3)
