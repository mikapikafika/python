import random


class Sheep:
    position = (0, 0)
    move_distance = 0.5
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    InitPosLimit = 10.0

    def move(self):
        direction = random.choice(self.directions)
        new_x = self.position[0] + (direction[0] * self.move_distance)
        new_y = self.position[1] + (direction[1] * self.move_distance)
        self.position = (new_x, new_y)


    def __init__(self, Number):
        new_x = random.uniform(-self.InitPosLimit, self.InitPosLimit)
        new_y = random.uniform(-self.InitPosLimit, self.InitPosLimit)
        self.position = (new_x, new_y)
        self.seqenceNumber = Number


'''owieczka = Sheep(1)
print(owieczka.position)
owieczka.move()
print(owieczka.position)
owieczka.move()
print(owieczka.position)'''
