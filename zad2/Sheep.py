from random import choice

class Sheep:
    position = (0, 0)
    move_distance = 0.5
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def move(self):
        direction = choice(self.directions)
        new_x = self.position[0] + (direction[0] * self.move_distance)
        new_y = self.position[1] + (direction[1] * self.move_distance)
        self.position = (new_x, new_y)
