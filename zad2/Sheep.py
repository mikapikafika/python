import random


class Sheep:
    move_distance = 0.5
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    InitPosLimit = 10.0

    def __init__(self, Number):
        new_x = random.uniform(-self.InitPosLimit, self.InitPosLimit)
        new_y = random.uniform(-self.InitPosLimit, self.InitPosLimit)
        self.position = (new_x, new_y)
        self.seqenceNumber = Number
        self.alive = True

    def move(self):
        direction = random.choice(self.directions)
        new_x = self.position[0] + (direction[0] * self.move_distance)
        new_y = self.position[1] + (direction[1] * self.move_distance)
        self.position = (new_x, new_y)
    def reportPosition(self):
        if self.position != None:
            return round(self.position[0], 3), round(self.position[1], 3)






'''owieczka = Sheep(1)
print(owieczka.position)
owieczka.move()
print(owieczka.position)
owieczka.move()
print(owieczka.position)'''
