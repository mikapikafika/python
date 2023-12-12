import logging
from Meadow import Meadow
from Jsonwriter import Jsonwriter
from Csvwriter import Csvwriter


class Game:
    max_rounds = 50
    break_after_round = False
    jsonwriter = Jsonwriter("data/pos.json")
    csvwriter = Csvwriter("data/alive.csv")

    def __init__(self):
        self.meadow = Meadow()

    def run(self):
        for i in range(self.max_rounds):
            logging.info("Round %s started", i)
            print(f"Round {i + 1} started")
            self.meadow.make_a_round()
            self.jsonwriter.position_info(i, self.meadow.wolf.report_position(),
                                          self.meadow.get_sheep_positions())
            alive_sheep = self.meadow.alive_sheep_amount()
            self.csvwriter.alive_sheep(i, alive_sheep)
            if alive_sheep == 0:
                print("Wolf won")
                logging.info("Simulation ended - wolf won")
                break
            if self.break_after_round:
                input("Press any key to continue \n")
        if alive_sheep != 0:
            print("Sheep won")
            print(f"Sheep left: {alive_sheep}")
            logging.info("Simulation ended, maximum rounds reached. Sheep won")
