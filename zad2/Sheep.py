import random
import logging


class Sheep:
    MoveDist = 0.5
    InitPosLimit = 10.0
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self, number):
        new_x = random.uniform(-self.InitPosLimit, self.InitPosLimit)
        new_y = random.uniform(-self.InitPosLimit, self.InitPosLimit)
        self.position = (new_x, new_y)
        self.sequence_number = number
        self.alive = True
        logging.debug(f"Sheep number {self.sequence_number} "
                      f"was created at position {self.position}")

    def move(self):
        direction = random.choice(self.directions)
        logging.debug(f"Sheep number {self.sequence_number} "
                      f"moves in direction {direction}")
        new_x = self.position[0] + (direction[0] * self.MoveDist)
        new_y = self.position[1] + (direction[1] * self.MoveDist)
        self.position = (new_x, new_y)
        logging.debug(f"Sheep number {self.sequence_number} "
                      f"is now at position {self.position}")

    def report_position(self):
        if self.position is not None:
            return round(self.position[0], 3), round(self.position[1], 3)
